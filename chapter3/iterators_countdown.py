from time import sleep


class CountDown:
    def __init__(self, step):
        self.step = step

    def __next__(self):
        """次の値を返す"""
        if self.step <= 0:
            raise StopIteration
        self.step -= 1
        return self.step

    def __iter__(self):
        """自分をイテレータとして返す"""
        return self


if __name__ == "__main__":
    print("カウントダウン:")

    for element in CountDown(10):
        print('*', element)
        sleep(0.2)
