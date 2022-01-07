#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created: Aug 2017

    @author: D34D9001@9R0GR4M13
"""
import kerri
import os
import time
import webbrowser
import random
import subprocess
import sys
import urllib
from bs4 import BeautifulSoup as bs
from termcolor import colored

###########
# STALKER #
###########

colors = ("green", "red", "blue", "white", "grey", "magenta", "cyan")
def get_permission(info, bypass=0):
    if bypass == 1:
        pass
    else:
        print(colored("[!] STALKER NEEDS YOUR PERMISSION TO CONTINUE!", 'red', attrs=['bold']))
        print(colored("%s" % info, 'yellow', attrs=['bold']))
        permission = raw_input(colored("Do You Wish To Continue? (y)es/(no): ", 'blue', attrs=['bold']))
        if str(permission) != "y" and str(permission) != "yes":
            sys.stderr.write("[!] PERMISSION DENIED BY USER!")
            sys.exit()
        else:
            print(colored("[*] PERMISSION GRANTED", 'green', attrs=['bold']))

class Stalker(object):
    """ Returns Information On Target From Multiple Servers """
# SOME OF THE DATABASES THAT STALKER WILL SEARCH REQUIRE AN ABREVIATED STATE
# NAME. TO PREVENT THE USER FROM HAVING TO INPUT BOTH THE ACTUAL STATE NAME
# AND THE ABREVIATED VERSION, WE HAVE ADDED THE 'ABV' DICTIONARY TO CONVERT
# THE STATE NAME TO THE ABREVIATED VERSION AUTOMATICALLY WHEN NEEDED
    def __init__(self):
        global abv
        abv = {"Alabama": "AL", "Alaska": "AK", "Arizona": "AZ",
               "Arkansas": "AR", "California": "CA", "Colorado": "CO",
               "Connecticut": "CT", "Delaware": "DE", "Florida": "FL",
               "Georgia": "GA", "Hawaii": "HI", "Idaho": "ID",
               "Illinois": "IL", "Indiana": "IN", "Iowa": "IA", "Kansas": "KS",
               "Kentucky": "KY", "Louisiana": "LA", "Maine": "ME",
               "Maryland": "MD", "Massachusetts": "MA", "Michigan": "MI",
               "Minnesota": "MN", "Mississippi": "MS", "Missouri": "MO",
               "Montana": "MT", "Nebraska": "NE", "Nevada": "NV",
               "New Hampshire": "NH", "New Jersey": "NJ", "New Mexico": "NM",
               "New York": "NY", "North Carolina": "NC", "North Dakota": "ND",
               "Ohio": "OH", "Oklahoma": "OK", "Oregon": "OR",
               "Pennsylvania": "PA", "Rhode Island": "RI",
               "South Carolina": "SC", "South Dakota": "SD", "Tennessee": "TN",
               "Texas": "TX", "Utah": "UT", "Vermont": "VT", "Virginia": "VA",
               "Washington": "WA", "West Virginia": "WV", "Wisconsin": "WI",
               "Wyoming": "WY", "Washington DC": "DC"}

    def __str__(self):
        return """ Turns Kaos Into Your Average Super Stalker """

    def stalk(self, first=None, middle=None, last=None, city=None, state=None,
              save=1, gui=0, bypass=0, *args):
        """ Search Public Servers For Information On The Target.
            Data can be saved to a file using the \'save\' parameter.
            If the gui parameter is set to 1 (enabled), the data will
            not be printed to stdout or saved to a file, instead it
            will be opened in the default web browser."""

# MAKE SURE USER DOESN'T ENTER TOO MANY ARGUMENTS
        if len(args) >= 1:
            raise kerri.ExcessArguments("staker()", 5)
# MAKE SURE THE USER ENTERED A FIRST NAME
        elif first is None:
            raise kerri.InvalidInput("stalk()",
                                     """You Must At Least Specify A First And
                                     Last Name Along With A City And State""")
        else:
# CHECK TO SEE IF THE USER INTENDS TO USE A TARGETS MIDDLE NAME IN A SEARCH
# IF THE MIDDLE NAME IS PROVIDED BUT NOT THE LAST NAME, THE MIDDLE NAME IS REMOVED AND USED AS
# THE TARGETS LAST NAME
            if last is None and middle is not None:
                last = str(middle)
                middle = None
# MAKE SURE THE USER ENTERED MORE THAN JUST THE TARGETS FIRST NAME
            elif last == None and middle == None:
                raise kerri.InvalidInput("stalk()", "You Must At Least Specify A First And Last Name Along With A City And State")
            try:
# DO NOT LET THE USER ATTEMPT TO SAVE THE DATA FROM THE SEARCH IF GUI MODE IS ENABLED
                if gui == 1 and save == 1:
                    raise kerri.InvalidInput("stalk()", "If the gui option is enabled, the data can not be save to a file...")
                if gui == 0:
# DEFINE URLS TO BE USED IF A MIDDLE NAME FOR THE TARGET WAS SUPPLIED
                    if middle != None:
                        urls = {'find_mugs':"https://www.findmugshots.com/arrests/%s_%s_%s" % (first, last, abv[state]),
                                'mugshots':"http://mugshots.com/search.html?q=%s+%s" % (first, last),
#                                'zaba_search':"http://www.zabasearch.com/people/%s+%s/%s/" % (first, last, abv[state]),
                                'yandex':"https://www.yandex.com/search/smart/?text=%s+%s+%s" % (first, middle, last),
                                'google':"https://www.google.com/search?q=%s+%s+%s+%s+%s" % (first, middle, last, city, state),
                                'policearrests':"https://www.policearrests.com/arrests/%s_%s_%s/" % (first, last, abv[state]),
                                'mylife':"https://www.mylife.com/%s-%s/" % (first, last),
                                'peekyou':"https://www.peekyou.com/%s_%s" % (first, last),
                                'peoplesmart':"https://www.peoplesmart.com/find/name/%s-%s/%s/%s" % (first, last, city, abv[state].lower()),
                                'publicrecords360':"https://www.publicrecords360.com/%s/people-search/%s/%s?city=%s" % (state.lower(), last, first, city.lower()),
                                'topix':"http://www.topix.com/forumsearch/city/%s-%s?q=%s+%s+%s" % (city.lower(), abv[state].lower(), first, middle, last),
                                'truepeoplesearch':"https://www.truepeoplesearch.com/results?name="+first+"%20"+last+"&citystatezip="+city+",%20"+abv[state]}
# DEFINE URLS TO BE USED IF THE USER DID NOT SUPPLY THE TARGETS MIDDLE NAME
                    else:
                        urls = {'find_mugs':"https://www.findmugshots.com/arrests/%s_%s_%s" % (first, last, abv[state]),
                                'mugshots':"http://mugshots.com/search.html?q=%s+%s" % (first, last),
#                                'zaba_search':"http://www.zabasearch.com/people/%s+%s/%s/" % (first, last, abv[state]),
                                'yandex':"https://www.yandex.com/search/smart/?text=%s+%s" % (first, last),
                                'google':"https://www.google.com/search?q=%s+%s+%s+%s" % (first, last, city, state),
                                'policearrests':"https://www.policearrests.com/arrests/%s_%s_%s/" % (first, last, abv[state]),
                                'mylife':"https://www.mylife.com/%s-%s/" % (first, last),
                                'peekyou':"https://www.peekyou.com/%s_%s" % (first, last),
                                'peoplesmart':"https://www.peoplesmart.com/find/name/%s-%s/%s/%s" % (first, last, city, abv[state].lower()),
                                'publicrecords360':"https://www.publicrecords360.com/%s/people-search/%s/%s?city=%s" % (state.lower(), last, first, city.lower()),
                                'topix':"http://www.topix.com/forumsearch/city/%s-%s?q=%s+%s" % (city.lower(), abv[state].lower(), first, last),
                                'truepeoplesearch':"https://www.truepeoplesearch.com/results?name="+first+"%20"+last+"&citystatezip="+city+",%20"+abv[state]}

                    try:
# CHECK TO SEE IF THE USER INTENDS TO SAVE THE OUTPUT DATA
# IF THE USER DOES NOT WANT TO SAVE THE DATA, PRINT IT TO STDOUT
                        if save == 0:
                            try:
                                for url in urls:
                                    if middle != None:
                                        print(colored("[*] Searching %s For %s %s %s in %s, %s" % (url, first, middle, last, city, state), random.choice(colors), attrs=['bold']))
                                    else:
                                        print(colored("[*] Searching %s For %s %s in %s, %s" % (url, first, last, city, state), random.choice(colors), attrs=['bold']))
# STALKER USES URLLIB AND BEAUTIFULSOUP4 TO GET AND PARSE THE TEXT FROM WEBPAGES
                                    html = urllib.urlopen(urls[url]).read()
# 'lxml' WAS ADDED TO PREVENT bs4 FROM DISPLAYING A WARNING MESSAGE
                                    soup = bs(html, "lxml")
# REMOVE ALL STYLE AND SCRIPT BLOCKS FROM THE PAGE
                                    for script in soup(["script", "style"]):
                                        script.extract()
# GET THE REMAINING TEXT FROM THE PAGE
                                    text = soup.get_text()
                                    print(text.encode('utf-8'))
# SPLIT THE TEXT INTO MULTIPLE LINES
                                    lines= (line.strip() for line in text.splitlines())
# LINES CONTAINING (2) OR MORE SPACES ARE SEPERATED INTO (2) (OR MORE) SEPERATE LINES
                                    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# REJOIN LINES AND THEN PRINT THE TEXT
                                    data = '\n'.join(chunk for chunk in chunks if chunk).encode('utf-8')
                                    print(data)
                            except Exception as error:
                                print("%s FAILED WITH ERROR:\n%s" % (url, error))
                        if save == 1:
                            try:
# IF THE USER WANTS TO SAVE THE OUTPUT DATA TO A SERIES OF FILES,
# FIRST CHECK TO MAKE SURE THE DATABASE DIRECTORY EXSITS
                                if not os.path.isdir("/root/Stalker"):
                                    os.mkdir("/root/Stalker")
                                    stalk_dir = "/root/Stalker"
                                else:
                                    stalk_dir = "/root/Stalker"
# THE NEW DIRECTORY FOR THE TARGET WILL BE NAMED AFTER THE TARGET (/root/Stalker/[FIRST_LAST])
                                if middle == None:
                                    out_dir = "%s/%s_%s" % (stalk_dir, first, last)
                                else:
                                    out_dir = "%s/%s_%s_%s" % (stalk_dir, first, middle, last)
                                if not os.path.isdir(out_dir):
                                    os.mkdir(out_dir)
                                else:
# IF THE TARGETS DIRECTORY ALREADY EXSISTS, ASK THE USER IF THEY WOULD LIKE TO OVERWRITE THE EXSISTING DATA
                                    overwrite = raw_input(colored("[!] THIS TARGET ALREADY HAS A DIRECTORY!!!\nDo You Want To Overwrite It? [ (y)es or (n)o ]\n--> ", 'red', attrs=['bold']))
                                    if overwrite == "yes" or overwrite == "y" or overwrite == "YES" or overwrite == "Yes" or overwrite == "Y":
                                        subprocess.call(["/usr/bin/srm", "-r", out_dir])
                                        os.mkdir(out_dir)
# IF THE USER DOES NOT WANT TO OVERWRITE THE DATA (or enters anything other than ["y", "Y", "yes", "Yes"
# or "YES"]). Stalker will
# terminate the data search)
                                    else:
                                        raise kerri.DuplicationError("stalk()", "%s ALREADY EXSISTS!" % out_dir)
# CREATE AN INTRODUCTION (.intro) FILE FOR THE TARGET. THIS FILE IS NOT CURRENTLY USED FOR ANY DATA
# BUT MAY BE USED IN THE FUTURE AS A 'CHEAT SHEET' FOR THE TARGET OR SOMETHING SIMILAR
                            except Exception as error:
                                print("%s FAILED WITH ERROR: \n%s" % (url, error))
                            intro = "%s/%s_%s.intro" % (out_dir, first, last)
                            with open(intro, 'w') as outfile:
                                outfile.write("################################## ")
                                outfile.write("Kaos.Stalker Intro For %s %s From %s %s" % (first, last, city, state))
                                outfile.write(" ##################################")
                                outfile.close()
                            for url in urls:
                                if middle != None:
                                    print(colored("Searching %s For %s %s %s in %s, %s" % (url, first, middle, last, city, state), random.choice(colors), attrs=['bold']))
                                else:
                                    print(colored("Searching %s For %s %s in %s, %s" % (url, first, last, city, state), random.choice(colors), attrs=['bold']))
# CREATE A FILE IN THE TARGETS DIRECTORY WITH THE NAMING FORMAT [${FIRSTNAME}_${LASTNAME}.${URL_NAME}]
# EXAMPLE:   John_Doe.foogle
                                with open("%s/%s_%s.%s" % (out_dir, first, last, url), 'w') as out_file:
# [this process is explained above (lines: 93-110)]
                                    html = urllib.urlopen(urls[url]).read()
                                    soup = bs(html, "lxml")
                                    for script in soup(["script", "style"]):
                                        script.extract()
                                    text = soup.get_text()
                                    lines= (line.strip() for line in text.splitlines())
                                    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
                                    data = '\n'.join(chunk for chunk in chunks if chunk).encode('utf-8')
                                    out_file.write(data)
                                    out_file.close()
                                    time.sleep(1)
                    except Exception as error:
                        raise kerri.Unknown("stalker()", error)
                elif gui == 1:
# THE SAME URL DECISION PROCESS IS USED FROM ABOVE (DETERMINED BY USERS INPUT OF A MIDDLE NAME)
                    if bypass == 0:
                        get_permission("[!] THIS WILL TAKE SEVERAL MINS WITH A SLOW CONNECTION...")
                    else:
                        pass
                    if middle != None:
                        urls = {'find_mugs':"https://www.findmugshots.com/arrests/%s_%s_%s" % (first, last, abv[state]),
                                'arrests':"https://%s.arrests.org/search.php?fname=%s&lname=%s&fpartial=True" % (state.lower(), first, last),
#                                'mugshots':"http://mugshots.com/search.html?q=%s+%s" % (first, last),
#                                'zaba_search':"http://www.zabasearch.com/people/%s+%s/%s/" % (first, last, abv[state]),
                                'google':"https://www.google.com/search?q=%s+%s+%s+%s+%s" % (first, middle, last, city, state),
#                                'pipl':"https://pipl.com/search/?q=%s+%s+%s&l=%s%2C+%s&slocUS%7C%s%7C&in=5" % (first, middle, last, city, state, abv[state]),
                                'spokeo':"https://www.spokeo.com/%s-%s/%s/%s" % (first, last, state, city),
                                'people_search':"https://www.peoplefinders.com/peoplesearch/searchresults?search=People&fn=%s&mn=%s&ln=%s&city=%s&state=%s" % (first, middle, last, city, abv[state]),
#                                'publicrecords':"https://publicrecords.com/people-search-record/%s-%s" % (first, last),
                                '411':"https://www.411.com/name/%s-%s/%s-%s" % (first, last, city, state),
                                'yandex':"https://www.yandex.com/search/smart/?text=%s+%s+%s" % (first, middle, last),
#                                'lakako':"https://www.lakako.com/user/"+first+"%20"+last,
#                                'policearrests':"https://www.policearrests.com/arrests/%s_%s_%s/" % (first, last, abv[state]),
                                'mylife':"https://www.mylife.com/%s-%s/" % (first, last),
                                'peekyou':"https://www.peekyou.com/%s_%s" % (first, last),
#                                'peoplesmart':"https://www.peoplesmart.com/find/name/%s-%s/%s/%s" % (first, last, city, abv[state].lower()),
                                'ussearch':"https://www.ussearch.com/search/?firstName=%s&lastName=%s&city=%s&state=%s" % (first, last, city, abv[state]),
#                                'topix':"http://www.topix.com/forumsearch/city/%s-%s?q=%s+%s+%s" % (city.lower(), abv[state].lower(), first, middle, last),
                                'facebook':"https://www.facebook.com/public/%s+%s+%s" % (first, middle, last),
                                'twitter':"https://www.twitter.com/search?q="+first+"%20"+middle+"%20"+last+"&src=typed_query",
                                'truepeoplesearch':"https://www.truepeoplesearch.com/results?name="+first+"%20"+last+"&citystatezip="+city+",%20"+abv[state],
                                'bing':"https://www.bing.com/search?q=%s+%s+%s" % (first, middle, last),
                                'whitepages':"https://www.whitepages.com/name/%s-%s/%s" % (first, last, abv[state]),
                                'yahoo':"https://www.yahoo.com/search?p=%s+%s+%s" % (first, middle, last)}
                    else:
                        urls = {'find_mugs':"https://www.findmugshots.com/arrests/%s_%s_%s" % (first, last, abv[state]),
                                'arrests':"https://%s.arrests.org/search.php?fname=%s&lname=%s&fpartial=True" % (state.lower(), first, last),
#                                'mugshots':"http://mugshots.com/search.html?q=%s+%s" % (first, last),
#                                'zaba_search':"http://www.zabasearch.com/people/%s+%s/%s/" % (first, last, abv[state]),
                                'google':"https://www.google.com/search?q=%s+%s+%s+%s" % (first, last, city, state),
#                                'pipl':"https://pipl.com/search/?q=%s+%s&l=%s%2C+%s&slocUS%7C%s%7C&in=5" % (first, last, city ,state, abv[state]),
                                'spokeo':"https://www.spokeo.com/%s-%s/%s/%s" % (first, last, state, city),
                                'people_search':"https://www.peoplefinders.com/peoplesearch/searchresults?search=People&fn=%s&ln=%s&city=%s&state=%s" % (first, last, city, abv[state]),
#                                'publicrecords':"https://publicrecords.com/people-search-record/%s-%s" % (first, last),
                                '411':"https://www.411.com/name/%s-%s/%s-%s" % (first, last, city, state),
                                'yandex':"https://www.yandex.com/search/smart/?text=%s+%s" % (first, last),
#                                'policearrests':"https://www.policearrests.com/arrests/%s_%s_%s/" % (first, last, abv[state]),
                                'mylife':"https://www.mylife.com/%s-%s/" % (first, last),
                                'peekyou':"https://www.peekyou.com/usa/%s/%s_%s" % (state.lower(), first, last),
#                                'topix':"http://www.topix.com/forumsearch/city/%s-%s?q=%s+%s" % (city.lower(), abv[state].lower(), first, last),
#                                'peoplesmart':"https://www.peoplesmart.com/find/name/%s-%s/%s/%s" % (first, last, city, abv[state].lower()),
                                'facebook':"https://www.facebook.com/public/%s+%s" % (first, last),
                                'twitter':"https://www.twitter.com/search?q="+first+"%20"+last+"&src=typed_query",
                                'lakako':"https://www.lakako.com/user/"+first+"%20"+last,
                                'social-searcher':"https://www.soical-searcher.com/social-buzz/?q5=%s+%s" % (first, last),
                                'google-social-searcher':"https://www.social-searcher.com/google-social-search/?q=%s+%s&fb=on&tw=on&gp=on&in=on&li=on&pi=on" % (first, last),
                                'socialmention':"http://socialmention.com/search?q=%s+%s&t=all&btnG=Search" % (first, last),
                                'ussearch':"https://www.ussearch.com/search/?firstName=%s&lastName=%s&city=%s&state=%s" % (first, last, city, abv[state]),
                                'boardreader':"http://boardreader.com/s/"+first+"%2520"+last+".html;language=English",
                                'bing':"https://www.bing.com/search?q=%s+%s" % (first, last),
                                'yahoo':"https://www.yahoo.com/search?p=%s+%s" % (first, last),
                                'whitepages':"https://www.whitepages.com/name/%s-%s/%s" % (first, last, abv[state]),
                                'truepeoplesearch':"https://www.truepeoplesearch.com/results?name="+first+"%20"+last+"&citystatezip="+city+",%20"+abv[state]}

                    try:
# INSTEAD OF USING URLLIB AND BEAUTIFULSOUP4, THE WEBBROWSER MODULE IS USED TO OPEN THE WEBPAGES IN THE
# USERS DEFAULT BROWSER
                        for url in urls:
                            try:
#                                webbrowser.open(urls[url])
#                                os.system("/usr/bin/chromium --no-sandbox %s" % urls[url])

###

#                                subprocess.Popen(["/usr/bin/chromium", "--no-sandbox", "%s" % urls[url]])
#                            except Exception:

###

                                subprocess.Popen(["/usr/bin/firefox", "%s" % urls[url]])
                            except Exception:


# IF THE WEBPAGE COULD NOT BE OPENED IN THE USERS DEFAULT BROWER, STALKER ATTEMPTS TO DISPLAY
# THE PAGE WITH W3M
                                subprocess.call(["/usr/bin/w3m", urls[url]])
                            time.sleep(4)
                    except Exception as error:
                        sys.stderr.write("[!] I Wasn\'t able to load that site...")
                        sys.stderr.write(error)
                        time.sleep(1)

                else:
# IF THE ABOVE CONDITIONS ARE NOT MET, WE ASSUME THE USER HAS ENTERED AN INVALID OPTION FOR THE
# GUI PARAMETER AND RETURN AN ERROR MESSAGE
                    return "The \'gui\' parameter must be either a [1 (enabled)] or a [0 (disabled)]"
            except ValueError as error:
# RAISE AN ERROR IF THE USER ATTEMPTS TO USE THE GUI OPTION IN A NON-GRAPHICAL ENVIRONMENT
# (ex: multiuser mode or 'text' mode)
                raise kerri.ProcessFailure("stalk()", error)
            except Exception as error:
# IF STALKER HAS NO IDEA WHAT HAPPENED, BUT SOMETHING DIDN'T WORK, ATTEMPT TO SHOW THE USER WHAT
# THE ERROR WAS
                raise kerri.Unknown("stalk()", error)

    def group_stalk(self, file_name, save_data=0, *args):
        if len(args) >= 1:
            raise kerri.ExcessArguments("group_stalk()", 1)
        else:
            try:
                targets = open(file_name, 'r').readlines()
                for target in targets:
                    print("\n"+("#"*33)+"\n")
                    decider = len(target.split())
                    if decider == 4:
                        if save_data == 1:
                            stalk(first=str(target.split()[0]), last=str(target.split()[1]), city=str(target.split()[2]), state=str(target.split()[3]), save=1)
                        else:
                            stalk(first=str(target.split()[0]), last=str(target.split()[1]), city=str(target.split()[2]), state=str(target.split()[3]), save=0)
                    elif decider == 5:
                        if save_data == 1:
                            stalk(first=str(target.split()[0]), last=str(target.split()[1]), city=str(target.split()[2]), state=str(target.split()[3]), save=1)
                        else:
                            stalk(first=str(target.split()[0]), middle=str(target.split()[1]), last=str(target.split()[2]), city=str(target.split()[3]), state=str(target.split()[4]), save=0)
                    else:
                        raise kerri.InvalidInput("stalk()", "You Must At Least Specify A First And Last Name Along With A City And State")
                print(colored("[*] The Group Has Been Stalked!", 'blue', attrs=['bold']))
            except Exception as error:
                raise kerri.Unknown("group_stalk()", error)

#########
# INITs #
#########

# WE INITIALIZE THE CLASS TO MAKE IT A LITTLE EASIER FOR THE USER
stalker = Stalker()
stalk = stalker.stalk
group_stalk = stalker.group_stalk
