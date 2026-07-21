#!/bin/bash

echo "Enter your name:"
read -t 5 NAME

if [ -n "$NAME" ] ; then
       echo "Hi $NAME"
       exit 0
else 
	echo "you waste my time" 
	exit 1
fi
