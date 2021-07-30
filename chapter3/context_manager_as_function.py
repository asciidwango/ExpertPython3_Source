from contextlib import contextmanager


@contextmanager
def context_illustration():
    print('コンテキストに入った')
    try:
        yield
    except Exception as e:
        print('コンテキストから出た')
        print(f'エラーあり ({e})')
        # 例外を送出し直す必要がある
        raise
    else:
        print('コンテキストから出た')
        print('エラーなし')


if __name__ == "__main__":
    print("コンテキストマネージャ内での処理の実行（エラーがなし）")

    with context_illustration():
        print(">> inside context")
    print()

    print("コンテキストマネージャ内での処理の実行（エラーがあり）")
    try:
        with context_illustration():
            print(">> コンテキスト内")
            raise RuntimeError("コンテキストマネージャ内部でのエラー")
    except RuntimeError:
        pass