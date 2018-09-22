#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='pling',
    version='0.0',
    author='Björn Lässig',
    url='https://github.com/pengutronix/pling',
    author_email='b.laessig@pengutronix.de',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'netaddr',
        'pyroute2',
        'ipython',
    ],
    scripts=[
        'bin/pling',
    ],
)
