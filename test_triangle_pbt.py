from hypothesis import Verbosity, given, assume, settings
from hypothesis.strategies import integers
from hypothesis.strategies import sampled_from

from itertools import permutations

from triangle_classifier import Triangle, TriangleType

# Teste equilátero: todos os lados iguais
@settings(verbosity=Verbosity.verbose)
@given(integers(min_value=1))
def test_equilateral_property(side):

    t = Triangle(side, side, side)

    assert t.type == TriangleType.EQUILATERAL

# Teste inválido: lados negativos ou zero
@given(
    integers(max_value=0),
    integers(),
    integers()
)
def test_non_positive_invalid(a, b, c):

    t = Triangle(a, b, c)

    assert t.type == TriangleType.INVALID

# Teste desigualdade triangular: a >= b + c
@settings(verbosity=Verbosity.verbose)
@given(
    integers(min_value=1),
    integers(min_value=1),
)
def test_triangle_inequality(a, b):

    c = a + b

    t = Triangle(a, b, c)

    assert t.type == TriangleType.INVALID

# Ordem dos lados não deve afetar a classificação
@given(
    integers(min_value=1, max_value=100),
    integers(min_value=1, max_value=100),
    integers(min_value=1, max_value=100),
)
def test_permutation_invariance(a, b, c):

    expected = Triangle(a, b, c).type

    for x, y, z in permutations([a, b, c]):
        assert Triangle(x, y, z).type == expected


# Teste triângulo retângulo: a^2 + b^2 = c^2
# No caso deste exemplo, estamos usando um conjunto fixo de trios de lados que formam triângulos retângulos conhecidos.
# Gera diretamente dados válidos para triângulos retângulos, evitando a necessidade de suposições adicionais.
@given(
    sampled_from([
        (3, 4, 5),
        (5, 12, 13),
        (8, 15, 17),
        (7, 24, 25),
    ])
)
def test_right_triangle_property(triple):

    a, b, c = triple

    t = Triangle(a, b, c)

    assert t.type == TriangleType.RIGHT

# Teste escaleno
@given(
    integers(min_value=1, max_value=100),
    integers(min_value=1, max_value=100),
    integers(min_value=1, max_value=100),
)
def test_scalene_property(a, b, c):

    assume(a != b)
    assume(a != c)
    assume(b != c)

    assume(a < b + c)
    assume(b < a + c)
    assume(c < a + b)

    assume(not (
        a*a == b*b + c*c or
        b*b == a*a + c*c or
        c*c == a*a + b*b
    ))

    t = Triangle(a, b, c)

    assert t.type == TriangleType.SCALENE

# Explicações nunca vazias
@given(
    integers(),
    integers(),
    integers()
)
def test_explanation_not_empty(a, b, c):

    t = Triangle(a, b, c)

    assert t.explanation.strip() != ""

# Explicação consistente com o tipo
@given(integers(min_value=1))
def test_equilateral_explanation(side):

    t = Triangle(side, side, side)

    assert "equilateral" in t.explanation.lower()

