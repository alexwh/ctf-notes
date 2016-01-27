#!/usr/bin/env python2

with open("encrypted.txt") as file:
    input_data = file.read().decode("hex")

with open("encrypted.raw", "wb") as file:
    file.write(input_data)
