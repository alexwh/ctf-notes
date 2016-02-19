#!/usr/bin/env python3

text = "857:g67?5ABBo:BtDA?tIvLDKL{MQPSRQWW."

for i, char in enumerate(text):
    print(chr(ord(char) - i), end='')
