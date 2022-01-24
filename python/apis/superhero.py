#!/usr/bin/env python3

import requests
import sys
import json
import getopt

api_token = 10209987755167818

argv = sys.argv[1:]
char_id = 0
options, args = getopt.getopt(argv, "i:h",
                           ["id=",
                            "help"])
for name, value in options:
    if name in ['-i', '--id']:
        char_id = value

if int(char_id) < 1:
    print("[*] You Must Specify A Hero ID....")
    sys.exit()

else:
    data = requests.get("https://superheroapi.com/api/%s/%s" %(api_token, char_id))
    hero = data.json()
    print("Name: " + hero['name'])
    print("Photo: " + hero['image']['url'])
    print("ID: " + hero['id'])

    for item in hero['powerstats']:
        print(item + ": " + hero['powerstats'][item])

    for item in hero['biography']:
        try:
            print(item + ": " + hero['biography'][item])
        except Exception:
            print("%s: %s" %(item, hero['biography'][item]))

    for item in hero['appearance']:
        try:
            print(item + ": " + hero['appearance'][item])
        except Exception:
            print("%s: %s" %(item, hero['appearance'][item]))

    for item in hero['work']:
        print(item + ": " + hero['work'][item])

    for item in hero['connections']:
        print(item + ": " + hero['connections'][item])
