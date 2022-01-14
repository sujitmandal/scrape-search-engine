import requests
from bs4 import BeautifulSoup

#Github: https://github.com/sujitmandal
#This programe is create by Sujit Mandal
"""
Github: https://github.com/sujitmandal
Pypi : https://pypi.org/user/sujitmandal/
LinkedIn : https://www.linkedin.com/in/sujit-mandal-91215013a/
"""

#search on google "my user agent"
# userAgent = ('') #my user agent
# search = ('') #Enter Anything for Search

httpResponseStatusCodes = {
    100 : 'Continue',
    101 : 'Switching Protocol',
    102 : 'Processing (WebDAV)',
    103 : 'Early Hints',
    201 : 'Created',
    202 : 'Accepted',
    203 : 'Non-Authoritative Information',
    204 : ' No Content',
    205 : 'Reset Content',
    206 : 'Partial Content',
    207 : 'Multi-Status (WebDAV)',
    208 : 'Already Reported (WebDAV)',
    226 : 'IM Used (HTTP Delta encoding)',
    300 : 'Multiple Choice',
    301 : 'Moved Permanently',
    203 : 'Found',
    303 : 'See Other',
    304 : 'Not Modified',
    305 : 'Use Proxy',
    306 : 'unused',
    307 : 'Temporary Redirect',
    308 : 'Permanent Redirect',
    400 : 'Bad Request',
    401 : 'Unauthorized',
    402 : 'Payment Required',
    403 : 'Forbidden',
    404 : 'Not Found',
    405 : 'Method Not Allowed',
    406 : 'Not Acceptable',
    407 : 'Proxy Authentication Required',
    408 : 'Request Timeout',
    409 : 'Conflict',
    410 : 'Gone',
    411 : 'Length Required',
    412 : 'Precondition Failed',
    413 : 'Payload Too Large',
    414 : 'URI Too Long',
    415 : 'Unsupported Media Type',
    416 : 'Range Not Satisfiable',
    417 : 'Expectation Failed',
    418 : 'I am a teapot',
    421 : 'Misdirected Request',
    422 : 'Unprocessable Entity (WebDAV)',
    423 : 'Locked (WebDAV)',
    424 : 'Failed Dependency (WebDAV)',
    425 : 'Too Early',
    426 : 'Upgrade Required',
    428 : 'Precondition Required',
    429 : 'Too Many Requests',
    431 : 'Request Header Fields Too Large',
    451 : 'Unavailable For Legal Reasons',
    500 : 'Internal Server Error',
    501 : 'Not Implemented',
    502 : 'Bad Gateway',
    503 : 'Service Unavailable',
    504 : 'Gateway Timeout',
    505 : 'HTTP Version Not Supported',
    506 : 'Variant Also Negotiates',
    507 : 'Insufficient Storage (WebDAV)',
    508 : 'Loop Detected (WebDAV)',
    510 : 'Not Extended',
    511 : 'Network Authentication Required'
}

def Google(search, userAgent):
    URL = ('https://google.com/search?q=' + search)
    headers = {'user-agent' : userAgent}
    request = requests.get(URL, headers=headers)

    results = []
    texts = []
    if request.status_code == 200:
        soup = BeautifulSoup(request.content, 'html.parser')

        for i in soup.find_all('div', {'class' : 'yuRUbf'}):
            link = i.find_all('a')
            link_text = i.find('h3')
            links = link[0]['href']
            results.append(links)
            texts.append(link_text.text)
    else:
        results.append('HTTP Status : {}'.format(httpResponseStatusCodes.get(request.status_code)))
        texts.append('HTTP Status : {}'.format(httpResponseStatusCodes.get(request.status_code)))

    return(texts, results)

def Duckduckgo(search , userAgent):
    URL = ('https://duckduckgo.com/html/?q=' + search)
    headers = {'user-agent' : userAgent}
    request = requests.get(URL, headers=headers)

    results = []
    texts = []
    if request.status_code == 200:
        soup = BeautifulSoup(request.content, 'html.parser')

        for i in soup.find_all('a', attrs={'class':'result__a'}):
            links = i['href']
            results.append(links)
            texts.append(i.text)
    else:
        results.append('HTTP Status : {}'.format(httpResponseStatusCodes.get(request.status_code)))
        texts.append('HTTP Status : {}'.format(httpResponseStatusCodes.get(request.status_code)))

    return(texts, results)

def Ecosia(search, userAgent):
    URL = ('https://www.ecosia.org/search?q='+search)
    headers = {'user-agent' : userAgent}
    request = requests.get(URL, headers=headers)

    results = []
    texts = []
    if request.status_code == 200:
        soup = BeautifulSoup(request.content, 'html.parser')
        text = []

        for i in soup.find_all('div', {'class' : 'result-firstline-container'}):
            link = i.find_all('a')
            link_text = i.find('a')
            links = link[0]['href']
            results.append(links)
            text.append(link_text.text)

        for j in text:
            a = j.strip()
            texts.append(a)
    else:
        results.append('HTTP Status : {}'.format(httpResponseStatusCodes.get(request.status_code)))
        texts.append('HTTP Status : {}'.format(httpResponseStatusCodes.get(request.status_code)))
    
    return(texts, results)

def Bing(search, userAgent):
    URL = ('https://www.bing.com/search?q='+search)
    headers = {'user-agent' : userAgent}
    request = requests.get(URL, headers=headers)

    results = []
    texts = []
    if request.status_code == 200:
        soup = BeautifulSoup(request.content, "html.parser")

        for i in soup.find_all('li', {'class' : 'b_algo'}):
            link = i.find_all('a')
            link_text = i.find('a')
            links = link[0]['href']
            results.append(links)
            texts.append(link_text.text)
    else:
        results.append('HTTP Status : {}'.format(httpResponseStatusCodes.get(request.status_code)))
        texts.append('HTTP Status : {}'.format(httpResponseStatusCodes.get(request.status_code)))
 
    return(texts, results)

def Givewater(search, userAgent):
    URL = ('https://search.givewater.com/serp?q='+search)
    headers = {'user-agent' : userAgent}
    request = requests.get(URL, headers=headers)

    results = []
    texts = []
    if request.status_code == 200:
        soup = BeautifulSoup(request.content, 'html.parser')

        for i in soup.find_all('div', {'class' : 'web-bing__result'}):
            link = i.find_all('a')
            link_text = i.find('a')
            links = link[0]['href']
            results.append(links)
            texts.append(link_text.text)
    else:
        results.append('HTTP Status : {}'.format(httpResponseStatusCodes.get(request.status_code)))
        texts.append('HTTP Status : {}'.format(httpResponseStatusCodes.get(request.status_code)))

    return(texts, results)

def Yahoo(search, userAgent):
    URL = ('https://search.yahoo.com/search?q=' + search)
    request = requests.get(URL)

    results = []
    texts = []
    if request.status_code == 200:
        soup = BeautifulSoup(request.content, 'html.parser')

        for i in soup.find_all(attrs={"class": "d-ib ls-05 fz-20 lh-26 td-hu tc va-bot mxw-100p"}):
            results.append(i.get('href'))
            texts.append(i.text)
    else:
        results.append('HTTP Status : {}'.format(httpResponseStatusCodes.get(request.status_code)))
        texts.append('HTTP Status : {}'.format(httpResponseStatusCodes.get(request.status_code)))

    return(texts, results)

if __name__ == "__main__":
    Bing(search, userAgent)
    Yahoo(search, userAgent)
    Google(search, userAgent)
    Ecosia(search, userAgent)
    Givewater(search, userAgent)
    Duckduckgo(search, userAgent)
