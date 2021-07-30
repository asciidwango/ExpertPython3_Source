"""このモジュールはPythonバージョン間で変更があったものを
選択する、互換レイヤーを提供します
"""
import sys

if sys.version_info < (3, 0, 0):
    import urlparse  # noqa


    def is_string(s):
        """値が文字列ならTrueを返す"""
        return isinstance(s, basestring)

else:
    # メモ: Python 3ではurlparseはurllib.parseに移動した
    from urllib import parse as urlparse  # noqa


    def is_string(s):
        """値が文字列ならTrueを返す"""
        return isinstance(s, str)