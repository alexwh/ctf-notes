#!/usr/bin/env python3

with open("token") as f:
    text = f.read().strip() # doesn't like newlines

for i, char in enumerate(text):
    print(chr(ord(char) - i), end='')
