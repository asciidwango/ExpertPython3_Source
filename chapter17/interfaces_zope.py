"""
「インターフェイス」の節で登場するサンプルコード
`zope.interface` パッケージを使ってインターフェイスを実現する方法

"""
from zope.interface import Interface, Attribute, implementer


class IRectangle(Interface):
    width = Attribute("長方形の幅")
    height = Attribute("長方形の高さ")

    def area():
        """ 長方形の面積を返す
        """

    def perimeter():
        """ 長方形の周の長さを返す
        """


@implementer(IRectangle)
class Square:
    """ 長方形のインターフェイスを持つ正方形の具象クラス
    """

    def __init__(self, size):
        self.size = size

    @property
    def width(self):
        return self.size

    @property
    def height(self):
        return self.size

    def area(self):
        return self.size ** 2

    def perimeter(self):
        return 4 * self.size


@implementer(IRectangle)
class Rectangle:
    """ 長方形の具象クラス
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return self.width * 2 + self.height * 2
