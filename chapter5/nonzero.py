class NonZero(int):
    def __new__(cls, value):
        return super().__new__(cls, value) if value != 0 else None

    def __init__(self, skipped_value):
        # このケースでは __init__ の実装は不要ですが、
        # このメソッドが呼ばれないケースがあることを
        # 確認するために残してあります
        print("__init__() called")
        super().__init__()


if __name__ == "__main__":
    print("NonZero(-12)    =", NonZero(-12))
    print("NonZero(-3.123) =", NonZero(-3.123))
    print("NonZero(0)      =", NonZero(0))
