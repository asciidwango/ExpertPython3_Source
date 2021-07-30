"""
「非同期プログラミング」の節で登場するサンプルコード
ブロックする命令の呼び出し時にイベントループの制御を解放し、2つのコルーチンを協調的に動作させる。

"""
import random
import asyncio


async def waiter(name):
    for _ in range(4):
        time_to_sleep = random.randint(1, 3) / 4
        await asyncio.sleep(time_to_sleep)
        print(f"{name} は {time_to_sleep} 秒待ちました")


async def main():
    await asyncio.wait([
        asyncio.create_task(waiter("first")),
        asyncio.create_task(waiter("second"))
    ])


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
