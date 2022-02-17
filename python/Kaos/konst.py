#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created: Aug 2017

    @author: D34D9001@9R0GR4M13
"""
import os
import subprocess
from termcolor import colored

# __init__

USER_ID = os.getuid()
UNAME = subprocess.Popen(["whoami"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
std_out, std_err = UNAME.communicate()
if len(std_out) >= 1:
    USER = str(std_out)
else:
    USER = str(std_err)

KAOS_VERSION = "Kaos_v3.5.601 (Beta)"
ENVIRONMENT = os.environ.copy()
OP_SYS = subprocess.check_output(["uname", "-r"])
LOG_DIRECTORY = "/var/log/kaos"

noroot = """You Must Be Root To Use The Kaos Module. Some Functions Will Not Work Without Root Access!!!"""
osna_warn = """IT IS NOT RECOMMENDED TO USE THIS MODULE WITH ANY\nSYSTEM OTHER THAN KALI LINUX. DOING SO MAY CAUSE SERIOUS,\nUNRESOLVABLE ISSUES TO YOUR OPERATING SYSTEM...\nYOU HAVE BEEN WARNED!!!"""
osrpi_warn = """The Kaos Module Has Not Been Properly Tested With The RaspberryPi. It May Not Work As Expected!"""
osarch_warn = """(BLACK)ARCH WAS USED TO ASSIST WITH THE DEVELOPMENT OF KAOS, HOWEVER, IT IS NOT RECOMMENDED TO USE THIS MODULE WITH ANY SYSTEM OTHER THAN KALI LINUX!!!"""

def log_mkr():
    print(colored("\nNo Kaos Logfile Exsists!!!", 'red', attrs=['bold']))
    print(colored("Creating One Now..."))
    os.mkdir(LOG_DIRECTORY)
    print(colored("The Kaos Log Directory Has Been Created @:   %s")
                  % LOG_DIRECTORY)

# gui_kFuncs

tfields = ("First_Name", "Middle_Name", "Last_Name", "City", "State")
device_info = 'IP Address', 'MAC Address', 'Host Name'
site_info = 'Host Name'
tshark_fields = "Interface"

logo_loc = "/usr/lib/kaos/media/logo/13-1.png"
logo_loc_bak = "/usr/share/wallpapers/KaliNeon/contents/images/1600x1200.png"

mac_vendors = '/usr/lib/kaos/mac_vendors'

pwd = os.getcwd()
