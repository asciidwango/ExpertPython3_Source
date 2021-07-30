"""
「Adapterパターン」の節で登場するサンプルコード
アダプターの実装方法

"""
from os.path import split, splitext


class DublinCoreAdapter:
    def __init__(self, filename):
        self._filename = filename

    @property
    def title(self):
        return splitext(split(self._filename)[-1])[0]

    @property
    def languages(self):
        return 'en',

    def __getitem__(self, item):
        return getattr(self, item, 'Unknown')


class DublinCoreInfo:
    def summary(self, dc_dict):
        print(f'タイトル: {dc_dict["title"]}')
        print(f'著者: {dc_dict["creator"]}')
        print(f'言語: {", ".join(dc_dict["languages"])}')


if __name__ == "__main__":
    file_name = 'example.txt'

    print(
        "DublinCoreAdapterで '{}' をラップして要約を取り出す"
        "".format(file_name)
    )
    DublinCoreInfo().summary(DublinCoreAdapter(file_name))
