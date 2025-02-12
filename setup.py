#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 22:32:52 2019

@author: cole roberson
"""
from ftr_classifier.info import INFO

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages


setup(name='ftr_classifier2',
      py_modules=['ftr_classifier'],
      url = 'https://github.com/jonaskonig/ftr_classifier.git',
      author = 'cole robertson, Jonas Koenig',
      author_email = 'pypi@jonaskoenig.com',
      version = INFO['version'],
      license = 'MIT',
      packages=find_packages(),
      description = INFO['description'],
      long_description = INFO['long_description'],
      install_requires=[
            "spacy>=spacy",
            "pandas>=1.4.3 ",
            'openpyxl==3.0.10',
            'pathlib2==2.3.7.post1; python_version > "3.4"'],
        python_requires='>3.6.*',
        download_url='https://github.com/jonaskonig/future_modality/archive/{}.tar.gz'.format(INFO['version']),
        package_data = {'ftr_classifier':['data/lemma_map','data/meta_data','data/bibtex.bib']},
        classifiers = []
      )
