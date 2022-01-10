#!/usr/bin/env python3
import requests
#import urllib
import sys
import json
import getopt

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)
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
                print("""###################################################\n
                    Authors                             \n
        ###################################################
                      """)
                for item in data.json()['authors']:
                    print(item)
                sys.exit()

            elif name in ['-p', '--poems']:
                headers = {"User-Agent": "PoetPy"}
                data = requests.get("https://poetrydb.org/title", headers=headers)
                print("""###################################################\n
                     Titles                             \n
        ###################################################
                      """)
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
            print("""###################################################\n
                    %s                             \n
                    By: %s                         \n
    ###################################################
                  """ % (title, author))
            for item in data.json()[0]['lines']:
                print(item)

        else:
            headers = {"User-Agent": "PoetPy"}
            data = requests.get("https://poetrydb.org/title/%s/lines.json" % (title), headers=headers)
            print("""###################################################\n
                        %s                         \n
    ###################################################
                  """ % title)
            for item in data.json()[0]['lines']:
                print(item)

except KeyError:
    print("[!] Poem Not Found...\n    Please Try Another Poem.")
    sys.exit()
