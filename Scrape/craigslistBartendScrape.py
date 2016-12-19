from bs4 import BeautifulSoup
import requests
import datetime
import time
from datetime import timedelta
try:
    from urlparse import urljoin  # PY2
except ImportError:
    from urllib.parse import urljoin  # PY3

keywordTerm = input("If one exists, please enter the keyword you'd like to filter gig titles for: ")

def defineCities():
    urlList = ['http://austin.craigslist.org/search/ggg','http://austin.craigslist.org/search/jjj']
    index = 100
    numberList = []
    while index <= 2400:
        numberList.append(index)
        index += 100
    for number in numberList:
        numberURL = 'http://austin.craigslist.org/search/jjj?s=%s' % number
        urlList.append(numberURL)
    return urlList

def downloadGigs(urlList):
    resultsList = []
    for i in urlList:
        # status printing if running in console//currently commented out to write to file
        #print('Retrieving gigs from %s... Progress: %s / 100' % (i , round((urlList.index(i)/len(urlList)/100)*10000,2)))
        response = requests.get(i)
        soup = BeautifulSoup(response.content, 'html.parser')
        for row in soup.find_all('li', {'class': 'result-row'}):
            link = row.find('a', {'class': 'result-title hdrlnk'})
            id = link.attrs['data-id']
            name = link.text
            url = urljoin(i, link.attrs['href'])
            time = row.find('time')
            if time:
                datetime = time.attrs['datetime']
            else:
                pl = row.find('span', {'class': 'pl'})
                datetime = pl.text.split(':')[0].strip() if pl else None
            result = {'id': id,
                'name': name,
                'url': url,
                'datetime': datetime,
            }
            resultsList.append(result)
    return resultsList

def filterDateGigsList(gigsList):
    index = 0
    filteredDateList = []
    for i in gigsList:
        listingTime = datetime.datetime.strptime(i['datetime'], '%Y-%m-%d %H:%M')
        yesterdaysDate = datetime.datetime.now() - timedelta(days=14)
        if listingTime > yesterdaysDate:
            filteredDateList.append(gigsList.pop(index))
        index += 1
    return filteredDateList

def filterSpamGigsList(filteredDateList):
    def is_spam(value):
        spamTerms = ['paid','hire','review','survey','home','rent','cash',
                     'pay','flex','facebook','sex','$$$','boss','secretary','loan',
                     'supplemental','income','sales','dollars','money']
        setSpam = False
        for term in spamTerms:
            if term in value.lower():
                setSpam = True
        return setSpam
    return [i for i in filteredDateList if not is_spam(i['name'])]

def filterKeywordGigsList(filteredSpamList):
    filteredKeywordList = []
    for i in filteredSpamList:
        if keywordTerm.lower() in i['name'].lower():
            filteredKeywordList.append(i)
    return filteredKeywordList

def printGigsList(filteredSpamList):
    print('ID | Date | Name | Link')
    for i in filteredSpamList:
        print(i['id'],' | ',i['datetime'],' | ',i['name'],' | ',i['url'])

urlList = defineCities()
gigsList = downloadGigs(urlList)
# debug
# print(gigsList)
filteredDateList = filterDateGigsList(gigsList)
# debug
# print(filteredDateList)
filteredSpamList = filterSpamGigsList(filteredDateList)
filteredSpamList.sort(key=lambda i:i['datetime'], reverse=True)
if keywordTerm:
    filteredKeywordList = filterKeywordGigsList(filteredSpamList)
    printGigsList(filteredKeywordList)
else:
    printGigsList(filteredSpamList)