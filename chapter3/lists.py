"""
"リストとタプル"のセクションのリスト内包表記のサンプル
"""


def evens_using_for_loop(count):
    """　ループを回して偶数を計算 """
    evens = []
    for i in range(count):
        if i % 2 == 0:
            evens.append(i)
    return evens


def evens_using_list_comprehension(count):
    """ リスト内包表記で偶数を計算 """
    return [i for i in range(count) if i % 2 == 0]


def enumerate_elements(elements):
    for index, element in enumerate(elements):
        print(index, element)


if __name__ == "__main__":
    print(
        "ループを使って0-10の間の偶数を計算:",
        evens_using_for_loop(11)
    )
    print()

    print(
        "リスト内包表記を使って0-10の間の偶数を計算:",
        evens_using_list_comprehension(11)
    )
    print()

    print("0-10の偶数を列挙:")
    enumerate_elements(evens_using_list_comprehension(11))
    print()