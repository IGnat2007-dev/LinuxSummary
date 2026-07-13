#!/bin/bash

echo "Hello ,my name is $MY_NAME, enter word that you want to find:"
read SECRET_WORD

echo '------------------------------------------------'
find . -name '*.txt' -type f 2>/dev/null | xargs grep -n "$SECRET_WORD" 2>/dev/null
echo '-----------------------------------------------------'
 
if [$? -eq 0 ]; then
	echo 'Search succeded'
else
	echo 'Nothing found or there is a mistake'
fi
