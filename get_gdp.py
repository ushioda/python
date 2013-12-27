#! usr/bin/python
# -*- coding: utf-8 -*- 

import urllib3
from bs4 import BeautifulSoup
 
http = urllib3.PoolManager()
r = http.request('GET', 'http://aoimorirailway.com/jikoku/zikoku_2_018.html')
s = r.data

soup = BeautifulSoup(s)

table = soup.findAll("table")
print table


# row = table.findAll("tr")
# print row