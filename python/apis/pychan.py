#!/usr/bin/env python3

"""
Created With: 4chanAPI [https://github.com/4chan/4chan-API]
Created By: D34D9001
Jan. 10, 2022

This script will get a list of forum boards from
4chan with the '-l' flag. The user can input one of the boards as an option
with the '-b' flag to return a list topics within that board.

[!] Currently only works with select boards
"""

__author__ = "D34D9001"
__license__ = "MIT"
__version__ = "1.0.1"
__maintainer__ = "D34D9001"
__status__ = "Prototype"

import getopt
import requests
import sys
import json
from datetime import datetime as dt

argv = sys.argv[1:]

try:
    total = len(sys.argv)
    if int(total) < 1:
        print("[Invalid] Please Try Again\npychan.py -b [board]")
        sys.exit()
    else:
        options, args = getopt.getopt(argv, "b:lh",
                                   ["board =",
                                    "list",
                                    "help"])
        for name, value in options:
            if name in ['-b', '--board']:
                board = value

                print("Getting data from https://a.4cdn.org/%s/catalog.json" % board)

                r = requests.get("https://a.4cdn.org/%s/catalog.json" % board)
                r = r.json()

                for items in r:
                    for thread in items['threads']:
            #        print(thread.values())
            #        print(thread.keys())
                        print(thread['now'] + " | " + thread['name'] + " | " + thread['id'] + "\n" + thread['com']+"\n\n")

            elif name in ['-l', '--list']:
                r = requests.get("https://a.4cdn.org/boards.json")
                r = r.json()
                for item in r['boards']:
#                    for board in items['board']:
                    print(item['board'] + " | " + item['meta_description'])


            elif name in ['-h', '--help']:
                print("[Usage]:  ./pychan.py -b/--board [board]")
                sys.exit()

except KeyError:
    sys.exit()
