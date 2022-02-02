#!/usr/bin/env python3

__author__ = "D34D9001"
__license__ = "MIT"
__version__ = "1.0.1"
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
sender = ""
method = ""

try:
    total = len(sys.argv)
    if int(total) < 4:
        print("[Invalid] Please Try Again\nfoaas.py -m [method] -s [sender] -n [name]")
        sys.exit()
    else:
        options, args = getopt.getopt(argv, "m:n:s:h",
                                   ["method=",
                                    "sender=",
                                    "name=",
                                    "help"])

    for name, value in options:
        if name in ['-m', '--method']:
            method = value

        if name in ['-s', '--sender']:
            sender = value

        if name in ['-n', '--name']:
            name = value

        if name in ['-h', '--help']:
            print("Usage: ./foaas.py -n [name] -s [sender]")
            sys.exit()

    try:

        if len(name) < 1:
            print("[!] You must provide a valid name.")
            sys.exit()

        elif len(sender) < 1:
            print("[*] You Must Specify A Sender....")
            sys.exit()

        elif len(method) < 1:
            print("[!] You must choose a method...")
            sys.exit()

        headers = {"User-Agent": "FOaaS"}
        data = requests.get("https://foaas.com/%s/%s/%s" % (method, name, sender), headers=headers)
        tree = fromstring(data.content)
        fuckoff = tree.findtext('.//title')
        print(fuckoff)

    except Exception as error:
        print(error)
        print("[!] There was a problem... Your connection maybe??\nPlease try again.")

except Exception as error:
    print(error)
