#!/usr/bin/env python3
"""
Examples

single verse
    https://bible-api.com/john 3:16
abbreviated book name
    https://bible-api.com/jn 3:16
verse range
    https://bible-api.com/romans+12:1-2
multiple ranges
    https://bible-api.com/romans 12:1-2,5-7,9,13:1-9&10
different translation
    https://bible-api.com/john 3:16?translation=kjv
verse numbers
    https://bible-api.com/john 3:16?verse_numbers=true
jsonp
    https://bible-api.com/john+3:16?callback=func
"""
import requests
import sys
import json
import getopt

argv = sys.argv[1:]

bname = ""
book = ""
verse = ""

try:
    total = len(sys.argv)
    if int(total) < 2:
        print("[INVALID OPTIONS]\nPlease Try Again...\n")
        sys.exit()
    else:
        options, args = getopt.getopt(argv, "n:b:v:h",
                                   ["name =",
                                    "book =",
                                    "verse =" ,
                                    "help"])
        for name, value in options:
            if name in ['-n', '--name']:
                bname = value
            elif name in ['-b', '--book']:
                book = value
            elif name in ['-v', '--verse']:
                verse = value
            elif name in ['-h', '--help']:
                print("./bibler.py -n [book name] -b [book #] -v [verse #]\nEX: ./bibler.py -n John -b 3 -v 16\n")
                sys.exit()

        headers = {"User-Agent": "PoetPy"}
        out_verse = []
        data = requests.get("https://bible-api.com/%s %s:%s?translation=kjv" % (bname, book, verse), headers=headers)
        print("###################################################\n")
        print("                      %s %s:%s                             \n" %(bname, book, verse))
        print("###################################################\n\n")
        print(data.json()['text'])

        sys.exit()

except Exception as error:
    print(error)
    sys.exit()
