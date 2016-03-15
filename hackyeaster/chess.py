#!/usr/bin/env python3

state = """00000001
00100001
01001100
10101000
00100100
01000011
10000011
00000000"""

print("-".join(str(int(i, 2)) for i in state.split()))
