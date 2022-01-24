#!/usr/bin/env python3

"""
This script will get a poem from poetrydb.org and display
it in the terminal. You can specify an author and a title or just a title.
To see all authors or all titles, type: $ ./poetpy.py -w [for authors] /-p [for titles]
"""
__author__ = "D34D9001"
__license__ = "MIT"
__version__ = "1.0.1"
__maintainer__ = "D34D9001"
__status__ = "Prototype"

import requests
import sys
import json
import getopt

argv = sys.argv[1:]

author = ""
title = ""

try:
    total = len(sys.argv)
    if int(total) < 2:
        print("[Invalid] Please Try Again\npoetpy.py -a [author] -t [title]")
        sys.exit()
    else:
        options, args = getopt.getopt(argv, "a:t:wp",
                                   ["author =",
                                    "title =",
                                    "writers",
                                    "poems"])
        for name, value in options:
            if name in ['-w', '--writers']:
                headers = {"User-Agent": "PoetPy"}
                data = requests.get("https://poetrydb.org/author", headers=headers)
                print("###################################################\n")
                print("                      Authors                             \n")
                print("###################################################\n")
                for item in data.json()['authors']:
                    print(item)
                sys.exit()

            elif name in ['-p', '--poems']:
                headers = {"User-Agent": "PoetPy"}
                data = requests.get("https://poetrydb.org/title", headers=headers)
                print("###################################################\n")
                print("                      Titles                             \n")
                print("###################################################\n")
                for item in data.json()['titles']:
                    print(item)
                sys.exit()

            elif name in ['-a', '--author']:
                author = value
            elif name in ['-t', '--title']:
                title = value

        if len(author) > 1:
            headers = {"User-Agent": "PoetPy"}
            data = requests.get("https://poetrydb.org/author,title/%s;%s/lines.json" % (author, title), headers=headers)
            print("###################################################\n")
            print("                      %s                             \n" % title)
            print("                  By: %s" % author)
            print("###################################################\n")
            for item in data.json()[0]['lines']:
                print(item)

        else:
            headers = {"User-Agent": "PoetPy"}
            data = requests.get("https://poetrydb.org/title/%s/lines.json" % (title), headers=headers)
            print("###################################################\n")
            print("                      %s                             \n" % title)
            print("###################################################\n")
            for item in data.json()[0]['lines']:
                print(item)

except KeyError:
    print("[!] Poem Not Found...\n    Please Try Another Poem.")
    sys.exit()
