#!/usr/bin/env python3

__author__ = "D34D9001"
__license__ = "MIT"
__version__ = "1.0.3"
__maintainer__ = "D34D9001"
__status__ = "Prototype"

import requests
import sys
import json
import getopt

argv = sys.argv[1:]
api_token = ""   # https://superheroapi.com/ <-- Get Free API Key Here.
char_id = 0
options, args = getopt.getopt(argv, "i:a:lh",
                           ["id=",
                            "api=",
                            "list"
                            "help"])
for name, value in options:
    if name in ['-i', '--id']:
        char_id = value

    if name in ['-a', '--api']:
        api_token = value

    if name in ['-l', "--list"]:
        a_file = open("../doc/superhero_api_ids")
        lines = a_file.readlines()
        for line in lines:
            print(line)
        sys.exit()

    if name in ['-h', '--help']:
        print("Usage: ./superhero.py -i [Superhero_ID] -a [API_KEY]")
        sys.exit()

if len(api_token) < 17 or len(api_token) > 17:
    print("[!] You must provide a valid API token.\nGet one for free --> https://superheroapi.com/")
    sys.exit()
elif int(char_id) < 1:
    print("[*] You Must Specify A Hero ID....")
    sys.exit()

else:
    try:
        data = requests.get("https://superheroapi.com/api/%s/%s" %(api_token, char_id))
        hero = data.json()
        print("Name:\n        " + hero['name'] + "\n")
        print("Photo:\n        " + hero['image']['url'] + "\n")
        print("ID:\n        " + hero['id'] + "\n")

        for item in hero['powerstats']:
            print(str(item).upper() + ":\n        " + hero['powerstats'][item] + "\n")

        for item in hero['biography']:
            try:
                print(str(item).upper() + ":\n        " + hero['biography'][item] + "\n")
            except Exception:
                print("%s:\n        %s" %(str(item).upper(), hero['biography'][item]) + "\n")

        for item in hero['appearance']:
            try:
                print(str(item).upper() + ":\n        " + hero['appearance'][item] + "\n")
            except Exception:
                print("%s:\n        %s" %(str(item).upper(), hero['appearance'][item]) + "\n")

        for item in hero['work']:
            print(str(item).upper() + ":\n        " + hero['work'][item] + "\n")

        for item in hero['connections']:
            print(str(item).upper() + ":\n        " + hero['connections'][item] + "\n")
    except Exception:
        print("[!] There was a problem... Your API Token maybe??\nPlease try again.")
