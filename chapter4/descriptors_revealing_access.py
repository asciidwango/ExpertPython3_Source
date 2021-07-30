class RevealAccess(object):
    """値を通常通り設定・返すデータディスクリプタ
       アクセスログも出力する
    """

    def __init__(self, initval=None, name='変数'):
        self.val = initval
        self.name = name

    def __get__(self, obj, objtype):
        print('取得', self.name)
        return self.val

    def __set__(self, obj, val):
        print('更新', self.name)
        self.val = val


class MyClass(object):
    x = RevealAccess(10, '変数"x"')
    y = 5


if __name__ == "__main__":
    my_instance = MyClass()

    # x属性をセット (ログ表示される)
    my_instance.x = 4
    # x属性にアクセス (ログ表示される)
    assert my_instance.x == 4

    # y属性をセット (ログ表示されない)
    my_instance.y = 2
    # y属性にアクセス (ログ表示されない)
    assert my_instance.y == 2