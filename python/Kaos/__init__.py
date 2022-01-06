#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import konst
import kmath
import kmess
import ksys
import ktime
import symbo
import os
import sys
import subprocess
from termcolor import colored

def __str__():
    """ Welcome To The "Kali Automated Operations System {KAOS}!!!"


    Created: Aug 2017

    @author: 73RM1N41@9R0GR4M13


    This module was created with both Kali and (Black)Arch Linux. Some functions may not
    be available on both operating systems. Alternatives for both may be added
    in future releases, (maybe)... or, solution: quit being a skid and just install the corresponding
    BlackArch program to Kali Linux.

    ============
    DISCLAIMER
    ============

    9ROGRAM13 NOR ANY OF IT'S DEVELOPERS SHALL BE HELD RESPONSIBLE FOR THE USERS
    ACTIONS WHILE USING THIS MODULE. ANY AND ALL DAMAGES INCURRED WHILE USING
    THIS MODULE SHALL REST SOLEY ON THE SHOULDERS OF THE USER THAT CAUSED
    SAID DAMAGES. BY USING THIS MODULE YOU ARE AGREEING TO WAIVE YOUR RIGHT
    TO HOLD 9R0GR4M13 OR ANY OF IT'S DEVELOPERS RESPONSIBLE FOR ABSOLUTELY
    ANYTHING THAT HAPPENS DUE TO YOUR (MIS)USE OF THIS MODULE. THE FUNCTIONS
    IN THIS MODULE MAY NOT HAVE BEEN FULLY TESTED AND MAY HAVE ADVERSE SIDE
    EFFECTS. 9R0GR4M13 IS NOT RESPONSIBLE FOR THAT EITHER. THIS MODULE HAS NOT
    BEEN RELEASED TO THE PUBLIC AND IS NOT INTENTED TO BE USED FOR ANY
    PRODUCTION LEVEL PROGRAMS. YOU MAY NOT USE THIS MODULE IN ANY PROGRAMS
    THAT YOU INTEND TO SELL. YOU MAY NOT USE THIS MODULE TO COMMIT ANY CRIMES
    ALTERATION.} YOU MAY NOT SELL THIS MODULE. YOU MAY NOT USE THIS MODULE
    CYBER OR OTHERWISE. YOU MAY NOT ALTER THIS MODULE IN ANY SIGNIFICANT WAY.
    {IF IT IS NOT NOTED IN A COMMENT OR OTHER STRING PRECEDING THE CHANGEABLE ITEM,
    THAT THE ITEM(S) MAY BE CHANGED, IT SHALL BE CONSIDERED A SIGNIFICANT
    TO FULFILL YOUR GOALS OF WORLD DOMINATION. IT IS IMPLIED THAT THE USER
    UNDERSTANDS IN FULL WHAT EVERY FUNCTION IN THIS MODULE DOES. IT IS UP TO
    THE USER OF THIS MODULE TO DETERMINE WHAT IS "SAFE" FOR USE IN THEIR
    CURRENT OPERATION AND WHAT IS "UNSAFE". THE USERS FAILURE TO DETERMINE
    THESE FACTORS IMPLIES THE USERS WILLING IGNORANCE AND, THIS MODULE
    SHALL BE CONSIDERED, FROM THAT POINT FORWARD, MISUSED. IT IS UP TO THE
    USER TO UNDERSTAND COMPLETELY, THE OUTCOME OF EACH KAOS FUNCTION USED
    WITHIN THE USERS SCRIPT/PROGRAM/MODULE. BY CONTINUING YOUR USE OF THIS
    MODULE YOU AGREE TO ALL OF THESE TERMS AND CONDITIONS.

    --enjoy :)
"""
# Portions Of Kaos Need Root Access To Function Properly
# Check To See If The User Is Root
USER_ID = os.getuid()

if USER_ID != 0:
#    sys.stderr.write(konst.noroot)
#    sys.exit(1)
    sys.stdout.write("User does not have root access! Some functions may not work.")
else:
#     print("You are %s, Let's Change The XAuth File...." % str(konst.USER))
# # SETUP XAUTHORITY
#     os.system("cp -a  => /home/$USER/.Xauthority .Xauthority")
#     os.system("chown root: .Xauthority")
#     os.system("XAUTHORITY=/root/.Xauthority")
#     print("XAuthority Set!")

    # outdata = subprocess.Popen(["sh", " => /home/$USER/Development/xauth_set.sh"],
    #                        stdout=subprocess.PIPE,
    #                        stderr=subprocess.PIPE)
    # std_out, std_err = outdata.communicate()
    # if len(std_err) != 0:
    #     sys.stderr.write(std_err.decode())
    # if len(std_out) != 0:
    #     print("%s" % std_out)

    KAOS_VERSION = konst.KAOS_VERSION
    ENVIRONMENT = konst.ENVIRONMENT
    OP_SYS = konst.OP_SYS
    LOG_DIRECTORY = konst.LOG_DIRECTORY
    OP_SYSTEM = None
    __all__ = ['KAOS_VERSION', 'OP_SYSTEM', 'symbo', 'kmath', 'ksys', 'kmess', 'ktime', 'stalker']

# Check The OS
    if b'kali' in OP_SYS:
        op_system = "Kali_Linux", OP_SYS, ENVIRONMENT
    elif b'Kali-Pi' in OP_SYS:
        op_system = "Kali-Pi", OP_SYS, ENVIRONMENT
        sys.stdout.write(konst.osrpi_warn)
    elif b'arch' in OP_SYS:
        op_system = "Arch_Linux", OP_SYS, ENVIRONMENT
        sys.stdout.write(konst.osarch_warn)
    else:
        op_system = b"N/A", OP_SYS
        print(konst.osna_warn)

# Check For The Kaos Log File
    if os.path.isdir(LOG_DIRECTORY):
        pass
# Create The Log File If It Does Not Exist
    else:
        konst.log_mkr()
