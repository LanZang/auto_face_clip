#!/bin/bash

SCOUTER='/opt/scouter/bin/scouter.py'

while true
do
  if pgrep -x scouter.py
  then
    #The scouter exists.
    sleep 1
  else
    #Restart scouter.
    $SCOUTER &
  fi
done
