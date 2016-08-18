from bs4 import BeautifulSoup
import requests
import datetime
from datetime import timedelta
try:
    from urlparse import urljoin  # PY2
except ImportError:
    from urllib.parse import urljoin  # PY3

def defineCities():
    urlList = []
    #citiesList = ['austin','charleston','phoenix','sandiego','losangeles','boulder','denver','hartford','delaware','washingtondc','daytona','orlando','jacksonville','miami','tampa','atlanta','honolulu','chicago','maine','neworleans','baltimore','boston','detroit','jackson','gulfport','kansascity','lasvegas','newyork','asheville','charlotte','columbus','philadelphia','pittsburgh','memphis','dallas','houston','sanantonio','richmond','seattle']
    citiesList = ['austin','charleston','newyork','denver','sandiego','jacksonville']
    for city in citiesList:
        cityURL = 'http://%s.craigslist.org/search/cpg' % city
        urlList.append(cityURL)
    return urlList

def downloadGigs(urlList):
    resultsList = []
    for i in urlList:
        print('Retrieving gigs from %s... Progress: %s / 100' % (i , round((urlList.index(i)/len(urlList)/100)*10000,2)))
        response = requests.get(i)
        soup = BeautifulSoup(response.content, 'html.parser')
        for row in soup.find_all('p', {'class': 'row'}):
            link = row.find('a', {'class': 'hdrlnk'})
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
        yesterdaysDate = datetime.datetime.now() - timedelta(days=1)
        if listingTime > yesterdaysDate:
            filteredDateList.append(gigsList.pop(index))
        index += 1
    return filteredDateList

def filterSpamList(filteredDateList):
    index = 0
    spamList = ['$','WANTED','wanted','Wanted','Fast','fast','pay','Pay','PAY','paid','PAID','Paying','PAYING','paying','TIRED','WORK','HOME','Money','money']
    filteredResults = []
    for i in filteredDateList:
        for x in spamList:
            if x in i['name']:
                filteredDateList.pop(index)
        index += 1
    return filteredDateList


urlList = defineCities()
gigsList = downloadGigs(urlList)
filteredDateList = filterDateGigsList(gigsList)
filteredList = filterSpamList(filteredDateList)
for i in filteredList:
    print('ID:',i['id'],'Time:',i['datetime'],' | ','Title:',i['name'],' | ',"Link:",i['url'])

