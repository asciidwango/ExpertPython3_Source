from random import shuffle

import ctypes
from ctypes.util import find_library

libc = ctypes.cdll.LoadLibrary(find_library('c'))

CMPFUNC = ctypes.CFUNCTYPE(
    # 戻り値の型
    ctypes.c_int,
    # 1つめの引数の型
    ctypes.POINTER(ctypes.c_int),
    # 2つめの引数の型
    ctypes.POINTER(ctypes.c_int),
)


def ctypes_int_compare(a, b):
    # 引数はポインタなので[0]インデックスでアクセスする
    print(" %s cmp %s" % (a[0], b[0]))

    # qsort の仕様により、戻り値は
    # * a < b のとき: 負
    # * a = b のとき: 0
    # * a > b のとき: 正
    return a[0] - b[0]


def main():
    numbers = list(range(5))
    shuffle(numbers)
    print("shuffled: ", numbers)

    # numbers と同じ長さの配列を表す新しい型を作る
    NumbersArray = ctypes.c_int * len(numbers)
    # その型を使ってC配列を作る
    c_array = NumbersArray(*numbers)

    libc.qsort(
        # ソート対象の配列へのポインタ
        c_array,
        # 配列の長さ
        len(c_array),
        # 配列の各要素の大きさ
        ctypes.sizeof(ctypes.c_int),
        # コールバック (Cの比較関数へのポインタ)
        CMPFUNC(ctypes_int_compare)
    )
    print("sorted:   ", list(c_array))


if __name__ == "__main__":
    main()
