#!/bin/bash

while read line; do
    if [[ `echo $line | grep -o "Part"`] =~ "Part"  ]];then
        echo "${line}\"Timestamp\"," >> processed-log.csv
    else
        timestamps=$(echo $line | echo `grep -E -o '[0-9]{2}-\w{3}-[0-9]{4}\s[0-9]{2}:[0-9]{2}'`)
        timestamp=${timestamps:0:17}
        if [[ `echo $line | grep -o "Hong Kong Summer Time"` =~ "Hong Kong Summer Time" ]];then
            echo "${line}\"${timestamp} HKT\"," >> processed-log.csv
        fi
        if [[ `echo $line | grep -o "British Summer Time"` =~ "British Summer Time" ]];then
            echo "${line}\"${timestamp} BST\"," >> processed-log.csv
        fi
        if [[ `echo $line | grep -o "Japan Daylight Time"` =~ "Japan Daylight Time" ]];then
            echo "${line}\"${timestamp} JST\"," >> processed-log.csv
        fi
        if [[ `echo $line | grep -o "Greenwich Mean Time"` =~ "Greenwich Mean Time" ]];then
            echo "${line}\"${timestamp} GMT\"," >> processed-log.csv
        fi
    fi
done < log.csv