# 比較しやすいようにタプル形式でのバージョン表記
VERSION = (0, 0, 1)
# 矛盾が生じないようにタプルから文字列を生成
__version__ = ".".join([str(x) for x in VERSION])
