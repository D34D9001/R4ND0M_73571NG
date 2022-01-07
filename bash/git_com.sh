#!/bin/bash

# Created By: D34D9001
# Jan. 1, 2022
######################

COM_MESS=$2   # Commit Message

AV_ARG=2
COUNT=$#  # Returns number of parameters user entered
ZERO=0

# HELP

help() {
    echo "USAGE: git_com.sh -m \"commit message\""
}

# COMMIT FUNCTION

commit() {                         # Create a function called io_test
    if [ "$COUNT" -gt "$AV_ARG" ] ; then              # Check to see how many parameters user entered
        printf "[❌] TOO MANY ARGUMENTS!\n";
        help
        exit;                                 # Exit and show error if too many parameters
    else
        printf "[...] Please wait while changes are commited...\n"
        git add -A
        git commit -m "$COM_MESS"
        git push origin
        printf "[✔] Repo Updates Commited With Message: $COM_MESS\n";   # Print parameters user entered
        exit
    fi
}

# MAIN

#if [ "$#" -eq "$ZERO" ] ; then
#    help
#    exit 0
#fi

while getopts ":hm" option; do
   case $option in
      h) # display Help
         help;
         exit;;
      m) # commit
         commit;
         exit;;
     \?) # Invalid option
         echo "[❌] INVALID OPTION!"
         help;
         exit;;
   esac
done

if [ $OPTIND -eq 1 ]; then
    echo "[❌] INVALID OPTION!"
    help
    exit 1
fi
