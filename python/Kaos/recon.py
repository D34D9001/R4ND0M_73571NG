#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created: Aug 2017

    @author: D34D9001@9R0GR4M13
"""
import kerri
import ktime
import symbo
import os
import random
import requests
import re
import subprocess
import sys
import time
from bs4 import BeautifulSoup
from lumberjack import logit
from timeit import timeit
from threading import Thread
from termcolor import colored

# Current Directory

global pwd

# THIS WILL SET THE CURRENT WORKING DIRECTORY AT TIME OF KAOS IMPORT
# IF THE DIRECTORY IS CHANGED AFTER KAOS IS IMPORTED, THIS VARIABLE
# WILL NOT CHANGE AUTOMATICALLY, BUT IT CAN BE CHANGED MANUALLY BY:
#   pwd = \'new/directory/path/\'

pwd = os.getcwd()

# Output Color
out_color = symbo.out_color

# MAC Vendor List Location
mac_vendors_list = "/usr/lib/kaos/mac_vendors"

#########################
# TARGET RECONNAISSANCE #
#########################


class Recon(object):
    """
    Recon Tools
    """

    def __str__(self):
        return """ Controls All Kaos Target Reconnaissance Operations """

    def arp(self, host, *args):
        if len(args) >= 1:
            raise kerri.ExcessArguments
        else:
            try:
                arp = subprocess.Popen(["/usr/bin/arp", host],
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE)
                std_out, std_err = arp.communicate()
                if len(std_out) != 0:
                    return std_out
                if len(std_err) != 0:
                    sys.stderr.write(std_err)
            except subprocess.CalledProcessError:
                raise kerri.ProcessFailure("arp()")
            except Exception as error:
                raise kerri.Unknown("arp()", error)

    def drift(self, interface, router_ip, local_ip, *args):
        """ Intercept All Images That Pass Over The Network """

        if len(args) >= 1:
            raise kerri.ExcessArguments("drift()", 3)
        else:
            try:
                os.system("""arpspoof -i %s -t %s %s &
                             ettercap -Tqi %s -M arp:remote /// &
                             driftnet -i %s""" % (interface, router_ip,
                                                  local_ip, interface,
                                                  interface))
            except KeyboardInterrupt:
                raise kerri.UsrInt("drift()")
            except Exception as error:
                raise kerri.Unknown("drift()", error)

    def local_arp(self, *args):
        """
        Runs arp-scan on localnet
        """

        if len(args) >= 1:
            raise kerri.ExcessArguments("arpscan()", 0)
        else:
            try:
                data = subprocess.check_output(["/usr/sbin/arp-scan", "-l"])
                return data
            except subprocess.CalledProcessError:
                raise kerri.ProcessFailure("arpscan()")
            except Exception as error:
                raise kerri.Unknown("arpscan()", error)

    def bingip(self, host, *args):
        if len(args) >= 1:
            raise kerri.ExcessArguments("bingip()")
        else:
            try:
                bing = subprocess.Popen(["/usr/bin/bing-ip2hosts", host],
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE)
                std_out, std_err = bing.communicate()
                if len(std_out) != 0:
                    return std_out
                if len(std_err) != 0:
                    sys.stderr.write(std_err)
            except subprocess.CalledProcessError:
                raise kerri.ProcessFailure("bing-ip2hosts()")
            except Exception as error:
                raise kerri.Unknown("bing-ip2hosts()", error)

    def httrack(self, url, *args):
        """
        Clones The Given Url
        """

        if len(args) >= 1:
            raise kerri.ExcessArguments("httrack()", 1)
        else:
            try:
                httrack = subprocess.Popen(["/usr/bin/httrack", url],
                                           stdout=subprocess.PIPE,
                                           stderr=subprocess.PIPE)
                std_out, std_err = httrack.communicate()
                if len(std_out) != 0:
                    return std_out
                else:
                    sys.stderr.write(std_err)
            except subprocess.CalledProcessError:
                raise kerri.ProcessFaiure("httrack()")
            except Exception as error:
                raise kerri.Unknown("httrack()", error)

    def citrix(self, target, port, *args):
        """
        Run Citrix With Specified Target And Port
        """

        if len(args) >= 1:
            raise kerri.ExcessArguments("citrix()", 2)
        else:
            try:
                out = subprocess.check_output(["/usr/bin/citrix",
                                               target, port])
                return out
            except subprocess.CalledProcessError:
                raise kerri.ProcessFaiure("citrix()")
            except Exception as error:
                raise kerri.Unknown("citrix()", error)

    def dig(self, target, *args):
        """
        Find Target Information With Dig
        """

        if len(args) >= 1:
            raise kerri.ExcessArguments("dig()", 1)
        else:
            try:
                dig_info = subprocess.check_output(['/usr/bin/dig', target])
                return dig_info
            except KeyboardInterrupt:
                raise kerri.UsrInt("dig()")
            except subprocess.CalledProcessError:
                raise kerri.ProcessFaiure("dig()")
            except Exception as error:
                raise kerri.Unknown("dig()", error)

    def whois(self, host, *args):
        """
        Preforms WhoIs Search On Specified Host
        """

        if len(args) >= 1:
            raise kerri.ExcessArguments("whois()", 1)
        else:
            try:
                data = subprocess.Popen(["/usr/bin/whois", host],
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE)
                std_out, std_err = data.communicate()
                if len(std_out) != 0:
                    return std_out
                if len(std_err) != 0:
                    return std_err
            except KeyboardInterrupt:
                raise kerri.UsrInt("whois()")
            except subprocess.CalledProcessError:
                raise kerri.ProcessFailure("whois()")
            except Exception as error:
                raise kerri.Unknown("whois()", error)

    def nslookup(self, url, *args):
        """
        Preforms NSLookup On Specified Host
        """

        if len(args) >= 1:
            raise kerri.ExcessArguments("nslookup()", 1)
        else:
            try:
                data = subprocess.check_output(["/usr/bin/nslookup",
                                                "-type=any", url])
                return colored(data, out_color, attrs=['bold'])
            except subprocess.CalledProcessError:
                raise kerri.ProcessFaiure("nslookup()")
            except Exception as error:
                raise kerri.Unknown("nslookup", error)

    def dmitry(self, host, *args):
        """
        Preforms Dmitry Scan On Target Host
        """

        if len(args) >= 1:
            raise kerri.ExcessArguments("dmitry()", 1)
        else:
            try:
                data = subprocess.check_output(["/usr/bin/dmitry", host])
                return colored(data, out_color, attrs=['bold'])
            except subprocess.CalledProcessError:
                raise kerri.ProcessFaiure("dmitry()")
            except Exception as error:
                raise kerri.Unknown("dmitry()", error)

    def webinfo(self, site, whois=1, dig=1, dig_s=1, nsl=1, nikto=0, *args):
        """
        Preforms WhoIs, Dig, NSLookuup, And Nikto On Specified Website
        By Default, All Scans Will Be Preformed. This May Take A Long Time...
        Disable Nikto To Significantly Increase The Completion Time Of The Scan
        """

        self.whois = whois
        self.dig = dig
        self.dig_s = dig_s
        self.nsl = nsl
        self.nikto = nikto
        global finished
        finished = False
        global runtime
        data = {}

        def info_getter():
            if len(args) >= 1:
                raise kerri.ExcessArguments("webinfo()", 1)
            else:
                data["host"] = str(site)
                start_time = ktime.marker()
# WHOIS
                try:
                    if self.whois == 1:
                        whois = subprocess.Popen(["/usr/bin/whois", site],
                                                 stdout=subprocess.PIPE,
                                                 stderr=subprocess.PIPE)
                        std_out, std_err = whois.communicate()
                        if len(std_err) != 0:
                            sys.stderr.write(std_err)
                        if len(std_out) != 0:
                            data["whois"] = std_out.decode().strip()
                    elif self.whois == 0:
                        data["whois"] = "N/A"
                    else:
                        sys.stderr.write("The \'whois\' parameter has to be" +
                                         "either a 0:{off} or a 1:{on}. If" +
                                         "this option is not a 0 or 1, the" +
                                         "WhoIs scan will not be preformed...")
# DIG
                    if self.dig == 1:
                        dig = subprocess.Popen(["/usr/bin/dig", site],
                                               stdout=subprocess.PIPE,
                                               stderr=subprocess.PIPE)
                        std_out, std_err = dig.communicate()
                        if len(std_err) != 0:
                            sys.stderr.write(std_err)
                        if len(std_out) != 0:
                            data["dig"] = std_out.decode().strip()
                    elif self.dig == 0:
                        data["dig"] = "N/A"
                    else:
                        sys.stderr.write("The \'dig\' parameter has to be" +
                                         "either a 0:{off} or a 1:{on}." +
                                         "If this option is not a 0 or 1," +
                                         "the Dig scan will not be preformed" +
                                         "...")
# SHORT DIG
                    if dig_s == 1:
                        dig_short = subprocess.Popen(["/usr/bin/dig", "+short",
                                                      site],
                                                     stdout=subprocess.PIPE,
                                                     stderr=subprocess.PIPE)
                        std_out, std_err = dig_short.communicate()
                        if len(std_err) != 0:
                            sys.stderr.write(std_err)
                        if len(std_out) != 0:
                            data["dig_short"] = std_out.decode().strip()
                    elif self.dig_s == 0:
                        data["dig_short"] = "N/A"
                    else:
                        sys.stderr.write("The \'dig_s\' parameter has to be" +
                                         "either a 0:{off} or a 1:{on}. If" +
                                         "this option is not a 0 or 1, the" +
                                         "Short Dig scan will not be" +
                                         "preformed...")
# NSLOOKUP
                    if self.nsl == 1:
                        nslook = subprocess.Popen(["/usr/bin/nslookup", site],
                                                  stdout=subprocess.PIPE,
                                                  stderr=subprocess.PIPE)
                        std_out, std_err = nslook.communicate()
                        if len(std_err) != 0:
                            sys.stderr.write(std_err)
                        if len(std_out) != 0:
                            data["nslookup"] = std_out.decode().strip()
                    elif self.nsl == 0:
                        data["nslookup"] = "N/A"
                    else:
                        sys.stderr.write("The \'nsl\' parameter has to be " +
                                         "either a 0:{off} or a 1:{on}. If " +
                                         "this option is not a 0 or 1, the " +
                                         "NSLookup will not be preformed...")
# NIKTO
                    if self.nikto == 1:
                        nikto = subprocess.Popen(["/usr/bin/nikto", "-host",
                                                  site, "-C", "all"],
                                                 stdout=subprocess.PIPE,
                                                 stderr=subprocess.PIPE)
                        std_out, std_err = nikto.communicate()
                        if len(std_err) != 0:
                            sys.stderr.write(std_err)
                        if len(std_out) != 0:
                            data["nikto"] = std_out.decode().strip()
                    elif self.nikto == 0:
                        data["nikto"] = "N/A"
                    else:
                        sys.stderr.write("The \'nikto\' parameter has to be " +
                                         "either a 0:{off} or a 1:{on}. If " +
                                         "this option is not a 0 or 1, the " +
                                         "Nikto scan will not be preformed...")
                        data["nikto"] = "N/A"

                    end_time = ktime.marker()
                    global runtime
                    runtime = end_time - start_time
                    global finished
                    finished = True
                except KeyboardInterrupt:
                    raise kerri.UsrInt("webinfo()")
                except Exception as error:
                    raise kerri.Unknown("webinfo()", error)

        def waiter():
            while True:
                global finished
                # Check To See If Webinfo Has Finished
                if finished is not True:
                    # If Webinfo Is Not Finished, Print The Message
                    for i in range(1, 2):
                        ktime.wait(.25)
                        sys.stdout.write(colored("\r[\\] Gathering Website " +
                                                 "Information. Please Wait...",
                                                 'yellow', 'on_red',
                                                 attrs=['bold']))
                        sys.stdout.flush()
                        ktime.wait(.25)
                        sys.stdout.write(colored("\r[|] Gathering Website " +
                                                 "Information. Please Wait...",
                                                 'yellow', 'on_red',
                                                 attrs=['bold']))
                        sys.stdout.flush()
                        ktime.wait(.25)
                        sys.stdout.write(colored("\r[/] Gathering Website " +
                                                 "Information. Please Wait...",
                                                 'yellow', 'on_red',
                                                 attrs=['bold']))
                        sys.stdout.flush()
                        ktime.wait(.25)
                        sys.stdout.write(colored("\r[-] Gathering Website " +
                                                 "Information. Please Wait...",
                                                 'yellow', 'on_red',
                                                 attrs=['bold']))
                        sys.stdout.flush()
                # If Webinfo Is Finished, Break The Loop
                elif finished is True:
                    sys.stdout.write(colored("\r[*] Target Scan: %s " +
                                             "Completed In %s seconds."
                                             % (site, str(float(runtime))),
                                             'green', 'on_blue',
                                             attrs=['bold'])+"\n")
                    break
                # If Kaos Somehow Lost Track Of The finished Variable,
                # Break The Loop
                else:
                    print("Not Sure If Webinfo Finished So Kaos Is Stopping...")
                    break

        getter = Thread(target=info_getter)
        watcher = Thread(target=waiter)

        getter.start()
        watcher.start()

        getter.join()
        watcher.join()
        finished = None
        runtime = None
        out_info = ""
        for item in data:
            out_info = out_info + "\n" + data[item] + item
        return out_info

    def wafw00f(self, url, *args):
        """
        Web Application Firewall Detection
        """

        if len(args) >= 1:
            raise kerri.ExcessArguments("wafw00f()", 1)
        else:
            try:
                data = subprocess.check_output(["/usr/bin/wafw00f", url])
                return colored(data, out_color, attrs=['bold'])
            except subprocess.CalledProcessError:
                raise kerri.ProcessFaiure("wafw00f()")
            except Exception as error:
                raise kerri.Unknown("wafw00f()", error)

    def p0f(self, interface, out_file="/tmp/p0f.log", *args):
        if len(args) >= 1:
            raise kerri.ExcessArguments("p0f()", 1)
        else:
            try:
                p0f = subprocess.Popen(["/usr/bin/p0f", "-i", interface, "-p",
                                        "-o",
                                       out_file],
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE)
                std_out, std_err = p0f.communicate()
                if len(std_err) != 0:
                    sys.stderr.write(std_err)
                if len(std_out) != 0:
                    return std_out
            except KeyboardInterrupt:
                raise kerri.UsrInt("p0f(-i %s -p -o %s)"
                                   % (interface, out_file))
            except subprocess.CalledProcessError:
                raise kerri.ProcessFailure("p0f()")
            except Exception as error:
                raise kerri.Unknown("p0f()", error)

    def arp_fprint(self, interface, target, *args):
        if len(args) >= 1:
            raise kerri.ExcessArguments("arp_fprint()", 2)
        else:
            try:
                output = subprocess.Popen(["/usr/sbin/arp-fingerprint", "-o",
                                          "-N -I %s" % interface, target],
                                          stdout=subprocess.PIPE,
                                          stderr=subprocess.PIPE)
                std_out, std_err = output.communicate()
                if len(std_out) != 0:
                    return std_out
                if len(std_err) != 0:
                    sys.stderr.write(std_err)
#                os.system("/usr/bin/arp-fingerprint -o \"-N -I "
#                          + interface + "\" " + target)
            except subprocess.CalledProcessError:
                raise kerri.ProcessFailure("arp-fprint()")
            except Exception as error:
                raise kerri.Unknown("arp-fprint()", error)

    def dcap(self, interface, *args):
        if len(args) >= 1:
            raise kerri.ExcessArguments("dcap()", 1)
        else:
            try:
                subprocess.call(["/usr/bin/dumpcap", "-i", interface])
            except subprocess.CalledProcessError:
                raise kerri.ProcessFailure("dcap()")
            except Exception as error:
                raise kerri.Unknown("dcap()", error)

#   ###############
#   # DNSANALYSIS #
#   ###############

    class DNSAnalysis(object):

        def __str__(self):
            return "Controls DNS Analysis Operations Preformed By Kaos"

        def dnsenum(self, url, *args):
            """
            Runs DNSEnum Against Target URL
            """

            if len(args) >= 1:
                raise kerri.ExcessArguments("dnsenum()", 1)
            else:
                try:
                    output = subprocess.Popen(["/usr/bin/dnsenum", "--enum",
                                               "--private", url],
                                              stdout=subprocess.PIPE,
                                              stderr=subprocess.PIPE)
                    std_out, std_err = output.communicate()
                    if len(std_out) != 0:
                        return std_out
                    else:
                        sys.stderr.write(std_err)
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFaiure("dnsenum()")
                except Exception as error:
                    raise kerri.Unknown("dnsenum()", error)

        def dnsmap(self, url, *args):
            """
            Runs DNSMap On Target URL
            """

            if len(args) >= 1:
                raise kerri.ExcessArguments("dnsmap()", 1)
            else:
                try:
                    data = subprocess.check_output(["/usr/bin/dnsmap", url])
                    return colored(data, out_color, attrs=['bold'])
#                except subprocess.CalledProcessError:
#                    raise kerri.ProcessFaiure("dnsmap()")
                except Exception as error:
                    raise kerri.Unknown("dnsmap()", error)

        def dnstracer(self, host, *args):
            """ Preform A Very Basic DNS Trace """

            if len(args) >= 1:
                raise kerri.ExcessArguments("dnstracer()", 1)
            else:
                try:
                    trace = subprocess.Popen(["/usr/bin/dnstracer", host],
                                             stdout=subprocess.PIPE,
                                             stderr=subprocess.PIPE)
                    std_out, std_err = trace.communicate()
                    if len(std_err) != 0:
                        sys.stderr.write(std_err)
                    if len(std_out) != 0:
                        return std_out
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFailure("dnstracer")
                except Exception as error:
                    raise kerri.Unknown("dnstracer()", error)

#   ########
#   # NMAP #
#   ########

    class NMap(object):
        """
        This class controls the NMap program
        for both Kali and [Black]Arch Linux
        """

        def __init__(self, spoof=0, log=0, logdir="/var/log/kaos/nmap/",
                     silent=0):
            self.silent = silent
            macs = []
            vendors = open(mac_vendors_list, 'r').read()
#            vendors = open("/usr/lib/kaos/mac_vendors", 'r').read()
            for item in vendors.split("\n"):
                macs.append(item)
            self.macs = macs
            self.spoof = spoof
            self.log = log
            self.nmap_logdir = logdir
            nmap_log = str(logdir) + "nmap.log"
            if str(os.path.isdir(self.nmap_logdir)) == "True":
                number = time.strftime("%m%d%H%M%S")
                nmap_log = "%snmap%s.log" % (logdir, number)
            else:
                print("There Is No Log Directory For NMap! Creating One Now...")
                try:
                    os.mkdir(logdir)
                    print("Log Directory Created @ %s" % logdir)
                except Exception as error:
                    raise kerri.Unknown("THERE WAS A PROBLEM CREATING THE " +
                                        "DIRECTORY!!! KAOS CANNOT CONTINUE!",
                                        error)
            self.nmap_log = nmap_log

        def __str__(self):
            return """ Controls All Kaos <=> NMap Interactions """

        def flush_log(self, log_file, *args):
            if len(args) >= 1:
                raise kerri.ExcessArguments("flush_log()", 1)
            else:
                try:
                    if str(os.path.isfile(log_file)) == "True":
                        file_name = log_file.split("/")[-1:][0]
                        if file_name.startswith("nmap"):
                            if file_name.endswith(".log"):
                                subprocess.call(["/usr/bin/srm", "-GCf",
                                                 log_file])
                            else:
                                raise kerri.FSError("flush_log()",
                                                    "NMap.flush_log() Is For" +
                                                    " Removing nmap Logs" +
                                                    " Only!", returncode=13)
                        else:
                            raise kerri.FSError("flush_log()",
                                                "NMap.flush_log() Is For ",
                                                "Removing nmap Logs Only!",
                                                returncode=13)
                        sys.stdout.write("Log Removed Successfully!")
                    else:
                        raise kerri.FSError("flush_log(%s)" % log_file)
                except Exception as error:
                    if error.returncode == 13:
                        sys.stderr.write("[ERROR]: %s does not appear to be " +
                                         "an nmap log. The proper naming" +
                                         " format is \'nmap[anything" +
                                         "_here].log\'" % log_file)
                        raise kerri.FSError("flush_log()", "NMap.flush_log()" +
                                            " Is For Removing nmap Logs Only!")
                    elif error.returncode == 3:
                        raise kerri.FSError("flush_log(%s)" % log_file)
                    else:
                        raise kerri.Unknown("flush_log()", error)

        # RETURN THE AMOUNT OF TIME IT TOOK A PROCESS TO COMPLETE
        def run_time(func, *args):
            """ Returns the amount of time it took a process
                to run. THIS DOES NOT RETURN THE OUTPUT OF THE
                FUNCTION TESTED, ONLY THE RUNTIME """
        # A SIMPLE FUNCTION WRAPPER
            def wrapper(func, *args, **kwargs):
                " A simple function wrapper "

                def wrapped():
                    return func(*args, **kwargs)
                return wrapped

            if len(args) >= 1:
                arg_list = []
                for item in args:
                    arg_list.append(item)
                wrapped = wrapper(func, str(arg_list).replace("'",
                                  "").replace(",", "").replace("[",
                                  "").replace("]", ""))
            else:
                wrapped = wrapper(func)
                runtime = timeit(wrapped, number=1)
                return runtime

        def pro_map(self, target, *args):
            """ Specify your own options for NMap
                NOT RECOMMENDED FOR BEGINNERS """

            if len(args) == 0:
                raise kerri.InvalidInput("pro_map",
                                         "You Must Specify At Least 1 " +
                                         "Option!!!")
            else:
                try:
                    print(str(args).replace("(", "").replace(")", ""))
                    pro = subprocess.Popen(["/usr/bin/nmap",
                                            str(args).replace("(",
                                                              "").replace(")",
                                                                          ""),
                                            str(target)],
                                           stdout=subprocess.PIPE,
                                           stderr=subprocess.PIPE)
                    std_out, std_err = pro.communicate()
                    if len(std_err) != 0:
                        if self.log == 0:
                            if self.silent == 0:
                                sys.stderr.write(std_err)
                            else:
                                pass
                        elif self.log == 1:
                            logit(std_err, self.nmap_log)
                        else:
                            pass
                    else:
                        return std_out
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFailure("pro_map()")
                except KeyboardInterrupt:
                    sys.stderr.write("[!] THE NMAP PROCESS DOES NOT FINISH " +
                                     "CORRECTLY WHEN CTRL^C\'d WITH KAOS!!!")
                    raise kerri.UsrInt("pro_map()",
                                       "[!] PLEASE DO NOT EXIT AN NMAP " +
                                       "PROCESS WITH CTRL^C")
                except Exception as error:
                    raise kerri.Unknown("pro_map()", error)

        def std_map(self, host, *args):
            """ Preform Basic NMap Scan On Target Host """

            if len(args) >= 1:
                raise kerri.ExcessArguments("std_map()", 1)
            else:
                try:
                    if self.spoof == 1:
                        mac = random.choice(self.macs)
                        data = subprocess.Popen(["/usr/bin/nmap", "-vv", "-A",
                                                 "--spoof-mac", str(mac),
                                                 str(host)],
                                                stdout=subprocess.PIPE,
                                                stderr=subprocess.PIPE)
                        std_out, std_err = data.communicate()
                    else:
                        data = subprocess.Popen(["/usr/bin/nmap", "-vv", "-A",
                                                 str(host)],
                                                stdout=subprocess.PIPE,
                                                stderr=subprocess.PIPE)
                        std_out, std_err = data.communicate()
                    if len(std_err) != 0:
                        if self.log == 0:
                            if self.silent == 0:
                                sys.stderr.write(std_err)
                            else:
                                pass
                        elif self.log == 1:
                            logit(std_err, self.nmap_log)
                        else:
                            pass
                    else:
                        return std_out
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFaiure("std_map()", 4, std_err)
                except Exception as error:
                    raise kerri.Unknown("std_map()", error)

        def connect_map(self, host, *args):
            """ Preform Connect() Scan On Target Host """

            if len(args) >= 1:
                raise kerri.ExcessArguments("connect_map()", 1)
            else:
                try:
                    if self.spoof == 1:
                        mac = random.choice(self.macs)
                        data = subprocess.Popen(["/usr/bin/nmap", "-vv", "-sT",
                                                 "--spoof-mac", str(mac),
                                                 str(host)],
                                                stdout=subprocess.PIPE,
                                                stderr=subprocess.PIPE)
                        std_out, std_err = data.communicate()
                    else:
                        data = subprocess.Popen(["/usr/bin/nmap", "-vv", "-sT",
                                                 str(host)],
                                                stdout=subprocess.PIPE,
                                                stderr=subprocess.PIPE)
                        std_out, std_err = data.communicate()
                    if len(std_err) != 0:
                        if self.log == 0:
                            if self.silent == 0:
                                sys.stderr.write(std_err)
                            else:
                                pass
                        elif self.log == 1:
                            logit(std_err, self.nmap_log)
                        else:
                            pass
                    else:
                        return std_out
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFaiure("connect_map()", 4, std_err)
                except Exception as error:
                    raise kerri.Unknown("connect_map()", error)

        def ack_map(self, host, *args):
            """ Preform ACK Scan On Target Host """

            if len(args) >= 1:
                raise kerri.ExcessArguments("ack_map()", 1)
            else:
                try:
                    if self.spoof == 1:
                        mac = random.choice(self.macs)
                        data = subprocess.Popen(["/usr/bin/nmap", "-vv", "-sA",
                                                 "--spoof-mac", str(mac),
                                                 str(host)],
                                                stdout=subprocess.PIPE,
                                                stderr=subprocess.PIPE)
                        std_out, std_err = data.communicate()
                    else:
                        data = subprocess.Popen(["/usr/bin/nmap", "-vv", "-sA",
                                                 str(host)],
                                                stdout=subprocess.PIPE,
                                                stderr=subprocess.PIPE)
                        std_out, std_err = data.communicate()
                    if len(std_err) != 0:
                        if self.log == 0:
                            if self.silent == 0:
                                sys.stderr.write(std_err)
                            else:
                                pass
                        elif self.log == 1:
                            logit(std_err, self.nmap_log)
                        else:
                            pass
                    else:
                        return std_out
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFaiure("ack_map()", 4, std_err)
                except Exception as error:
                    raise kerri.Unknown("ack_map()", error)

        def window_map(self, host, *args):
            """ Preform Window Scan On Target Host """

            if len(args) >= 1:
                raise kerri.ExcessArguments("window_map()", 1)
            else:
                try:
                    if self.spoof == 1:
                        mac = random.choice(self.macs)
                        data = subprocess.Popen(["/usr/bin/nmap", "-vv", "-sW",
                                                 "--spoof-mac", str(mac),
                                                 str(host)],
                                                stdout=subprocess.PIPE,
                                                stderr=subprocess.PIPE)
                        std_out, std_err = data.communicate()
                    else:
                        data = subprocess.Popen(["/usr/bin/nmap", "-vv", "-sW",
                                                 str(host)],
                                                stdout=subprocess.PIPE,
                                                stderr=subprocess.PIPE)
                        std_out, std_err = data.communicate()
                    if len(std_err) != 0:
                        if self.log == 0:
                            if self.silent == 0:
                                sys.stderr.write(std_err)
                            else:
                                pass
                        elif self.log == 1:
                            logit(std_err, self.nmap_log)
                        else:
                            pass
                    else:
                        return std_out
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFaiure("window_map()", 4, std_err)
                except Exception as error:
                    raise kerri.Unknown("window_map()", error)

        def maimon_map(self, host, *args):
            """ Preform Maimon Scan On Target Host """

            if len(args) >= 1:
                raise kerri.ExcessArguments("maimon_map()", 1)
            else:
                try:
                    if self.spoof == 1:
                        mac = random.choice(self.macs)
                        data = subprocess.Popen(["/usr/bin/nmap", "-vv", "-sM",
                                                 "--spoof-mac", str(mac),
                                                 str(host)],
                                                stdout=subprocess.PIPE,
                                                stderr=subprocess.PIPE)
                        std_out, std_err = data.communicate()
                    else:
                        data = subprocess.Popen(["/usr/bin/nmap", "-vv", "-sM",
                                                 str(host)],
                                                stdout=subprocess.PIPE,
                                                stderr=subprocess.PIPE)
                        std_out, std_err = data.communicate()
                    if len(std_err) != 0:
                        if self.log == 0:
                            if self.silent == 0:
                                sys.stderr.write(std_err)
                            else:
                                pass
                        elif self.log == 1:
                            logit(std_err, self.nmap_log)
                        else:
                            pass
                    else:
                        return std_out
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFaiure("maimon_map()", 4, std_err)
                except Exception as error:
                    raise kerri.Unknown("maimon_map()", error)

        def fast_map(self, target, *args):
            """ Preform a \'fast\' scan with NMap """

            if len(args) >= 1:
                raise kerri.ExcessArguments("fast_map()", 1)
            else:
                try:
                    if self.spoof == 1:
                        mac = random.choice(self.macs)
                        nmap = subprocess.Popen(["/usr/bin/nmap", "-vv", "-F",
                                                 "--spoof-mac", str(mac),
                                                 "%s" % str(target)],
                                                stdout=subprocess.PIPE,
                                                stderr=subprocess.PIPE)
                        std_out, std_err = nmap.communicate()
                    else:
                        nmap = subprocess.Popen(["/usr/bin/nmap", "-vv", "-F",
                                                 "%s" % str(target)],
                                                stdout=subprocess.PIPE,
                                                stderr=subprocess.PIPE)
                        std_out, std_err = nmap.communicate()
                    if len(std_err) != 0:
                        if self.log == 0:
                            if self.silent == 0:
                                sys.stderr.write(std_err)
                            else:
                                pass
                        elif self.log == 1:
                            logit(std_err, self.nmap_log)
                        else:
                            pass
                    else:
                        return std_out
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFailure("fast_map()")
                except Exception as error:
                    raise kerri.Unknown("fast_map()", error)

        def net_map(self, target, range, *args):
            """ Check for active devices on a network """

            if len(args) >= 1:
                raise kerri.ExcessArguments("net_map()", 2)
            else:
                try:
                    if self.spoof == 1:
                        mac = random.choice(self.macs)
                        nmap = subprocess.Popen(["/usr/bin/nmap", "-vv",
                                                 "-sn", "--spoof-mac", mac,
                                                 "%s/%s" % (str(target),
                                                            str(range))],
                                                stdout=subprocess.PIPE,
                                                stderr=subprocess.PIPE)
                        std_out, std_err = nmap.communicate()
                    else:
                        nmap = subprocess.Popen(["/usr/bin/nmap", "-vv", "-sn",
                                                 "%s/%s" % (str(target),
                                                            str(range))],
                                                stdout=subprocess.PIPE,
                                                stderr=subprocess.PIPE)
                        std_out, std_err = nmap.communicate()
                    if len(std_err) != 0:
                        if self.log == 0:
                            if self.silent == 0:
                                sys.stderr.write(std_err)
                            else:
                                pass
                        elif self.log == 1:
                            logit(std_err, self.nmap_log)
                        else:
                            pass
                    else:
                        return std_out
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFailure("net_map()")
                except KeyboardInterrupt:
                    sys.stderr.write("[!] THE NMAP PROCESS DOES NOT FINISH " +
                                     "CORRECTLY WHEN CTRL^C\'d WITH KAOS!!!")
                    raise kerri.UsrInt("net_map()",
                                       "[!] PLEASE DO NOT EXIT AN NMAP " +
                                       "PROCESS WITH CTRL^C")
                except Exception as error:
                    raise kerri.Unknown("net_map()", error)

        def port_map(self, target, *args):
            """ Check for \'possibly\' open ports """

            if len(args) >= 1:
                raise kerri.ExcessArguments("port_map()", 1)
            else:
                try:
                    if self.spoof == 1:
                        mac = random.choice(self.macs)
                        ports = subprocess.Popen(["/usr/bin/nmap", "-vv",
                                                  "-open", "--spoof-mac", mac,
                                                  "%s" % str(target)],
                                                 stdout=subprocess.PIPE,
                                                 stderr=subprocess.PIPE)
                        std_out, std_err = ports.communicate()
                    else:
                        ports = subprocess.Popen(["/usr/bin/nmap", "-vv",
                                                  "-open", "%s" % str(target)],
                                                 stdout=subprocess.PIPE,
                                                 stderr=subprocess.PIPE)
                        std_out, std_err = ports.communicate()
                    if len(std_err) != 0:
                        if self.log == 0:
                            if self.silent == 0:
                                sys.stderr.write(std_err)
                            else:
                                pass
                        elif self.log == 1:
                            logit(std_err, self.nmap_log)
                        else:
                            pass
                    else:
                        return std_out
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFailure("port_map()")
                except KeyboardInterrupt:
                    sys.stderr.write("[!] THE NMAP PROCESS DOES NOT FINISH " +
                                     "CORRECTLY WHEN CTRL^C\'d WITH KAOS!!!")
                    raise kerri.UsrInt("port_map()", "[!] PLEASE DO NOT EXIT" +
                                       " AN NMAP PROCESS WITH CTRL^C")
                except Exception as error:
                    raise kerri.Unknown("port_map()", error)

        def os_map(self, target, *args):
            """ Check OS of target [Not always 100% accurate] """

            if len(args) >= 1:
                raise kerri.ExcessArguments("os_map()", 1)
            else:
                try:
                    if self.spoof == 1:
                        mac = random.choice(self.macs)
                        os = subprocess.Popen(["/usr/bin/nmap", "-vv", "-O",
                                               "--spoof-mac", mac,
                                               "%s" % str(target)],
                                              stdout=subprocess.PIPE,
                                              stderr=subprocess.PIPE)
                        std_out, std_err = os.communicate()
                    else:
                        mac = random.choice(self.macs)
                        os = subprocess.Popen(["/usr/bin/nmap", "-vv", "-O",
                                               "%s" % str(target)],
                                              stdout=subprocess.PIPE,
                                              stderr=subprocess.PIPE)
                        std_out, std_err = os.communicate()
                    if len(std_err) != 0:
                        if self.log == 0:
                            if self.silent == 0:
                                sys.stderr.write(std_err)
                            else:
                                pass
                        elif self.log == 1:
                            logit(std_err, self.nmap_log)
                        else:
                            pass
                    else:
                        return std_out
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFailure("os_map()")
                except KeyboardInterrupt:
                    sys.stderr.write("[!] THE NMAP PROCESS DOES NOT FINISH " +
                                     "CORRECTLY WHEN CTRL^C\'d WITH KAOS!!!")
                    raise kerri.UsrInt("os_map()",
                                       "[!] PLEASE DO NOT EXIT AN NMAP " +
                                       "PROCESS WITH CTRL^C")
                except Exception as error:
                    raise kerri.Unknown("os_map()", error)

        def vers_map(self, target, *args):
            """ Check for software versions """

            if len(args) >= 1:
                raise kerri.ExcessArguments("vers_map()", 1)
            else:
                try:
                    if self.spoof == 1:
                        mac = random.choice(self.macs)
                        vers = subprocess.Popen(["/usr/bin/nmap", "-vv", "-sV",
                                                 "--version-all",
                                                 "--spoof-mac", mac,
                                                 "%s" % str(target)],
                                                stdout=subprocess.PIPE,
                                                stderr=subprocess.PIPE)
                        std_out, std_err = vers.communicate()
                    else:
                        vers = subprocess.Popen(["/usr/bin/nmap", "-vv", "-sV",
                                                 "%s" % str(target)],
                                                stdout=subprocess.PIPE,
                                                stderr=subprocess.PIPE)
                        std_out, std_err = vers.communicate()
                    if len(std_err) != 0:
                        if self.log == 0:
                            if self.silent == 0:
                                sys.stderr.write(std_err)
                            else:
                                pass
                        elif self.log == 1:
                            logit(std_err, self.nmap_log)
                        else:
                            pass
                    else:
                        return std_out
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFailure("vers_map()")
                except KeyboardInterrupt:
                    raise kerri.UsrInt("vers_map()",
                                       "[!] PLEASE DO NOT EXIT AN NMAP " +
                                       "PROCESS WITH CTRL^C")
                    sys.stderr.write("[!] THE NMAP PROCESS DOES NOT FINISH " +
                                     "CORRECTLY WHEN CTRL^C\'d WITH KAOS!!!")
                except Exception as error:
                    raise kerri.Unknown("vers_map()", error)

        def fire_map(self, target, *args):
            """ Check to see if target is protected by firewalls
                or packet filters """

            if len(args) >= 1:
                raise kerri.ExcessArguments("fire_map()", 1)
            else:
                try:
                    if self.spoof == 1:
                        mac = random.choice(self.macs)
                        fire = subprocess.Popen(["/usr/bin/nmap", "-vv", "-sA",
                                                 "--spoof-mac", mac,
                                                 "%s" % str(target)],
                                                stdout=subprocess.PIPE,
                                                stderr=subprocess.PIPE)
                        std_out, std_err = fire.communicate()
                    else:
                        fire = subprocess.Popen(["/usr/bin/nmap", "-vv", "-sA",
                                                 "%s" % str(target)],
                                                stdout=subprocess.PIPE,
                                                stderr=subprocess.PIPE)
                        std_out, std_err = fire.communicate()
                    if len(std_err) != 0:
                        if self.log == 0:
                            if self.silent == 0:
                                sys.stderr.write(std_err)
                            else:
                                pass
                        elif self.log == 1:
                            logit(std_err, self.nmap_log)
                        else:
                            pass
                    else:
                        return std_out
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFailure("fire_map()")
                except KeyboardInterrupt:
                    sys.stderr.write("[!] THE NMAP PROCESS DOES NOT FINISH " +
                                     "CORRECTLY WHEN CTRL^C\'d WITH KAOS!!!")
                    raise kerri.UsrInt("fire_map()",
                                       "[!] PLEASE DO NOT EXIT AN NMAP " +
                                       "PROCESS WITH CTRL^C")
                except Exception as error:
                    raise kerri.Unknown("fire_map()", error)

        def no_ping(self, target, *args):
            """Do not ping target before scan"""

            if len(args) >= 1:
                raise kerri.ExcessArguments("no_ping()", 1)
            else:
                try:
                    if self.spoof == 1:
                        mac = random.choice(self.macs)
                        np = subprocess.Popen(["/usr/bin/nmap", "-vv", "-Pn",
                                               "--spoof-mac", mac,
                                               "%s" % str(target)],
                                              stdout=subprocess.PIPE,
                                              stderr=subprocess.PIPE)
                        std_out, std_err = np.communicate()
                    else:
                        np = subprocess.Popen(["/usr/bin/nmap", "-vv", "-Pn",
                                               "%s" % str(target)],
                                              stdout=subprocess.PIPE,
                                              stderr=subprocess.PIPE)
                        std_out, std_err = np.communicate()
                    if len(std_err) != 0:
                        if self.log == 0:
                            if self.silent == 0:
                                sys.stderr.write(std_err)
                            else:
                                pass
                        elif self.log == 1:
                            logit(std_err, self.nmap_log)
                        else:
                            pass
                    else:
                        return std_out
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFailure("no_ping()")
                except KeyboardInterrupt:
                    sys.stderr.write("[!] THE NMAP PROCESS DOES NOT FINISH " +
                                     "CORRECTLY WHEN CTRL^C\'d WITH KAOS!!!")
                    raise kerri.UsrInt("no_ping()", "[!] PLEASE DO NOT EXIT " +
                                       "AN NMAP PROCESS WITH CTRL^C")
                except Exception as error:
                    raise kerri.Unknown("no_ping()", error)

        def stealth_map(self, target, *args):
            """ Preform stealthy TCP scan """

            if len(args) >= 1:
                raise kerri.ExcessArguments("stealth_map()", 1)
            else:
                try:
                    if self.spoof == 1:
                        mac = random.choice(self.macs)
                        stealth = subprocess.Popen(["/usr/bin/nmap", "-vv",
                                                    "-sS", "--spoof-mac", mac,
                                                    "%s" % str(target)],
                                                   stdout=subprocess.PIPE,
                                                   stderr=subprocess.PIPE)
                        std_out, std_err = stealth.communicate()
                    else:
                        stealth = subprocess.Popen(["/usr/bin/nmap", "-vv",
                                                    "-sS", "%s" % str(target)],
                                                   stdout=subprocess.PIPE,
                                                   stderr=subprocess.PIPE)
                        std_out, std_err = stealth.communicate()
                    if len(std_err) != 0:
                        if self.log == 0:
                            if self.silent == 0:
                                sys.stderr.write(std_err)
                            else:
                                pass
                        elif self.log == 1:
                            logit(std_err, self.nmap_log)
                        else:
                            pass
                    else:
                        return std_out
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFailure("stealth_map()")
                except KeyboardInterrupt:
                    sys.stderr.write("[!] THE NMAP PROCESS DOES NOT FINISH " +
                                     "CORRECTLY WHEN CTRL^C\'d WITH KAOS!!!")
                    raise kerri.UsrInt("stealth_map()",
                                       "[!] PLEASE DO NOT EXIT AN NMAP " +
                                       "PROCESS WITH CTRL^C")
                except Exception as error:
                    raise kerri.Unknown("stealth_map()", error)

        def no_dns(self, target, *args):
            """ Do not preform reverse DNS resolution on active IP
                Addresses found by NMap """

            if len(args) >= 1:
                raise kerri.ExcessArguments("os_map()", 1)
            else:
                try:
                    if self.spoof == 1:
                        mac = random.choice(self.macs)
                        no_d = subprocess.Popen(["/usr/bin/nmap", "-vv", "-n",
                                                 "--spoof-mac", mac,
                                                 "%s" % str(target)],
                                                stdout=subprocess.PIPE,
                                                stderr=subprocess.PIPE)
                        std_out, std_err = no_d.communicate()
                    else:
                        no_d = subprocess.Popen(["/usr/bin/nmap", "-vv", "-n",
                                                 "%s" % str(target)],
                                                stdout=subprocess.PIPE,
                                                stderr=subprocess.PIPE)
                        std_out, std_err = no_d.communicate()
                    if len(std_err) != 0:
                        if self.log == 0:
                            if self.silent == 0:
                                sys.stderr.write(std_err)
                            else:
                                pass
                        elif self.log == 1:
                            logit(std_err, self.nmap_log)
                        else:
                            pass
                    else:
                        return std_out
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFailure("no_dns()")
                except KeyboardInterrupt:
                    sys.stderr.write("[!] THE NMAP PROCESS DOES NOT FINISH" +
                                     " CORRECTLY WHEN CTRL^C\'d WITH KAOS!!!")
                    raise kerri.UsrInt("no_dns()",
                                       "[!] PLEASE DO NOT EXIT AN NMAP " +
                                       "PROCESS WITH CTRL^C")
                except Exception as error:
                    raise kerri.Unknown("no_dns()", error)

        def tcp_map(self, target, *args):
            """ Preform scan for all TCP ports """

            if len(args) >= 1:
                raise kerri.ExcessArguments("tcp_map()", 1)
            else:
                try:
                    if self.spoof == 1:
                        mac = random.choice(self.macs)
                        tcp = subprocess.Popen(["/usr/bin/nmap", "-vv", "-sT",
                                                "--spoof-mac", mac,
                                                "%s" % str(target)],
                                               stdout=subprocess.PIPE,
                                               stderr=subprocess.PIPE)
                        std_out, std_err = tcp.communicate()
                    else:
                        tcp = subprocess.Popen(["/usr/bin/nmap", "-vv", "-sT",
                                                "%s" % str(target)],
                                               stdout=subprocess.PIPE,
                                               stderr=subprocess.PIPE)
                        std_out, std_err = tcp.communicate()
                    if len(std_err) != 0:
                        if self.log == 0:
                            if self.silent == 0:
                                sys.stderr.write(std_err)
                            else:
                                pass
                        elif self.log == 1:
                            logit(std_err, self.nmap_log)
                        else:
                            pass
                    else:
                        return std_out
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFailure("tcp_map()")
                except KeyboardInterrupt:
                    sys.stderr.write("[!] THE NMAP PROCESS DOES NOT FINISH " +
                                     "CORRECTLY WHEN CTRL^C\'d WITH KAOS!!!")
                    raise kerri.UsrInt("tcp_map()",
                                       "[!] PLEASE DO NOT EXIT AN NMAP " +
                                       "PROCESS WITH CTRL^C")
                except Exception as error:
                    raise kerri.Unknown("tcp_map()", error)

        def udp_map(self, target, *args):
            """ Preform scan for all UDP ports """

            if len(args) >= 1:
                raise kerri.ExcessArguments("udp_map()", 1)
            else:
                try:
                    if self.spoof == 1:
                        mac = random.choice(self.macs)
                        udp = subprocess.Popen(["/usr/bin/nmap", "-vv", "-F",
                                                "-sU",  "--spoof-mac", mac,
                                                "%s" % str(target)],
                                               stdout=subprocess.PIPE,
                                               stderr=subprocess.PIPE)
                        std_out, std_err = udp.communicate()
                    else:
                        udp = subprocess.Popen(["/usr/bin/nmap", "-vv", "-F",
                                                "-sU", "%s" % str(target)],
                                               stdout=subprocess.PIPE,
                                               stderr=subprocess.PIPE)
                        std_out, std_err = udp.communicate()
                    if len(std_err) != 0:
                        if self.log == 0:
                            if self.silent == 0:
                                sys.stderr.write(std_err)
                            else:
                                pass
                        elif self.log == 1:
                            logit(std_err, self.nmap_log)
                        else:
                            pass
                    else:
                        return std_out
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFailure("udp_map()")
                except KeyboardInterrupt:
                    sys.stderr.write("[!] THE NMAP PROCESS DOES NOT FINISH " +
                                     "CORRECTLY WHEN CTRL^C\'d WITH KAOS!!!")
                    raise kerri.UsrInt("udp_map()",
                                       "[!] PLEASE DO NOT EXIT AN NMAP " +
                                       "PROCESS WITH CTRL^C")
                except Exception as error:
                    raise kerri.Unknown("udp_map()", error)

        # LET KAOS DEFINE YOUR TARGETS VARIABLES
        #   {'MAC ADDRESS', 'PORTS', 'VERSIONS', 'OS', etc...}
        def def_target(self, host, *args):
            """ Let Kaos Define Your Targets Information """

            if len(args) >= 1:
                raise kerri.ExcessArguments("def_target()", 1)
            else:
                try:
                    global nmap_finished
                    nmap_finished = False
                    target = {}

                    def arp(host_id):
                        host_id = host
                        arp_data = subprocess.check_output(["arp-scan",
                                                            host_id])
                        err_msg = """Can't Preform Arpscan On Host!
                        Unknown Name Or Service!"""

                        if "WARNING: get_host_address failed" in arp_data:
                            return "%s" % err_msg, "N/A"
                        elif "ioctl: No such device" in arp_data:
                            return """Could Not Preform Arpscan! Is The
                        Interface Up And Network Connected?""", "N/A"
                        else:
                            return arp_data

                    def info_getter():
                        _x = ktime.marker()
                        target['ID'] = str(host)
                        # ARP SCAN
                        try:
                            if "N/A" in arp(host):
                                target['arp'] = "N/A"
                            else:
                                target['arp'] = arp(host).split(
                                        "Iface")[1].strip()
                        except Exception:
                            target['arp'] = "N/A"
                        # Basic NMap Scan
                        try:
                            target['basic'] = self.std_map(host).split(
                                    "Nmap scan report for ")[1].split(
                                            "Read data files from")[0].split(
                                                    "NSE: Script Post-"+
                                                    "scanning.")[0].strip()
                        except Exception:
                            try:
                                target['basic'] = self.std_map(host).split("Nmap scan report for ")[1]
                            except Exception:
                                target['basic'] = "N/A"
                        # Get MAC Address From Basic NMap Scan
                        try:
                            target['mac'] = target['basic'].split("MAC Address: ")[1].split("\n")[0].strip()
                        except Exception:
                            try:
                                target['mac'] = "N/A"
                            except Exception:
                                target['mac'] = "N/A"
                        # Get Open/Closed Ports From NMap
                        try:
                            target['ports'] = self.port_map(host).split("Scanned at ")[1].split("MAC Address")[0].strip()
                        except Exception:
                            try:
                                target['ports'] = self.port_map(host)
                            except Exception:
                                target['ports'] = "N/A"
                        # Search Firewalls And Packet Sniffers With NMap
                        try:
                            target['firewall'] = self.fire_map(host).split("Nmap scan report for ")[1].split("MAC Address")[0].strip()
                        except Exception:
                            try:
                                target['firewall'] = self.fire_map(host).split("Nmap scan report for ")[1]
                            except Exception:
                                target['firewall'] = "N/A"
                        # Get Network Information From NMap
                        try:
                            target['network'] = self.net_map(host, 32).split("Nmap scan report for ")[1].split("Read data files from")[0].strip()
                        except Exception:
                            try:
                                target['network'] = self.net_map(host, 32).split("Nmap scan report for ")[1]
                            except Exception:
                                target['network'] = "N/A"
                        # Attempt To Identify Operating System With NMap
                        try:
                            target['os'] = self.os_map(host).split("Nmap scan report for ")[1].split("Read data files from")[0].strip()
                        except Exception:
                            try:
                                target['os'] = self.os_map(host).split("Nmap scan report for ")[1]
                            except Exception:
                                target['os'] = "N/A"
                        # Get Version Information From NMap
                        try:
                            target['versions'] = self.vers_map(host).split(
                                    "Nmap scan report for ")[1].split(
                                            "Read data files from")[0].strip()
                        except Exception:
                            try:
                                target['versions'] = self.vers_map(host).split(
                                        "Nmap scan report for ")[1]
                            except Exception:
                                target['versions'] = "N/A"
                        # Check For Open/Closed TCP Ports With NMap
                        try:
                            target['tcp'] = self.tcp_map(host).split(
                                    "Nmap scan report for ")[1].split(
                                            "Read data files from")[0].split(
                                                    "MAC Address")[0].strip()
                        except Exception:
                            try:
                                target['tcp'] = self.tcp_map(host).split(
                                        "Nmap scan report for ")[1]
                            except Exception:
                                target['tcp'] = "N/A"
                        # Check For Open/Closed UDP Ports With NMap
                        try:
                            target['udp'] = self.udp_map(host).split(
                                    "Nmap scan report for ")[1].split(
                                            "MAC Address")[0].strip()
                        except Exception:
                            try:
                                target['udp'] = self.udp_map(host).split(
                                        "Nmap scan report for ")[1]
                            except Exception:
                                target['udp'] = "N/A"
                        # Change nmap_finished variable To True To Allow
                        # Loop To Break
                        global nmap_finished
                        nmap_finished = True
                        _y = ktime.marker()
                        global runtime
                        runtime = float(_y) - float(_x)

                    def waiter():
                        while True:
                            global nmap_finished
                            # Check To See If NMap Has Finished
                            if nmap_finished is not True:
                                # NMap Is Not Finished, Print The Message
                                for i in range(1, 10):
                                    ktime.wait(.25)
                                    sys.stdout.write(colored(
                                            "\r[\\] Gathering Targets " +
                                            "Information. Please Wait...",
                                            'yellow', 'on_red',
                                            attrs=['bold']))
                                    sys.stdout.flush()
                                    ktime.wait(.25)
                                    sys.stdout.write(colored(
                                            "\r[|] Gathering Targets " +
                                            "Information. Please Wait...",
                                            'yellow', 'on_red',
                                            attrs=['bold']))
                                    sys.stdout.flush()
                                    ktime.wait(.25)
                                    sys.stdout.write(colored(
                                            "\r[/] Gathering Targets " +
                                            "Information. Please Wait...",
                                            'yellow', 'on_red',
                                            attrs=['bold']))
                                    sys.stdout.flush()
                                    ktime.wait(.25)
                                    sys.stdout.write(colored(
                                            "\r[-] Gathering Targets " +
                                            "Information. Please Wait...",
                                            'yellow', 'on_red',
                                            attrs=['bold']))
                                    sys.stdout.flush()
                            # If NMap Is Finished, Break The Loop
                            elif nmap_finished == True:
                                host_information = ""
                                for item in host:
                                    host_information = host_information + "\n" + str(item)
                                try:
                                    sys.stdout.write(colored("\r[*] Target: %s " +
                                                             "Completed In %s " +
                                                             "seconds." % (host, str(float(runtime))), 'green', 'on_blue', attrs=['bold'])+"\n")
                                except Exception:
                                    try:
                                        return(host_information, "\n\n\nRuntime: %s " % str(runtime))
                                    except Exception:
                                        return(host_information)
                                break
                            # If Kaos Somehow Lost Track Of The nmap_finished
                            # Variable,
                            # Break The Loop
                            else:
                                print("Not Sure If NMap Finished So Kaos Is" +
                                      " Stopping...")
                                break

                    getter = Thread(target=info_getter)
                    watcher = Thread(target=waiter)

                    getter.start()
                    watcher.start()

                    getter.join()
                    watcher.join()

                    del nmap_finished
                    if "Service Info: Device: broadband router" in target["basic"]:
                        try:
                            mac_address = subprocess.Popen(["/usr/bin/iwgetid", "-a"],
                                                           stdout=subprocess.PIPE,
                                                           stderr=subprocess.PIPE)
                            std_out, std_err = mac_address.communicate()
                            if len(std_err) != 0:
                                sys.stderr.write(std_err)
                            MAC = std_out.replace("  ","").split(" ")[2]
                            if MAC.strip() in target['basic']:
                                arp_scan = local_arp()
                                target["connected"] = str(arp_scan).split("(http://www.nta-monitor.com/tools/arp-scan/)")[1].split("Ending arp-scan")[0].strip()
                                sys.stdout.write(mac_address)
                            else:
                                sys.stdout.write("arp-scan was not preformed because you are not connected to %s" % target["ID"])
                        except Exception:
                            pass
                        target["type"] = "Broadband Router"
                    else:
                        pass
                    trg_inf = ""

                    for item in target:
                        trg_inf = trg_inf + "\n#################################\n%s:\n%s" % (str(item), str(target[item]))

#                    return runtime, target
                    return runtime, trg_inf

                except Exception as error:
                    raise kerri.Unknown("def_target()", error)

        # SAME AS DEF_TARGET BUT WORKS FOR MULTIPLE TARGETS AT ONCE
        def multi_def(self, *args):
            """ Let Kaos Define Your Target Lists Information:
                Insert a list of targets seperated by a comma
                [You May Pass Any Target Accepted By NMap]
                EX: multi_def(\"192.168.1.254\", \"Some_Network\", \"10.10.1.54\")"""

            devices = {}
            try:
                for arg in args:
                    devices[arg] = def_target(str(arg))
            except KeyboardInterrupt:
                raise kerri.UsrInt("multi_def()")
            except Exception as error:
                raise kerri.Unknown("multi_def()", error)
            return devices

#   ##############
#   # SNIFFSPOOF #
#   ##############

    class SniffSpoof(object):
        """
        Network Scanners and Spoofers
        """

        def __str__(self):
            return """ Controls Kaos' Interactions With Network Sniffers And Spoofers """

        def nc_listen(self, port, *args):
            """
            Listens For A Connection With NetCat
            """

            if len(args) >= 1:
                raise kerri.ExcessArguments("nc_listen()", )
            else:
                try:
                    subprocess.call(["/usr/bin/nc", "-l", "-p", port])
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFaiure("nc_listen()")
                except Exception as error:
                    raise kerri.Unknown("nc_listen()", error)

        def arpspoof(self, interface, destination_ip, *args):
            if len(args) >= 1:
                raise kerri.ExcessArguments("arpspoof", 2)
            else:
                try:
                    subprocess.call(["sudo", "arpspoof", "-i", interface,
                                     destination_ip])
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFaiure("arpspoof()")
                except Exception as error:
                    raise kerri.Unknown("arpspoof()", error)

        def arping(self, inter, chan, ip, *args):
            """
            Sends ARP Requests To Neighbor Hosts
            """

            if len(args) >= 1:
                raise kerri.ExcessArguments("arping()", 3)
            else:
                try:
                    out = subprocess.check_output(["/usr/bin/arping", "-I", inter, "-c",
                                                   chan, ip])
                    return out
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFaiure("arping()")
                except Exception as error:
                    raise kerri.Unknown("arping()", error)

        def sysprint(self, inter, ip_host, *args):
            """
            Get Remote System Information With Arp-Fingerprint
            """

            if len(args) >= 1:
                raise kerri.ExcessArguments("sysprint()", 2)
            else:
                try:
                    os.system("/usr/sbin/arp-fingerprint -o \"-N -I " + inter +
                              "\" "+ip_host)
                except KeyboardInterrupt:
                    raise kerri.UsrInt("sysprint(%s, %s)" % (inter, ip_host))
                except Exception as error:
                    raise kerri.Unknown("sysprint()", error)

        def det_sniff(self, interface, target, *args):
            """
            Attempts To Detect A Sniffer (If Present) On The Network
            Target Must Be An IPv6 Address
            """

            if len(args) >= 1:
                raise kerri.ExcessArguments("det_sniff()", 2)
            else:
                try:
                    os.system("atk6-detect_sniffer6 "+interface+" "+target)
                except KeyboardInterrupt:
                    raise kerri.UsrInt("det_sniff(\'%s, %s\')" % (interface, target))
                except Exception as error:
                    raise kerri.Unknown("det_sniff()", error)

        def airodump(self, interface, *args):
            """
            Start Airodump-ng On Specified Interface
            """

            if len(args) >= 1:
                raise kerri.ExcessArguments("airodump()", 1)
            else:
                try:
                    print(colored("Hit CTRL^C To Quit", 'yellow', attrs=['bold']))
                    subprocess.call(["/usr/bin/airodump-ng", "--berlin", "999999",
                                     "--wps", "-M", "-U", "-W", "--showack",
                                     "-g", interface])
                except KeyboardInterrupt:
                    raise kerri.UsrInt("airodump(\'%s\')" % interface)
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFaiure("airodump()")
                except Exception as error:
                    raise kerri.Unknown("airodump()", error)

        def airlog(self, interface, out="%s/airlog" % pwd, *args):
            """
            Start Airodump-ng On Specified Interface And Save Output To File
            """

            if len(args) >= 1:
                raise kerri.ExcessArguments("airodump()", 1)
            else:
                try:
                    print(colored("Hit CTRL^C To Quit", 'yellow', attrs=['bold']))
                    subprocess.call(["/usr/bin/airodump-ng", "--write", out,
                                     "--output-format=csv",
                                     "--write-interval=1","--berlin",
                                     "999999", "--wps", "-g", "-M", "-U",
                                     "-W", "--showack", interface])
                except KeyboardInterrupt:
                    subprocess.call(["sed", "-i", "-e", "1d", "%s-01.csv" % out])
                    raise kerri.UsrInt("airlog(\'%s\')" % interface)
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFaiure("airlog()")
                except Exception as error:
                    raise kerri.Unknown("airlog()", error)

        def tcpdump(self, interface, *args):
            if len(args) >= 1:
                raise kerri.ExcessArguments("tcpdump()", 1)
            else:
                try:
                    subprocess.call(["/usr/bin/tcpdump", "-vnnei", interface])
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFaiure("tcpdump()")
                except Exception as error:
                    raise kerri.Unknown("tcpdump()", error)

        def arp_scan(self, interface, *args):
            """
            Scan For IP Addresses On The Network With Arp-Scan
            """

            if len(args) >= 1:
                raise kerri.ExcessArguments("arp_scan()", 1)
            else:
                try:
                    subprocess.call(["/usr/bin/arp-scan", "-l", "--interface=", interface,
                                     "--localnet"])
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFaiure("arp_scan()")
                except Exception as error:
                    raise kerri.Unknown("arp_scan()", error)

        def tshark(self, interface, *args):
            """
            Starts TShark on Specified Interface
            This Function Shows Only \'wlan\' Packets And Addresses
            """

            if len(args) >= 1:
                raise kerri.ExcessArguments("tshark()", 1)
            else:
                try:
                    subprocess.call(["/usr/bin/tshark", "-i", interface, "-I", "-Tfields",
                                     "-e", "wlan.bssid", "-e",
                                     "wlan.bssid_resolved", "-e", "wlan.sa", "-e",
                                     "wlan.da", "-e", "wlan"])
                except KeyboardInterrupt:
                    raise kerri.UsrInt('tshark(%s)' % interface)
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFaiure("tshark()")
                except Exception as error:
                    raise kerri.Unknown("tshark()", error)

        def std_tshark(self, interface, *args):
            """
            Starts (Default) TShark On Specified Interface
            """

            if len(args) >= 1:
                raise kerri.ExcessArguments("std_tshark()", 1)
            else:
                try:
                    subprocess.call(["/usr/bin/tshark", "-i", interface])
                except KeyboardInterrupt:
                    raise kerri.UsrInt("std_tshark(%s)" % interface)
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFaiure("std_tshark()")
                except Exception as error:
                    raise kerri.Unknown("std_tshark()", error)

        def wireshark(self, interface, *args):
            """
            Starts WireShark On Specified Interface
            """

            if len(args) >= 1:
                raise kerri.ExcessArguments("wireshark()", 1)
            else:
                try:
                    subprocess.call(["/usr/bin/wireshark", "-i", interface, "-k"])
                except KeyboardInterrupt:
                    raise kerri.UsrInt("wireshark(%s)" % interface)
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFaiure("wireshark()")
                except Exception as error:
                    raise kerri.Unknown("wireshark()", error)

        def kis_log(self, logfile, *args):
            """ Returns Captured Network Data From A Kismet.nettxt File.

                To Show Individual Client Data From The Networks:
                    import re
                    re.split("Client\s.:",networks[x])[y]
                    ###  'x' Represents The Network Number And 'y' Is The Client"""

            if len(args) >= 1:
                raise kerri.ExcessArguments("kis_log()")
            else:
                try:
                    networks = []
                    data = open(logfile, 'r')
                    for item in re.split("Network\s.:",str(data.read())):   #.split("Network "):
                        networks.append(item)
                    return networks
                except Exception as error:
                    raise kerri.Unknown("kis_log()", error)

#   ##################
#   # VULNERABLILITY #
#   ##################

    class Vulnerability(object):
        """
        Vulnerability Analysis
        """

        def __str__(self):
            return """ Controls Kaos' Vulnerability Analysis Operations """

        def nikto(self, host, *args):
            """
            Run Nikto Scan On Host
            """

            if len(args) >= 1:
                raise kerri.ExcessArguments("nikto()", 1)
            else:
                try:
                    out = subprocess.check_output(["/usr/bin/nikto", "-host", host, "-C",
                                               "all"])
                    return out
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFaiure("nikto()")
                except Exception as error:
                    raise kerri.Unknown("nikto()", error)

        def golismero(self, host, *args):
            """
            Run Golismero Search On Target Host
            """

            if len(args) >= 1:
                raise kerri.ExcessArguments("golismero()", 1)
            else:
                try:
                    print((symbo.SYM['echo'])+colored("golismero "+host, 'grey',
                                                attrs=['bold']))
                    data = subprocess.Popen(["golismero", str(host)],
                                             stdout=subprocess.PIPE,
                                             stderr=subprocess.PIPE)
                    output, outerr = data.communicate()
                    return output
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFailure('golismero')
                except KeyboardInterrupt:
                    raise kerri.UsrInt("golismero(%s)" % host)

        def lynis(self, *args):
            """
            Preforms Lynis System Audit On Local Machine
            """

            if len(args) >= 1:
                raise kerri.ExcessArguments("lynis()", 0)
            else:
                try:
                    subprocess.call(["/usr/bin/lynis", "audit", "system", "--pentest"])
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFailure('lynis()')
                except Exception:
                    raise kerri.Unknown('lynis()')

        def remote_lynis(self, target, *args):
            """
            Preforms Lynis System Audit On Remote Host
            """

            if len(args) >= 1:
                raise kerri.ExcessArguments("remote_lynis()", 1)
            else:
                try:
#                    subprocess.call(["/usr/bin/clear"])
                    def lynis_proc():
                        lynis = subprocess.Popen(["/usr/sbin/lynis", "audit system remote", target,
                                         "--pentest"], stdout=subprocess.PIPE,
                                                       stderr=subprocess.PIPE)
                        lynis.wait()
                        std_out, std_err = lynis.communicate()
                        if len(std_out) != 0:
                            return std_out
                        if len(std_err) != 0:
                            sys.stderr.write(std_err)
                    lynis_proc()
#                   def waiting():
 #                       print("Lynis Is Scanning Remote System For Vulnerabilities...")
 #                       print("PLEASE WAIT!!!")
 #                       while True:
 #                           print(" ")
 #                           for i in range(100):
 #                               time.sleep(10)
 #                               sys.stdout.write(colored("\r%d%%" % i, 'red'))
 #                               sys.stdout.flush()
 #                           subprocess.call(["clear"])
 #                       update = Thread(target=lynis_proc)
 #                       watcher = Thread(target=waiting)
 #                       update.start()
 #                       watcher.start()
 #                       update.join()
 #                       watcher.join()
                except KeyboardInterrupt:
                    raise kerri.UsrInt("remote_lynis()")
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFaiure("remote_lynis()")
                except Exception as error:
                    raise kerri.Unknown("remote_lynis()", error)

        def privesc(self, check_type, *args):
            """
            Preforms Privalege Escalation Check
            """

            if len(args) >= 1:
                raise kerri.ExcessArguments("privesc()", 1)
            else:
                try:
                    subprocess.call(["/usr/bin/unix-privesc-check",
                                     check_type])
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFaiure("privesc()")
                except Exception as error:
                    raise kerri.Unknown("", error)

        def vulnchk(self, check_type='standard', output=pwd, *args):
            """
            Checks System For Vulnerabilities
            """

            if len(args) >= 1:
                raise kerri.ExcessArguments("vulnchk()", 2)
            else:
                try:
                    if check_type == "detailed":
                        print(colored("This Detailed Analysis Could Take More Than 1" +
                                      " Hour To Complete", 'yellow', attrs=['bold']))
                        print(colored('Please Be Patient...', 'magenta',
                                      attrs=['bold']))
                    if check_type == "standard":
                        print(colored("This Standard Analysis Should Take About 5" +
                                      " Mins To Complete", 'yellow', attrs=['bold']))
                        print(colored('Please Be Patient...', 'magenta',
                                      attrs=['bold']))
                    start = int(time.time())
                    time.sleep(1)
                    print(colored("Starting Lynis System Check..."))
                    print(colored("This Scan Will Take Approx. 3.5 Mins Depending On" +
                                  " Your System.", 'yellow', attrs=['bold']))
                    lynischk = subprocess.check_output(["/usr/bin/lynis", "audit", "system",
                                                        "--pentest"])
                    lynfin = int(time.time())
                    lyncomp = int(lynfin) - int(start)
                    lyntime = lyncomp / 60.0
                    print("Lynis Completed In: %s Mins" % (colored(lyntime, 'yellow',
                                                                   attrs=['bold',
                                                                          'underline']))
                                                           )
                    time.sleep(2)
                    print(str(lynischk))
                    time.sleep(1)
                    print(colored("Starting Unix-PrivEsc-Check...", 'yellow',
                                  attrs=['bold']))
                    if check_type == "detailed":
                        print(colored("This Scan Could Take More Than 1 Hour To" +
                                      " Complete...\nPlease Be Patient", 'red'))
                        time.sleep(2)
                    if check_type == "standard":
                        print(colored("This Scan Should Take About 30 Seconds" +
                                      " To Complete..."))
                        time.sleep(2)
                    privstrt = int(time.time())
                    privchk = subprocess.check_output(["/usr/bin/unix-privesc-check",
                                                       check_type])
                    end = int(time.time())
                    privtime = int(end) - int(privstrt)
                    total_privtime = int(privtime) / 60.0
                    if check_type == "detailed":
                        print(("Unix-Privesc-Check Completed In %s Minutes"
                               % (colored(total_privtime, 'magenta',
                                       attrs=['bold', 'underline']))))
                    if check_type == "standard":
                        print("Unix-Privesc-Check Completed In %s Seconds"
                               % (colored(privtime, 'magenta', attrs=['bold',
                                                                      'underline'])))
                    print(colored(str(privchk), 'green', attrs=['bold']))
                    total_time = int(end) - int(start)
                    mins = total_time / 60.0
                    print("Vulnerability Scan Completed In: %s Minutes"
                           % (colored(mins, 'red', attrs=['bold', 'underline'])))
                    if check_type == "standard":
                        print(colored("For A More Detailed Analysis, Run This " +
                                      "Scanner In Detailed Mode", 'red'))
                    with open(output, 'w') as out:
                        out.write("\n#########################\n+++++++++++++" +
                                  " Lynis Vulnerability Scan +++++++++++++" +
                                  "\n#####################")
                        out.write(str(lynischk))
                        out.write("#########################\n+++++++++++++" +
                                  " Unix-PrivEsc-Check +++++++++++++" +
                                  "\n#####################")
                        out.write(str(privchk))
                        out.close
                    print("Your Vulnerability Analysis Has Been Saved @ %s"
                           % (colored(output, 'yellow', attrs=['bold'])))
                    time.sleep(2)
                    warnings = subprocess.check_output(["grep", "WARNING", output])
                    suggestions = subprocess.check_output(["grep", "-F", "suggestion",
                                                           "/var/log/lynis-report.dat"]
                                                          )
                    time.sleep(2)
                    print(colored("\n\nHere Are A Few Issues That I Have Discovered: ",
                                  'red'))
                    if check_type == "standard":
                        print(colored("Consider Running A Detailed Scan For More" +
                                      " Information", 'white'))
                    time.sleep(2)
                    print(warnings)
                    print(colored("According To My Data You Should Take The " +
                                  "Following Steps To Secure Your System:\n",
                                  'yellow'))
                    time.sleep(2)
                    print(colored(suggestions, 'yellow', attrs=['bold']))
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFaiure("vulnchk()")
                except Exception as error:
                    raise kerri.Unknown("vulnchk()", error)

#   #################
#   # ROUTEANALYSIS #
#   #################

    class RouteAnalysis(object):
        """
        Route Analysis Tools
        """

        def __str__(self):
            return """ Controls Kaos' Route Analysis Operations """

        def ass(self, interface, spoofed_ip, target, *args):
            """
            Runs Autonomous System Scan On Target IP
            """

            if len(args) >= 1:
                raise kerri.ExcessArguments("ass()", 3)
            else:
                try:
                    subprocess.call(["/usr/bin/ass", "-i", interface,
                                     "-a", "-b", "-S",
                                     spoofed_ip, "-D", target])
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFaiure("ass()")
                except Exception as error:
                    raise kerri.Unknown("ass()", error)

        def netdiscover(self, interface, *args):
            """
            Runs NetDiscover On Specified Interface
            """

            if len(args) >= 1:
                raise kerri.ExcessArguments("netdiscover()", 1)
            else:
                try:
                    data = subprocess.Popen(["/usr/sbin/netdiscover", "-i", interface, "-N", "-P"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    std_out, std_err = data.communicate()
                    if len(std_out) >= 1:
                        return std_out
                    else:
                        return std_err
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFaiure("netdiscover()")
                except Exception as error:
                    raise kerri.Unknown("netdiscover()", error)

        def zerotrace(self, interface, target_ip, target_port, *args):
            """ Preform Traceroute On Established Connection """

            if len(args) >= 1:
                raise kerri.ExcessArguments("zerotrace()", 3)
            else:
                try:
                    subprocess.call(["/usr/bin/0trace.sh", interface,
                                     target_ip, target_port])
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFailure("zerotrace")
                except Exception as error:
                    raise kerri.Unknown("zerotrace()", error)

#   #########
#   # OSINT #
#   #########

    class Osint(object):
        """
        Open Source Intelligence Tools
        """

        def __str__(self):
            return """ Turns Kaos Into Your Average Stalker """

        def urlcrazy(self, domain, out_file="%s/url_crazy.kaos" % pwd, *args):
            """
            Runs UrlCrazy On Target Domain
            """

            if len(args) >= 1:
                raise kerri.ExcessArguments("urlcrazy()", 2)
            else:
                try:
                    subprocess.call(["urlcrazy", "-p", "-o", out_file, domain])
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFaiure("urlcrazy()")
                except Exception as error:
                    raise kerri.Unknown("urlcrazy()", error)

        def automater(self, host, *args):
            """
            Preforms Automater Scan On Target Host
            """

            if len(args) >= 1:
                raise kerri.ExcessArguments("automater()", 1)
            else:
                try:
                    subprocess.call(["/usr/bin/automater", host])
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFaiure("automater()")
                except Exception as error:
                    raise kerri.Unknown("automater()", error)

        def harvester(self, query, output='%s/kaos.harvester' % pwd, *args):
            """
            Run TheHarvester To Gather Information About The Target
            Domain Or Company Name
            """

            if len(args) >= 1:
                raise kerri.ExcessArguments("harvester()", 2)
            else:
                try:
                    out = "%s.html" % str(output)
                    data = subprocess.Popen(["/usr/bin/theHarvester", "-d", query,
                                     "-b", "all"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    std_out, std_err = data.communicate()
                    s_info = ""
                    if len(std_out) >= 1:
#                        b_info = std_out.split('\n')
                        return std_out
                    else:
                        return std_err
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFaiure("harvester()")
                except Exception as error:
                    raise kerri.Unknown("harvester()", error)

        def ip_locate(self, ip, *args):
            if len(args) >= 1:
                raise kerri.ExcessArguments("harvester()", 2)
            else:
                output = {}
                count = 0
#                count2 = 0
                try:
                    headers = {"pragma": "no-cache",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36",
                    "x-requested-with": "XMLHttpRequest"}
                    ip_addr = str(ip)
                    url = "https://tools.keycdn.com/geo?host=%s" % ip_addr
                    resp = requests.get(url, headers=headers)
                    soup = BeautifulSoup(resp.content, 'html.parser')
                    labels = soup.find_all("dt", {"class": "col-4"}) #"bg-light medium rounded p-3"})
                    values = soup.find_all("dd", {"class": "col-8 text-monospace"})
                    for item in labels:
                        output["%s" % labels[count].getText()] = values[count].getText()
                        count+=1

                    return output

#                    for item in output:
#                        print("%s   %s" % (labels[count2].getText(), values[count2].getText()))
#                        count2+=1

                except subprocess.CalledProcessError:
                    raise kerri.ProcessFaiure("ip_locate()")
                except Exception as error:
                    raise kerri.Unknown("ip_locate()", error)

#########
# INITs #
#########
recon = Recon()
arp = recon.arp
drift = recon.drift
local_arp = recon.local_arp
bingip = recon.bingip
httrack = recon.httrack
citrix = recon.citrix
dig = recon.dig
whois = recon.whois
nslookup = recon.nslookup
dmitry = recon.dmitry
webinfo = recon.webinfo
wafw00f = recon.wafw00f
p0f = recon.p0f
arp_fprint = recon.arp_fprint

dns = recon.DNSAnalysis()
dnsenum = dns.dnsenum
dnsmap = dns.dnsmap
dnstrace = dns.dnstracer

nmap = recon.NMap(spoof=0, log=0, logdir="/var/log/kaos", silent=0)
flush_log = nmap.flush_log
pro_map = nmap.pro_map
std_map = nmap.std_map
connect_map = nmap.connect_map
ack_map = nmap.ack_map
window_map = nmap.window_map
maimon_map = nmap.maimon_map
fast_map = nmap.fast_map
net_map = nmap.net_map
port_map = nmap.port_map
os_map = nmap.os_map
vers_map = nmap.vers_map
fire_map = nmap.fire_map
no_ping = nmap.no_ping
stealth_map = nmap.stealth_map
no_dns = nmap.no_dns
tcp_map = nmap.tcp_map
udp_map = nmap.udp_map
def_target = nmap.def_target
multi_target = nmap.def_target

sspoof = recon.SniffSpoof()
nc_listen = sspoof.nc_listen
arpspoof = sspoof.arpspoof
arping = sspoof.arping
sysprint = sspoof.sysprint
det_sniff = sspoof.det_sniff
airodump = sspoof.airodump
airlog = sspoof.airlog
tcpdump = sspoof.tcpdump
arp_scan = sspoof.arp_scan
tshark = sspoof.tshark
std_tshark = sspoof.std_tshark
wireshark = sspoof.wireshark
kis_log = sspoof.kis_log
vuln = recon.Vulnerability()
nikto = vuln.nikto
golismero = vuln.golismero
lynis = vuln.lynis
remote_lynis = vuln.remote_lynis
privesc = vuln.privesc
vulnchk = vuln.vulnchk

ranal = recon.RouteAnalysis()
ass = ranal.ass
netdiscover = ranal.netdiscover
zerotrace = ranal.zerotrace

osint = recon.Osint()
urlcrazy = osint.urlcrazy
automater = osint.automater
harvester = osint.harvester
iploc = osint.ip_locate
