#!/bin/bash

# Created By: D34D9001
# Jan. 1, 2022

##############   USER  VARIABLES   #################
####################################################
GPG_UID=""				           # GPG User ID
FILENAME="$(date +"%m%d%Y%H%M").txt" 		   # Filename to use for blog entry
MNT_DIR=""		                           # Mount directory of encrypted drive
BLOG_DIR=""  					   # Blog directory
####################################################


####################################################
TAR_FILE=""	                                   # Filename to use for tar file creation
ENC_TAR=""	                                   # Filename to use for GPG encrypted file
####################################################

####################################################
####################################################
####################################################


if [ -d $MNT_DIR ]; then
    if ! gpg -o $TAR_FILE -d $ENC_TAR; then
        echo "GPG FAILED!"
#        exit
    fi
    srm -v "$BLOG_DIR.tar.gz.gpg";
    tar xzvf $TAR_FILE -C "$MNT_DIR";
    sleep 3
    srm -v "$BLOG_DIR.tar.gz";
    nano "$BLOG_DIR/$FILENAME";
    sleep 1
    gpg -r $GPG_UID -e "$BLOG_DIR/$FILENAME";
    srm -v "$BLOG_DIR/$FILENAME";
    sleep 1
    tar czf $TAR_FILE $BLOG_DIR;
    srm -R -v $BLOG_DIR;
    sleep 3
    gpg -r $GPG_UID -e $TAR_FILE;
    srm -v "$BLOG_DIR.tar.gz";
    echo "$FILENAME Succesfully Encrypted";
    exit
else
    echo "$FILENAME WAS NOT CREATED! $MNT_DIR COULD NOT BE LOCATED...";
    exit
fi
