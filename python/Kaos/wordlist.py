#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created: Aug 2017

    @author: D34D9001@9R0GR4M13
"""
import kerri
import symbo
import os
import time
from termcolor import colored

CSTR_START = symbo.CSTR_START
CSTR_END = symbo.CSTR_END
SYM = symbo.SYM

# Current Directory

global pwd

# THIS WILL SET THE CURRENT WORKING DIRECTORY AT TIME OF KAOS IMPORT
# IF THE DIRECTORY IS CHANGED AFTER KAOS IS IMPORTED, THIS VARIABLE
# WILL NOT CHANGE AUTOMATICALLY, BUT IT CAN BE CHANGED MANUALLY BY:
#   pwd = \'new/directory/path/\'

pwd = os.getcwd()

#######################
# WORDLIST GENERATION #
#######################

class Wordlist(object):
    """
    Wordlist Generators
    """

    def __str__(self):
        return """ Controls Wordlist Generation Preformed By Kaos """

    def crunch(self, start, end, linecount, output='%s/wordlist.kaos' % pwd, *args):
        """
        Create A Wordlist Using Crunch
        """

        def crunchchars():
            """
            Displays Crunch Charset Options
            """
            print("hex-lower = [0123456789abcdef]\n" +
                  "hex-upper = [0123456789ABCDEF]\n" +
                  "numeric = [0123456789]\n" +
                  "numeric-space = [0123456789 ]\n" +
                  "symbols14 = [!@#$%^&*()-_+=]\n" +
                  "symbols14-space = [!@#$%^&*()-_+= ]\n" +
                  "symbols-all = [!@#$%^&*()-_+=~`[]{}|\\" +
                  ":;\"'<>,.?/]\n" +
                  "symbols-all-space = [!@#$%^&*()-_+=~`[]{}|\\" +
                  ":;\"'<>,.?/ ]\n" +
                  "ualpha = [ABCDEFGHIJKLMNOPQRSTUVW" +
                  "XYZ]\n" +
                  "ualpha-space = [ABCDEFGHIJKLMNOPQRSTU" +
                  "VWXYZ ]\n" +
                  "ualpha-numeric = [ABCDEFGHIJKLMNOPQRSTUVW" +
                  "XYZ0123456789]\n" +
                  "ualpha-numeric-space = [ABCDEFGHIJKLMNOPQRSTUVW" +
                  "XYZ0123456789 ]\n" +
                  "ualpha-numeric-symbol14 = [ABCDEFGHIJKLMNOPQRSTUVW" +
                  "XYZ0123456789!@#$%^&*()-_+=]]n" +
                  "ualpha-numeric-symbol14-space = [ABCDEFGHIJKLMNOPQRSTUVW" +
                  "XYZ0123456789!@#$%^&*()-_+= ]]n" +
                  "ualpha-numeric-all = [ABCDEFGHIJKLMNOPQRSTUVW" +
                  "XYZ0123456789!@#$%^&*()-_+=~`[]{}|\\:;\"'<>,.?/]\n" +
                  "ualpha-numeric-all-space = [ABCDEFGHIJKLMNOPQRSTUVW" +
                  "XYZ0123456789!@#$%^&*()-_+=~`[]{}|\\:;\"'<>,.?/ ]]n" +
                  "lalpha = [abcdefghijklmnopqrstuvw" +
                  "xyz]\n" +
                  "lalpha-space = [abcdefghijklmnopqrstuvw" +
                  "xyz ]\n" +
                  "lalpha-numeric = [abcdefghijklmnopqrstuvw" +
                  "xyz0123456789]\n"
                  "lalpha-numeric-space = [abcdefghijklmnopqrstuvw" +
                  "xyz0123456789 ]\n" +
                  "lalpha-numeric-symbol14 = [abcdefghijklmnopqrstuvw" +
                  "xyz0123456789!@#$%^&*()-_+=]\n" +
                  "lalpha-numeric-symbol14-space = [abcdefghijklmnopqrstuvw" +
                  "xyz0123456789!@#$%^&*()-_+= ]\n" +
                  "lalpha-numeric-all = [abcdefghijklmnopqrstuvw" +
                  "xyz0123456789!@#$%^&*()-_+=~`[]{}|\\:;\"'<>,.?/]\n" +
                  "lalpha-numeric-all-space = [abcdefghijklmnopqrstuvw" +
                  "xyz0123456789!@#$%^&*()-_+=~`[]{}|\\:;\"'<>,.?/ ]\n" +
                  "mixalpha = [abcdefghijklmnopqrstuvwxyz" +
                  "ABCDEFGHIJKLMNOPQRSTUVWXYZ]\n" +
                  "mixalpha-space = [abcdefghijklmnopqrstuvwxyz" +
                  "ABCDEFGHIJKLMNOPQRSTUVWXYZ ]\n" +
                  "mixalpha-numeric = [abcdefghijklmnopqrstuvwxyz" +
                  "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789]\n" +
                  "mixalpha-numeric-space = [abcdefghijklmnopqrstuvwxyz" +
                  "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ]\n" +
                  "mixalpha-numeric-symbol14 = [abcdefghijklmnopqrstuvw" +
                  "xyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_+=]\n" +
                  "mixalpha-numeric-symbol14-space = [abcdefghijklmnopqrstu" +
                  "vwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_" +
                  "+= ]\n" +
                  "mixalpha-numeric-all = [abcdefghijklmnopqrstuvwxy" +
                  "zABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_+=~`[]" +
                  "{}|\\:;\"'<>, .?/]\n" +
                  "mixalpha-numeric-all-space = [abcdefghijklmnopqrstuvwxyz" +
                  "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_+=~`[]{}" +
                  "|\\:;\"'<>,.?/ ]\n")
        if len(args) >= 1:
            raise kerri.ExcessArguments("crunch()", 4)
        else:
            try:
                crunchchars()
                charset = raw_input(CSTR_START +
                                    colored("[Charset] \n", 'blue',
                                            attrs=['bold'])+(CSTR_END))
                os.system("crunch " + start + " " + end +
                          " -f /usr/share/crunch/charset.lst " + charset +
                          " -c " + linecount + " -o " + output)
            except KeyboardInterrupt:
                raise kerri.UsrInt("crunch(%s, %s, %s, %s)" % (start, end, linecount, output))
            except Exception as error:
                raise kerri.Unknown("crunch()", error)

    def cewl(self, url, keep='y', *args):
        """
        Creates A Cewl Wordlist
        """

        if len(args) >= 1:
            raise kerri.ExcessArguments("cewl()", 1)
        else:
            try:
                if keep == "y":
                    wfile = raw_input(CSTR_START+colored("[Output File] \n",
                                                         'blue', attrs=['bold']) +
                                      (CSTR_END))
                    kemail = raw_input(colored("{y/n}\n" + CSTR_START +
                                               "[Keep Emails] \n", 'blue',
                                               attrs=['bold'])+(CSTR_END))
                    if kemail == "y":
                        email_store = raw_input(CSTR_START +
                                                colored("[Email File] \n", 'blue',
                                                        attrs=['bold'])+(CSTR_END))
                        offsite = raw_input(colored("{y/n}\n" + CSTR_START +
                                                    "[Allow Offsite] \n", 'blue',
                                                    attrs=['bold']))
                        if offsite == "n":
                            print(SYM['notice'])+colored("Starting Cewl...",
                                                         'blue', attrs=['bold'])
                            print(SYM['echo'])+colored("cewl -k -w " + wfile +
                                                       " -e --email_file " +
                                                       email_store + " -v " +
                                                       url, 'grey',
                                                       attrs=['bold'])
                            time.sleep(.25)
                            os.system("cewl -k -w " + wfile + " -e --email_file " +
                                      email_store + " -v " + url)
                        else:
                            print(SYM['notice'])+colored("Starting Cewl...",
                                                         'blue', attrs=['bold'])
                            print(SYM['echo'])+colored("cewl -k -o -w " + wfile +
                                                       " -e --email_file " +
                                                       email_store + " -v " +
                                                       url,
                                                       'grey', attrs=['bold'])
                            time.sleep(.25)
                            os.system("cewl -k -o -w " + wfile +
                                      " -e --email_file " + email_store + " -v " +
                                      url)
                    else:
                        offsite = raw_input(colored("{y/n}\n" + CSTR_START +
                                                    "[Allow Offsite]: : ", 'blue',
                                                    attrs=['bold'])+(CSTR_END))
                        if offsite == "n":
                            print(SYM['notice'])+colored("Starting Cewl...",
                                                         'blue', attrs=['bold'])
                            print(SYM['echo'])+colored("cewl -k -w " + wfile +
                                                       " -v " + url, 'grey',
                                                       attrs=['bold'])
                            time.sleep(.25)
                            os.system("cewl -k -w " + wfile + " -v " + url)
                        else:
                            print(SYM['notice']+colored("Starting Cewl...",
                                                        'blue', attrs=['bold']))
                            print(SYM['echo'])+colored("cewl -k -o -w " + wfile +
                                                       " -v " + url, 'grey',
                                                       attrs=['bold'])
                            time.sleep(.25)
                            os.system("cewl -k -o -w " + wfile + " -v " + url)
                else:
                    wfile = raw_input(CSTR_START+colored("[Output File] \n",
                                                         'blue', attrs=['bold']) +
                                      CSTR_END)
                    kemail = raw_input(colored("{y/n}\n" + CSTR_START +
                                               "[Keep Emails] \n", 'blue',
                                               attrs=['bold'])+CSTR_END)
                    if kemail == "y":
                        email_store = raw_input(CSTR_START +
                                                colored("[Email File] \n", 'blue',
                                                        attrs=['bold']) + CSTR_END)
                        offsite = raw_input(colored("{y/n}\n" + CSTR_START +
                                                    "[Allow Offsite] \n", 'blue',
                                                    attrs=['bold'])+CSTR_END)
                        if offsite == "n":
                            print(SYM['notice'])+colored("Starting Cewl...",
                                                         'blue', attrs=['bold'])
                            print(SYM['echo'])+colored("cewl -w " + wfile +
                                                       " -e --email_file " +
                                                       email_store + " -v " +
                                                       url, 'grey',
                                                       attrs=['bold'])
                            time.sleep(.25)
                            os.system("cewl -w " + wfile + " -e --email_file " +
                                      email_store + " -v " + url)
                        else:
                            print(SYM['notice']) + colored("Starting Cewl...",
                                                           'blue', attrs=['bold'])
                            print(SYM['echo'])+colored("cewl -o -w " + wfile +
                                                       " -e --email_file " +
                                                       email_store + " -v " + url,
                                                       'grey', attrs=['bold'])
                            time.sleep(.25)
                            os.system("cewl -o -w " + wfile + " -e --email_file " +
                                      email_store + " -v " + url)
                    else:
                        offsite = raw_input(colored("{y/n}\n" + CSTR_START +
                                                    "[Allow Offsite[ \n", 'blue',
                                                    attrs=['bold'])+CSTR_END)
                        if offsite == "n":
                            print(SYM['notice'])+colored("Starting Cewl...",
                                                         'blue', attrs=['bold'])
                            print(SYM['echo'])+colored("cewl -w " + wfile +
                                                       " -v " + url, 'grey',
                                                       attrs=['bold'])
                            time.sleep(.25)
                            os.system("cewl -w " + wfile + " -v " + url)
                        else:
                            print(SYM['notice']) + colored("Starting Cewl...",
                                                           'blue', attrs=['bold'])
                            print(SYM['echo'])+colored("cewl -o -w " + wfile +
                                                       " -v " + url, 'grey',
                                                       attrs=['bold'])
                            time.sleep(.25)
                            os.system("cewl -o -w " + wfile + " -v " + url)
            except KeyboardInterrupt:
                raise kerri.UsrInt("cewl(%s)" % url)
            except Exception as error:
                raise kerri.Unknown("cewl()", error)

#########
# INITs #
#########

wordlist = Wordlist()
crunch = wordlist.crunch
cewl = wordlist.cewl
