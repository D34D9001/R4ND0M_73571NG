#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created: Aug 2017

    @author: 73RM1N41@9R0GR4M13
"""
import kerri
import os
import time
import sys
from termcolor import colored

####################
# MESSAGE HANDLING #
####################


class Messaging(object):
    """ Message Handling """

    def __str__(self):
        return """This Class Handles All Messaging Functions For Kaos.
Subclasses:
        Standard - Controls Standard Messaging
        Warn - Controls Warnings, Errors, and other important messages """

    class Standard(object):
        """ Standard Message Handling """

        def __init__(self, out_color='yellow', alt_out='blue'):
            self.out_color = out_color
            self.alt_out = alt_out

        def __str__(self):
            return """Print A Standard Message To The Screen.
All Functions Except For stdout_msg() And stderr_msg() Are Colored
By Default.

The Current Default Colors Are:
                                out_color: %s
                                alt_out: %s """ % (self.out_color,
                                                   self.alt_out)

        def stdout_msg(self, message, *args):
            """ Print a message directly to stdout """

            if len(args) >= 1:
                raise kerri.ExcessArguments("stdout_msg()", 1)
            else:
                try:
                    sys.stdout.write(message)
                except Exception as error:
                    raise kerri.Unknown("stdout_msg()", error)

        def stderr_msg(self, message, *args):
            """ Print a message directly to stderr """

            if len(args) >= 1:
                raise kerri.ExcessArguments("stderr_msg()", 1)
            else:
                try:
                    sys.stderr.write(message)
                except Exception as error:
                    raise kerri.Unknown("stderr_msg()", error)

        def std_msg(self, message, out_color=None, atts='bold', *args):
            """ Print A Standard Colored Message To stdout """

            if len(args) >= 1:
                raise kerri.ExcessArguments('std_msg()', 3)
            else:
                try:
                    if out_color is None:
                        out_color = self.out_color
                    if len(atts) != 0:
                        print(colored(message, out_color, attrs=[atts]))
                    else:
                        print(colored(message, out_color))
                except Exception as error:
                    raise kerri.Unknown("std_msg()", error)

        def tmd_msg(self, message, out_color=None, atts='bold', timer='1',
                    *args):
            """ Print A Message To stdout, Then Wait (n) Seconds """

            if len(args) >= 1:
                raise kerri.ExcessArguments('tmd_msg()', 4)
            else:
                if out_color is None:
                    out_color = self.out_color
                try:
                    print(colored(message, out_color, attrs=[atts]))
                    time.sleep(timer)
                except Exception as error:
                    raise kerri.Unknown("tmd_msg()", error)

        def aless_msg(self, message, out_color=None, *args):
            """ Print an attributeless message to stdout """

            if len(args) >= 1:
                raise kerri.ExcessArguments('aless_msg()', 2)
            else:
                if out_color is None:
                    out_color = self.out_color
                try:
                    print(colored(message, out_color))
                except Exception as error:
                    raise kerri.Unknown("aless_msg()", error)

        def typed_msg(self, message, speed=.05, color=None, atts=None, *args):
            if len(args) >= 1:
                raise kerri.ExcessArguments('typed_msg()', 3)
            else:
                if color is None:
                    for i in message:
                        os.system("printf '%s'" % i)
                        time.sleep(speed)
                if atts is not None:
                    for i in message:
                        os.system("printf '%s'" % colored(i, str(color),
                                                          attrs=["%s" % atts]))
                        time.sleep(speed)
                else:
                    for i in message:
                        os.system("printf '%s'" % colored(i, str(color)))
                        time.sleep(speed)

    class Warn(object):
        """ Warning and Error messaging handling """

        def __init__(self, out_color='yellow', on_color='red'):
            self.out_color = out_color
            self.on_color = on_color

        def __str__(self):
            return """ This Class Handles All Warnings, Errors, And Other
Important Messages That Are Not Handled By The Exceptions Defined In Kaos.

The Current Default Colors Are:
                                out_color: %s
                                on_color: %s """ % (self.out_color,
                                                    self.on_color)

        def warning(self, message, out_color=None, *args):
            """ Print a colored warning message to stdout """

            if len(args) >= 1:
                raise kerri.ExcessArguments("warning()", 1)
            else:
                if out_color is None:
                    out_color = self.out_color
                try:
                    print(colored("[*] %s" % message, out_color,
                                  attrs=['bold']))
                except Exception as error:
                    raise kerri.Unknown("warning()", error)

        def error_msg(self, message, out_color='red', *args):
            """ Print a colored error message to stdout """

            if len(args) >= 1:
                raise kerri.ExcessArguments("error_msg()", 1)
            else:
                if out_color is None:
                    out_color = self.out_color
                try:
                    print(colored("[!] %s" % message, out_color,
                                  attrs=['bold']))
                except Exception as error:
                    raise kerri.Unknown("error_msg()", error)

        def imp_not(self, message, out_color=None, on_color=None, atts='bold',
                    *args):
            """ Print colored important message to stdout """

            if len(args) >= 1:
                raise kerri.ExcessArguments("imp_not()", 4)
            else:
                if out_color is None:
                    out_color = self.out_color
                if on_color is None:
                    on_color = self.on_color
                try:
                    print(colored("[-] %s" % message, '%s' % out_color,
                                  'on_%s' % on_color, attrs=[atts]))
                except Exception as error:
                    raise kerri.Unknown("imp_not()", error)


#########
# INITs #
#########

kmess = Messaging()

std = kmess.Standard()
stdout_msg = std.stdout_msg
stderr_msg = std.stderr_msg
std_msg = std.std_msg
tmd_msg = std.tmd_msg
typed = std.typed_msg
aless_msg = std.aless_msg

warn = kmess.Warn()
warning = warn.warning
error_msg = warn.error_msg
imp_not = warn.imp_not
