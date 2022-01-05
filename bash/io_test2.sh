#!/bin/bash

OPT1=$1   # User param #1
OPT2=$2   # User param #2
          # We can create as many of these as needed
AV_ARG=2
COUNT=$#  # Returns number of parameters user entered

io_test() {                         # Create a function called io_test
    if [ "$COUNT" -gt "$AV_ARG" ] ; then              # Check to see how many parameters user entered
        printf "TOO MANY ARGUMENTS!";
        exit                                 # Exit and show error if too many parameters
    else
        printf "Your First Parameter Was $OPT1 And The Second One Was $OPT2";   # Print parameters user entered
        exit
    fi
}

io_test   # Call function
