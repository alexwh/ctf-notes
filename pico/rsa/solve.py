#!/usr/bin/env python3

import rsa


with open("ciphertext.txt") as file:
    ciphertext = bytes.fromhex(file.read())

with open("key_data.txt") as file:
    key_data = file.read()

dik = dict()
for value in key_data.splitlines():
    fields = value.split(" ")
    del fields[1] # del =
    dik[fields[0]] = int(fields[1], 0)

key = rsa.PrivateKey(**dik)
print(rsa.decrypt(ciphertext, key))
