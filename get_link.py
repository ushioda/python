#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import urllib3
from bs4 import BeautifulSoup
 
http = urllib3.PoolManager()
r = http.request('GET', 'http://www.aoki.e.u-tokyo.ac.jp')
s = r.data
 
soup = BeautifulSoup(s)
for link in soup.find_all('a'):
    print(link.get('href'))
