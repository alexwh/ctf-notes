#!/usr/bin/env python2

from pwn import *
import operator
r = remote("188.166.133.53", 11027)
mapper = {
	"+": operator.sub,
	"-": operator.add,
	"*": operator.div,
}
for i in range(1, 101):
	r.readuntil("Level {}.: x ".format(i))
	type = r.recv(1)
	r.recv(1)
	first = r.recvuntil(" ").strip()
	r.recvuntil("= ")
	result = r.recvuntil("\n").strip()
	print(type, first, result)
	tosend = str(mapper[type](int(result), int(first)))
	print(tosend)
	r.sendline(tosend)
	output = r.recvuntil("\n")
print(r.recv(1024))
