# import os
template = '''<!DOCTYPE HTML>
<!--
	Directive by HTML5 UP
	html5up.net | @n33co
	Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
-->
<html>
	<head>
		<title>shelfie results</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1" />
    <!--[if lte IE 8]><script src="{{root}}/js/ie/html5shiv.js"></script><![endif]-->
    <link rel="stylesheet" href="{{root}}/css/main.css" />
    <!--[if lte IE 8]><link rel="stylesheet" href="{{root}}/css/ie8.css" /><![endif]-->
	</head>
	<body>
		<!--book,author,link-->
		Suggestions based on "%s" by %s:
		<ul>%s</ul>
	</body>
</html>'''

li = '<li>\"%s\" by %s</li>'
title = 'The Book'
author = 'That Guy'
books = [['Book A','Author 1'],['Book B','Author 2'],['Book C','Author 3']]
lis = ''
for book in books:
	lis += li%(book[0],book[1])
f = open('screen.html','w')
f.write(template%(title,author,lis))
f.close()
# os.system('scp screen.')