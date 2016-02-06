# import pprint
# import sys
from apiclient.discovery import build
import httplib2
import hackAmazon as ha


api_key = 'AIzaSyBhtLjbQ5F3XoqEElobXVsNhpPf3nkR3WU'
try:
	service = build('books', 'v1', developerKey=api_key)
except Exception, e:
	# print 'Could not connect, exiting...'
	print e
	exit()

request = service.volumes().list(source='public', q='asimov', maxResults=3)
response = request.execute()
# pprint.pprint(response)

#Returns list of top n<=3 queries for title/author info
#(Title,Author,ISBN10,ISBN13,rating)
#Later: incorporate bonus data (e.g.book dimensions) for lolz
#	bvi['pageCount']
def top3Queries(q):
	result = []
	request = service.volumes().list(source='public', q='asimov', maxResults=3)
	response = request.execute()
	# print 'Found %d books:' % len(response['items'])
	for book in response.get('items', []):
		rating = None
		buyLink = None
		bvi = book['volumeInfo']
		if 'averageRating' in bvi:
			rating = '%.1f'%bvi['averageRating']
		
	  	ISBN10,ISBN13 = None,None
	  	for e in bvi['industryIdentifiers']:
	  		if '10' in e['type']:
	  			ISBN10 = e['identifier']
	  		if '13' in e['type']:
	  			ISBN13 = e['identifier']
	  	
	  	title = bvi['title']
	  	author = bvi['authors'][0] #main author
	  	result += [(title,author,ISBN10,ISBN13,rating)]
  	return result

print top3Queries('hunger games')
