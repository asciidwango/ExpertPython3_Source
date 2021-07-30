"""
「非同期プログラミング」の節で登場するサンプルコード
非同期に対応していないライブラリをasyncioベースのアプリケーションで利用するために
`futures` やマルチスレッド・マルチプロセスを使う方法　

"""
import asyncio
import time

import requests

SYMBOLS = ('USD', 'EUR', 'PLN', 'NOK', 'CZK')
BASES = ('USD', 'EUR', 'PLN', 'NOK', 'CZK')
ACCESS_KEY = '<ACCESS_KEY>'

THREAD_POOL_SIZE = 4


async def fetch_rates(base):
    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(
        None, requests.get,
        f"http://api.exchangeratesapi.io/latest?access_key={ACCESS_KEY}&base={base}"
    )
    response.raise_for_status()
    rates = response.json()["rates"]
    # note: 同じ通貨の交換レートは 1:1 となる。
    rates[base] = 1.
    return base, rates


async def present_result(result):
    base, rates = (await result)

    rates_line = ", ".join(
        [f"{rates[symbol]:7.03} {symbol}" for symbol in SYMBOLS]
    )
    print(f"1 {base} = {rates_line}")


async def main():
    await asyncio.wait([
        asyncio.create_task(present_result(fetch_rates(base)))
        for base in BASES
    ])


if __name__ == "__main__":
    started = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    elapsed = time.time() - started

    print()
    print("経過時間: {:.2f}s".format(elapsed))
