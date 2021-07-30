from collections import UserDict


class DistinctError(ValueError):
    """distinctdictに重複した値を登録しようとした時に送出される例外です。"""


class distinctdict(UserDict):
    """重複した値を許さない辞書です。"""

    def __setitem__(self, key, value):
        if value in self.values():
            if (
                (key in self and self[key] != value) or
                key not in self
            ):
                raise DistinctError(
                    "この値はすでに他のキーで登録されています"
                )

        super().__setitem__(key, value)


if __name__ == "__main__":
    names_to_numbers = {
        "one": 1,
        "two": 2,
        "uno": 1,
    }

    ddict = distinctdict()
    for key, value in names_to_numbers.items():
        try:
            ddict[key] = value
        except DistinctError:
            pass

    print("ordinary dictionary:", names_to_numbers)
    print("distinctdict dictionary:", ddict)