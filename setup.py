from setuptools import setup, find_packages

import afh_dl

long_desc = ""
try:
    import pypandoc
    long_desc = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_desc = open('README.md').read()

setup(
    name = "afh-dl",
    version = "1.0.0",
    description = "A command-line tool for downloading files from AndroidFileHost.",
    long_description = long_desc,
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",        
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6"
    ],
    entry_points = {
        'console_scripts': [
            'afh-dl = afh_dl:main'
        ]
    },
    keywords = "android file host downloader",
    author = "Kade Robertson",
    author_email = "kade@kaderobertson.pw",
    url = "https://github.com/kade-robertson/afh-dl",
    license = "MIT",
    packages = find_packages(),
    install_requires = [
        "future",
        "requests",
        "humanize",
        "clint"
    ],
    python_requires = '>=2.7, <4',
)