"""
「生成に関するパターン」の節で登場するサンプルコード
PythonでBorgを実装する別の方法

"""
class Borg:
    _state = {}

    def __new__(cls, *args, **kwargs):
        ob = super().__new__(cls, *args, **kwargs)
        ob.__dict__ = cls._state
        return ob
