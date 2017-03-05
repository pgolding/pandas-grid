# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='grid',
    version='0.1.0',
    description='Grid-based HTML renderer for Pandas',
    long_description=readme,
    author='Paul Golding',
    author_email='paul@paulgolding.com',
    url='https://github.com/pgolding/pandas-grid',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

