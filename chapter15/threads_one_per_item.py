"""
「スレッドを使用したアプリケーション例」の節で登場するサンプルコード
`threading` モジュールの使い方 (アイテムごとに1スレッドを使う)

"""
import time
from threading import Thread

import requests

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


def main():
    threads = []
    for base in BASES:
        thread = Thread(target=fetch_rates, args=[base])
        thread.start()
        threads.append(thread)

    while threads:
        threads.pop().join()


if __name__ == "__main__":
    started = time.time()
    main()
    elapsed = time.time() - started

    print()
    print("経過時間: {:.2f}s".format(elapsed))
