from random import shuffle

from cffi import FFI

ffi = FFI()

ffi.cdef("""
void qsort(void *base, size_t nel, size_t width,
           int (*compar)(const void *, const void *));
""")
C = ffi.dlopen(None)


@ffi.callback("int(void*, void*)")
def cffi_int_compare(a, b):
    # コールバックのシグネチャは完全に一致する必要があります。
    # ctypesに比べてより「魔法」が少なくなるというメリットがあるものの、
    # 明示的なキャストが必要になります。
    int_a = ffi.cast('int*', a)[0]
    int_b = ffi.cast('int*', b)[0]
    print(" %s cmp %s" % (int_a, int_b))

    # qsort の仕様により、戻り値は
    # * a < b のとき: 負
    # * a = b のとき: 0
    # * a > b のとき: 正
    return int_a - int_b


def main():
    numbers = list(range(5))
    shuffle(numbers)
    print("shuffled: ", numbers)

    c_array = ffi.new("int[]", numbers)

    C.qsort(
        # ソート対象の配列へのポインタ
        c_array,
        # 配列の長さ
        len(c_array),
        # 配列の各要素の大きさ
        ffi.sizeof('int'),
        # コールバック (Cの比較関数へのポインタ)
        cffi_int_compare,
    )
    print("sorted:   ", list(c_array))

if __name__ == "__main__":
    main()
