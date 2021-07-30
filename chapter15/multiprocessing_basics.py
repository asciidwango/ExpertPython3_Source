"""
「マルチプロセス」の節で登場するサンプルコード
`multiprocessing` モジュールを用いて新しいプロセスを生成する

"""
from multiprocessing import Process
import os


def work(identifier):
    print(f'こんにちは、私はプロセス {identifier}, pid: {os.getpid()} です')


def main():
    processes = [
        Process(target=work, args=(number,))
        for number in range(5)
    ]
    for process in processes:
        process.start()

    while processes:
        processes.pop().join()


if __name__ == "__main__":
    main()
