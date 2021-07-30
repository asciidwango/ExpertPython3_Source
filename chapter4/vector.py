class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

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

    def __repr__(self):
        """ベクトルのテキスト表現を返す"""
        return f"<Vector: x={self.x}, y={self.y}>"

    def __eq__(self, other):
        """二つのベクトルの等価比較"""
        return self.x == other.x and self.y == other.y