import setuptools
import wbubbler


# To run: python setup.py sdist bdist_wheel
# To upload: python -m twine upload --sign --skip-existing (--comment COMMENT) (--repository testpypi) dist/*


with open('README.md', 'r', encoding='utf-8') as readme_file:
    long_description = readme_file.read()

setuptools.setup(
    name='wbubbler',
    version=wbubbler.__version__,
    author='JMcB',
    author_email='joel.mcbride1@live.com',
    license='GPLv3',
    description='The Wbubbler package.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/wbubblerteam/wbubblerpy',
    packages = setuptools.find_packages(),
    python_requires='>=3',
)
