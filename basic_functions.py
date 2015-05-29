import os, webbrowser
import urllib2
from bs4 import BeautifulSoup

# basic functions

# list functions
def print_list(list):

	if len(list) == 0:
		print "list is empty"
		return -1

	for item in list:
		print item
	return True

def openpage(soup):
	
	webfile = urllib2.urlopen(soup.link)
	html = str(BeautifulSoup(webfile))

	path = os.path.abspath('temp.html')
	url = 'file://' + path

	print "opening " + path
	
	with open(path, 'w') as pagefile:
		pagefile.write(html)
	webbrowser.open(url)

	return True
