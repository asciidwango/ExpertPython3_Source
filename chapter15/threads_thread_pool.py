"""
「スレッドを使用したアプリケーション例」の節で登場するサンプルコード
シンプルなスレッドプールの実装方法

"""
import time
from queue import Queue, Empty
from threading import Thread

import requests

THREAD_POOL_SIZE = 4


SYMBOLS = ('USD', 'EUR', 'PLN', 'NOK', 'CZK')
BASES = ('USD', 'EUR', 'PLN', 'NOK', 'CZK')
ACCESS_KEY = '<ACCESS_KEY>'


def fetch_rates(base):
    response = requests.get(
        f"http://api.exchangeratesapi.io/latest?access_key={ACCESS_KEY}&base={base}"
    )

    response.raise_for_status()
    rates = response.json()["rates"]
    # note: 同じ通貨の交換レートは 1:1 となる。
    rates[base] = 1.

    rates_line = ", ".join(
        [f"{rates[symbol]:7.03} {symbol}" for symbol in SYMBOLS]
    )
    print(f"1 {base} = {rates_line}")


def worker(work_queue):
    while not work_queue.empty():
        try:
            item = work_queue.get(block=False)
        except Empty:
            break
        else:
            fetch_rates(item)
            work_queue.task_done()


def main():
    work_queue = Queue()

    for base in BASES:
        work_queue.put(base)

    threads = [
        Thread(target=worker, args=(work_queue,))
        for _ in range(THREAD_POOL_SIZE)
    ]

    for thread in threads:
        thread.start()

    work_queue.join()

    while threads:
        threads.pop().join()


if __name__ == "__main__":
    started = time.time()
    main()
    elapsed = time.time() - started

    print()
    print("経過時間: {:.2f}s".format(elapsed))
