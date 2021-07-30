"""
「マルチプロセス」の節で登場するサンプルコード
POSIXシステムで os.fork を使って新しいプロセスを生成する

"""
import os

pid_list = []


def main():
    pid_list.append(os.getpid())
    child_pid = os.fork()

    if child_pid == 0:
        pid_list.append(os.getpid())
        print()
        print("子: こんにちは、私は子プロセスです")
        print("子: 私が知っているPID番号は %s です" % pid_list)

    else:
        pid_list.append(os.getpid())
        print()
        print("親: こんにちは、私は親プロセスです")
        print("親: 子プロセスのPID番号は %d です" % child_pid)
        print("親: 私が知っているPID番号は %s です" % pid_list)


if __name__ == "__main__":
    main()
