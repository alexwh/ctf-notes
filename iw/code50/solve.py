#!/usr/bin/env python2

from pwn import *
import operator
r = remote("188.166.133.53", 11027)
mapper = {
    "+": operator.sub,
    "-": operator.add,
    "*": operator.div,
}
r.recvline() # welcome
while True:
    output = r.recvline()
    if "IW" in output:
        break
    print(output)
    expr = output.split()
    # expr looks like ['Level', '1.:', 'x', '+', '7', '=', '11']
    oper = expr[3]
    first = expr[4]
    result = expr[6]
    answer = str(mapper[oper](int(result), int(first)))
    log.info(answer)
    r.sendline(answer)
    print(r.recvline())
print(output)
