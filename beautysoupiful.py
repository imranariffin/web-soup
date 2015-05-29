from bs4 import BeautifulSoup
import urllib2

#setup
url = "http://imranariffin.com/"
page = urllib2.urlopen(url)
soup = BeautifulSoup(page)

#demo
print "printing soupFB prettily...\n"
# print soup.prettify()
print "type(soup.prettify()): " + str(type(soup.prettify()))
print "type(soup): " + str(type(soup))
print "type(str(soup): " + str(type(str(soup)))
# print str(soup)
print "soup.html: "
print soup.html
# print soup