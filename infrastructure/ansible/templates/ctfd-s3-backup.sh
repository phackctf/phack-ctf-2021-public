#!/bin/bash

USER="ctfd"
PASSWORD="{{ ctfd_db_password }}"
HOST="localhost"
DB_NAME="ctfd"

#Backup_Directory_Locations
BACKUPROOT="/tmp/backups"
TSTAMP=$(date +"%d-%b-%Y-%H-%M-%S")
S3BUCKET="s3://phack-ctfd-backup"

mkdir $BACKUPROOT
docker exec ctfd_db_1 mysqldump --user ctfd --password=jhqmponhggtftsfgsqm0e63dd ctfd | gzip -9 > $BACKUPROOT/$DB_NAME-$TSTAMP.sql.gz

if [ $? -ne 0 ]
then
mkdir /tmp/$TSTAMP
s3cmd put -r /tmp/$TSTAMP $S3BUCKET/
s3cmd sync -r $BACKUPROOT/ $S3BUCKET/$TSTAMP/
rm -rf $BACKUPROOT/*
else
 s3cmd sync -r $BACKUPROOT/ $S3BUCKET/$TSTAMP/
 rm -rf $BACKUPROOT/*
fi
