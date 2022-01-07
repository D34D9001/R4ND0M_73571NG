#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created: Aug 2017

    @author: D34D9001@9R0GR4M13

This Is The Kaos Error Integration Module, AKA: Kerri
The Exceptions Defined Here Were Designed To Allow A Greater Output From
Program And Script Errors. These Errors May Not Include Every Available
Exception And May Not Be Any Easier To Use With Your Program Or Script
Than The Standard Imported Exceptions.
"""

import time
import os
from termcolor import colored

# Current Directory

global pwd

# THIS WILL SET THE CURRENT WORKING DIRECTORY AT TIME OF KAOS IMPORT
# IF THE DIRECTORY IS CHANGED AFTER KAOS IS IMPORTED, THIS VARIABLE
# WILL NOT CHANGE AUTOMATICALLY, BUT IT CAN BE CHANGED MANUALLY BY:
#   pwd = \'new/directory/path/\'

pwd = os.getcwd()

##################
# ERROR HANDLING #
##################

# Change This Variable To Change The Error Log Location
elog = "/var/log/kaos/error.log"

def e_date():
    """ This date/time string is for use with the Exceptions defined in the
        Error Handling Section """

    return (time.strftime("%d/%m/%Y") + " | "+time.strftime("%H:%M:%S"))

E_Sym = colored("[ERROR]:", 'red')

Alt_E = "[ERROR]:"

"""
######################
# ERROR RETURN CODES #
######################

These are the returncodes and definitions
of when the errors should be raised:

Error Name:         RCode    Definition:
################    #####    ###############

# ProcessFailure      4      Raised When Process Fails
                             To Complete {Same As
                             subprocess.CalledProcessError
                             but with optional logging}

# InvalidInput        1      Raised When User Inputs Invalid
                             Argument Data Into A Function

# ExcessArguments     2      Raised When User Inputs Too Many
                             Arguments Into A Function Call

# INetFailure         5      Raised When Program Or Function
                             Cannot Connect To The Internet

# FSError             3      Raised When The File Or Directory
                             A User Requests Does Not Exist.
                             Or When The User Attempts To Use
                             An Invalid Filetype

# OutOfRange          8      Raised When Index For Function Call
                             Is Out Of Range. {Same As The Standard
                             IndexError But With Optional Logging}

# UsrInt              7      Raised When The User Interrupts A
                             Process {Same As KeyboardInterrupt
                             But With Optional Logging}

# Duplication         9      Raise When User Attempts To
                             Create A File Or Directory That
                             Already Exists.

# AttribError         10     Raised when user attempts to use an
                             invalid attribute with an object

# Unknown             6      Raised To Catch All Other Errors
                             That Are Not Defined Here

# 13 - 21             13     Return Codes that are reserved for special
                      14     instances where a function may throw the
                      15     same exception for 2 or more different errors.
                      16     The developer should change an instance of
                      17     the exception to match one of these return
                      18     codes while leaving the other exception(s) as
                      19     it is. Using the \'except Exception as error:\'
                      20     statement, the developer may then be able to more
                      21     easily define exactly which error message
                             should be displayed for each exception caught.

###   Ex:

try:
    if filename.endswith(".gz"):
        raise FSError("func()", "This Is The Wrong Type Of File!!!",
                       returncode=13)
    else:
        if os.path.isfile(filename):
            print("Coolio!")
        else:
            raise FSError("func()", "File or Directory Does Not Exist!")
except Exception as error:
    if error.returncode == 3:
        raise FSError("func()", "Doesn't Exist!")
    elif error.returncode == 13:
        raise FSError("func()", "Wrong Filetype!")
    else:
        raise Unknown("func()", error)
"""

class ProcessFailure(Exception):
    """ Error called when process fails to complete """

    def __init__(self, cmd, output=None, log=1,
                 elog_file=elog, returncode=4):
        self.returncode = returncode
        self.cmd = cmd
        self.output = output
        self.log = log
        self.elog_file = elog_file

    def __str__(self):
        if self.output == None:
            if self.log == 1:
                with open(self.elog_file, 'a') as errfile:
                    errfile.write("[%s]   %s returned a non-zero exit status [%d]: %s Failed To Complete Process!\n" % (str(e_date()), self.cmd, self.returncode, Alt_E))
                    errfile.close()
            return "%s returned a non-zero exit status [%d]: %s Failed To Complete Process!" % (self.cmd, self.returncode, E_Sym)
        else:
            if self.log == 1:
                with open(self.elog_file, 'a') as errfile:
                    errfile.write("[%s]   %s returned a non-zero exit status [%d]: %s %s\n" % (str(e_date()), self.cmd, self.returncode, Alt_E, self.output))
                    errfile.close()
            return "%s returned a non-zero exit status [%d]: %s %s" % (self.cmd, self.returncode, E_Sym, self.output)

class InvalidInput(Exception):
    """ Error called when user inputs invalid data or variables """

    def __init__(self, cmd, output=None, log=1,
                 elog_file=elog, returncode=1):
        self.returncode = returncode
        self.cmd = cmd
        self.output = output
        self.log = log
        self.elog_file = elog_file

    def __str__(self):
        if self.output == None:
            if self.log == 1:
                with open(self.elog_file, 'a') as errfile:
                    errfile.write("[%s]   %s returned a non-zero exit status [%d]: %s Invalid Input!\n" % (str(e_date()), self.cmd, self.returncode, Alt_E))
                    errfile.close()
            return "%s returned a non-zero exit status [%d]: %s Invalid Input!" % (self.cmd, self.returncode, E_Sym)
        else:
            if self.log == 1:
                with open(self.elog_file, 'a') as errfile:
                    errfile.write("[%s]   %s returned a non-zero exit status [%d]: %s %s\n" % (str(e_date()), self.cmd, self.returncode, Alt_E, self.output))
                    errfile.close()
            return "%s returned a non-zero exit status [%d]: %s %s" % (self.cmd, self.returncode, E_Sym, self.output)

class ExcessArguments(Exception):
    """ Error called when user inputs too many arguments """

    def __init__(self, cmd, arg_count, output=None, log=0,
                 elog_file=elog, returncode=2):
        self.returncode = returncode
        self.cmd = cmd
        self.arg_count = arg_count
        self.output = output
        self.log = log
        self.elog_file = elog_file

    def __str__(self):
        if self.output == None:
            if self.log == 1:
                with open(self.elog_file, 'a') as errfile:
                    errfile.write("[%s]   %s returned a non-zero exit status [%d]: %s %s Takes (%i) Arguments!\n" % (str(e_date()), self.cmd, self.returncode, Alt_E, self.cmd, self.arg_count))
                    errfile.close()
            return "%s returned a non-zero exit status [%d]: %s %s Takes (%i) Arguments!" % (self.cmd, self.returncode, E_Sym, self.cmd, self.arg_count)
        else:
            if self.log == 1:
                with open(self.elog_file, 'a') as errfile:
                    errfile.write("[%s]   %s returned a non-zero exit status [%d]: %s %s\n" % (str(e_date()), self.cmd, self.returncode, Alt_E, self.output))
                    errfile.close()
            return "%s returned a non-zero exit status [%d]: %s %s" % (self.cmd, self.returncode, E_Sym, self.output)

class INetFailure(Exception):
    """ Error called when the program cannot connect to the internet """

    def __init__(self, cmd, output=None, log=1,
                 elog_file=elog, returncode=5):
        self.returncode = returncode
        self.cmd = cmd
        self.output = output
        self.log = log
        self.elog_file = elog_file

    def __str__(self):
        if self.output == None:
            if self.log == 1:
                with open(self.elog_file, 'a') as errfile:
                    errfile.write("[%s]   %s returned a non-zero exit status [%d]: %s %s Could Not Connect To The Internet!\n" % (str(e_date()), self.cmd, self.returncode, Alt_E, self.cmd))
                    errfile.close()
            return "%s returned a non-zero exit status [%d]: %s %s Could Not Connect To The Internet!" % (self.cmd, self.returncode, E_Sym, self.cmd)
        else:
            if self.log == 1:
                with open(self.elog_file, 'a') as errfile:
                    errfile.write("[%s]   %s returned a non-zero exit status [%d]: %s %s\n" % (str(e_date()), self.cmd, self.returncode, Alt_E, self.output))
                    errfile.close()
            return "%s returned a non-zero exit status [%d]: %s %s" % (self.cmd, self.returncode, E_Sym, self.output)

class FSError(Exception):
    """ Error called when a file or directory cannot be found or when
        the user attempts to use an invalid filetype.
        This exception defaults to \"FileNotFound\". To specify an invalid
        filetype you must change the output message"""

    def __init__(self, cmd, output=None, log=1,
                 elog_file=elog, returncode=3):
        self.cmd = cmd
        self.output = output
        self.returncode = returncode
        self.log = log
        self.elog_file = elog_file

    def __str__(self):
        if self.output == None:
            if self.log == 1:
                with open(self.elog_file, 'a') as errfile:
                    errfile.write("[%s]   %s File Or Directory Does Not Exist! %s Failed!\n" % (str(e_date()), Alt_E, self.cmd))
                    errfile.close()
            return "%s File Or Directory Does Not Exist! %s Failed!" % (E_Sym, self.cmd)
        else:
            if self.log == 1:
                with open(self.elog_file, 'a') as errfile:
                    errfile.write("[%s]   %s returned a non-zero exit status [%d]: %s %s\n" % (str(e_date()), self.cmd, self.returncode, Alt_E, self.output))
                    errfile.close()
            return "%s returned a non-zero exit status [%d]: %s %s" % (self.cmd, self.returncode, E_Sym, self.output)

class OutOfRange(Exception):
    """ Error called when user index input is out of range """

    def __init__(self, cmd, output=None, log=0,
                 elog_file=elog, returncode=8):
        self.returncode = returncode
        self.cmd = cmd
        self.output = output
        self.log = log
        self.elog_file = elog_file

    def __str__(self):
        if self.output == None:
            if self.log == 1:
                with open(self.elog_file, 'a') as errfile:
                    errfile.write("[%s]   %s returned a non-zero exit code [%d]: %s Index Out Of Range!\n" % (str(e_date()), self.cmd, self.returncode, Alt_E))
                    errfile.close()
            return "%s returned a non-zero exit code [%d]: %s Index Out Of Range!" % (self.cmd, self.returncode, E_Sym)
        else:
            if self.log == 1:
                with open(self.elog_file, 'a') as errfile:
                    errfile.write("[%s]   %s returned a non-zero exit status [%d]: %s %s\n" % (str(e_date()), self.cmd, self.returncode, Alt_E, self.output))
                    errfile.close()
            return "%s returned a non-zero exit status [%d]: %s %s" % (self.cmd, self.returncode, E_Sym, self.output)

class UsrInt(Exception):
    """ Error called when user interrupts a process """

    def __init__(self, cmd, output=None, log=0,
                 elog_file=elog, returncode=7):
        self.returncode = returncode
        self.cmd = cmd
        self.output = output
        self.log = log
        self.elog_file = elog_file

    def __str__(self):
        if self.output == None:
            if self.log == 1:
                with open(self.elog_file, 'a') as errfile:
                    errfile.write("[%s]   [%d] User Hit CTRL^C! %s Was Halted...\n" % (str(e_date()), self.returncode, self.cmd))
                    errfile.close()
            return "[%d] User Hit CTRL^C! %s Was Halted..." % (self.returncode, self.cmd)
        else:
            if self.log == 1:
                with open(self.elog_file, 'a') as errfile:
                    errfile.write("[%s]   %s returned a non-zero exit status [%d]: %s %s\n" % (str(e_date()), self.cmd, self.returncode, Alt_E, self.output))
                    errfile.close()
            return "User Halted %s With CTRL^C [%d]: %s %s" % (self.cmd, self.returncode, E_Sym, self.output)

class DuplicationError(Exception):
    """ Error called when user tries to create a file or directory that
        already exists """

    def __init__(self, cmd, output=None, log=0,
                 elog_file=elog, returncode=9):
        self.returncode = returncode
        self.cmd = cmd
        self.output = output
        self.log = log
        self.elog_file = elog_file

    def __str__(self):
        if self.output == None:
            if self.log == 1:
                with open(self.elog_file, 'a') as errfile:
                    errfile.write("[%s]   %s File Or Directory Already Exists!!! %s Can Not Create Another One!\n" % (str(e_date()), Alt_E, self.cmd))
                    errfile.close()
            return "%s File Or Directory Already Exists!!! %s Can Not Create Another One!" % (E_Sym, self.cmd)
        else:
            if self.log == 1:
                with open(self.elog_file, 'a') as errfile:
                    errfile.write("[%s]   %s returned a non-zero exit status [%d]: %s %s\n" % (str(e_date()), self.cmd, self.returncode, Alt_E, self.output))
                    errfile.close()
            return "%s returned a non-zero exit status [%d]: %s %s" % (self.cmd, self.returncode, E_Sym, self.output)

class Unknown(Exception):
    """ Error called when an exception is encountered that is not defined in
        another kaos.Exception """

    def __init__(self, cmd, output=None, log=1,
                 elog_file=elog, returncode=6):
        self.returncode = returncode
        self.cmd = cmd
        self.output = output
        self.log = log
        self.elog_file = elog_file

    def __str__(self):
        if self.output == None:
            if self.log == 1:
                with open(self.elog_file, 'a') as errfile:
                    errfile.write("[%s]   %s returned a non-zero exit code [%d]: %s An Unknown Error Has Occured!\n" % (str(e_date()), self.cmd, self.returncode, Alt_E))
                    errfile.close()
            return "%s returned a non-zero exit code [%d]: %s An Unknown Error Has Occured!" % (self.cmd, self.returncode, E_Sym)
        else:
            if self.log == 1:
                with open(self.elog_file, 'a') as errfile:
                    errfile.write("[%s]   %s returned a non-zero exit status [%d]: %s %s\n" % (str(e_date()), self.cmd, self.returncode, Alt_E, self.output))
                    errfile.close()
            return "%s returned a non-zero exit status [%d]: %s %s" % (self.cmd, self.returncode, E_Sym, self.output)
