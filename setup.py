__author__ = 'Sujit Mandal'
#Date : 22-08-2020
from setuptools import setup 

def readme():
    with open('README.md') as files:
        README = files.read()

    return(README)

setup(
    name = 'scrape-search-engine',
    version = '0.1.8',
    description = "Search anything on the different Search Engine's it will collect all the links.",
    long_description = readme(),
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/sujitmandal/scrape-search-engine',
    author = 'Sujit Mandal',
    author_email = 'mandals974@gmail.com',
    license = 'MIT',
    classifiers = [
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],

    packages = ['ScrapeSearchEngine'],
    include_package_data = True,
)