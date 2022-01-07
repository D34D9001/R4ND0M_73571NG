#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created: Aug 2017

    @author: D34D9001@9R0GR4M13
"""
import time
from termcolor import colored

# Global Output Colors

out_color = 'yellow'

alt_color = 'blue'

# Global Seperator
SEP = "############################################################################"

###
# Echo Symbol
###
ECHO_SYMB = (colored("\n[", 'grey', attrs=['bold']) +
             colored(">", 'green', attrs=['bold']) +
             colored("] ", 'grey', attrs=['bold']))

###
# Error Symbol
###
ERROR_SYMB = (colored("\n[", 'yellow', 'on_red', attrs=['bold']) +
              colored("ERROR", 'yellow', 'on_red', attrs=['bold']) +
              colored("]", 'yellow', 'on_red', attrs=['bold']))

###
# Notice Symbol
###
NOTIC_SYMB = (colored("\n[", 'yellow', attrs=['bold']) +
              colored("*", 'yellow', attrs=['bold']) +
              colored("] ", 'yellow', attrs=['bold']))

###
# Warning Symbol
###
WARN_SYMB = (colored("\n[", 'yellow', attrs=['bold']) +
             colored("!", 'red', attrs=['bold']) +
             colored("] ", 'yellow', attrs=['bold']))

###
# Notifier Coloring Dictionary
###
NOTIFIER = {'ok': 'green', 'notice': 'yellow', 'warning': 'blue',
            'error': 'red', 'echo': 'grey'}

###
# Keyword Coloring Dictionary
###
BGR = {'ok': 'on_green', 'notice': 'on_blue', 'warning': 'on_yellow',
       'error': 'on_red'}

###
# Symbol Dictionary
###
SYM = {'echo': ECHO_SYMB, 'notice': NOTIC_SYMB, 'warning': WARN_SYMB,
       'error': ERROR_SYMB}

###
# Start User Input Decorator String
###
CSTR_START = colored("┌─", 'grey', attrs=['bold'])

###
# End User Input Decorator Sting
###
CSTR_END = (colored("└──╼", 'grey', attrs=['bold']) +
            colored("[ ", 'green', attrs=['bold']))

###
# Colored Date And Time String
###
FULL_DATE = (colored(time.strftime("%d/%m/%Y") +
                     " | "+time.strftime("%H:%M:%S"), 'red'))

###
# Colored Date String
###
DATE = colored(time.strftime("%m/%d/%y"))

###
# Colored Time String
###
NOW = colored(time.strftime("%H:%M:%S"))

###
# Check Mark
###
CHECK = u'\u2713'

###
# Asterisk
###
STAR = "*"

###
# SMILEY
###
SMILEY = colored(":)", 'green', attrs=['bold'])
