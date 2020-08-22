## Scrape Search Engine :
search anything on Search Engine it will collect the all the links ans save it into JSON file format.

## Package Installation : 
```
pip install scrape-search-engine
```
[Package LInk](https://github.com/sujitmandal/scrape-search-engine)

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

[LinkedIn](https://www.linkedin.com/in/sujit-mandal-91215013a/)

[Facebook](https://www.facebook.com/sujit.mandal.33671748)

[Twitter](https://twitter.com/mandalsujit37)
