#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = ['numpy>=1.22']

test_requirements = ['pytest']

setup(
    packages=find_packages(),
    install_requires=requirements,
    tests_require=test_requirements,
    test_suite='tests',
    zip_safe=False,
)
