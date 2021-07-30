"""
「インターフェイス」の節で登場するサンプルコード
抽象基底クラスで定義したインターフェイスの検証/チェックを、関数アノテーションを利用して行う方法

"""
from abc import (
    ABCMeta,
    abstractmethod,
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
        """ Return rectangle area
        """

    @abstractmethod
    def perimeter(self):
        """ Return rectangle perimeter
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

from functools import wraps
import inspect


def ensure_interface(function):
    signature = inspect.signature(function)
    parameters = signature.parameters

    @wraps(function)
    def wrapped(*args, **kwargs):
        bound = signature.bind(*args, **kwargs)
        for name, value in bound.arguments.items():
            annotation = parameters[name].annotation

            if not isinstance(annotation, ABCMeta):
                continue

            if not isinstance(value, annotation):
                raise TypeError(
                    "{} は {} インターフェイスを実装していません"
                    "".format(value, annotation)

                )

        function(*args, **kwargs)

    return wrapped


@ensure_interface
def draw_rectangle(rectangle: IRectangle):
    print(
        "{} × {} の長方形を描画します"
        "".format(rectangle.width, rectangle.height)
    )


def attempt_draw(instance):
    print(instance, "の描画を試みます")
    try:
        draw_rectangle(instance)
    except TypeError as error:
        print("次の理由で描画に失敗しました:", error)
    else:
        print("描画に成功しました")


if __name__ == "__main__":
    for maybe_rectangle in (
        "foo",
        ImplicitRectangle(10, 12),
        Rectangle(10,5),
        (10, 23)
    ):
        attempt_draw(maybe_rectangle)
        print()
