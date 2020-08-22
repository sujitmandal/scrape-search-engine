import json
import requests
from bs4 import BeautifulSoup

#Github: https://github.com/sujitmandal
#This programe is create by Sujit Mandal
"""
Github: https://github.com/sujitmandal
This programe is create by Sujit Mandal
LinkedIn : https://www.linkedin.com/in/sujit-mandal-91215013a/
Facebook : https://www.facebook.com/sujit.mandal.33671748
Twitter : https://twitter.com/mandalsujit37
"""

#search on google "my user agent"
#USER_AGENT = ('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36')
#search = ('')

userAgent = ('') #my user agent
search = ('') #Enter Anything for Search

def Google(search, userAgent):
    URL = ('https://google.com/search?q=' + search)
    headers = {'user-agent' : userAgent}
    request = requests.get(URL, headers=headers)

    if request.status_code == 200:
        soup = BeautifulSoup(request.content, 'html.parser')
        results = []
    
        for i in soup.find_all('div', {'class' : 'r'}):
            link = i.find_all('a')
            links = link[0]['href']
            results.append(links)
    return(results)

def Givewater(search, userAgent):
    URL = ('https://search.givewater.com/serp?q='+search)
    headers = {'user-agent' : userAgent}
    request = requests.get(URL, headers=headers)

    if request.status_code == 200:
        soup = BeautifulSoup(request.content, 'html.parser')
        results = []

        for i in soup.find_all('div', {'class' : 'web-bing__result'}):
            link = i.find_all('a')
            links = link[0]['href']
            results.append(links)
        return(results)


def Ecosia(search, userAgent):
    URL = ('https://www.ecosia.org/search?q='+search)
    headers = {'user-agent' : userAgent}
    request = requests.get(URL, headers=headers)

    if request.status_code == 200:
        soup = BeautifulSoup(request.content, 'html.parser')
        results = []

        for i in soup.find_all('div', {'class' : 'result-firstline-container'}):
            link = i.find_all('a')
            links = link[0]['href']
            results.append(links)
    return(results)

def Bing(search, userAgent):
    URL = ('https://www.bing.com/search?q='+search)
    headers = {'user-agent' : userAgent}
    request = requests.get(URL, headers=headers)

    if request.status_code == 200:
        soup = BeautifulSoup(request.content, "html.parser")
        results = []
    
        for i in soup.find_all('li', {'class' : 'b_algo'}):
            link = i.find_all('a')
            links = link[0]['href']
            results.append(links)
    return(results)

def Ask(search, userAgent):
    URL = ('https://www.ask.com/web?o=0&l=dir&qo=serpSearchTopBox&q='+search)
    headers = {'user-agent' : userAgent}
    request = requests.get(URL, headers=headers)

    if request.status_code == 200:
        soup = BeautifulSoup(request.content, 'html.parser')
        results = []
    
        for i in soup.find_all('div', {'class' : 'PartialSearchResults-item-title'}):
            link = i.find_all('a')
            links = link[0]['href']
            results.append(links)
        return(results)

def CommonLinks(search, userAgent):
    googleSearch = Google(search, userAgent)
    givewaterSearch = Givewater(search, userAgent)
    ecosiaSearch = Ecosia(search, userAgent)
    bingSearch = Bing(search, userAgent)
    askSearch = Ask(search, userAgent)
    

    googleSet = set(googleSearch)
    givewaterSet = set(givewaterSearch)
    ecosiaSet = set(ecosiaSearch)
    bingSet = set(bingSearch)
    askSet = set(askSearch)

    intersection1 = googleSet.intersection(givewaterSet)
    intersection2 = intersection1.intersection(ecosiaSet)
    intersection3 = intersection2.intersection(bingSet)
    intersection4 = intersection3.intersection(askSet)
    
    intersectionList = list(intersection4)
    finalList = []

    for i in intersectionList:
        finalList.append(i)

    finalList.sort()
    keys = []
    for i in range(len(finalList)):
        key = i + 1
        keys.append(key)

    commonDictionary = {}
    commonDictionary['CommonLinks'] = dict(zip(keys, finalList))
    return(commonDictionary)

def makeJson(name, searchEngine):
    keys = []

    for i in range(len(searchEngine)):
        key = i + 1
        keys.append(key)

    Dictionary = {}
    Dictionary[name] = dict(zip(keys, searchEngine))
    return(Dictionary)



if __name__ == "__main__":
    Ask(search, userAgent)
    Bing(search, userAgent)
    Google(search, userAgent)
    Ecosia(search, userAgent)
    Givewater(search, userAgent)
    CommonLinks(search, userAgent)
    makeJson(name, searchEngine)