#!/usr/bin/env python3

__author__ = "D34D9001"
__license__ = "MIT"
__version__ = "1.0.2"
__maintainer__ = "D34D9001"
__status__ = "Prototype"

import requests
import json
from termcolor import colored

def get_joke():
    try:
        joke = requests.get("https://v2.jokeapi.dev/joke/Any")

        for item in joke.json()['flags']:
            if joke.json()['flags'][item] == True:
                col_flag = str(item) + " : " + str(joke.json()['flags'][item])
                print(colored(col_flag, 'red', attrs=['bold']))

        print(joke.json()['setup'])
        print(joke.json()['delivery'])

    except Exception as error:
        return error

get_joke()
