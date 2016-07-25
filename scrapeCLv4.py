#! Scrapes craigslist computer gigs to create a list of gigListing 
# objects with attributes entryID, title, date, link

# import requests and beautifulsoup4 modules
import requests, bs4
from datetime import datetime as dt, date
'''from slackclient import slackclient'''

# gigListing & cityLink object class definitions
class gigListing(object):
	def __init__(self, entryID, gigTitle, gigDate, gigLink):
		self.entryID = entryID
		self.title = gigTitle
		self.date = gigDate
		self.link = gigLink

class cityLink(object):
	def __init__(self, link, state, country):
		self.link = link
		self.state = state
		self.country = country

# country pick list creation and function to allow user selection of cities
def initializeUSLinks():
	cityLinkList = ['virgin.craigslist.org', 'puertorico.craigslist.org', 'micronesia.craigslist.org', 'wyoming.craigslist.org', 'wausau.craigslist.org', 'sheboygan.craigslist.org', 'northernwi.craigslist.org', 'milwaukee.craigslist.org', 'madison.craigslist.org', 'lacrosse.craigslist.org', 'racine.craigslist.org', 'janesville.craigslist.org', 'greenbay.craigslist.org', 'eauclaire.craigslist.org', 'appleton.craigslist.org', 'wv.craigslist.org', 'swv.craigslist.org', 'parkersburg.craigslist.org', 'wheeling.craigslist.org', 'morgantown.craigslist.org', 'huntington.craigslist.org', 'martinsburg.craigslist.org', 'charlestonwv.craigslist.org', 'yakima.craigslist.org', 'wenatchee.craigslist.org', 'spokane.craigslist.org', 'skagit.craigslist.org', 'seattle.craigslist.org', 'pullman.craigslist.org', 'olympic.craigslist.org', 'moseslake.craigslist.org', 'kpr.craigslist.org', 'bellingham.craigslist.org', 'winchester.craigslist.org', 'swva.craigslist.org', 'roanoke.craigslist.org', 'richmond.craigslist.org', 'blacksburg.craigslist.org', 'lynchburg.craigslist.org', 'harrisonburg.craigslist.org', 'norfolk.craigslist.org', 'fredericksburg.craigslist.org', 'danville.craigslist.org', 'charlottesville.craigslist.org', 'vermont.craigslist.org', 'stgeorge.craigslist.org', 'saltlakecity.craigslist.org', 'provo.craigslist.org', 'ogden.craigslist.org', 'logan.craigslist.org', 'wichitafalls.craigslist.org', 'waco.craigslist.org', 'victoriatx.craigslist.org', 'easttexas.craigslist.org', 'texoma.craigslist.org', 'bigbend.craigslist.org', 'sanmarcos.craigslist.org', 'sanantonio.craigslist.org', 'sanangelo.craigslist.org', 'odessa.craigslist.org', 'mcallen.craigslist.org', 'lubbock.craigslist.org', 'laredo.craigslist.org', 'killeen.craigslist.org', 'houston.craigslist.org', 'galveston.craigslist.org', 'elpaso.craigslist.org', 'delrio.craigslist.org', 'nacogdoches.craigslist.org', 'dallas.craigslist.org', 'corpuschristi.craigslist.org', 'collegestation.craigslist.org', 'brownsville.craigslist.org', 'beaumont.craigslist.org', 'austin.craigslist.org', 'amarillo.craigslist.org', 'abilene.craigslist.org', 'tricities.craigslist.org', 'nashville.craigslist.org', 'memphis.craigslist.org', 'knoxville.craigslist.org', 'jacksontn.craigslist.org', 'cookeville.craigslist.org', 'clarksville.craigslist.org', 'chattanooga.craigslist.org', 'sd.craigslist.org', 'siouxfalls.craigslist.org', 'rapidcity.craigslist.org', 'csd.craigslist.org', 'nesd.craigslist.org', 'myrtlebeach.craigslist.org', 'hiltonhead.craigslist.org', 'greenville.craigslist.org', 'florencesc.craigslist.org', 'columbia.craigslist.org', 'charleston.craigslist.org', 'providence.craigslist.org', 'york.craigslist.org', 'williamsport.craigslist.org', 'pennstate.craigslist.org', 'scranton.craigslist.org', 'reading.craigslist.org', 'poconos.craigslist.org', 'pittsburgh.craigslist.org', 'philadelphia.craigslist.org', 'meadville.craigslist.org', 'allentown.craigslist.org', 'lancaster.craigslist.org', 'harrisburg.craigslist.org', 'erie.craigslist.org', 'chambersburg.craigslist.org', 'altoona.craigslist.org', 'salem.craigslist.org', 'roseburg.craigslist.org', 'portland.craigslist.org', 'oregoncoast.craigslist.org', 'medford.craigslist.org', 'klamath.craigslist.org', 'eugene.craigslist.org', 'eastoregon.craigslist.org', 'corvallis.craigslist.org', 'bend.craigslist.org', 'tulsa.craigslist.org', 'stillwater.craigslist.org', 'oklahomacity.craigslist.org', 'enid.craigslist.org', 'lawton.craigslist.org', 'zanesville.craigslist.org', 'youngstown.craigslist.org', 'tuscarawas.craigslist.org', 'toledo.craigslist.org', 'sandusky.craigslist.org', 'mansfield.craigslist.org', 'limaohio.craigslist.org', 'dayton.craigslist.org', 'columbus.craigslist.org', 'cleveland.craigslist.org', 'cincinnati.craigslist.org', 'chillicothe.craigslist.org', 'athensohio.craigslist.org', 'ashtabula.craigslist.org', 'akroncanton.craigslist.org', 'nd.craigslist.org', 'grandforks.craigslist.org', 'fargo.craigslist.org', 'bismarck.craigslist.org', 'winstonsalem.craigslist.org', 'wilmington.craigslist.org', 'raleigh.craigslist.org', 'outerbanks.craigslist.org', 'onslow.craigslist.org', 'hickory.craigslist.org', 'greensboro.craigslist.org', 'fayetteville.craigslist.org', 'eastnc.craigslist.org', 'charlotte.craigslist.org', 'boone.craigslist.org', 'asheville.craigslist.org', 'watertown.craigslist.org', 'utica.craigslist.org', 'twintiers.craigslist.org', 'syracuse.craigslist.org', 'rochester.craigslist.org', 'potsdam.craigslist.org', 'plattsburgh.craigslist.org', 'oneonta.craigslist.org', 'newyork.craigslist.org', 'longisland.craigslist.org', 'ithaca.craigslist.org', 'hudsonvalley.craigslist.org', 'glensfalls.craigslist.org', 'fingerlakes.craigslist.org', 'elmira.craigslist.org', 'chautauqua.craigslist.org', 'catskills.craigslist.org', 'buffalo.craigslist.org', 'binghamton.craigslist.org', 'albany.craigslist.org', 'santafe.craigslist.org', 'roswell.craigslist.org', 'lascruces.craigslist.org', 'farmington.craigslist.org', 'clovis.craigslist.org', 'albuquerque.craigslist.org', 'southjersey.craigslist.org', 'newjersey.craigslist.org', 'jerseyshore.craigslist.org', 'cnj.craigslist.org', 'nh.craigslist.org', 'reno.craigslist.org', 'lasvegas.craigslist.org', 'elko.craigslist.org', 'scottsbluff.craigslist.org', 'omaha.craigslist.org', 'northplatte.craigslist.org', 'lincoln.craigslist.org', 'grandisland.craigslist.org', 'montana.craigslist.org', 'missoula.craigslist.org', 'kalispell.craigslist.org', 'helena.craigslist.org', 'greatfalls.craigslist.org', 'butte.craigslist.org', 'bozeman.craigslist.org', 'billings.craigslist.org', 'stlouis.craigslist.org', 'stjoseph.craigslist.org', 'springfield.craigslist.org', 'semo.craigslist.org', 'loz.craigslist.org', 'kirksville.craigslist.org', 'kansascity.craigslist.org', 'joplin.craigslist.org', 'columbiamo.craigslist.org', 'natchez.craigslist.org', 'northmiss.craigslist.org', 'meridian.craigslist.org', 'jackson.craigslist.org', 'hattiesburg.craigslist.org', 'gulfport.craigslist.org', 'stcloud.craigslist.org', 'marshall.craigslist.org', 'rmn.craigslist.org', 'minneapolis.craigslist.org', 'mankato.craigslist.org', 'duluth.craigslist.org', 'brainerd.craigslist.org', 'bemidji.craigslist.org', 'up.craigslist.org', 'thumb.craigslist.org', 'swmi.craigslist.org', 'saginaw.craigslist.org', 'porthuron.craigslist.org', 'nmi.craigslist.org', 'muskegon.craigslist.org', 'monroemi.craigslist.org', 'lansing.craigslist.org', 'kalamazoo.craigslist.org', 'jxn.craigslist.org', 'holland.craigslist.org', 'grandrapids.craigslist.org', 'flint.craigslist.org', 'detroit.craigslist.org', 'centralmich.craigslist.org', 'battlecreek.craigslist.org', 'annarbor.craigslist.org', 'worcester.craigslist.org', 'westernmass.craigslist.org', 'southcoast.craigslist.org', 'capecod.craigslist.org', 'boston.craigslist.org', 'westmd.craigslist.org', 'smd.craigslist.org', 'frederick.craigslist.org', 'easternshore.craigslist.org', 'baltimore.craigslist.org', 'annapolis.craigslist.org', 'maine.craigslist.org', 'shreveport.craigslist.org', 'neworleans.craigslist.org', 'monroe.craigslist.org', 'lakecharles.craigslist.org', 'lafayette.craigslist.org', 'houma.craigslist.org', 'cenla.craigslist.org', 'batonrouge.craigslist.org', 'westky.craigslist.org', 'owensboro.craigslist.org', 'louisville.craigslist.org', 'lexington.craigslist.org', 'eastky.craigslist.org', 'bgky.craigslist.org', 'wichita.craigslist.org', 'topeka.craigslist.org', 'swks.craigslist.org', 'seks.craigslist.org', 'salina.craigslist.org', 'nwks.craigslist.org', 'ksu.craigslist.org', 'lawrence.craigslist.org', 'waterloo.craigslist.org', 'ottumwa.craigslist.org', 'siouxcity.craigslist.org', 'quadcities.craigslist.org', 'masoncity.craigslist.org', 'iowacity.craigslist.org', 'fortdodge.craigslist.org', 'dubuque.craigslist.org', 'desmoines.craigslist.org', 'cedarrapids.craigslist.org', 'ames.craigslist.org', 'terrehaute.craigslist.org', 'southbend.craigslist.org', 'richmondin.craigslist.org', 'muncie.craigslist.org', 'tippecanoe.craigslist.org', 'kokomo.craigslist.org', 'indianapolis.craigslist.org', 'fortwayne.craigslist.org', 'evansville.craigslist.org', 'bloomington.craigslist.org', 'quincy.craigslist.org', 'springfieldil.craigslist.org', 'carbondale.craigslist.org', 'rockford.craigslist.org', 'peoria.craigslist.org', 'mattoon.craigslist.org', 'lasalle.craigslist.org', 'decatur.craigslist.org', 'chicago.craigslist.org', 'chambana.craigslist.org', 'bn.craigslist.org', 'twinfalls.craigslist.org', 'lewiston.craigslist.org', 'eastidaho.craigslist.org', 'boise.craigslist.org', 'honolulu.craigslist.org', 'valdosta.craigslist.org', 'statesboro.craigslist.org', 'savannah.craigslist.org', 'nwga.craigslist.org', 'macon.craigslist.org', 'columbusga.craigslist.org', 'brunswick.craigslist.org', 'augusta.craigslist.org', 'atlanta.craigslist.org', 'athensga.craigslist.org', 'albanyga.craigslist.org', 'treasure.craigslist.org', 'tampa.craigslist.org', 'tallahassee.craigslist.org', 'staugustine.craigslist.org', 'spacecoast.craigslist.org', 'miami.craigslist.org', 'sarasota.craigslist.org', 'pensacola.craigslist.org', 'panamacity.craigslist.org', 'orlando.craigslist.org', 'okaloosa.craigslist.org', 'ocala.craigslist.org', 'lakecity.craigslist.org', 'lakeland.craigslist.org', 'jacksonville.craigslist.org', 'cfl.craigslist.org', 'gainesville.craigslist.org', 'fortmyers.craigslist.org', 'fortlauderdale.craigslist.org', 'keys.craigslist.org', 'daytona.craigslist.org', 'miami.craigslist.org', 'washingtondc.craigslist.org', 'delaware.craigslist.org', 'nwct.craigslist.org', 'newhaven.craigslist.org', 'hartford.craigslist.org', 'newlondon.craigslist.org', 'westslope.craigslist.org', 'pueblo.craigslist.org', 'rockies.craigslist.org', 'fortcollins.craigslist.org', 'eastco.craigslist.org', 'denver.craigslist.org', 'cosprings.craigslist.org', 'boulder.craigslist.org', 'yubasutter.craigslist.org', 'visalia.craigslist.org', 'ventura.craigslist.org', 'susanville.craigslist.org', 'stockton.craigslist.org', 'siskiyou.craigslist.org', 'santamaria.craigslist.org', 'santabarbara.craigslist.org', 'slo.craigslist.org', 'sfbay.craigslist.org', 'sandiego.craigslist.org', 'sacramento.craigslist.org', 'redding.craigslist.org', 'palmsprings.craigslist.org', 'orangecounty.craigslist.org', 'monterey.craigslist.org', 'modesto.craigslist.org', 'merced.craigslist.org', 'mendocino.craigslist.org', 'losangeles.craigslist.org', 'inlandempire.craigslist.org', 'imperial.craigslist.org', 'humboldt.craigslist.org', 'hanford.craigslist.org', 'goldcountry.craigslist.org', 'fresno.craigslist.org', 'chico.craigslist.org', 'bakersfield.craigslist.org', 'texarkana.craigslist.org', 'littlerock.craigslist.org', 'jonesboro.craigslist.org', 'fortsmith.craigslist.org', 'fayar.craigslist.org', 'yuma.craigslist.org', 'tucson.craigslist.org', 'sierravista.craigslist.org', 'showlow.craigslist.org', 'prescott.craigslist.org', 'phoenix.craigslist.org', 'mohave.craigslist.org', 'flagstaff.craigslist.org', 'juneau.craigslist.org', 'kenai.craigslist.org', 'fairbanks.craigslist.org', 'anchorage.craigslist.org', 'tuscaloosa.craigslist.org', 'montgomery.craigslist.org', 'mobile.craigslist.org', 'huntsville.craigslist.org', 'gadsden.craigslist.org', 'shoals.craigslist.org', 'dothan.craigslist.org', 'bham.craigslist.org', 'auburn.craigslist.org']
	linkStateList = ['Virgin Islands', 'Puerto Rico', 'Guam', 'Wyoming', 'Wisconsin', 'Wisconsin', 'Wisconsin', 'Wisconsin', 'Wisconsin', 'Wisconsin', 'Wisconsin', 'Wisconsin', 'Wisconsin', 'Wisconsin', 'Wisconsin', 'West Virginia', 'West Virginia', 'West Virginia', 'West Virginia', 'West Virginia', 'West Virginia', 'West Virginia', 'West Virginia', 'Washington', 'Washington', 'Washington', 'Washington', 'Washington', 'Washington', 'Washington', 'Washington', 'Washington', 'Washington', 'Virginia', 'Virginia', 'Virginia', 'Virginia', 'Virginia', 'Virginia', 'Virginia', 'Virginia', 'Virginia', 'Virginia', 'Virginia', 'Vermont', 'Utah', 'Utah', 'Utah', 'Utah', 'Utah', 'Texas', 'Texas', 'Texas', 'Texas', 'Texas', 'Texas', 'Texas', 'Texas', 'Texas', 'Texas', 'Texas', 'Texas', 'Texas', 'Texas', 'Texas', 'Texas', 'Texas', 'Texas', 'Texas', 'Texas', 'Texas', 'Texas', 'Texas', 'Texas', 'Texas', 'Texas', 'Texas', 'Tennessee', 'Tennessee', 'Tennessee', 'Tennessee', 'Tennessee', 'Tennessee', 'Tennessee', 'Tennessee', 'South Dakota', 'South Dakota', 'South Dakota', 'South Dakota', 'South Dakota', 'South Carolina', 'South Carolina', 'South Carolina', 'South Carolina', 'South Carolina', 'South Carolina', 'Rhode Island', 'Pennsylvania', 'Pennsylvania', 'Pennsylvania', 'Pennsylvania', 'Pennsylvania', 'Pennsylvania', 'Pennsylvania', 'Pennsylvania', 'Pennsylvania', 'Pennsylvania', 'Pennsylvania', 'Pennsylvania', 'Pennsylvania', 'Pennsylvania', 'Pennsylvania', 'Oregon', 'Oregon', 'Oregon', 'Oregon', 'Oregon', 'Oregon', 'Oregon', 'Oregon', 'Oregon', 'Oregon', 'Oklahoma', 'Oklahoma', 'Oklahoma', 'Oklahoma', 'Oklahoma', 'Ohio', 'Ohio', 'Ohio', 'Ohio', 'Ohio', 'Ohio', 'Ohio', 'Ohio', 'Ohio', 'Ohio', 'Ohio', 'Ohio', 'Ohio', 'Ohio', 'Ohio', 'North Dakota', 'North Dakota', 'North Dakota', 'North Dakota', 'North Carolina', 'North Carolina', 'North Carolina', 'North Carolina', 'North Carolina', 'North Carolina', 'North Carolina', 'North Carolina', 'North Carolina', 'North Carolina', 'North Carolina', 'North Carolina', 'New York', 'New York', 'New York', 'New York', 'New York', 'New York', 'New York', 'New York', 'New York', 'New York', 'New York', 'New York', 'New York', 'New York', 'New York', 'New York', 'New York', 'New York', 'New York', 'New York', 'New Mexico', 'New Mexico', 'New Mexico', 'New Mexico', 'New Mexico', 'New Mexico', 'New Jersey', 'New Jersey', 'New Jersey', 'New Jersey', 'New Hampshire', 'Nevada', 'Nevada', 'Nevada', 'Nebraska', 'Nebraska', 'Nebraska', 'Nebraska', 'Nebraska', 'Montana', 'Montana', 'Montana', 'Montana', 'Montana', 'Montana', 'Montana', 'Montana', 'Missouri', 'Missouri', 'Missouri', 'Missouri', 'Missouri', 'Missouri', 'Missouri', 'Missouri', 'Missouri', 'Mississippi', 'Mississippi', 'Mississippi', 'Mississippi', 'Mississippi', 'Mississippi', 'Minnesota', 'Minnesota', 'Minnesota', 'Minnesota', 'Minnesota', 'Minnesota', 'Minnesota', 'Minnesota', 'Michigan', 'Michigan', 'Michigan', 'Michigan', 'Michigan', 'Michigan', 'Michigan', 'Michigan', 'Michigan', 'Michigan', 'Michigan', 'Michigan', 'Michigan', 'Michigan', 'Michigan', 'Michigan', 'Michigan', 'Michigan', 'Massachusetts', 'Massachusetts', 'Massachusetts', 'Massachusetts', 'Massachusetts', 'Maryland', 'Maryland', 'Maryland', 'Maryland', 'Maryland', 'Maryland', 'Maine', 'Louisiana', 'Louisiana', 'Louisiana', 'Louisiana', 'Louisiana', 'Louisiana', 'Louisiana', 'Louisiana', 'Kentucky', 'Kentucky', 'Kentucky', 'Kentucky', 'Kentucky', 'Kentucky', 'Kansas', 'Kansas', 'Kansas', 'Kansas', 'Kansas', 'Kansas', 'Kansas', 'Kansas', 'Iowa', 'Iowa', 'Iowa', 'Iowa', 'Iowa', 'Iowa', 'Iowa', 'Iowa', 'Iowa', 'Iowa', 'Iowa', 'Indiana', 'Indiana', 'Indiana', 'Indiana', 'Indiana', 'Indiana', 'Indiana', 'Indiana', 'Indiana', 'Indiana', 'Illinois', 'Illinois', 'Illinois', 'Illinois', 'Illinois', 'Illinois', 'Illinois', 'Illinois', 'Illinois', 'Illinois', 'Illinois', 'Idaho', 'Idaho', 'Idaho', 'Idaho', 'Hawaii', 'Georgia', 'Georgia', 'Georgia', 'Georgia', 'Georgia', 'Georgia', 'Georgia', 'Georgia', 'Georgia', 'Georgia', 'Georgia', 'Florida', 'Florida', 'Florida', 'Florida', 'Florida', 'Florida', 'Florida', 'Florida', 'Florida', 'Florida', 'Florida', 'Florida', 'Florida', 'Florida', 'Florida', 'Florida', 'Florida', 'Florida', 'Florida', 'Florida', 'Florida', 'Florida', 'District of Columbia', 'Delaware', 'Connecticut', 'Connecticut', 'Connecticut', 'Connecticut', 'Colorado', 'Colorado', 'Colorado', 'Colorado', 'Colorado', 'Colorado', 'Colorado', 'Colorado', 'California', 'California', 'California', 'California', 'California', 'California', 'California', 'California', 'California', 'California', 'California', 'California', 'California', 'California', 'California', 'California', 'California', 'California', 'California', 'California', 'California', 'California', 'California', 'California', 'California', 'California', 'California', 'California', 'Arkansas', 'Arkansas', 'Arkansas', 'Arkansas', 'Arkansas', 'Arizona', 'Arizona', 'Arizona', 'Arizona', 'Arizona', 'Arizona', 'Arizona', 'Arizona', 'Alaska', 'Alaska', 'Alaska', 'Alaska', 'Alabama', 'Alabama', 'Alabama', 'Alabama', 'Alabama', 'Alabama', 'Alabama', 'Alabama', 'Alabama']
	overallLinkList = []
	y = 0
	while y < len(cityLinkList):
		linkEntry = cityLink(cityLinkList[y],linkStateList[y],"United States")
		overallLinkList.append(linkEntry)
		y += 1
	return overallLinkList

def linkFilter(overallLinkList):
	statesList = []
	query1 = input("Would you like to search all states? Enter Y or N: ")
	if query1 == "Y":
		return overallLinkList
	else:
		state = input("Please enter the exact name of the State you would like to include in your craigslist search: ")
		statesList.append(state)
		addCheck = input("Do you want to add another state? Enter Y or N: ")
		while addCheck == "Y":
			state = input("Please enter the exact name of a State you would like to include in your craigslist search: ")
			statesList.append(state)
			addCheck = input("Do you want to add another state? Enter Y or N: ")
		filteredLinkList = []
		for i in overallLinkList:
			if i.state in statesList:
				filteredLinkList.append(i)
		return filteredLinkList

# scrape and parse of craigslist/cpg page, extend to multiple cities soon
def downloadGigs(cityPartialURL):
	cityURL = 'https://' + cityPartialURL + '/search/cpg'
	res = requests.get(cityURL)
	print("Downloading gigs from " + cityURL + "...")
	res.raise_for_status()
	clGigs = bs4.BeautifulSoup(res.text)
	gigTitles = clGigs.select('#titletextonly')
	gigDates = clGigs.select('span time')
	gigLinks = clGigs.select('#sortable-results .rows a')
	gigTitleList = []
	gigDateList = []
	gigLinkList = []
	for i in gigTitles:
		gigTitleList.append(i.getText())
	for i in gigDates:
		gigDateList.append(i['datetime'])
	for i in gigLinks:
		if 'craigslist' in str(i['href']):
			gigLinkList.append('https://' + str(i['href']))
		else:
			gigLinkList.append('https://' + cityPartialURL + str(i['href']))
	return (cityURL, gigTitleList, gigDateList, gigLinkList)

# creation of gigListing objects from parsed info lists, and creation of overall list to store gig objects
def createGigEntries(cityIndex, cityURL, gigTitleList, gigDateList, gigLinkList):
	x = 0;
	while x < len(gigTitleList):
		entryID = "00" + str(cityIndex) + "_" + str(x);
		gigTitle = gigTitleList[x]
		gigDate = gigDateList[x]
		gigLink = gigLinkList[x]
		gigKey = "gigEntry_" + str(entryID)
		gigEntry = gigListing(entryID, gigTitle, gigDate, gigLink)
		overallGigsList.append(gigEntry)
		x+=1
	return

# main driver
overallGigsList = []
postFilterGigsList = []
cityIndex = 1
overallLinkList = initializeUSLinks()
filteredLinkList = linkFilter(overallLinkList)
scrapeFile = open('scrapeAttempt.txt', 'w')
scrapeFile.write("EntryID,Timestamp,Title,Link\n")
for a in filteredLinkList:
	cityURL, gigTitleList, gigDateList, gigLinkList = downloadGigs(a.link)
	createGigEntries(cityIndex, cityURL, gigTitleList, gigDateList, gigLinkList)
	print("Progress: " + str(round(cityIndex/len(filteredLinkList)*100,2)) + "%")
	cityIndex += 1
print(len(overallGigsList))
for i in overallGigsList:
	iDateYear = i.date[2:4]
	iDateMonth = i.date[5:7]
	iDateDay = i.date[8:10]
	iDate = str(iDateMonth) + "/" + str(iDateDay) + "/" + str(iDateYear)
	a = dt.strptime(str(iDate), "%m/%d/%y")
	b = dt.strptime(date.today().strftime("%m/%d/%y"), "%m/%d/%y")
	if a >= b:
		postFilterGigsList.append(i)
for i in postFilterGigsList:
	scrapeFile.write(i.entryID + ", " + i.date[0:11] + ", " + i.title + ", " + i.link + "\n")
print("Process Complete. Check scrapeAttempt.txt in your local directory for gig list.")


''' #initialize Slack Bot
SLACK_TOKEN = "xoxp-62700144342-62708409989-62699012484-151adf3f90"
SLACK_CHANNEL = "#gigs"

sc = SlackClient(SLACK_TOKEN)
desc = "{0} | {1} | {2} | {3} | <{4}>".format(result["area"], result["price"], result["bart_dist"], result["name"], result["url"])
sc.api_call(
	"chat.postMessage", channel=SLACK_CHANNEL, text=desc,
	username='pybot', icon_emoji=':robot_face:'
	)
'''
