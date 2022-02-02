#!/bin/bash

# Created By: D34D9001
# Date: 02/02/2022

# This script can be used to create a backup .tar.gz of a directory
# $ sh backup.sh [DIRECTORY]
# The backup file will be saved in the users current working directory

DIRNAME=$1
D_NAME=$(date +"%m%d%Y%H%M")
CUR_DIR=$(pwd)
OUTFILE="$DIRNAME$D_NAME"
if [ -d $DIRNAME ]; then
  tar -czvf "$OUTFILE.tar.gz" $DIRNAME/* -P
  if [ -e "$OUTFILE.tar.gz" ]; then
    echo "[*] Backup complete! Your backup file is: $CUR_DIR/$OUTFILE.tar.gz"
  else
    echo "[!] COULD NOT VERIFY FILE EXISTS... SOMETHING MAY HAVE WENT WRONG!"
    echo "    PLEASE CHECK FOR BACKUP FILE BEFORE RUNNING THIS SCRIPT AGAIN!"
    exit
  fi
else
  echo "[!] INVALID DIRECTORY!!!"
  exit
fi
