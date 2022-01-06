#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created: Aug 2017

    @author: 73RM1N41@9R0GR4M13
"""
import kerri
import subprocess
import sys
from termcolor import colored
# import stem   # CURRENTLY UNUSED #

##########################
# THE ONION ROUTER {TOR} #
##########################

class Tor(object):
    """ Control The TOR Service """

    def __str__(self):
        return """ Controls Kaos Interactions With The Onion Router And Related TOR Services """

    def tserv(self, action="start", *args):
        """ Controls The TOR Service """
        if len(args) >= 1:
            raise kerri.ExcessArguments("tor_serv", 1)
        else:
            if str(action) == "start" or str(action) == "stop" or str(action) == "restart":
                try:
                    tor = subprocess.Popen(["systemctl", str(action), "tor"],
                                           stdout=subprocess.PIPE,
                                           stderr=subprocess.PIPE)
                    std_out, std_err = tor.communicate()
                    if len(std_out) != 0:
                        return std_out
                    if len(std_err) != 0:
                        sys.stderr.write(std_err)
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFailure("tor_serv()")
                except Exceptin as error:
                    raise kerri.Unknown("tor_serv(), error")
            else:
                print(colored("\"action\" must be either [start], [stop], or [restart]"))
                kerri.InvalidInput("tserv()", "\"action\" must be either [start], [stop], or [restart]")

#########
# INITs #
#########

tor = Tor()
tserv = tor.tserv
