class InitOnAccess:
    def __init__(self, klass, *args, **kwargs):
        self.klass = klass
        self.args = args
        self.kwargs = kwargs
        self._initialized = None

    def __get__(self, instance, owner):
        if self._initialized is None:
            print('初期化!')
            self._initialized = self.klass(*self.args, **self.kwargs)
        else:
            print('キャッシュ済み!')
        return self._initialized


class MyClass:
    lazily_initialized = InitOnAccess(list, "argument")


if __name__ == "__main__":
    instance = MyClass()

    print("instance.lazily_initializedへの初回のアクセス")
    print(">> instance.lazily_initialized =", instance.lazily_initialized, '\n')

    print("instance.lazily_initializedへの2回目のアクセス")
    print(">> instance.lazily_initialized =", instance.lazily_initialized, '\n')