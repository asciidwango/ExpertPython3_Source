"""
「非同期プログラミング」の節で登場するサンプルコード
数字列を非同期に表示する

"""
import asyncio


async def print_number(number):
    print(number)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()

    loop.run_until_complete(
        asyncio.wait([
            loop.create_task(print_number(number))
            for number in range(10)
        ])
    )
    loop.close()
