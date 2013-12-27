#! usr/bin/python
# -*- coding: utf-8 -*- 

import urllib3
from bs4 import BeautifulSoup
 
http = urllib3.PoolManager()
r = http.request('GET', 'http://en.wikipedia.org/wiki/List_of_countries_by_GDP_(PPP)_per_capita')
s = r.data

soup = BeautifulSoup(s)
table = soup.findall("tr")
print table