import requests, bs4

res = requests.get('http://www.craigslist.org/about/sites')
res.raise_for_status()
cityLinksHTML = bs4.BeautifulSoup(res.text)
cityLinksList = []
cityLinks = cityLinksHTML.select('li a')
for i in cityLinks:
	cityLinksList.append(i['href'])
print(cityLinksList)