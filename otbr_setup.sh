#!/bin/bash

while ! ot-ctl reset
do
	echo Waiting for RCP up
	sleep 5 
done

while ! ot-ctl ifconfig up
do
	echo Waiting for ifconfig up
	sleep 5 
done

ot-ctl thread start
ot-ctl dataset init new
ot-ctl dataset networkkey 00112233445566778899aabbccddeeff
ot-ctl dataset channel 21
ot-ctl dataset panid 0xface
ot-ctl dataset networkname BlueIrisLabs 
ot-ctl dataset commit active
ot-ctl prefix add fd11:22::/64 pasor
ot-ctl txpower 2
ot-ctl netdata register

