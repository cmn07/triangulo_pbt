from hypothesis import given, assume
from hypothesis.strategies import integers
from hypothesis.strategies import sampled_from

from itertools import permutations

from triangle_classifier import Triangle, TriangleType

# Teste equilátero: todos os lados iguais
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
"""
Exemplo de failing example:
No triângulo_classifier.oy trocar a propriedade para a> b + c
Nunca será possível gerar valores que satisfaçam a condição de desigualdade triangular, pois c = a + b
Com isso, chegamos a uma situação onde todos os exemplos gerados na fase de geração são inválidos, 
e o teste falha consistentemente, pois não há casos válidos para testar.
Failing example: a=1, b= 1, c = 2
Assert falha, pois Triangle(1, 1, 2) é classificado como TriangleType.ISOSCELES, e não TriangleType.INVALID como esperado.
Além disso, na fase de shrinking, O hypothesis tentará reduzir os valores para encontrar um exemplo mínimo que falha
No caso de 0 sucessful shrinks, o shrinking não consegue encontrar um exemplo mais simples que falha, e o teste permanece falho com o exemplo original.

Com o shrinking o hypothesis mostra o menor caso de contraexemplo 
Falsifying example: test_triangle_inequality(
           # The test always failed when commented parts were varied together.
           a=1,  # or any other generated value
           b=1,  # or any other generated value
"""



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
"""
Saída do teste escaleno:
test_triangle_pbt.py::test_scalene_property:

  - during generate phase (0.62 seconds):
    - Typical runtimes: < 1ms, of which < 1ms in data generation
    - 100 passing examples, 0 failing examples, 659 invalid examples
    - Events:
      * 29.64%, invalid because: failed to satisfy assume() in test_scalene_property (line 83)
      * 23.72%, invalid because: failed to satisfy assume() in test_scalene_property (line 85)
      * 20.82%, invalid because: failed to satisfy assume() in test_scalene_property (line 84)
      * 4.48%, invalid because: failed to satisfy assume() in test_scalene_property (line 88)
      * 4.22%, invalid because: failed to satisfy assume() in test_scalene_property (line 89)
      * 3.95%, invalid because: failed to satisfy assume() in test_scalene_property (line 87)

  - Stopped because settings.max_examples=100

Devido às diversas restrições (assume) necessárias o hypothesis gera muitos exemplos que são descartados.
Para gerar 100 exemplos válidos, o hypothesis gerou 659 exemplos inválidos, o que representa uma taxa de filtragem de aproximadamente 86.5%.
  
Filtragem excessiva -> teste fica mais lento e menos eficiente, pois muitos exemplos gerados são descartados.

Gerar entradas validas é difícil

Essa é uma desvantagem do PBT, em alguns casos ele precisa gerar muitos exemplos para encontrar os casos válidos.
No caso do teste escaleno, este é um teste trivial, mas em testes em grande escala o número de lixo acumulado pode ser muito ineficiente.

"""

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

