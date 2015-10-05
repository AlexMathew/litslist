#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages


readme = open('README.md').read()
requirements = open('requirements.txt').read().split('\n')

setup(
    name='litslist',
    version='0.1',
    description='',
    long_description=readme,
    author='Alex Mathew',
    author_email='alexmathew003@gmail.com',
    url='https://alexmathew.github.io',
    packages=find_packages(exclude=('tests',)),
    package_dir={'litslist':
                 'litslist'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords=['els'],
    entry_points={
        'console_scripts': ['litslist = litslist.cmd:runCLI']
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4'
    ],
)
