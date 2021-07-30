class lazy_class_attribute(object):
    def __init__(self, function):
        self.fget = function

    def __get__(self, obj, cls):
        value = self.fget(obj or cls)
        # note: クラスレベルのアクセスか、インスタンスレベルの
        #       アクセスかに関係なく、すべてをクラスオブジェクト
        #       に格納する
        setattr(cls, self.fget.__name__, value)
        return value


class MyComplexClass:
    @lazy_class_attribute
    def evaluated_only_once(self):
        print("メソッドの評価中!")
        return sum(x ** 2 for x in range(200))


if __name__ == "__main__":
    instance = MyComplexClass()

    print("インスタンスのレベルで、属性への初回アクセス")
    print("instance.evaluated_only_once =",
          instance.evaluated_only_once,
          '\n')

    print("インスタンスのレベルで、属性への2回目のアクセス")
    print("instance.evaluated_only_once =",
          instance.evaluated_only_once,
          '\n')

    print("クラスのレベルで、属性へのアクセス")
    print("MyComplexClass.evaluated_only_once =",
          MyComplexClass.evaluated_only_once,
          '\n')

    print("まったく新しいインスタンスからの、属性へのアクセス")
    print("MyComplexClass().evaluated_only_once =",
          MyComplexClass().evaluated_only_once,
          '\n')
