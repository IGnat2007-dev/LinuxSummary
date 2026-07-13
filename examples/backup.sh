#!/bin/bash

BACKUP_DIR="./my_backups"

check_and_copy () {
local FILE=$1
if [ -f "$FILE" ]; then 
	cp "$FILE" "$BACKUP_DIR/"
	echo "File $FILE coppied successfully!"
else return 0 
fi
}

if [ ! -d "$BACKUP_DIR" ]; then
echo "Creating dir for backups...."
mkdir -p my_backups
else echo "Directory for backups already exists!"
fi

for file in *;
do 
	if [ "$file" == 'backup.sh' ]; then 
		continue
	else check_and_copy "$file"
	fi
done

echo "SUCCESS"
exit 0
