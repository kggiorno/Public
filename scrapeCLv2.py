#! Scrapes craigslist computer gigs to create a list of gigListing 
# objects with attributes entryID, title, date, link

#import requests and beautifulsoup4 modules
import requests, bs4

# gigListing object class definition
class gigListing(object):
	def __init__(self, entryID, gigTitle, gigDate, gigLink):
		self.entryID = entryID
		self.title = gigTitle
		self.date = gigDate
		self.link = gigLink

# scrape and parse of craigslist/cpg page, extend to multiple cities soon
res = requests.get('https://austin.craigslist.org/search/cpg')
res.raise_for_status()
clGigs = bs4.BeautifulSoup(res.text)
gigTitles = clGigs.select('#titletextonly')
gigDates = clGigs.select('span time')
gigLinks = clGigs.select('#sortable-results .rows a')


# further parsing/grabbing attributes from tag objects created by beatifulsoup parse above
gigTitleTextList = []
gigDatesTextList = []
gigLinksList = []
for i in gigTitles:
	gigTitleTextList.append(i.getText())
for i in gigDates:
	gigDatesTextList.append(i['datetime'])
for i in gigLinks:
	gigLinksList.append('https://austin.craigslist.org' + str(i['href']))

# creation of gigListing objects from parsed info lists, and creation of overall list to store gig objects
x = 0;
overallGigsList = []
while x < len(gigTitles):
	entryID = x;
	gigTitle = gigTitleTextList[x]
	gigDate = gigDatesTextList[x]
	gigLink = gigLinksList[x]
	gigKey = "gigEntry" + str(x)
	gigEntry = gigListing(entryID, gigTitle, gigDate, gigLink)
	overallGigsList.append(gigEntry)
	x+=1

#test print of first gig object's attributes
print(overallGigsList[0].entryID)
print(overallGigsList[0].gigTitle)
print(overallGigsList[0].gigDate)
print(overallGigsList[0].gigLink)