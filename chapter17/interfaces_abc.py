"""
「インターフェイス」の節で登場するサンプルコード
抽象基底クラスを使って暗黙的なインターフェイス定義し振る舞いを検証する方法

"""
from abc import (
    ABCMeta,
    abstractmethod
)


class IRectangle(metaclass=ABCMeta):

    @property
    @abstractmethod
    def width(self):
        return

    @property
    @abstractmethod
    def height(self):
        return

    @abstractmethod
    def area(self):
        """ 長方形の面積を返す
        """

    @abstractmethod
    def perimeter(self):
        """ 長方形の周の長さを返す
        """

    @classmethod
    def __subclasshook__(cls, C):
        if cls is IRectangle:
            if all([
                any("area" in B.__dict__ for B in C.__mro__),
                any("perimeter" in B.__dict__ for B in C.__mro__),
                any("width" in B.__dict__ for B in C.__mro__),
                any("height" in B.__dict__ for B in C.__mro__),
            ]):
                return True
        return NotImplemented


class Rectangle(IRectangle):
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return self.width * 2 + self.height * 2


class ImplicitRectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return self.width * 2 + self.height * 2


if __name__ == "__main__":
    rectangle = Rectangle(10, 10)

    print("インスタンスの型:", type(rectangle))
    print("インスタンスのメソッド解決順序(MRO): ", rectangle.__class__.mro())
    print("isinstance(rectangle, IRectangle) =",
          isinstance(rectangle, IRectangle))
    print()

    rectangle = ImplicitRectangle(10, 10)
    print("インスタンスの型:", type(rectangle))
    print("インスタンスのメソッド解決順序: ", rectangle.__class__.mro())
    print("isinstance(rectangle, IRectangle) =",
          isinstance(rectangle, IRectangle))
    print()
