#!/bin/bash

shopt -s nullglob

if [ -z "$1" ];
then
    echo "$0: missing output filename"
    exit 1
fi

# Auto-detect the modem device name
MODEM_DEVS=(`cd /dev && /bin/ls -1d cu.usb*`)
MODEM_DEV=/dev/${MODEM_DEVS[0]}

if [ ! -c $MODEM_DEV ];
then
    echo "$0: unable to determine USB modem device name"
    exit 1
fi

# Run the collector, teeing off its stdout into a results file
./collector.py $MODEM_DEV | tee -a $1
