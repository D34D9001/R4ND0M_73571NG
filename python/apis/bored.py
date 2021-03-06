#!/usr/bin/env python3

"""
Are you bored?? This program will generate
a random activity for you to do. Got friends?
Tell the program how many with the -f flag.

*8 friends max [The more friends you have the
less diverse your options will be.]

Created With: 'The Bored API' [https://www.boredapi.com/]
Created By: D34D9001
Jan. 10, 2022
"""

__author__ = "D34D9001"
__license__ = "MIT"
__version__ = "1.0.3"
__maintainer__ = "D34D9001"
__status__ = "Prototype"

import requests
import sys
import json
import getopt
from termcolor import colored

def solo_act(tries):
    try:
        r = requests.get("http://www.boredapi.com/api/activity?participants=1")
        r = r.json()

        index = 1

        if 'error' in r:

            while index <= int(tries):
                print("[*] Activity not found... Trying again.")
                r = requests.get("http://www.boredapi.com/api/activity?participants=1")
                r = r.json()
                index += 1

            if 'error' in r:
                print("[*] No activity found after %s tries... Try again later." % index)
                sys.exit()

        else:
            print("[7H3 80R3D 491]:\n                   Are you bored? Maybe you should...\n")
            print("                   [Activity]: " + str(r['activity']))

            if float(r['accessibility'] >= .5):
                print(colored("                   [Accessibility]: " + str(r['accessibility']), 'red', attrs=['bold']))

            else:
                print(colored("                   [Accessibility]: " + str(r['accessibility']), 'green', attrs=['bold']))
                print("                   [Type]: " + str(r['type']))
                print("                   [Participants]: " + str(r['participants']))

            if float(r['price'] >= .5):
                print(colored("                   [Price]: " + str(r['price']), 'red', attrs=['bold']))

            else:
                print(colored("                   [Price]: " + str(r['price']), 'green', attrs=['bold']))
                print("                   [Link]: " + str(r['link']))
                print("                   [Key]: " + str(r['key']))
    except Exception as error:
        return error

def get_activity(friends, tries):

    if solo == True:
        solo_act(tries)
    else:

        r = requests.get("http://www.boredapi.com/api/activity?participants=%s" % str(friends))
        r = r.json()

        index = 1

        if 'error' in r:

            while index <= int(tries):
                print("[*] Activity not found... Trying again.")
                r = requests.get("http://www.boredapi.com/api/activity?participants=%s" % str(friends))
                r = r.json()
                index += 1

            if 'error' in r:
                print("[*] No activity found after %s tries... Try again with more or less friends." % str(tries))
                sys.exit()
        else:
            print("http://www.boredapi.com/api/activity?participants=%s" % str(friends))
            print("[7H3 80R3D 491]:\n                   Are you bored? Maybe you should...\n")
            print("                   [Activity]: " + str(r['activity']))

            if float(r['accessibility'] >= .5):
                print(colored("                   [Accessibility]: " + str(r['accessibility']), 'red', attrs=['bold']))

            else:
                print(colored("                   [Accessibility]: " + str(r['accessibility']), 'green', attrs=['bold']))
                print("                   [Type]: " + str(r['type']))
                print("                   [Participants]: " + str(r['participants']))

            if float(r['price'] >= .5):
                print(colored("                   [Price]: " + str(r['price']), 'red', attrs=['bold']))

            else:
                print(colored("                   [Price]: " + str(r['price']), 'green', attrs=['bold']))
                print("                   [Link]: " + str(r['link']))
                print("                   [Key]: " + str(r['key']))


argv = sys.argv[1:]
friends = 0
tries = 3
solo = False

if len(argv) == 0:
    print("[Invalid] Please Try Again\nbored -f [# of friends]")
    sys.exit()

try:
    total = len(sys.argv)

    if int(total) < 1:
        print("[Invalid] Please Try Again\nbored -s/-f [# of friends]")
        sys.exit()

    else:
        options, args = getopt.getopt(argv, "t:f:sh",
                                   ["tries=",
                                    "friends=",
                                    "solo",
                                    "help"])
        for name, value in options:
            if name in ['-t', '--tries']:
                tries = value

            # elif name not in ['-t', '--tries']:
            #     tries = 5

            elif name in ['-f', '--friends']:
                friends = value

                try:

                    if int(friends) <= 1:
                        print("You have no friends...\nTry: ./bored -s")
                        sys.exit()

                    if int(friends) >= 9:
                        print("You have too many friends...")
                        sys.exit()

                except Exception as error:
                    print(error)
                    sys.exit()

            elif name in ['-s', '--solo']:
                if int(friends) >= 1:
                    print("[*] The \'-f\' option and the \'-s\' option cannot be used together!")
                    sys.exit()
                else:
                    solo = True

            elif name in ['-h', '--help']:
                print("[Usage:] ./bored -f [friends]")
                print("-f should be an int (# of participants)")
                sys.exit()

            else:
                print("[Usage:] ./bored -f [friends]")
                print("-f should be an int (# of participants)")
                sys.exit()

        get_activity(friends, tries)

except Exception as error:
    print(error)
    sys.exit()
