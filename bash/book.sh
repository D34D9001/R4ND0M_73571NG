#!/bin/bash

# Created By: 73RM1N41
# Jan. 1, 2022

FILENAME=""    # filename of book
ENC_FILE=""    # name of encrypted file
DIR_PATH=""    # path to books directory
GPG_UN=""      # gpg key username
FILE=/etc/resolv.conf
if [ -f "" ]; then    # full path to book (ex: /home/[user]/Documents/my_book.txt)
    gpg -o $DIR_PATH/$FILENAME -d $DIR_PATH/$ENC_FILE
    srm -v $DIR_PATH/$ENC_FILE;
    echo "$FILENAME Succesfully Encrypted";
    nano $DIR_PATH/$FILENAME;
    gpg -r $GPG_UN -e $DIR_PATH/$FILENAME;
    srm -v $DIR_PATH/$FILENAME;
    echo "$FILENAME Succesfully Encrypted";
    exit
else
    echo "$FILENAME could not be located! Check to see if $DIR_PATH is mounted...";
    exit
fi
