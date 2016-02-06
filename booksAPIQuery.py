import pprint
# import sys
from apiclient.discovery import build
import httplib2

api_key = 'AIzaSyBhtLjbQ5F3XoqEElobXVsNhpPf3nkR3WU'
try:
	service = build('books', 'v1', developerKey=api_key)
except Exception, e:
	# print 'Could not connect, exiting...'
	print e
	exit()

request = service.volumes().list(source='public', q='android')
response = request.execute()
pprint.pprint(response)

print 'Found %d books:' % len(response['items'])
for book in response.get('items', []):
  print 'Title: %s, Authors: %s' % (
    book['volumeInfo']['title'],
    book['volumeInfo']['authors'])