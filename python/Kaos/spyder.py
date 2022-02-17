#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created: Aug 2017

    @author: D34D9001@9R0GR4M13
"""
import kerri
import konst
import os
import requests
import subprocess
from bs4 import BeautifulSoup as bs

# Current Directory

global pwd

# THIS WILL SET THE CURRENT WORKING DIRECTORY AT TIME OF KAOS IMPORT
# IF THE DIRECTORY IS CHANGED AFTER KAOS IS IMPORTED, THIS VARIABLE
# WILL NOT CHANGE AUTOMATICALLY, BUT IT CAN BE CHANGED MANUALLY BY:
#   pwd = \'new/directory/path/\'

pwd = konst.pwd

#######################
# INTERNET OPERATIONS #
#######################

class Spyder(object):
    """ Spyder saves webpages to a specified file.
        * get_site() only displays output of webpage to
        stdout. (get_site().data can be save to file manually)* """

    def __str__(self):
        return """ Controls All Internet Operations Preformed By Kaos """

    def print_site(self, url, *args):
        """ Retrieve data from a website """

        if len(args) >= 1:
            raise kerri.ExcessArguments("get_site()", 1)
        else:
            try:
                page = requests.get(url)
                html = page.text
                text_only = bs(html, 'html.parser')
                text = text_only.get_text()
                data = text.encode('ascii', 'ignore').decode('ascii')
                return(data)
            except requests.ConnectionError:
                raise kerri.INetFailure('get_site()')
            except Exception as error:
                raise kerri.Unknown("get_site()", error)


    def get_site(self, url, *args):
        """ Retrieve data from a website """

        if len(args) >= 1:
            raise kerri.ExcessArguments("get_site()", 1)
        else:
            try:
                page = requests.get(url)
                html = page.text
                text_only = bs(html, 'html.parser')
                text = text_only.get_text()
                data = text.encode('ascii', 'ignore').decode('ascii')
                return (data)
            except requests.ConnectionError:
                raise kerri.INetFailure('get_site()')
            except Exception as error:
                raise kerri.Unknown("get_site()", error)

    def save_site(self, url, filename, *args):
        """ Save the contents of a webpage to a file """

        if len(args) >= 1:
            raise kerri.ExcessArguments("save_site()", 2)
        else:
            try:
                page = requests.get(url)
                html = page.text
                text_only = bs(html, 'html.parser')
                text = text_only.get_text()
                data = text.encode('ascii', 'ignore').decode('ascii')
                cur_dir = os.path.abspath(os.curdir)
                outfile = open("%s/%s" % (cur_dir, str(filename.replace('http://', '').replace('https://', ''))), 'w')
                outfile.write(data)
                outfile.close()
            except requests.ConnectionError:
                raise kerri.INetFailure('save_site()')
            except Exception as error:
                raise kerri.Unknown("save_site()", error)

    def multi_save(self, url, path, *args):
        """ Saves multiple web pages to a file """

        if len(args) >= 1:
            raise kerri.ExcessArguments("multi_save()", 2)
        else:
            try:
                page = requests.get(url)
                html = page.text
                text_only = bs(html, 'html.parser')
                text = text_only.get_text()
                data = text.encode('ascii', 'ignore').decode('ascii')
                with open(path,'a') as xfile:
                    xfile.write(data)
                    xfile.close()
            except requests.ConnectionError:
                raise kerri.INetFailure("multi_save()")
            except Exception as error:
                raise kerri.Unknown("muti_save()", error)

    def f_get(self, url, save_path=pwd, *args):
        """ Download a file from url to specified directory """

        if len(args) >= 1:
            raise kerri.ExcessArguments("f_get()", 2)
        else:
            try:
                pipes = subprocess.Popen(["wget", url,
                                          "--directory-prefix=%s" % save_path],
                                         stdout=subprocess.PIPE,
                                         stderr=subprocess.PIPE)
                std_out, std_err = pipes.communicate()
                if pipes.returncode != 0:
                    raise kerri.ProcessFailure('f_get()', "[%d]: %s" % (pipes.returncode, str(std_err)))
                else:
                    return "[*] Save Successful!"
            except Exception as error:
                raise kerri.Unknown("f_get()", error)

#########
# INITs #
#########

spyder = Spyder()
print_site = spyder.print_site
get_site = spyder.get_site
save_site = spyder.save_site
multi_save = spyder.multi_save
f_get = spyder.f_get
