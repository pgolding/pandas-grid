# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='griddy',
    version='0.1.0',
    description='Grid-based HTML renderer for Pandas',
     classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities',
      ],
    long_description=readme,
    author='Paul Golding',
    author_email='paul@paulgolding.com',
    url='https://github.com/pgolding/pandas-grid',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    package_data={'griddy':['resources/*']},
    install_requires=[
        'jinja2',
        'pandas'
    ]
)

