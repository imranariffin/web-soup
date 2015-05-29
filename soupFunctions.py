from bs4 import BeautifulSoup
import urllib2
# from basic_functions import *

# from classes import soup_page

def get_page_links(url):
	#open page
	page = urllib2.urlopen(url)
	#make soup
	soup = BeautifulSoup(page)

	links = []
	for linktag in soup.find_all('a'):
		# print "linktag: " + str(linktag)
		link = linktag.get('href')
		if link != None:
			links.append(link)

	return links

# recursively get links
def get_page_links_all(root, url, links):
	links = links

	if is_valid_url(url) == False:
		url = make_complete_url(url)

	print "url: " + urllib2

	page = urllib2.urlopen(url)
	if (page != True):
		return -1

	soup = BeautifulSoup(page)

	for linktag in soup.find_all('a'):
		link = linktag.get('href')
		print "in get_page_links_all: \nlink: " + link
		print "type(link): " + str(type(link))

		if link != None or link not in links:
			links.append(link)
			get_page_links_all(root, link, links)

	return links

def make_valid_url(url):
	if url[:7] != "http://":
		url = "http://" + url
	return url

def make_complete_url(child_url):
	print "make_complete_url"

def is_valid_url(url):

	#if got http:// or https:// return true
	if url[:7] == "http://" or url[:8] == "https://":
		return True
	else:
		return False
	#else return false

# def get_

def get_page_plaintext(url):

	print "get plain text of page " + str(url)

	return 0

#web_page functions

def create_web(url):
	web_page = soup_page(url)

	return web_page

def print_web(web_page):

	# print web_page's link
	print "link: " + web_page.link

	# print web_page's list of links
	print "children links: "
	print_list(web_page.links)

