def fibonacci():
    a, b = 0, 1

    while True:
        yield b
        a, b = b, a + b


if __name__:
    fib = fibonacci()

    print("フィボナッチ関数の返り値の型:", type(fib))
    print(
        "最初の10個のフィボナッチ数 (next利用):",
        [next(fib) for _ in range(10)]
    )
    print(
        "次の10個のフィボナッチ数 (継続):",
        [next(fib) for _ in range(10)]
    )