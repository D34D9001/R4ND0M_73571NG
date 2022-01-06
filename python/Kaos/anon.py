#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Created: Aug 2017

    @author: 73RM1N41@9R0GR4M13
"""

import kerri
import ktime
import ksys
import fakeid
import symbo

# Occasional Issues Loading Module
# Will Be Skipped Upon Failure
# May Cause Functionality Errors

try:
    import GeoIP
except Exception as error:
    print("%s" % error)
    print("GeoIP Failed To Load! Continuing Without It...")
    print("Some Functions May Not Work As A Result!")

import os
import subprocess
import sys
import time
from termcolor import colored

sep = symbo.SEP
wait = ktime.wait
ex = ksys.ex

########
# ANON #
########


class Anon(object):
    """ These functions should help the user stay anon or
        cover their tracks at the very least
        USE THESE FUNCTIONS AT YOUR OWN RISK!!! """

    def __init__(self, auth_log="/var/log/auth.log",
                 bash_history="/root/.bash_history", dev_null="/dev/null",
                 *args):
        """ Define The Various Log/History Files And ID Variables Used By Anon.
            The Default Values Are Usually The Default Locations Of The
            Referenced Files And Should Not Be Changed Unless You Know The
            File Is In A Different Location. """

        self.anoid_nameset = {"American": "us", "Arabic": "ar", "Brazil": "br",
                              "Chechen": "celat", "Chinese": "ch",
                              "Chinese-Traditional": "zhtw", "Croation": "hr",
                              "Czech": "cs", "Danish": "dk", "Dutch": "nl",
                              "England/Wales": "en", "Eritrean": "er",
                              "Finnish": "fi", "French": "fr", "German": "gr",
                              "Greenland": "gl", "Hispanic": "sp",
                              "Hobbit": "hobbit", "Hungarian": "hu",
                              "Icelandic": "is", "Igbo": "ig", "Italian": "it",
                              "Japanese": "jpja", "Japanese-Anglicized": "jp",
                              "Ninja": "ninja", "Norwegian": "no",
                              "Persian": "fa", "Polish": "pl", "Russian": "ru",
                              "Russian-Cyrillic": "rucyr", "Scottish": "gd",
                              "Slovenian": "sl", "Swedish": "sw", "Thai": "th",
                              "Vietnamese": "vn"}

        self.country = {"Australia": "au", "Austria": "as", "Belgium": "bg",
                        "Brazil": "br", "Canada": "ca",
                        "Cyprus Anglicized": "cyen", "Cyprus Greek": "cygk",
                        "Czech Republic": "cz", "Denmark": "dk",
                        "Estonia": "ee", "Finland": "fi", "France": "fr",
                        "Germany": "gr", "Greenland": "gl", "Hungarian": "hu",
                        "Iceland": "is", "Italy": "it", "Netherlands": "nl",
                        "New Zealand": "nz", "Norway": "no", "Poland": "pl",
                        "Portugal": "pt", "Slovenia": "sl",
                        "South Africa": "za", "Spain": "sp", "Sweden": "sw",
                        "Switzerland": "sz", "Tunisia": "tn",
                        "United Kingdom": "uk", "United States": "us",
                        "Uruguay": "uy"}

        print("[!] NO FUNCTION IN THIS MODULE SHOULD BE CONSIDERED " +
              "PERFECT. *ALWAYS DOUBLE CHECK THAT EVERYHTNG\n" +
              "WORKED CORRECTLY.* THIS MODULE COMES WITH NO " +
              "GUARENTEES OF ANY KIND. USE THIS AT YOUR OWN RISK!!!")

        if len(args) >= 1:
            raise kerri.ExcessArguments("Anon()", 3)
        else:
            self.auth_log = auth_log
            self.bash_history = bash_history
            self.dev_null = dev_null

    def __str__(self):
        return """ Hide In The Kaos """

    def watergate(self, *args):
        """ Erase (most) traces of having accessed a system
            This will log the user out and delete important
            log files and history files. USE AT YOUR OWN RISK"""

        # The user is advised to run Anon.blackhole() after logging
        # back in, to permanently send all bash_history commands to
        # /dev/null

        if len(args) >= 1:
            raise kerri.ExcessArguments("watergate()", 0)
        else:
            try:
                # clear auth log file
                with open(self.auth_log, 'w') as log:
                    log.write("")
                    log.close()
                # clear current user bash history
                with open(self.bash_history, 'w') as hist:
                    hist.write("")
                    hist.close()
                # delete ~/.bash_history file
                srm = subprocess.Popen(["srm", "-r", self.bash_history],
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE)
                std_out, std_err = srm.communicate()
                if len(std_err) != 0:
                    sys.stderr.write(std_err)
                # clear current session history
                history = subprocess.Popen(["history", "-c"],
                                           stdout=subprocess.PIPE,
                                           stderr=subprocess.PIPE)
                std_out, std_err = history.communicate()
                if len(std_err) != 0:
                    sys.stderr.write(std_err)
                # set history max lines to 0
                export = subprocess.Popen(["export", "HISTFILESIZE=0"],
                                          stdout=subprocess.PIPE,
                                          stderr=subprocess.PIPE)
                std_out, std_err = export.communicate()
                if len(std_err) != 0:
                    sys.stderr.write(std_err)
                # set history max commands to 0
                exp = subprocess.Popen(["export", "HISTSIZE=0"],
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE)
                std_out, std_err = exp.communicate()
                if len(std_err) != 0:
                    sys.stderr.write(std_err)
                # disable history {this requires a logout afterwards
                unset = subprocess.Popen(["unset", "HISTFILE"],
                                         stdout=subprocess.PIPE,
                                         stderr=subprocess.PIPE)
                std_out, std_err = unset.communicate()
                if len(std_err) != 0:
                    sys.stderr.write(std_err)
                # kill the current session {this will
                # force the user to be logged out}
                kill = subprocess.Popen(["kill", "-9", "$$"],
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE)
                std_out, std_err = kill.communicate()
                if len(std_err) != 0:
                    sys.stderr.write(std_err)
            except subprocess.CalledProcessError:
                raise kerri.ProcessFailure("watergate()")
            except Exception as error:
                raise kerri.Unknown("watergate()", error)

    def blackhole(self, *args):
        """ Send All Bash History Commands To /dev/null """

        if len(args) >= 1:
            raise kerri.ExcessArguments("blackhole()")
        else:
            try:
                # clear the current user bash history
                with open(self.bash_history, 'w') as hist:
                    hist.write("")
                    hist.close()
                # permanently send all bash history commands to /dev/null
                link = subprocess.Popen(["ln", "-sf", self.dev_null,
                                         self.bash_history],
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE)
                std_out, std_err = link.communicate()
                if len(std_err) != 0:
                    sys.stderr.write(std_err)
            except subprocess.CalledProcessError:
                raise kerri.ProcessFailure("blackhole()")
            except Exception as error:
                raise kerri.Unknown("blackhole()", error)

    def histoclear(self, *args):
        """ Clear The ~/.bash_history File """

        if len(args) >= 1:
            raise kerri.ExcessArguments("histoclear()", 0)
        else:
            try:
                # open the bash_history file and erase the data
                with open("/root/bash_history", 'w') as hist:
                    hist.write("")
                    hist.close()
                subprocess.Popen(["history", "-c"])
            except Exception as error:
                raise kerri.Unknown("histoclear()", error)

    def dishist(self, *args):
        """ Disable The ~/.bash_history File {Requires A Logout}"""

        if len(args) >= 1:
            raise kerri.ExcessArguments("dishist()", 0)
        else:
            try:
                # Disable The Bash History File
                subprocess.Popen(["unset", "HISTFILE"])
                # Kill All Current Processes
                # This Will Automatically Log The User Out
                subprocess.Popen(["kill", "-9", "$$"])
            except subprocess.CalledProcessError:
                raise kerri.ProcessFailure("dishist()")
            except Exception as error:
                raise kerri.Unknown("dishist()", error)

#############################################
# These Functions Are Still In BETA Testing #
#############################################

    def anoid(self, *args):
        if len(args) >= 1:
            raise kerri.ExcessArguments("", )
        else:
            # GET CURRENT IP ADDRESS
            print("Getting Your Current IP Address...")
            wait(.25)
            try:
                orig_ip = subprocess.check_output(["curl", "-s",
                                                   "ifconfig.me/ip"])
            except Exception:
                print("[!] COULD NOT GET IP ADDRESS FROM SERVER!!!")
                print("    IF THE PROBLEM CONTINUES, CHECK YOUR " +
                              "INTERNET CONNECTION")
            command = "curl -s ifconfig.me/ip"
            print("[%s] {' %s '}\n" % (symbo.CHECK, command))

            # RESTORE DEFAULT IPTABLES RULES
            print("Flushing Iptables...")
            if os.path.isfile("/root/iptables.kaos.default"):
                os.system("iptables-restore < /root/iptables.kaos.default")
                command = "iptables-restore < /root/iptables.kaos.default"
                print("[%s] {' %s '}\n" % (symbo.CHECK, command))
            else:
                pass

            # RESTART TOR SERVICE
            print("Restarting TOR...")
            subprocess.call(["systemctl", "restart", "tor"])
            command = "systemctl restart tor"
            print("[%s] {' %s '}\n" % (symbo.CHECK, command))

            # WAIT 10 SECONDS TO ENSURE TOR BOOTSTRAP COMPLETION
            print("Waiting 10 Seconds For TOR To Complete " +
                          "Bootstrapping...")
            count = 0
            subprocess.call(["printf", "["])
            while count <= 9:
                wait(1)
                os.system("printf '%s'" % symbo.STAR)
                count += 1
            print("] [%s]" % symbo.CHECK)
            print(" ")
            wait(1)

            # CHECK THAT BOOTSTRAP COMPLETED
            try:
                report = os.popen("systemctl status tor | grep 'Done'").read()
                if "Done" in str(report):
                    print("%s" % report)
                else:
                    print("Your System Does Not Appear To Be Using TOR!")
                    print("Please Make Sure You Are Connected To The Internet And Try Again.")
                    sys.exit("[!] Could Not Verify Tor Bootstrap. Program Terminated...")

            except Exception as e:
                print("SOMETHING WENT HORRIBLY WRONG!!!\n" +
                              "KERNAL PANIC!!!!!!")
                wait(3)
                print("Nah I'm just screwing with you...\n " +
                      "Something did go wrong though, that part " +
                      "wasn\'t a joke.")
                print(e)

            # Apply TOR IPTABLES RULES
            print("Applying TOR Iptables Rules...")
            tor_ip_rules = """*nat
:PREROUTING ACCEPT [0:0]
:OUTPUT ACCEPT [0:0]
:POSTROUTING ACCEPT [0:0]
-A PREROUTING -d 192.168.0.12/32 -j RETURN
-A PREROUTING -p udp -m udp --dport 53 -j REDIRECT --to-ports 53
-A PREROUTING -p tcp -m tcp --tcp-flags FIN,SYN,RST,ACK SYN -j REDIRECT --to-ports 49151
-A OUTPUT -o lo -j RETURN
-A OUTPUT -m owner --uid-owner 0 -j RETURN
-A OUTPUT -p udp -m udp --dport 53 -j REDIRECT --to-ports 53
-A OUTPUT -p tcp -m tcp --tcp-flags FIN,SYN,RST,ACK SYN -j REDIRECT --to-ports 49151
COMMIT
*filter
:INPUT DROP [0:0]
:FORWARD DROP [0:0]
:OUTPUT DROP [0:0]
-A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT
-A INPUT -p icmp -j ACCEPT
-A INPUT -i lo -j ACCEPT
-A INPUT -p tcp -m conntrack --ctstate NEW -m tcp -d 127.0.0.1 --dport 22 -j ACCEPT
-A INPUT -j LOG --log-prefix "IPV4 REJECT INPUT: "
-A FORWARD -j LOG --log-prefix "IPV4 REJECT FORWARD: "
-A OUTPUT -m state --state RELATED,ESTABLISHED -j ACCEPT
-A OUTPUT -o lo -j ACCEPT
-A OUTPUT -d 127.0.0.1/32 -p udp -m udp --dport 53 -j ACCEPT
-A OUTPUT -d 127.0.0.1/32 -p tcp -m tcp --dport 49151 -j ACCEPT
-A OUTPUT -m owner --uid-owner 0 -m conntrack --ctstate NEW -j ACCEPT
-A OUTPUT -j LOG --log-prefix "IPV4 REJECT OUTPUT: "
COMMIT
"""
            # Save The Current Iptables Rules
            subprocess.Popen(["iptables-save", "-f",
                              "/root/iptables.kaos.default"])
            # Check To See If The IPRules Exist
            if not os.path.isfile("/root/tor.iptables"):
                with open("/root/tor.iptables" 'w') as ip_rules:
                    ip_rules.write("%s" % tor_ip_rules)
                    ip_rules.close()
                os.system("iptables-restore < /root/tor.iptables")
            else:
                os.system("iptables-restore < /root/tor.iptables")
            command = "iptables-restore < /root/tor.iptables"
            print("[%s] {' %s '}\n" % (symbo.CHECK, command))
            rules = subprocess.check_output(["iptables", "-L"])
            wait(1)

            # DISPLAY NEW IPTABLES RULES
            print("%s" % sep)
            print("          New Firewall Rules")
            print("%s" % sep)
            print("%s\n" % rules)
            print("%s" % sep)
            wait(1)

            # CHECK TOR CONNECTIVITY STATUS
            print("Checking TOR Connectivity Status...")
            print("%s" % sep)
            try:
                status = subprocess.Popen(("curl", "-s",
                                           "https://check.torproject.org"),
                                          stdout=subprocess.PIPE)
                output = subprocess.check_output(("grep", "-o", "-m", "1",
                                                  "Congratulations"),
                                                 stdin=status.stdout)
                con_status = output.strip('\n')
                if con_status == "Congratulations":
                    connected = "CONNECTED"
                    print("You Are %s To TOR" % connected)
                else:
                    not_con = "NOT CONNECTED"
                    print("You Are %s To TOR" % not_con)
                    print("Something Seems To Have Gone Wrong...\n" +
                          "Try Running This Command Again.")
            except subprocess.CalledProcessError:
                sys.exit("[!] COULD NOT VERIFY TOR CONNECTION!!!\n" +
                         "PLEASE TRY AGAIN")
            print(" ")
            wait(.25)

            # CHECK FOR NEW IP ADDRESS AND OTHER CONNECTION INFO
            print("%s" % sep)
            print("Checking IP Address...")
            try:
                global ip
                ip = subprocess.check_output(["curl", "-s", "ifconfig.me/ip"])
                command = "curl -s ifconfig.me/ip"
                print("[%s] {' %s '}\n" % (symbo.CHECK, command))
                print("Getting Connection Information...")
                connection_info = subprocess.check_output(["curl", "-s",
                                                           "ifconfig.me/all"])
                command = "curl -s ifconfig.me/all"
                print("[%s] {' %s '}\n" % (symbo.CHECK, command))
                wait(.5)

            # DISPLAY NEW IDENTITY INFORMATION
                print("%s" % sep)
                print("            NEW ID INFORMATION")
                print("%s" % sep)
                for i in connection_info:
                    os.system("printf '%s'" % i)
                    wait(.025)
            except subprocess.CalledProcessError:
                sys.exit("[!] COULD NOT RECEIVE IP ADDRESS FROM " +
                         "SERVER...\nCHECK YOUR INTERNET CONNECTION " +
                         "AND RUN THIS COMMAND AGAIN")
            time.sleep(1)

            # CHECK TO MAKE SURE IP ADDRESS IS DIFFERENT THAN ORIGINAL
            print("%s" % sep)
            try:
                if str(orig_ip) == str(ip):
                    wait(.5)
                    sys.exit("[!] YOUR IP ADDRESS WAS NOT CHANGED..." +
                             "\nPLEASE TRY AGAIN.")
                else:
                    time.sleep(.5)
                    print("Your IP Address Was Changed!")
                    print("\n[ORIGINAL]: ")
            except NameError:
                print("[!] Your Original IP Address Could Not Be " +
                      "Located\n    This Could Be Due To " +
                      "Connectivity Issues When\n    This Program " +
                      "Was Started. If You Got No\n    Other Error " +
                      "Messages You Should Be Fine.")
            # PRINT ORIGINAL IP ADDRESS
            try:
                for i in orig_ip:
                    os.system("printf '%s'" % i)
                    wait(.050)
            except NameError:
                print("[!] Your Original IP Address Could Not Be " +
                      "Located...")

            # PRINT NEW IP ADDRESS
            print("\n[NEW]: ")
            try:
                for i in ip:
                    os.system("printf '%s'" % i)
                    wait(.050)
                print("%s" % sep)
                print("\n * If This Is Not The IP Address From The ID\n" +
                      "Information Section, It May Have Gotten Changed\n" +
                      "Twice. You May Manually Check Your IP With\n'curl " +
                      "ifconfig.me' Or Run This Command Again.")
            except Exception as e:
                print("[!] THERE WAS A PROBLEM!")
                print(e)
            # PRINT COMPLETION MESSAGE AND EXIT
            print("%s" % sep)
            string = "[*] PROCESS COMPLETE!!!"
            for i in string:
                os.system("printf '%s'" % i)
                wait(.025)
            print("\n\n")
            print("%s" % sep)

            print(""" As with all products claiming to provide
                  anonymity, this should not be your only line of
                  defense. Please make sure your browser(s) and
                  terminal(s) are configured correctly. Do NOT provide
                  ANY information to ANYONE that may give clues as to
                  your true identity. Do NOT open any downloaded
                  files while connected to the internet. CHECK ALL
                  FILES for viruses and malware before opening. And
                  of course, most importantly, DON'T BE STUPID!
                  9R0GR4M13 nor any of its developers/affiliates
                  shall be held accountable for your actions while
                  using this, or any other, 9R0GR4M13 software.""")
            print("\n\n")

    def fake_id(self, ip=None, *args):
        if len(args) >= 1:
            raise kerri.ExcessArguments("fake_id()", 1)
        else:
#            if ip is None:
                # Replace subprocess with kaos
                # ip = ex("curl -s ifconfig.me/ip")
#                ip = subprocess.check_output(["curl", "-s", "ifconfig.me/ip"])
#                ip = ip.strip()
#            else:
#                pass
#            country_code = subprocess.check_output(["geoip",  ip])
#            with open("/tmp/anoid_geoip", 'w') as geo:
#                geo.write(country_code.lower())
#                geo.close()

#            cntry = subprocess.check_output(["cut", "-d ", "-f5-6",
#                                             "/tmp/anoid_geoip"])
#            with open("/tmp/anoid_geoip", 'w') as geoip:
#                geoip.write(cntry)
#                geoip.close()
#            ip_location = subprocess.check_output(["cat", "/tmp/anoid_geoip"])
#            country = str(ip_location)
#            cty = country.rstrip()
#            geoip = GeoIP.new(1)
#            cntry = geoip.country_name_by_addr("%s" % str(ip))
#            cty = str(cntry)
#            if cty == "Address not":
#                print("IP Address Location Not Available...\nIDGen Will Use " +
#                      "Default Settings.\nNameset: American\nCountry: " +
#                      "United States")
#                cty = "United States"
#            else:
#                print colored("IPAddress Location: %s" % self.anoid_nameset[cty],
#                              'magenta', attrs=['bold'])
#            wait(2)
#        fakeid.id_gen(ncntry="%s" % self.anoid_nameset[cty], sex="random")

            fakeid.id_gen(nset="American", cntry="United States", sex="random", out="/root/fake_id.txt")

#########
# INITs #
#########


anon = Anon()
watergate = anon.watergate
blackhole = anon.blackhole
histoclear = anon.histoclear
dishist = anon.dishist
anoid = anon.anoid
fake_id = anon.fake_id
