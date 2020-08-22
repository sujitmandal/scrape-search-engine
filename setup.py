#!/bin/bash
__author__ = 'Sujit Mandal'
#Date : 22-08-2020
from setuptools import setup 

def readme():
    with open('README.md') as files:
        README = files.read()

    return(README)

setup(
    name = 'scrape-search-engine',
    version = '0.0.5',
    description = 'Search Anything on Search Engine it will collect the all the links ans save it into JSON file format.',
    long_description = readme(),
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/sujitmandal/scrape-search-engine',
    author = 'Sujit Mandal',
    author_email = 'mandals974@gmail.com',
    license = 'MIT',
    classifiers = [
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    packages = ['ScrapeSearchEngine'],
    include_package_data = True,
)
