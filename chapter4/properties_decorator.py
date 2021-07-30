class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2

    @property
    def width(self):
        """長方形の幅"""
        return self.x2 - self.x1

    @width.setter
    def width(self, value):
        self.x2 = self.x1 + value

    @property
    def height(self):
        """長方形の高さ"""
        return self.y2 - self.y1

    @height.setter
    def height(self, value):
        self.y2 = self.y1 + value


if __name__ == "__main__":
    rectangle = Rectangle(0, 0, 10, 10)
    print(
        f"最初の図形は {rectangle} で"
        f"大きさは {rectangle.width} x {rectangle.height} です"
    )

    rectangle.width = 2
    rectangle.height = 8
    print(
        f"サイズを変更したあとの図形は {rectangle} で"
        f"大きさは {rectangle.width} x {rectangle.height} です"
    )
