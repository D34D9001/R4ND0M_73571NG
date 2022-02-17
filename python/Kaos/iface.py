#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created: Aug 2017

    @author: D34D9001@9R0GR4M13
"""
import kerri
import ksys
import random
import subprocess
import sys
import time
from termcolor import colored

########################
# INTERFACE MANAGEMENT #
########################

user_wireless_interface = "wlan0"
user_monitor_interface = "wlan0mon"

### DO NOT EDIT BELOW THIS LINE ###

global inter
inter = None, None

# def check_interface(std_interface=user_wireless_interface, monitor_interface=user_monitor_interface):
#     check = subprocess.Popen(["ifconfig", "-a"],
#                              stderr=subprocess.PIPE,
#                              stdout=subprocess.PIPE)
#     grep_out = subprocess.Popen(["grep", "-e", user_wireless_interface],
#                                 stdin=check.stdout,
#                                 stdout=subprocess.PIPE,
#                                 stderr=subprocess.PIPE)
#     std_out, std_err = grep_out.communicate()
#     if len(std_err) != 0:
#         sys.stderr.write(std_err)
#     else:
#         global inter
#         if "%s" % monitor_interface in std_out:
#             inter = monitor_interface, "monitor_interface"
#         else:
#             inter = std_interface, "standard_interface"

class Interface(object):
    """
    Controls Interface Behavior
    """

    def __init__(self, *args):
        """ Check For The Current Networking Interface """
        return None
        #check_interface()

    def __str__(self):
        #check_interface()
        return "DISABLED BY DEVELOPER"
        #return "Current Networking Interface: %s %s" % (inter[0], inter[1])

    def btaddr(self, device, *args):
        if len(args) >= 1:
            raise kerri.ExcessArguments("btaddr()", 1)
        else:
            try:
                data = subprocess.Popen(["btaddr", "-i", device],
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE)
                std_out, std_err = data.communicate()
                if len(std_out) != 0:
                    return std_out
                if len(std_err) != 0:
                    sys.stderr.write(std_err)
            except subprocess.CalledProcessError:
                raise kerri.ProcessFailure("btaddr()")
            except Exception as error:
                raise kerri.Unknown("btaddr", error)

    def btscan(self, device, *args):
        """
        Scans For Bluetooth Devices In Range
        """

        if len(args) >= 1:
            raise kerri.ExcessArguments("btscan()", 1)
        else:
            try:
                subprocess.call(["btmgmt", "auto-power", device])
                btmgmt = subprocess.Popen("btmgmt find".split(),
                                           stdout=subprocess.PIPE)
                grep = subprocess.Popen("grep -i -e 'dev_found' -e 'name'".split(),
                                         stdin=btmgmt.stdout,
                                         stdout=subprocess.PIPE)
                btmgmt.stdout.close()
                grep.wait()
                subprocess.call(["btmgmt", "power", device])
            except subprocess.CalledProcessError:
                raise kerri.ProcessFailure('btscan()')
            except Exception as error:
                raise kerri.Unknown('btscan()', error)

    def btinfo(self, *args):
        """ Display Bluetooth Controller Information """

        if len(args) >= 1:
            raise kerri.ExcessArguments("btinfo()", 0)
        else:
            try:
                info = subprocess.Popen(["btmgmt", "info"],
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE)
                std_out, std_err = info.communicate()
                if len(std_out) != 0:
                    return std_out
            except subprocess.CalledProcessError:
                raise kerri.ProcessFailure("btinfo()")
            except Exception as error:
                raise kerri.Unknown("btinfo()", error)

    def btext_info(self, *args):
        """ Show Extended Bluetooth Controller Information """

        if len(args) >= 1:
            raise kerri.ExcessArguments("btdev_info()", 0)
        else:
            try:
                btmgmt = subprocess.Popen(["btmgmt", "extinfo"],
                                          stdout=subprocess.PIPE,
                                          stderr=subprocess.PIPE)
                std_out, std_err = btmgmt.communicate()
                if len(std_out) != 0:
                    return std_out
            except subprocess.CalledProcessError:
                raise kerri.ProcessFailure("btdev_info()")
            except Exception as error:
                raise kerri.Unknown("btdev_info()", error)

    def btauto(self, *args):
        """ Auto power on all builtin bluetooth devices
            and enable all features """

        if len(args) >= 1:
            return kerri.ExcessArguments("btauto()", 0)
        else:
            try:
                power = subprocess.Popen(["btmgmt", "auto-power"],
                                         stdout=subprocess.PIPE,
                                         stderr=subprocess.PIPE)
                std_out, std_err = power.communicate()
                if len(std_out) != 0:
                    return std_out
            except subprocess.CalledProcessError:
                raise kerri.ProcessFailure("btauto()")
            except Exception as error:
                raise kerri.Unknown("btauto()", error)

    def btpower(self, device, power='on', *args):
        """
        Powers On/Off Builtin Bluetooth Device
        """

        if len(args) >= 1:
            raise kerri.ExcessArguments("btpower()", 1)
        else:
            try:
                btmgmt = subprocess.Popen(["btmgmt", "power", power, device],
                                          stdout=subprocess.PIPE,
                                          stderr=subprocess.PIPE)
                std_out, std_err = btmgmt.communicate()
                if len(std_out) != 0:
                    return std_out
                else:
                    if len(std_err) != 0:
                        sys.stderr.write(std_err)
            except subprocess.CalledProcessError:
                raise kerri.ProcessFailure('btpower()')
            except Exception as error:
                raise kerri.Unknown('btpower()', error)

    def btpair(self, device_addr, *args):
        """
        Pairs Builtin Bluetooth Device With Remote Device
        """

        if len(args) >= 1:
            raise kerri.ExcessArguments("btpair", 1)
        else:
            try:
                btmgmt = subprocess.Popen(["btmgmt", "pair", device_addr],
                                          stdout=subprocess.PIPE,
                                          stderr=subprocess.PIPE)
                std_out, std_err = btmgmt.communicate()
                if len(std_out) != 0:
                    return std_out
                else:
                    if len(std_err) != 0:
                        sys.stderr.write(std_err)
            except subprocess.CalledProcessError:
                raise kerri.ProcessFailure('btpair()')
            except Exception as error:
                raise kerri.Unknown('btpair', error)

    def btcon_info(self, *args):
        """
        Displays Bluetooth Connection Information
        """

        if len(args) >= 1:
            raise kerri.ExcessArguments("btcon_info", 0)
        else:
            try:
                results = subprocess.check_output(["btmgmt", "con"])
                return results
            except subprocess.CalledProcessError:
                raise kerri.ProcessFailure('btcon_info')
            except Exception as error:
                raise kerri.Unknown('btcon_info', error)

    def start_mon(self, check_kill=1, *args):
        """
        Start Monitor Mode On Specified Interface
        """

        if len(args) >= 1:
            raise kerri.ExcessArguments("start_mon()", 1)
        else:
            check_interface()
            try:
                if inter[1] == "monitor_interface":
                    raise kerri.InvalidInput("[!] %s Is Already In Monitor Mode!" % inter)
                if check_kill == 1:
                    pipes = subprocess.Popen(["airmon-ng", "check", "kill"],
                                             stdout=subprocess.PIPE,
                                             stderr=subprocess.PIPE)
                    std_out, std_err = pipes.communicate()
            except subprocess.CalledProcessError:
                raise kerri.ProcessFailure('start_mon()', std_err)
            except Exception as error:
                sys.stderr.write("[ERROR]: 'airmon-ng check kill' returned a non-zero exit code. Attempting to set monitor mode anyways...")
            try:
                pipes = subprocess.Popen(["airmon-ng", "start", inter[0]],
                                         stdout=subprocess.PIPE,
                                         stderr=subprocess.PIPE)
                std_out, std_err = pipes.communicate()
            except subprocess.CalledProcessError:
                raise kerri.ProcessFailure('start_mon()', std_err)
            except Exception as error:
                raise kerri.Unknown('start_mon()', error)

    def stop_mon(self, *args):
        """
        Disable Monitor Mode On Specified Interface
        """

        if len(args) >= 1:
            raise kerri.ExcessArguments("stop_mon()", 1)
        else:
            check_interface()
            if inter[1] == "user_interface":
                raise kerri.InvalidInput("%s Is Not In Monitor Mode!" % inter[0])
            try:
                pipes = subprocess.Popen(["airmon-ng", "stop", inter[0]],
                                         stdout=subprocess.PIPE,
                                         stderr=subprocess.PIPE)
                std_out, std_err = pipes.communicate()
            except subprocess.CalledProcessError:
                raise kerri.ProcessFailure('stop_mon()', std_err)
            except Exception as error:
                raise kerri.Unknown('stop_mon()', error)
            check_interface()
            try:
                pipes = subprocess.Popen(["ifconfig", inter[0], "up"],
                                         stdout=subprocess.PIPE,
                                         stderr=subprocess.PIPE)
                std_out, std_err = pipes.communicate()
            except subprocess.CalledProcessError:
                raise kerri.ProcessFailure('stop_mon()', std_err)
            except Exception as error:
                raise kerri.Unknown('stop_mon()', error)

    def iconf_chk(self, *args):
        """
        Check Current Configuration Of Network Devices
        """

        if len(args) >= 1:
            raise kerri.ExcessArguments("iconf_chk()", 0)
        else:
            try:
                result = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE)
                std_out = result.communicate()
                if len(std_out) != 0:
                    return std_out
            except subprocess.CalledProcessError:
                raise kerri.ProcessFailure('iconf_chk()')
            except Exception as error:
                raise kerri.Unknown('iconf_chk()', error)

    def inter_chk(self, *args):
        """
        Check Interface Configuration
        """

        if len(args) >= 1:
            raise kerri.ExcessArguments("inter_chk()", 1)
        else:
            check_interface()
            try:
                int_info = subprocess.check_output(["ifconfig", inter[0]])
                return "[Interface]: %s\n%s" % (inter[0], int_info)
            except subprocess.CalledProcessError:
                raise kerri.ProcessFailure('inter_chk()')
            except Exception as error:
                raise kerri.Unknown('inter_chk()', error)

    def reset_netint(self, *args):
        """
        Reset Network Services As Well As The Specified Interface
        {This only works if Network-Manager is the networking service used by
        the operating system}
        """

        if len(args) >= 1:
            raise kerri.ExcessArguments("reset_netint()", 1)
        else:
            check_interface()
            try:
                subprocess.call(["ifconfig", inter[0], "down"])
                subprocess.call(["service", "network-manager", "restart"])
                subprocess.call(["service", "networking", "restart"])
                subprocess.call(["ifconfig", inter[0], "up"])
            except subprocess.CalledProcessError:
                raise kerri.ProcessFailure('reset_netint()')
            except Exception as error:
                raise kerri.Unknown('reset_netint()', error)

#   ######################
#   # ADDRESS MANAGEMENT #
#   ######################

    class Addressing(object):
        """
        Controls Interface Addresses
        """

        def __str__(self):
            return """ Controls All Interface Operations Preformed By Kaos """

        def get_route(self, *args):
            if len(args) >= 1:
                raise kerri.ExcessArguments("get_route()", 0)
            else:
                try:
                    route = subprocess.Popen(["/sbin/route", "-n"],
                                             stdout=subprocess.PIPE,
                                             stderr=subprocess.PIPE)
                    std_out, std_err = route.communicate()
                    if len(std_err) != 0:
                        sys.stderr.write(std_err)
                    if len(std_out) != 0:
                        return std_out
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFailure("get_route()")
                except Exception as error:
                    raise kerri.Unknown("get_route()", error)

        def aval_inter(self, *args):
            """ See A Short List Of Available Network Interfaces """

            if len(args) >= 1:
                raise kerri.ExcessArguments("aval_inter()", 0)
            else:
                try:
                    interfaces = subprocess.check_output(["ifconfig", "-a", "-s"])
                    return interfaces
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFailure('aval_inter()')
                except Exception as error:
                    raise kerri.Unknown('aval_inter()', error)


        def verb_aval(self, *args):
            """ See A Detailed List Of Available Network Interfaces """

            if len(args) >= 1:
                raise kerri.ExcessArguments("verb_aval()", 0)
            else:
                try:
                    interfaces = subprocess.check_output(["ifconfig", "-a"])
                    return interfaces
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFailure('verb_aval()')
                except Exception as error:
                    raise kerri.Unknown('verb_avail()', error)


        def uface(self, *args):
            """ Bring Interface Up """

            if len(args) >= 1:
                raise kerri.ExcessArguments("uface()", 1)
            else:
                check_interface()
                try:
                    pipes = subprocess.Popen(["ifconfig", inter, "up"],
                                             stdout=subprocess.PIPE,
                                             stderr=subprocess.PIPE)
                    std_out, std_err = pipes.communicate()
                    if len(std_err) != 0:
                        return std_err
                    else:
                        print("Interface %s Successfully Raised" % inter)
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFailure('uface()')
                except Exception as error:
                    raise kerri.Unknown('uface()', error)


        def dface(self, *args):
            """ Bring Interface Down """

            if len(args) >= 1:
                raise kerri.ExcessArguments("dface()", 1)
            else:
                check_interface()
                try:
                    pipes = subprocess.Popen(["ifconfig", inter, "down"],
                                             stdout=subprocess.PIPE,
                                             stderr=subprocess.PIPE)
                    std_out, std_err = pipes.communicate()
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFailure('dface()')
                except Exception as error:
                    raise kerri.Unknown('dface()', error)


        def mac_change(self, *args):
            """
            Changes Mac Address On Specified Interface
            """
            check_interface()
            if len(args) >= 1:
                raise kerri.ExcessArguments("mac_change()", 1)
            else:
                try:
                    subprocess.call(["ifconfig", inter, "down"])
                    subprocess.call(["macchanger", "-rb", inter])
                    subprocess.call(["ifconfig", inter, "up"])
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFailure('mac_change()')
                except Exception as error:
                    raise kerri.Unknown('mac_change()', error)

        def ip_change(self, digits, *args):
            """
            Changes IP Address On Specified Network
            """

            if len(args) >= 1:
                raise kerri.ExcessArguments("ip_change()", 2)
            else:
                check_interface()
                count = int(digits)

                def randig(n):
                    """
                    Generate Random Digits Of Specified Length
                    {This will only change the LOCAL IP Address
                    * IT WILL NOT CHANGE YOUR PUBLIC IP ADDRESS *}
                    """

                    range_start = 10**(n-1)
                    range_end = (10**n)-1
                    return random.randint(range_start, range_end)
                new_ip = str(randig(count))
                try:
                    subprocess.call(["ifconfig", inter, "192.168.1.%s"
                                    % new_ip, "netmask", "255.255.255.0"])
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFailure('ip_change()')
                except Exception as error:
                    raise kerri.Unknown('ip_change()', error)

        def ip_route(self, *args):
            if len(args) >= 1 :
                raise kerri.ExcessArguments("ip_route()", 0)
            else:
                try:
                    route = subprocess.check_output(["ip", "route"])
                    return route
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFailure("ip_route()")
                except Exception as error:
                    raise kerri.Unknown("ip_route()", error)

        def chk_ip(self, interface, *args):
            """
            Gets The Current IP Address Of The Specified Interface
            """

            if len(args) >= 1:
                raise kerri.ExcessArguments("chk_ip()", 1)
            else:
                check_interface()
                try:
                    out = subprocess.check_output(["ifconfig", inter,
                                                   "|", "egrep", "inet"])
                    my_ip = subprocess.check_output(["curl", "ifconfig.me"])
                    print("Your Local IP Address Is: %s" % str(out))
                    print("Your Public IP Address Is: %s" % str(my_ip))
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFailure('chk_ip()')
                except Exception as error:
                    raise kerri.Unknown('chk_ip()', error)

        def ip_loc(self, ip_ad=None, *args):
            """ Get information about IP address' physical location"""

            if len(args) >= 1:
                raise kerri.ExcessArguments("ip_loc()", 1)
            else:
                if ip_ad == None:
                    ip_ad = subprocess.check_output(["curl", "-s",
                                                     "ifconfig.me/ip"])
                else:
                    pass
                try:
                    country_code = subprocess.check_output(["geoiplookup", ip_ad])
                    with open("/tmp/kaos_geoip", 'w') as geoip:
                        geoip.write(country_code)
                        geoip.close()

                    cntry = subprocess.check_output(["cut", "-d ", "-f5-6",
                                                     "/tmp/kaos_geoip"])
                    with open("/tmp/kaos_geoip", 'w') as geoip:
                        geoip.write(cntry)
                        geoip.close()
                    ip_location = subprocess.check_output(["cat",
                                                           "/tmp/kaos_geoip"])
                    country = str(ip_location)
                    coty = country.rstrip()
                    if coty == "Address not":
                        print("IP Address Location Not Available...")
                    else:
                        print("IPAddress Location: %s" % ip_location)
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFailure('ip_loc()')
                except Exception as error:
                    raise kerri.Unknown('ip_loc()', error)
                finally:
                    ksys.srem("/temp/kaos_geoip")
                    sys.stdout.write("Temp File Removed")

        def vend_mac(self, *args):
            """
            Lists Mac Addresses And Vendor Names
            """

            if len(args) >= 1:
                raise kerri.ExcessArguments("vend_mac()", 0)
            else:
                try:
                    time.sleep(1)
                    time.sleep(.25)
                    ad_list = subprocess.check_output(["macchanger", "-l"])
                    return colored(ad_list, 'yellow', attrs=['bold'])
                except KeyboardInterrupt:
                    raise kerri.UsrInt('vend_mac()')
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFailure('vend_mac()')
                except Exception as error:
                    raise kerri.Unknown('vend_mac()', error)

        def search_mac(self, vendor, *args):
            """
            Search For Mac Address by Vendor Name
            """

            if len(args) >= 1:
                raise kerri.ExcessArguments("search_mac()", 1)
            else:
                try:
                    ad_list = subprocess.check_output(["macchanger", "--list=%s" % vendor])
                    return ad_list
                except KeyboardInterrupt:
                    raise kerri.UsrInt('search_mac()')
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFailure('search_mac()')
                except Exception as error:
                    raise kerri.Unknown('search_mac()', error)

#   #######################################
#   # WIRELESS NETWORK ADAPTOR MANAGEMENT #
#   #######################################

    class Wifi(object):
        """
        Controls Interface Interactions With Wifi Networks
        """

        def __str__(self):
            return """ Controls Kaos Interactions With WiFi Networks """

        def man_chk(self, *args):
            """
            Checks To See Which Network Managers Are Installed
            """

            if len(args) >= 1:
                raise kerri.ExcessArguments("man_chk()", 0)
            else:
                status = None
                stat_num = None
                managers = ("wicd", "nmcli", "NetworkManager",
                            "ifconfig", "iwconfig", "iwlist")
                available = []
                for manager in managers:
                    try:
                        stat_num = 1
                        status = "True"
                    except (OSError, subprocess.CalledProcessError) as e:
                        if subprocess.CalledProcessError:
                            stat_num = 0
                            status = "False"
                        elif e.errno == 2:
                            stat_num = 0
                            status = "False"
                        else:
                            stat_num = 2
                            status = "Unknown"
                    except Exception as error:
                        raise kerri.Unknown("man_chk()", error)
                    results = "%s: [%i]: %s" % (manager.title(), stat_num, status)
                    available.append(results)
                return available

        def current_network(self, *args):
            if len(args) >= 1:
                raise kerri.ProcessFailure("current_network()")
            else:
                try:
                    network = subprocess.Popen(["iwgetid", "-r"],
                                               stdout=subprocess.PIPE,
                                               stderr=subprocess.PIPE)
                    std_out, std_err = network.communicate()
                    if len(std_err) != 0:
                        sys.stderr.write(std_err)
                    if len(std_out) != 0:
                        sys.stdout.write(std_out)
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFailure("current_network()")
                except Exception as error:
                    raise kerri.Unknown("current_network()", error)

        def netman(self, action="start", *args):
            """ Start Or Stop NetworkManager """

            if len(args) >= 1:
                raise kerri.ExcessArguments("netman()", 1)
            else:
                try:
                    act = action.lower()
                    if str(action.lower()) != "start" and str(action.lower()) != "stop":
                        raise kerri.InvalidInput("netman()", "The action parameter must be either \'start\' or \'stop\'...")
                    subprocess.call(["systemctl", act, "NetworkManager"])
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFailure("netman()")
                except Exception as error:
                    raise kerri.Unknown("netman()", error)

        def nmcli_con(self, ssid=None, password=None, *args):
            """
            Connects To Specified Wifi Network
            """

            if len(args) >= 1:
                raise kerri.ExcessArguments("nmcli_con()", 2)
            else:
                if ssid == None:
                    raise kerri.InvalidInput("nmcli_con()", "You Must Specify The SSID To Connect To!")
                else:
                    try:
                        if password != None:
                            subprocess.call(["nmcli", "d", "wifi", "connect",
                                             ssid, "password", password])
                        else:
                            subprocess.call(["nmcli", "d", "wifi",
                                             "connect", ssid])
                    except subprocess.CalledProcessError:
                        raise kerri.ProcessFailure('nmcli_con()')
                    except Exception as error:
                        raise kerri.Unknown('nmcli_con()', error)

        def iw_scan(self, interface, *args):
            """
            Scan For Local Wifi Networks In Range
            """

            if len(args) >= 1:
                raise kerri.ExcessArguments("iw_scan()", 1)
            else:
                try:
                    networks = subprocess.Popen(["iwlist", interface,
                                                 "scanning"],
                                                 stdout=subprocess.PIPE,
                                                 stderr=subprocess.PIPE)
                    std_out, std_err = networks.communicate()
                    if len(std_out) != 0:
                        return std_out
                    if len(std_err) != 0:
                        sys.stderr.write(std_err)
                except KeyboardInterrupt:
                    raise kerri.UsrInt('iw_scan()')
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFailure('iw_scan()')
                except Exception as error:
                    raise kerri.Unknown('iw_scan()', error)

        def simple_iw(self, _interface, *args):
            """
            Simple Wifi Scan That Shows Only The Most \'Important\' Information
            """

            if len(args) >= 2:
                raise kerri.ExcessArguments("simple_iw()", 1)
            else:
                inter = _interface
                try:
                    iwlist = subprocess.Popen(["iwlist", inter,
                                               "scanning"],
                                              stdout=subprocess.PIPE)
                    grep = subprocess.Popen(["grep", "-i", "-e", "Address",
                                             "-e", "ESSID", "-e", "Channel",
                                             "-e", "Frequency", "-e", "Quality",
                                             "-e", "Encryption", "-e", "Group",
                                             "-e", "Pairwise", "-e",
                                             "Authentication"],
                                            stdin=iwlist.stdout,
                                            stdout=subprocess.PIPE,
                                            stderr=subprocess.PIPE)
                    iwlist.stdout.close()
                    std_out, std_err = grep.communicate()
                    grep.wait()
                    nets = []
                    for item in std_out.split("Cell "):
                        nets.append(item)
                    return nets.encode()
                except Exception as error:
                    raise kerri.Unknown('simple_iw()', error)

        def wicd_d(self, action='start', *args):
            """ Start the wicd daemon """

            if len(args) >= 1:
                raise kerri.ExcessArguments("wicd_d()", 1)
            else:
                try:
                    # Check To See If Wicd Is Installed
                    avail = subprocess.Popen(["wicd", "-h"],
                                             stdout=subprocess.PIPE,
                                             stderr=subprocess.PIPE)
                    std_out, std_err = avail.communicate()
                    # If the program check throws an error, print it to stderr
                    if len(std_err)!= 0:
                        sys.stderr.write(std_err)
                    # If the program does not throw an error, continue with the wicd_d function
                    if len(std_out) != 0:
                        subprocess.call(["systemctl", action, "wicd"])
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFailure('wicd_d()')
                except OSError:
                    raise kerri.ProcessFailure("wicd_d()", "Wicd IS NOT INSTALLED ON THIS SYSTEM!")
                except Exception as error:
                    raise kerri.Unknown('wicd_d()', error)

        def wicd_scan(self, type='wireless', *args):
            """ Scan for in range WiFi networks with wicd-cli """

            if len(args) >= 1:
                raise kerri.ExcessArguments("wicd_scan", 1)
            else:
                try:
                    # Check To See If Wicd Is Installed
                    avail = subprocess.Popen(["wicd", "-h"],
                                             stdout=subprocess.PIPE,
                                             stderr=subprocess.PIPE)
                    std_out, std_err = avail.communicate()
                    # If the program check throws an error, print it to stderr
                    if len(std_err)!= 0:
                        sys.stderr.write(std_err)
                    # If the program does not throw an error, continue with the wicd_d function
                    if len(std_out) != 0:
                        subprocess.call(["wicd-cli", "--%s" % type, "--scan"])
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFailure('wicd_scan()')
                except Exception as error:
                    raise kerri.Unknown('wicd_scan()', error)

        def wicd_net(self, type='wireless', *args):
            """ List networks found by wicd_scan(). Network number is needed for
                wicd_con()
                [type]: wireless // wired """

            if len(args) >= 1:
                raise kerri.ExcessArguments("wicd_net()", 1)
            else:
                try:
                    # Check To See If Wicd Is Installed
                    avail = subprocess.Popen(["wicd", "-h"],
                                             stdout=subprocess.PIPE,
                                             stderr=subprocess.PIPE)
                    std_out, std_err = avail.communicate()
                    # If the program check throws an error, print it to stderr
                    if len(std_err)!= 0:
                        sys.stderr.write(std_err)
                    # If the program does not throw an error, continue with the wicd_d function
                    if len(std_out) != 0:
                        networks = subprocess.check_output(["wicd-cli",
                                                            "--%s" % type,
                                                            "--list-networks"])
                        return networks
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFailure('wicd_net()')
                except Exception as error:
                    raise kerri.Unknown('wicd_net()', error)

        def wicd_con(self, type='wireless', network_num=0, *args):
            """ Connect to network with Wicd network manager
                You must get the network number using wicd_net(int_type) """

            if len(args) >= 1:
                raise kerri.ExcessArguments("wicd_con()", 2)
            else:
                try:
                    # Check To See If Wicd Is Installed
                    avail = subprocess.Popen(["wicd", "-h"],
                                             stdout=subprocess.PIPE,
                                             stderr=subprocess.PIPE)
                    std_out, std_err = avail.communicate()
                    # If the program check throws an error, print it to stderr
                    if len(std_err)!= 0:
                        sys.stderr.write(std_err)
                    # If the program does not throw an error, continue with the wicd_d function
                    if len(std_out) != 0:
                        subprocess.call(["wicd-cli", "--%s" % type, "--connect",
                                         "--network=%i" % network_num])
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFailure('wicd_con()')
                except Exception as error:
                    raise kerri.Unknown('wicd_con()', error)

        def wicd_dis(self, type='wireless', *args):
            """ Disconnect from network using Wicd-cli """

            if len(args) >= 1:
                raise kerri.ExcessArguments("wicd_dis()", 1)
            else:
                try:
                    # Check To See If Wicd Is Installed
                    avail = subprocess.Popen(["wicd", "-h"],
                                             stdout=subprocess.PIPE,
                                             stderr=subprocess.PIPE)
                    std_out, std_err = avail.communicate()
                    # If the program check throws an error, print it to stderr
                    if len(std_err)!= 0:
                        sys.stderr.write(std_err)
                    # If the program does not throw an error, continue with the wicd_d function
                    if len(std_out) != 0:
                        subprocess.Popen(["wicd-cli", "--%s" % type, "disconnect"])
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFailure('wicd_dis()')
                except Exception as error:
                    raise kerri.Unknown('wicd_dis()', error)

#########
# INITs #
#########

iface = Interface()
btaddr = iface.btaddr
btscan = iface.btscan
btinfo = iface.btinfo
btext_ifno = iface.btext_info
btauto = iface.btauto
btpower = iface.btpower
btpair = iface.btpair
btcon_info = iface.btcon_info
stop_mon = iface.stop_mon
start_mon = iface.start_mon
iconf_chk = iface.iconf_chk
inter_chk = iface.inter_chk
reset_netint = iface.reset_netint
addr = iface.Addressing()
get_route = addr.get_route
aval_inter = addr.aval_inter
verb_aval = addr.verb_aval
dface = addr.dface
uface = addr.uface
mac_change = addr.mac_change
ip_change = addr.ip_change
ip_route = addr.ip_route
chk_ip = addr.chk_ip
ip_loc = addr.ip_loc
vend_mac = addr.vend_mac
search_mac = addr.search_mac
wifi = iface.Wifi()
man_chk = wifi.man_chk
current_network = wifi.current_network
netman = wifi.netman
nmcli_con = wifi.nmcli_con
iw_scan = wifi.iw_scan
simple_iw = wifi.simple_iw
