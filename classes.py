# from bs4 import BeautifulSoup
# import urllib2
from soupFunctions import *
from basic_functions import *

# class definitions
class SoupPage:
	"""
	SoupPage is a set of nodes
	node is a child page
	page has its own root link.
	"""
	def __init__(self, link):
		#the page's own link
		self.link = link
		# main page
		main_page = urllib2.urlopen(link)
		self.main_page = main_page
		# list of links the root page has
		# url = make_valid_url(link)
		self.links = get_page_links(link)
		#children pages pointed to by respective links
		self.pages = {}

	def add_page(self, link):
		# check if link is already in list of links
		if link in self.links:
			return False

		self.page = urllib2.urlopen(link);
		self.links.append(link)
		self.pages[link] = page

		return True

	# assumes child_url is relative url to parent (e.g. /about)
	def add_child_page(self, self_url, child_url):

		# ensures child_url is relative url
		if is_relative_url(child_url) != True:
			print "err: child_url not relative"
			return False

		# create child page
		child_full_url = self_url + child_url
		print "creating SoupPage(" + child_full_url + ")"
		child_page = SoupPage(child_full_url)
		# add child page to pages dictionary
		self.pages[child_url] = child_page

		return True

	def show_all_pages(self):
		for url in self.pages:
			print "url: " + url
			page = self.pages[url]
			print "self.pages[url]:"
			print_web(page)

	def set_page_links(self):
		#get links
		links = get_page_links(self.link)
		self.links = links

	def get_rel_links(self):
		rel_links = []
		for link in self.links:
			if is_relative_url(link) == True:
				rel_links.append(link)
		
		return rel_links

#web_page functions

def create_web(url):
	web_page = SoupPage(url)

	return web_page

def print_web(web_page):

	# print web_page's link
	print "root link: " + web_page.link

	# print basic information
	num_links = len(web_page.links)
	print "children links: " + str(num_links) + " in total"

def is_relative_url(url):
	""" relative url must start with / """
	if url[0] == '/':
		return True

	return False

class NodePage:

	def __init__(self, url, parent_url):
		self.url = url
		self.parent_url = parent_url
		# links are relative links to self (e.g. /about)
		self.links = []
		self.pages = {}

	# assumes child_url is relative url to parent (e.g. /about)
	def add_child_page(self, self_url, child_url):

		# ensures child_url is relative url
		if is_relative_url(child_url) != False:
			return False

		# create child page
		child_full_url = self_url + child_url
		child_page = urllib2.urlopen(child_full_url)
		# add child page to pages dictionary
		self.pages[child_url] = child_page

		return True


