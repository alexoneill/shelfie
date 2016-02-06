from bs4 import BeautifulSoup
import urllib
url = 'http://www.amazon.com/s/ref=nb_sb_noss_1?url=search-alias%3Dstripbooks&field-keywords=asimov'
r = urllib.urlopen(url).read()
soup = BeautifulSoup(r)

for e in soup.find_all(class_="a-link-normal s-access-detail-page  a-text-normal"):
	print e["title"]