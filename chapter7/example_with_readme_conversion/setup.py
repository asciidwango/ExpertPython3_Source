from setuptools import setup
import os

try:
    from pypandoc import convert

    def read_asciidoc(file_path):
        return convert(file_path, to='rst', format='asciidoc')

except ImportError:
    convert = None
    print(
        "warning: pypandoc module not found, "
        "could not convert Asciidoc to RST"
    )

    def read_asciidoc(file_path):
        with open(file_path, encoding='utf-8') as f:
            return f.read()

README = os.path.join(os.path.dirname(__file__), 'README')

setup(
    name='some-package',
    long_description=read_asciidoc(README),
    long_description_content_type='text/x-rst',
    # ...
)
