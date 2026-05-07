from triangle_classifier import Triangle, TriangleType


def test_equilateral():
    assert Triangle(3, 3, 3).type == TriangleType.EQUILATERAL


def test_isosceles():
    assert Triangle(2, 2, 3).type == TriangleType.ISOSCELES


def test_scalene():
    assert Triangle(3, 4, 6).type == TriangleType.SCALENE


def test_right():
    assert Triangle(3, 4, 5).type == TriangleType.RIGHT


def test_invalid():
    assert Triangle(1, 2, 3).type == TriangleType.INVALID


def test_negative():
    assert Triangle(-1, 2, 2).type == TriangleType.INVALID