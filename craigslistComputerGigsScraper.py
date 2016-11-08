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
    citiesList = ['atlanta','tallahassee', 'chattanooga', 'myrtlebeach', 'houston', 'easttexas', 'santabarbara', 'norfolk', 'sandiego', 'newjersey', 'fresno', 'annapolis', 'montana', 'waco', 'neworleans', 'lasvegas', 'spokane', 'phoenix', 'tampa', 'milwaukee', 'dallas', 'newhaven', 'newyork', 'daytona', 'sd', 'rochester', 'detroit', 'richmond', 'philadelphia', 'florence', 'hartford', 'columbia', 'sfbay', 'denver', 'raleigh', 'saltlakecity', 'charlottesville', 'amarillo', 'iowacity', 'greenville', 'collegestation', 'boone', 'albuquerque', 'omaha', 'tricities', 'lexington','charlestonwv', 'savannah', 'cleveland', 'bend', 'madison', 'charleston', 'asheville', 'albany', 'harrisburg', 'staugustine', 'columbus', 'sacramento', 'lafayette', 'pennstate', 'jerseyshore', 'fortcollins', 'tucson', 'washingtondc', 'baltimore', 'indianapolis', 'austin', 'oklahomacity', 'birmingham', 'gainesville', 'delaware', 'jackson', 'longisland','provo',  'gulfport', 'seattle', 'minneapolis', 'athensga', 'louisville', 'portland', 'orangecounty', 'miami', 'boston', 'jacksonville','orlando','knoxville', 'boulder','chicago', 'vermont', 'reno','cincinnati','nashville', 'charlotte', 'wyoming','maine', 'florencesc', 'sanantonio', 'losangeles', 'augusta', 'honolulu', 'fortlauderdale']
    #citiesList = ['austin','charleston','seattle']
    for city in citiesList:
        cityURL = 'http://%s.craigslist.org/search/cpg' % city
        urlList.append(cityURL)
    return urlList

def downloadGigs(urlList):
    resultsList = []
    debugCounter = 0
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
        yesterdaysDate = datetime.datetime.now() - timedelta(days=3)
        if listingTime > yesterdaysDate:
            filteredDateList.append(gigsList.pop(index))
        index += 1
    return filteredDateList

def filterSpamGigsList(filteredDateList):
    def is_spam(value):
        spamTerms = ['paid','hire','work','review','survey','home','rent','cash',
                     'pay','flex','facebook','sex','$$$','boss','secretary','loan',
                     'supplemental','income','sales','dollars','money']
        setSpam = False
        for term in spamTerms:
            if term in value.lower():
                setSpam = True
        return setSpam
    return [i for i in filteredDateList if not is_spam(i['name'])]

def printGigsList(filteredSpamList):
    print('ID | Date | Name | Link')
    for i in filteredSpamList:
        print(i['id'],' | ',i['datetime'],' | ',i['name'],' | ',i['url'])

urlList = defineCities()
gigsList = downloadGigs(urlList)
filteredDateList = filterDateGigsList(gigsList)
filteredSpamList = filterSpamGigsList(filteredDateList)
filteredSpamList.sort(key=lambda i:i['datetime'], reverse=True)
printGigsList(filteredSpamList)