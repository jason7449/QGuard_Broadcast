#!/bin/sh
pid=$(lsof -nP -i4TCP:6666 | grep LISTEN |  cut -c 9-12)
if [[ -n $pid ]]; then
    kill $pid
    echo "Close port successful!!
    exit
else
    echo "Does not exist"
fi
