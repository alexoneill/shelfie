# hackAmazon.py
# We don't want to register, so let's hack a BS4 API!!

from bs4 import BeautifulSoup
import urllib
# url = 'http://www.amazon.com/s/ref=nb_sb_noss_1?url=search-alias%3Dstripbooks&field-keywords=asimov'
# r = urllib.urlopen(url).read()
# soup = BeautifulSoup(r)

# for e in soup.find_all(class_="a-link-normal s-access-detail-page  a-text-normal"):
# 	print e["title"]

# def amazonResults(isbn):
# 	# isbn = '9780545670319'
# 	url = 'http://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Dstripbooks&field-keywords='+str(isbn)+'&rh=n%3A283155%2Ck%3A'+str(isbn)
# 	r = urllib.urlopen(url).read()
# 	soup = BeautifulSoup(r)
# 	return soup

isbn = '9780545670319'
url = 'http://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Dstripbooks&field-keywords='+str(isbn)+'&rh=n%3A283155%2Ck%3A'+str(isbn)
r = urllib.urlopen(url).read()
soup = BeautifulSoup(r)
# print soup.prettify()
# <h2 class="a-size-medium a-color-null s-inline s-access-title a-text-normal">The Hunger Games Trilogy: The Hunger Games / Catching Fire / Mockingjay</h2>
res = soup.find(class_="a-size-medium a-color-null s-inline s-access-title a-text-normal")
itemTitle = res.contents
link = res.parent["href"]
print itemTitle
print link

r = urllib.urlopen(link).read()
soup = BeautifulSoup(r)
res = soup.find(class_="a-carousel-card a-float-left")
print res.prettify()
print '='*50
for e in res.find_all('a'):
	print '- %s'%e