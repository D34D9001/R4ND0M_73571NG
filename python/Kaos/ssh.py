#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created: Aug 2017

    @author: 73RM1N41@9R0GR4M13
"""
import kerri
import sys
import subprocess

##################
# SSH OPERATIONS #
##################

class SSH(object):
    """ Control SSH Operations """

    def __str__(self):
        return """ Controls All SSH Operations Preformed By Kaos """

    def ssh_con(self, user, ip, *args):
        if len(args) >= 1:
            raise kerri.ExcessArguments("ssh_con()", 2)
        else:
            try:
                subprocess.call(["ssh", "%s@%s" % (user, ip)])
            except subprocess.CalledProcessError:
                raise kerri.ProcessFailure("ssh_con()")
            except Exception as error:
                raise kerri.Unknown("ssh_con()", error)

    def scp(self, ifile, source, dest, recursive=0, *args):
        """ Copy Files To Remote Host With SSH """

        if len(args) >= 1:
            raise kerri.ExcessArguments("scp()", 4)
        else:
            try:
                if recursive == 0:
                    sec_copy = subprocess.Popen(["scp", "-i %s" % ifile, source, dest],
                                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    std_out, std_err = sec_copy.communicate()
                    if len(std_err) != 0:
                        sys.stderr.write(std_err)
                    if len(std_out) != 0:
                        return std_out
                elif recursive == 1:
                    sec_copy = subprocess.Popen(["scp", "-r", "-i %s" % ifile, source, dest],
                                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    std_out, std_err = sec_copy.communicate()
                    if len(std_err) != 0:
                        sys.stderr.write(std_err)
                    if len(std_out) != 0:
                        return std_out
                else:
                    raise kerri.InvalidInput("scp()", "The \'recursive\'option must be either a 0:{off} or a 1:{on}")
            except subprocess.CalledProcessError:
                raise kerri.ProcessFailure("scp()")
            except Exception as error:
                raise kerri.Unknown("scp()", error)

#########
# INITs #
#########

ssh = SSH()
ssh_con = ssh.ssh_con
scp = ssh.scp
