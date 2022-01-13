#!/usr/bin/env python3

"""
This program was built using the
Disney API @ https://disneyapi.dev

You can list all Disney characters using the
-a/--all flag or you can show a single character
using the -i/--id flag.

Unfortunately, the DisneyAPI does not offer a way
to search by character name so the ID is the best
we can offer...

Created By: D34D9001
Jan. 11, 2022
"""

import requests
import sys
import json
import getopt

argv = sys.argv[1:]

id = ""

index = 1
test = 0

# try:
total = len(sys.argv)

if int(total) < 2:
    print("[INVALID OPTIONS]\nPlease Try Again...\n")
    sys.exit()

else:
    options, args = getopt.getopt(argv, "n:i:ah",
                               ["name",
                                "id",
                                "all" ,
                                "help"])

    for name, value in options:
        if name in ['-a', '--all']:

                try:
                    while True:
                        headers = {"User-Agent": "Disney.py"}
                        data = requests.get("https://api.disneyapi.dev/characters?page=%s" % str(index))
                        if data.status_code != 200:
                            print("[!] Page not found!")
                            sys.exit()
                        for item in data.json()['data']:
                            if len(item['name']) == 0:
                                sys.exit()
                            print("###################################################")
                            print("                      %s" % item['name'])
                            print("###################################################")
                            try:
                                print("ID: %i" % item['_id'])
                            except Exception:
                                print("ID : [unknown]")
                            try:
                                print("Image: " + item['imageUrl'])
                            except Exception:
                                print("Image : [unknown]")
                            try:
                                print("URL: " + item['url'])
                            except Exception:
                                print("ID : [unknown]")
                            print("###################################################\n\n")
                        index+=1

                except Exception as error:
                    sys.stderr.write(str(error))
                    sys.exit()

        elif name in ['-n', '--name']:
            dname = str(value)
            index = 1
            try:
                while True:
                    headers = {"User-Agent": "Disney.py"}
                    data = requests.get("https://api.disneyapi.dev/characters?page=%s" % str(index))
                    if data.status_code != 200:
                        print("[!] Page not found!")
                        sys.exit()
                for item in data.json()['data']:
                        if dname == item['name']:
                            print("###################################################")
                            print("                      %s" % item['name'])
                            print("###################################################")
                            try:
                                print("ID: %i" % item['_id'])
                            except Exception:
                                print("ID : [unknown]")
                            try:
                                print("Image: " + item['imageUrl'])
                            except Exception:
                                print("Image : [unknown]")
                            try:
                                print("URL: " + item['url'])
                            except Exception:
                                print("URL : [unknown]")
                            print("###################################################\n\n")
                        else:
                            print("[!] Character could not be located.\nPlease try again...")
                            sys.exit()

            except Exception as error:
                sys.stderr.write(str(error))
                sys.exit()

        elif name in ['-i', '--id']:
            id = value
            try:
                headers = {"User-Agent": "Disney.py"}
                data = requests.get("https://api.disneyapi.dev/characters/%s" % str(id))
                if data.status_code != 200:
                    print("[!] Page not found!")
                    sys.exit()
                for item in data.json()['data']:
                    print("###################################################")
                    print("                      %s" % item['name'])
                    print("###################################################")
                    try:
                        print("ID: %i" % item['_id'])
                    except Exception:
                        print("ID : [unknown]")
                    try:
                        print("Image: " + item['imageUrl'])
                    except Exception:
                        print("Image : [unknown]")
                    try:
                        print("URL: " + item['url'])
                    except Exception:
                        print("ID : [unknown]")
                    print("###################################################\n\n")
            except ValueError:
#                sys.stderr.write(str(error))
                print("[!] Character Not Found...")
                sys.exit()

        elif name in ['-h', '--help']:
            print("./disney.py -a/--all")
            sys.exit()

        else:
            print("./disney.py -a/--all")
            sys.exit()
# except Exception as error:
#     print(error)
#     sys.exit()
