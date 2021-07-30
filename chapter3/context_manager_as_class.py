class ContextIllustration:
    def __enter__(self):
        print('コンテキストに入った')

    def __exit__(self, exc_type, exc_value, traceback):
        print('コンテキストから出た')

        if exc_type is None:
            print('エラーなし')
        else:
            print(f'エラーあり ({exc_value})')


if __name__ == "__main__":
    print("コンテキストマネージャ内での処理の実行（エラーなし）")

    with ContextIllustration():
        print(">> コンテキスト内")
    print()

    print("コンテキストマネージャ内での処理の実行（エラーあり）")
    try:
        with ContextIllustration():
            print(">> コンテキスト内")
            raise RuntimeError("コンテキストマネージャ内部でのエラー")
    except RuntimeError:
        pass