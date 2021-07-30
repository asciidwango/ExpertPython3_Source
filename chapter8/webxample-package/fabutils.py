import os

# 'devpi'を使って専用のパッケージインデックスを作ったとします
PYPI_URL = 'http://devpi.webxample.example.com'

# これはリリース版をインストールするリモートサーバーのパス
# です。リリースディレクトリはプロジェクトのバージョンごとに
# 分かれていて、それぞれが独立した仮想環境ディレクトリです。
# 'current' は最後にデプロイされたバージョンを指すシンボリッ
# クリンクです。このシンボリックリンクはプロセス監視ツール
# などで参照されるディレクトリパスです。例:
# .
# ├── 0.0.1
# ├── 0.0.2
# ├── 0.0.3
# ├── 0.1.0
# └── current -> 0.1.0/

REMOTE_PROJECT_LOCATION = "/var/projects/webxample"


def prepare_release(c):
    """ 新しいリリースのために、ソース配布物を作って専用の
    パッケージインデックスにアップロードします
    """
    c.local(f'python setup.py build sdist')
    c.local(f'twine upload --repository-url {PYPI_URL}')


def get_version(c):
    """  setuptools経由で、現在のバージョンを取得します """
    return c.local('python setup.py --version').stdout.strip()


def switch_versions(c, version):
    """ シンボリックリンクを差し替えることでアトミックにバージョンを切り替えます """
    new_version_path = os.path.join(REMOTE_PROJECT_LOCATION, version)
    temporary = os.path.join(REMOTE_PROJECT_LOCATION, 'next')
    desired = os.path.join(REMOTE_PROJECT_LOCATION, 'current')

    # 既にある場合も強制的に(-f)シンボリックリンクを作成します
    c.run(f"ln -fsT {new_version_path} {temporary}")
    # mv -T によってこの操作をアトミックに行います
    c.run(f"mv -Tf {temporary} {desired}")