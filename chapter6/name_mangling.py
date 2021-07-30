class Base:
    def __secret(self):
        print("秘密です")

    def public(self):
        self.__secret()


class Derived(Base):
    def __secret(self):
        print("参照されません")


if __name__ == "__main__":

    print("Baseクラスの属性:", dir(Base))
    print("Derivedクラスの属性:", dir(Derived))

    print("Base.public() の結果:")
    Base().public()

    print("Derived.public() の結果:")
    Derived().public()
