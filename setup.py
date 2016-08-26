#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)

    with open(file_path, encoding='utf-8') as f:
        contents = f.read()

    return contents


setup(
    name='pytest-emoji',
    version='0.1.0',
    author='Raphael Pierzina',
    author_email='raphael@hackebrot.de',
    maintainer='Raphael Pierzina',
    maintainer_email='raphael@hackebrot.de',
    license='MIT',
    url='https://github.com/hackebrot/pytest-emoji',
    description='pytest + emoji',
    long_description=read('README.rst'),
    packages=[
        'pytest_emoji',
    ],
    package_dir={'pytest_emoji': 'pytest_emoji'},
    include_package_data=True,
    install_requires=['pytest>=3.0.1'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'pytest11': [
            'emoji = pytest_emoji.plugin',
        ],
    },
    keywords=['pytest', 'emoji'],
)
