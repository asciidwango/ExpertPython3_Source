from time import sleep


class CounterState:
    def __init__(self, step):
        self.step = step

    def __next__(self):
        """カウンタ値を1つずつ0まで変更する"""
        if self.step <= 0:
            raise StopIteration
        self.step -= 1
        return self.step


class CountDown:
    def __init__(self, steps):
        self.steps = steps

    def __iter__(self):
        """自分をイテレータとして返す"""
        return CounterState(self.steps)


if __name__ == "__main__":
    print("カウントダウン:")

    for element in CountDown(10):
        print('*', element)
        sleep(0.2)
