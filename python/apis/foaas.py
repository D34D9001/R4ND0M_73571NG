#!/usr/bin/env python3

"""This program is still a little bit buggy.
Feel free to imporove it!
"""

__author__ = "D34D9001"
__license__ = "MIT"
__version__ = "1.0.2"
__maintainer__ = "D34D9001"
__status__ = "Prototype"

import requests
import json
import getopt
import sys
from lxml.html import fromstring
from termcolor import colored

argv = sys.argv[1:]

name = ""
_from = ""
company = ""
# action = "" ## This variable is not currently being used
# reference = "" ## This variable is not currently being used
# reaction = "" ## This variable is not currently being used
# language = "" ## This variable is not currently being used
method = ""

try:

    options, args = getopt.getopt(argv, "m:f:c:n:h",
                               ["method=",
                                "from=",
                                "company=",
                                "name=",
                                "help"])

    for name, value in options:
        if name in ['-m', '--method']:
            method = value

        if name in ['-f', '--from']:
            _from = value

        if name in ['-c', '--company']:
            company = value

        # if name in ['-a', '--action']:
        #     action = value

        # if name in ['-r', '--reference']:
        #     reference = value

        # if name in ['-e', '--reaction']:
        #     reference = value

        # if name in ['-l', '--language']:
        #     language = value

        if name in ['-n', '--name']:
            name = value

        if name in ['-h', '--help']:
            print("Usage: ./foaas.py -n [name] -s [sender]")
            sys.exit()

    try:

        if len(_from) < 1:
            print("[*] You Must Specify A Sender....")
            sys.exit()

        elif len(method) < 1:
            print("[!] You must choose a method...")
            sys.exit()


        elif len(name) <= 2:
            headers = {"User-Agent": "FOaaS"}
            data = requests.get("https://foaas.com/%s/%s/" % (method, _from), headers=headers)
            tree = fromstring(data.content)
            fuckoff = tree.findtext('.//title')
            print(fuckoff)

        elif len(company) >= 2:
            headers = {"User-Agent": "FOaaS"}
            data = requests.get("https://foaas.com/%s/%s/%s/" % (method, company, _from), headers=headers)
            tree = fromstring(data.content)
            fuckoff = tree.findtext('.//title')
            print(fuckoff)

        else:
            headers = {"User-Agent": "FOaaS"}
            data = requests.get("https://foaas.com/%s/%s/%s" % (method, name, _from), headers=headers)
            tree = fromstring(data.content)
            fuckoff = tree.findtext('.//title')
            print(fuckoff)

    except Exception as error:
        print(error)
        print("[!] There was a problem... Your connection maybe??\nPlease try again.")

except Exception as error:
    print(error)
