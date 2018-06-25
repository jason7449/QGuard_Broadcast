#!/bin/sh
pid=$(sudo netstat -nap | grep 6666 |  cut -d'/' -f 1 | rev | cut -d' ' -f 1 | rev)
if [ $pid -ne 0 ]; then
    kill $pid
    echo "Close port successful!
    exit

else
    echo "Does not exist"
fi
