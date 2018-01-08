from setuptools import setup, find_packages

import afh_dl

setup(
    name = "afh-dl",
    version = "1.0.0.dev2",
    description = "A command-line tool for downloading files from AndroidFileHost.",
    long_description = "",
    classifiers = [
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
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
    install_requires = [],
    python_requires = '~=3.4',
)