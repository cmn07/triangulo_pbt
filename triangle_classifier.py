from dataclasses import dataclass
from enum import Enum, auto


class TriangleType(Enum):
    EQUILATERAL = auto()
    ISOSCELES = auto()
    SCALENE = auto()
    RIGHT = auto()
    INVALID = auto()


@dataclass(frozen=True, slots=True)
class Triangle:
    side1: int
    side2: int
    side3: int

    @property
    def type(self) -> TriangleType:

        a, b, c = self.side1, self.side2, self.side3

        # lados inválidos
        if (
            a <= 0 or
            b <= 0 or
            c <= 0
        ):
            return TriangleType.INVALID

        # desigualdade triangular
        if (
            a >= b + c or
            b >= a + c or
            c >= a + b
        ):
            return TriangleType.INVALID

        # equilátero
        if a == b == c:
            return TriangleType.EQUILATERAL

        # retângulo
        if (
            a*a == b*b + c*c or
            b*b == a*a + c*c or
            c*c == a*a + b*b
        ):
            return TriangleType.RIGHT

        # isósceles
        if (
            a == b or
            a == c or
            b == c
        ):
            return TriangleType.ISOSCELES

        return TriangleType.SCALENE
    
    @property
    def explanation(self) -> str:

        if self.type == TriangleType.INVALID:
            return "Invalid triangle"

        if self.type == TriangleType.EQUILATERAL:
            return "Equilateral triangle"

        if self.type == TriangleType.RIGHT:
            return "Right triangle"

        if self.type == TriangleType.ISOSCELES:
            return "Isosceles triangle"

        return "Scalene triangle"