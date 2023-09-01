#!/bin/bash

# Write a infinite loop which will 
# print current date
# sleep for some time 
# print a sequence of numbers
# continue loop 

# to test: 
# bash ./bashloop.sh 
# will print continuously until interrupted.

while :
  do
    echo $(date)
    sleep 1  # 10 secs
    for i in 1 2 3 4
    do
      echo $i
    done
  done
