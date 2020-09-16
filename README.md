## Scrape Search Engine :
[![Build Status](https://travis-ci.org/sujitmandal/scrape-search-engine.svg?branch=master)](https://travis-ci.org/sujitmandal/scrape-search-engine) [![GitHub license](https://img.shields.io/github/license/sujitmandal/scrape-search-engine)](https://github.com/sujitmandal/scrape-search-engine/blob/master/LICENSE) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/scrape-search-engine) ![PyPI - Wheel](https://img.shields.io/pypi/wheel/scrape-search-engine) ![PyPI](https://img.shields.io/pypi/v/scrape-search-engine)


[![Downloads](https://pepy.tech/badge/scrape-search-engine)](https://pepy.tech/project/scrape-search-engine)

Search anything on the different Search Engine's it will collect all the links and save it into 'json' file format.

## Package Installation : 
```
pip install scrape-search-engine
```
[Package Link](https://pypi.org/project/scrape-search-engine/)

## Scrape Search Engine :
search Anything on Search Engine it will collect the all the links ans save it into JSON file format.

## How to import the module:
```
userAgent = ('') #search on google "my user agent"
search = ('')  #Enter Anything for Search
```
## Google Search Engine : 
```
from ScrapeSearchEngine.ScrapeSearchEngine import Google

google = Google(search, userAgent)

print(google)

```
## Duckduckgo Search Engine : 
```
from ScrapeSearchEngine.ScrapeSearchEngine import Duckduckgo

duckduckgo = Duckduckgo(search, userAgent)

print(duckduckgo)
```
## Givewater Search Engine : 
```
from ScrapeSearchEngine.ScrapeSearchEngine import Givewater

givewater = Givewater(search, userAgent)

print(givewater)

```
## Ecosia Search Engine : 
```
from ScrapeSearchEngine.ScrapeSearchEngine import Ecosia

ecosia = Ecosia(search, userAgent)

print(ecosia)
```
## Bing Search Engine : 
```
from ScrapeSearchEngine.ScrapeSearchEngine import Bing

bing = Bing(search, userAgent)

print(bing)
```
## Ask Search Engine : 
```
from ScrapeSearchEngine.ScrapeSearchEngine import Ask

ask = Ask(search, userAgent)

print(ask)
```
## CommonLinks Search Engine : 
```
from ScrapeSearchEngine.ScrapeSearchEngine import CommonLinks

comminlinks = CommonLinks(search, userAgent)

print(comminlinks)

```
## Save into Json File formate :
```
from ScrapeSearchEngine.ScrapeSearchEngine import makeJson

googleJson = makeJson('google', google)

print(googleJson)

givewaterJson = makeJson('givewater', givewater)

print(givewaterJson)

ecosiaJson = makeJson('ecosia', ecosia)

print(ecosiaJson)

bingJson = makeJson('bing', bing)

print(bingJson)

askJson = makeJson('ask', ask)

print(askJson)

```
## Save All into Json File formate as finalJson :
```
finalJson = makeJson('finalJson',googleJson)

finalJson.update(givewaterJson)

finalJson.update(ecosiaJson)

finalJson.update(bingJson)

finalJson.update(askJson)

print(finalJson)
```

## Requirement’s:
```
• Python 

• Anaconda

• Visual Studio Code
```
## LINK’S:
• [Python Download](https://www.python.org/downloads/)

• [Anaconda Download](https://www.anaconda.com/downloads)

• [Visual Studio Download](https://code.visualstudio.com/Download)

## Linux:
 How to install Anaconda In Linux | Create Environment | Install TensorFlow | Opencv library |
 [![How to install | Python | | Anaconda | | Opencv library |](https://yt-embed.herokuapp.com/embed?v=Mfbrxy8gK6A)](https://www.youtube.com/watch?v=Mfbrxy8gK6A "How to install Anaconda In Linux | Create Environment | Install TensorFlow | Opencv library |")

##  Windows:
How to install | Python | | Anaconda | | Opencv library |
 [![How to install | Python | | Anaconda | | Opencv library |](https://yt-embed.herokuapp.com/embed?v=eVV3byQlYvA)](https://www.youtube.com/watch?v=eVV3byQlYvA "How to install | Python | | Anaconda | | Opencv library |")

## Installing the required package’s:
```
• pip install BeautifulSoup

• pip install requests

• pip install bs4
```
## License:
MIT Licensed

## Author:
Sujit Mandal

[GitHub](https://github.com/sujitmandal)

[PyPi](https://pypi.org/user/sujitmandal/)

[LinkedIn](https://www.linkedin.com/in/sujit-mandal-91215013a/)
