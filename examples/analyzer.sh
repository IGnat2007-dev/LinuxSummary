#!/bin/bash 
 
FILES="text.txt index.html python.py config.cfg" 

for item in $FILES
do 
	if [ -f "$item" ]; then 
		echo "File $item founded!" 
		file "$item"
		echo -n "Has strings:"
		wc -l < "$item"
	else
		echo "File - [$item] don't exist"
	fi
	echo "---------------------------------------"
done
