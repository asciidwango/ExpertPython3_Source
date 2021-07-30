import os

from distutils.core import setup
from distutils.extension import Extension

try:
    # Cythonがインストール済みの場合のみ、Cythonソースファイルをコンパイルします。
    import Cython
    # そしてCファイルを生成するためにCythonを使用するかどうか、
    # 特定の環境変数により指定します。
    USE_CYTHON = bool(os.environ.get("USE_CYTHON"))

except ImportError:
    USE_CYTHON = False

ext = '.pyx' if USE_CYTHON else '.c'

extensions = [Extension("fibonacci", ["fibonacci"+ext])]

if USE_CYTHON:
    from Cython.Build import cythonize
    extensions = cythonize(extensions)

setup(
    name='fibonacci',
    ext_modules=extensions,
    extras_require={
        # '[with-cython]'をパッケージのインストール時に指定することで、
        # 指定したバージョンのCythonがインストールされます。
        'with-cython': ['cython==0.23.4']
    }
)

