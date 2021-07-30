from dataclasses import dataclass


@dataclass
class Vector:
    x: int
    y: int

    def __add__(self, other):
        """+演算子を使ったベクトルの足し算"""
        return Vector(
            self.x + other.x,
            self.y + other.y,
        )

    def __sub__(self, other):
        """-演算子を使ったベクトルの引き算"""
        return Vector(
            self.x - other.x,
            self.y - other.y,
        )


@dataclass(frozen=True)
class FrozenVector:
    x: int
    y: int