# hackAmazon.py
# We don't want to register, so let's hack a BS4 API!!

from bs4 import BeautifulSoup
import urllib
# url = 'http://www.amazon.com/s/ref=nb_sb_noss_1?url=search-alias%3Dstripbooks&field-keywords=asimov'
# r = urllib.urlopen(url).read()
# soup = BeautifulSoup(r)

# for e in soup.find_all(class_="a-link-normal s-access-detail-page  a-text-normal"):
# 	print e["title"]
isbn = 99999
urlt = 'http://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Dstripbooks&field-keywords=%d&rh=n%3A283155%2Ck%3A%d'%(isbn,isbn)
print urlt
#http://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Dstripbooks&field-keywords=9780553900347&rh=n%3A283155%2Ck%3A9780553900347
# def 