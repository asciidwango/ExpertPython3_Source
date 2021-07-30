from functools import wraps


def repeat(number=3):
    """デコレートされた関数をnumberで指定された回数繰り返す。

    最後に呼ばれた関数の結果を、関数の返り値として返す。

    :param number: 繰り返す回数。指定しなければ3。
    """
    def actual_decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(number):
                result = function(*args, **kwargs)
            return result

        return wrapper

    return actual_decorator


@repeat(5)
def print_hello_world():
    """もっともシンプルな"hello world"実装."""
    print("Hello, world!")


if __name__ == "__main__":
    print(
        "repeat(5)デコレータ(メタデータは維持する)つきの"
        "print_hello_world()関数の呼び出し結果"
    )
    print_hello_world()
    print()

    print("デコレートされた関数名:", print_hello_world.__name__)
    print("関数のdocstring:", print_hello_world.__doc__)