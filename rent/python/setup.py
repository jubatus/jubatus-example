#!/usr/bin/env python

from setuptools import setup, find_packages
from jubahomes.version import get_version

setup(
    name             = 'jubahomes',
    version          = get_version(),
    description      = 'A sample to guess your rent.',
    packages         = find_packages(),
    install_requires = [
        'pyyaml',
        'jubatus',
    ],
    entry_points     = {
        'console_scripts': [
            'jubahomes = jubahomes.main:main',
        ]
    },
)
