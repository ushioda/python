# -*- coding: utf-8 -*-

import urllib3
opener = urllib2.build_opener()
html = opener.open('http://kishi-r.com/2008/02/ubuntu_1.html').read()
print htmlimport urllib3
from bs4 import BeautifulSoup
 
url = "http://www.yahoo.co.jp"
htmlfp = urllib2.urlopen(url)
html = htmlfp.read().decode("utf-8", "replace")
htmlfp.close()
 
soup = BeautifulSoup(html)
for link in soup.findAll("a"):
	print link