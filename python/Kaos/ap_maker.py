#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Created: Aug 2017

    @author: 73RM1N41@9R0GR4M13
"""

import kerri
import subprocess
import sys

#########################
# ACCESS POINT CREATION #
#########################


class AP(object):
    """ Used to create and manage created access points """

    def __init__(self, prog_loc="/usr/bin/create_ap", *args):
        if len(args) >= 1:
            raise kerri.ExcessArguments("AP()", 1)
        else:
            self.prog_loc = prog_loc

    def __str__(self):
        return """ Controls All Kaos Access Point Creation And Management """

    def ls_aps(self, *args):
        """ List Created Access Points Currently Running """

        if len(args) >= 1:
            raise kerri.ExcessArguments("ls_ap()", 0)
        else:
            try:
                aps = subprocess.Popen([self.prog_loc,
                                        "--list-running"],
                                       stdout=subprocess.PIPE)
                std_out = aps.communicate()
                if len(std_out) != 0:
                    return std_out
            except subprocess.CalledProcessError:
                raise kerri.ProcessFailure("ls_ap()")
            except Exception as error:
                raise kerri.Unknown("ls_ap()", error)

    def ls_clients(self, ident, *args):
        """ List Clients Connected To Active Access Point """

        if len(args) >= 1:
            raise kerri.ExcessArguments("ls_clients()", 1)
        else:
            try:
                clients = subprocess.Popen([self.prog_loc, "--list-clients",
                                            str(ident)],
                                           stdout=subprocess.PIPE,
                                           stderr=subprocess.PIPE)
                std_out, std_err = clients.communicate()
                if len(std_err) != 0:
                    return std_err.decode()
                if len(std_out) != 0:
                    return std_out.decode()
            except subprocess.CalledProcessError:
                raise kerri.ProcessFailure("ls_clients()")
            except Exception as error:
                raise kerri.Unknown("ls_clients()", error)

    def stop_ap(self, ident, *args):
        """ Shutdown A Created Access Point """

        if len(args) >= 1:
            raise kerri.ExcessArguments("stop_ap()", 1)
        else:
            try:
                subprocess.Popen([self.prog_loc, "--stop",
                                  str(ident)], stdout=subprocess.PIPE)
            except subprocess.CalledProcessError:
                raise kerri.ProcessFailure("stop_ap()")
            except Exception as error:
                raise kerri.Unknown("stop_ap()", error)

    def open_ap(self, ap_interface, internet_interface, ap_name, iso_clients=0,
                hidden=0, *args):
        """ Create An Open Access Point """

        if len(args) >= 1:
            raise kerri.ExcessArguments("open_ap()", 3)
        else:
            try:
                if iso_clients == 0:
                    if hidden == 0:
                        subprocess.Popen([self.prog_loc, "--daemon",
                                          ap_interface, internet_interface,
                                          ap_name], stdout=subprocess.PIPE)
                    if hidden == 1:
                        subprocess.Popen([self.prog_loc, "--daemon",
                                          "--hidden", ap_interface,
                                          internet_interface, ap_name],
                                         stdout=subprocess.PIPE)
                elif iso_clients == 1:
                    if hidden == 0:
                        subprocess.Popen([self.prog_loc, "--daemon",
                                          "--isolate-clients",
                                          ap_interface, internet_interface,
                                          ap_name], stdout=subprocess.PIPE)
                    if hidden == 1:
                        subprocess.Popen([self.prog_loc, "--daemon",
                                          "--hidden", "--isolate-clients",
                                          ap_interface, internet_interface,
                                          ap_name], stdout=subprocess.PIPE)
                elif iso_clients != 0 and iso_clients != 1 or hidden != 0 and hidden != 1:
                    raise kerri.InvalidInput("open_ap()")
            except subprocess.CalledProcessError:
                kerri.ProcessFailure("open_ap()")
            except Exception as error:
                if error.returncode == 1:
                    raise kerri.InvalidInput("open_ap()", "iso_clients must be either a 0 => {off} or a 1 => {on}.")
                else:
                    raise kerri.Unknown("open_ap()", error)

    def internal_ap(self, ap_interface, ap_name, password, iso_clients=0, hidden=0, *args):
        """ Create An Access Point For An Internal Network.
            Access Point Users Will Have NO Internet Access """
        if len(args) >= 1:
            raise kerri.ExccessArguments("internal_ap()", 3)
        else:
            try:
                if iso_clients == 0:
                    if hidden == 0:
                        subprocess.Popen([self.prog_loc,
                                          "--daemon", "-n",
                                          ap_interface, ap_name,
                                          password], stdout=subprocess.PIPE)
                    if hidden == 1:
                        subprocess.Popen([self.prog_loc, "--daemon", "--hidden", "-n", ap_interface, ap_name, password], stdout=subprocess.PIPE)
                    elif iso_clients == 1:
                        if hidden == 0:
                            subprocess.Popen([self.prog_loc, "--daemon", "--isolate-clients", "-n", ap_interface, ap_name, password], stdout=subprocess.PIPE)
                        if hidden == 1:
                            subprocess.Popen([self.prog_loc, "--daemon", "--hidden", "--isolate-clients", "-n", ap_interface, ap_name, password], stdout=subprocess.PIPE)
                    else:
                        raise kerri.InvalidInput("internal_ap()")
            except subprocess.CalledProcessError:
                raise kerri.ProcessFailure("internal_ap()")
            except Exception as error:
                if error.returncode == 1:
                    raise kerri.InvalidInput("internal_ap()", "iso_clients must be either a 0 => {off} or a 1 => {on}.")
                else:
                    raise kerri.Unknown("internal_ap()", error)

    def std_ap(self, ap_interface, internet_interface, ap_name, password, iso_clients=0, hidden=0, *args):
        """ Create a standard access point with WPA/WPA2 passphrase """

        if len(args) >= 1:
            raise kerri.ExcessArguments("std_ap()")
        else:
            try:
                if iso_clients == 0:
                    if hidden == 0:
                        subprocess.Popen([self.prog_loc, "--daemon", ap_interface, internet_interface, ap_name, password], stdout=subprocess.PIPE)
                    if hidden == 1:
                        subprocess.Popen([self.prog_loc, "--daemon", "--hidden", ap_interface, internet_interface, ap_name, password], stdout=subprocess.PIPE)
                elif iso_clients == 1:
                    if hidden == 0:
                        subprocess.Popen([self.prog_loc, "--daemon", "--isolate-clients", ap_interface, internet_interface, ap_name, password], stdout=subprocess.PIPE)
                    if hidden == 1:
                        subprocess.Popen([self.prog_loc, "--daemon", "--hidden", "--isolate-clients", ap_interface, internet_interface, ap_name, password], stdout=subprocess.PIPE)
                else:
                    raise kerri.InvalidInput("std_ap()")
                return "AccessPoint %s Successfully Created On Interface %s\nAP Name: %s\nAP Interface: %s\nInet Interface: %s\nPassword: %s\nIsolated Clients: %s\nHidden Network: %s" % (ap_name, ap_interface, ap_name, ap_interface, internet_interface, password, iso_clients, hidden)
            except subprocess.CalledProcessError:
                raise kerri.ProcessFailure("std_ap()")
            except Exception as error:
                if error.returncode == 1:
                    raise kerri.InvalidInput("std_ap()", "iso_clients must be either a 0 => {off} or a 1 => {on}.")
                else:
                    raise kerri.Unknown("std_ap()", error)

    def pro_ap(self, ap_interface, internet_interface, ap_name, ap_mac, password, gateway='192.168.13.1', freq='2.4', iso_clients=0, hidden=0, *args):
        """ Create An Access Point With Semi-Advanced Configuration """

        if len(args) >= 1:
            raise kerri.ExcessArguments("pro_ap()", 9)
        else:
            try:
                if iso_clients == 0:
                    if hidden == 0:
                        subprocess.Popen([self.prog_loc, "--daemon",
                                          ap_interface, internet_interface,
                                          ap_mac, gateway, freq, ap_name,
                                          password], stdout=subprocess.PIPE)
                    if hidden == 1:
                        subprocess.Popen([self.prog_loc, "--daemon",
                                          "--hidden", ap_interface,
                                          internet_interface, ap_mac,
                                          gateway, freq, ap_name,
                                          password], stdout=subprocess.PIPE)
                elif iso_clients == 1:
                    if hidden == 0:
                        subprocess.Popen([self.prog_loc, "--daemon",
                                          "--isolate-clients", ap_interface,
                                          internet_interface, ap_mac,
                                          gateway, freq, ap_name,
                                          password], stdout=subprocess.PIPE)
                    if hidden == 1:
                        subprocess.Popen([self.prog_loc, "--daemon",
                                          "--hidden", "--isolate-clients",
                                          ap_interface, internet_interface,
                                          ap_mac, gateway, freq, ap_name,
                                          password], stdout=subprocess.PIPE)
                else:
                    raise kerri.InvalidInput("std_ap()")
                return "AccessPoint %s Successfully Created On Interface %s"
            except subprocess.CalledProcessError:
                raise kerri.ProcessFailure("std_ap()")
            except Exception as error:
                if error.returncode == 1:
                    raise kerri.InvalidInput("std_ap()", "iso_clients must be either a 0 => {off} or a 1 => {on}.")
                else:
                    raise kerri.Unknown("std_ap()", error)


#########
# INITs #
#########

ap = AP()
ls_aps = ap.ls_aps
ls_clients = ap.ls_clients
stop_ap = ap.stop_ap
open_ap = ap.open_ap
std_ap = ap.std_ap
internal_ap = ap.internal_ap
pro_ap = ap.pro_ap
