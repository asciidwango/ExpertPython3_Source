import os

from setuptools import setup
from setuptools import find_packages
from distutils.cmd import Command
from distutils.command.build import build as _build

try:
    from django.core.management.commands.compilemessages \
        import Command as CompileCommand
except ImportError:
    # 注意: Djangoのインストール前にはimportできません
    CompileCommand = None

# この環境変数はCompileCommandを実行するのに必須です
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "webxample.conf.settings"
)


class build_messages(Command):
    """ カスタムコマンド: Django内のgettextメッセージをビルド
    """
    description = """compile gettext messages"""
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        if CompileCommand:
            CompileCommand().handle(
                verbosity=2, locale=[], exclude=[],
                ignore_patterns=[], fuzzy=False
            )
        else:
            raise RuntimeError("could not build translations")


class build(_build):
    """ 既存のbuildコマンドを上書きして、ビルド手順を追加
    """
    sub_commands = [
                       ('build_messages', None),
                       ('build_sass', None),
                   ] + _build.sub_commands


setup(
    name='webxample',
    setup_requires=[
        'libsass == 0.20.1',
        'django == 3.1.4',
    ],
    install_requires=[
        'django == 3.1.4',
        'gunicorn == 20.0.4',
        'djangorestframework == 3.12.2',
        'django-allauth == 0.44.0',
    ],
    packages=find_packages('.'),
    sass_manifests={
        'webxample.myapp': ('static/sass', 'static/css')
    },
    cmdclass={
        'build_messages': build_messages,
        'build': build,
    },
    entry_points={
        'console_scripts': {
            'webxample = webxample.manage:main',
        }
    }
)