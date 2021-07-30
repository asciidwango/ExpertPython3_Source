"""
「非同期プログラミング」の節で登場するサンプルコード
aiohttpを使って非同期にHTTPのリクエストを送信する方法

"""
import asyncio
import time

import aiohttp

from asyncrates import get_rates

SYMBOLS = ('USD', 'EUR', 'PLN', 'NOK', 'CZK')
BASES = ('USD', 'EUR', 'PLN', 'NOK', 'CZK')


async def fetch_rates(session, place):
    return await get_rates(session, place)


async def present_result(result):
    base, rates = (await result)

    rates_line = ", ".join(
        [f"{rates[symbol]:7.03} {symbol}" for symbol in SYMBOLS]
    )
    print(f"1 {base} = {rates_line}")


async def main():
    async with aiohttp.ClientSession() as session:
        await asyncio.wait([
            asyncio.create_task(present_result(fetch_rates(session, base)))
            for base in BASES
        ])


if __name__ == "__main__":
    started = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    elapsed = time.time() - started

    print()
    print(f"経過時間: {elapsed:.2f}s")
