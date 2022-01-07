#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created: Aug 2017

    @author: D34D9001@9R0GR4M13
"""
import kerri
import subprocess

######################
# TELENET OPERATIONS #
######################

class Telnet(object):
    """ Controls Telnet Operations """

    def __str__(self):
        return """ Controls All Telnet Operations Preformed By Kaos """

    def telecon(self, host, *args):
        """ Connect to remote telnet host
            THIS IS VERY BUGGY ON KEYBOARDINTERRUPT """

        if len(args) >= 1:
            raise kerri.ExcessArguments("telecon()", 1)
        else:
            try:
                subprocess.call(["telnet", host])
            except KeyboardInterrupt:
                subprocess.call(["pkill", "-f", "telnet", host])
                raise kerri.UsrInt("telecon()", "The Connection Was Killed By The User!")
            except subprocess.CalledProcessError:
                raise kerri.ProcessFailure("telecon()")
            except Exception as error:
                raise kerri.Unknown("telecon()", error)

#########
# INITs #
#########

telnet = Telnet()
telecon = telnet.telecon
