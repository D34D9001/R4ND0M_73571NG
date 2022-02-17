#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created: Aug 2017

    @author: D34D9001@9R0GR4M13
"""
import kerri
import konst
import os
import random
import subprocess

# Current Directory

global pwd

# THIS WILL SET THE CURRENT WORKING DIRECTORY AT TIME OF KAOS IMPORT
# IF THE DIRECTORY IS CHANGED AFTER KAOS IS IMPORTED, THIS VARIABLE
# WILL NOT CHANGE AUTOMATICALLY, BUT IT CAN BE CHANGED MANUALLY BY:
#   pwd = \'new/directory/path/\'

pwd = konst.pwd

class Generator(object):
    """ Generator for various objects """

    def __str__(self):
        return """ Generate Various Objects:
 Passwords:        pass_gen()
 Files:            file_gen()
 Random Numbers:   randig()
 Random Bytes:     randbyte()"""

    def pass_gen(self, length=8, pass_amnt=1, *args):
        """ Generate Random Passwords
        """
        if len(args) >= 1:
            raise kerri.ExcessArguments("pass_gen()", 2)
        else:
            try:
                password = subprocess.check_output(["pwgen", "-cnys",
                                                    str(length),
                                                    str(pass_amnt)])
                return password
            except subprocess.CalledProcessError:
                raise kerri.ProcessFailure('pass_gen()')
            except Exception as error:
                raise kerri.Unknown('pass_gen()', error)

    def file_gen(self, fcount=1, path="%s" % (pwd), size='512K', count=1, *args):
        """ Generate {fcount} files with random data """

        if len(args) >= 1:
            raise kerri.ExcessArguments("file_gen()", 2)
        else:
            try:
                if fcount == 0:
                    raise kerri.InvalidInput("file_gen()")
                elif fcount > 1:
                    index = 0
                    while index < fcount:
                        rand_file = "/dev/urandom"
                        bytes = 2
                        random_number = subprocess.check_output(["od", "-vAn",
                                                                 "-N%i" % bytes,
                                                                 "-tu",
                                                                 rand_file])
                        generated_number = random_number.rstrip()
                        ret_num = generated_number.strip()
                        rd_num = ret_num.replace(" ", "")
                        rpath = str(path) + "/kaos.%s" % rd_num
                        dd = subprocess.Popen(["dd", "status=progress",
                                               "if=/dev/urandom",
                                               "of=%s" % rpath,
                                               "bs=%s" % size,
                                               "count=%s" % str(count)],
                                               stdout=subprocess.PIPE,
                                               stderr=subprocess.PIPE)
                        std_out, std_err = dd.communicate()
                        index += 1
                        if len(std_out) != 0:
                            print("File %s Was Probably Not Saved... You Should Double Check... %s" % (rpath, std_err))
                        else:
                            print("File Saved @: %s\n" % rpath)
                else:
                        rand_file = "/dev/urandom"
                        bytes = 2
                        random_number = subprocess.check_output(["od", "-vAn",
                                                                 "-N%i" % bytes,
                                                                 "-tu",
                                                                 rand_file])
                        generated_number = random_number.rstrip()
                        ret_num = generated_number.strip()
                        rd_num = ret_num.replace(" ", "")
                        rpath = str(path) + "/kaos.%s" % rd_num
                        subprocess.call(["dd", "status=progress",
                                         "if=/dev/urandom", "of=%s" % rpath,
                                         "bs=%s" % size,
                                         "count=%s" % str(count)])
                        print("File Saved @: %s\n" % rpath)
            except subprocess.CalledProcessError as error:
                raise kerri.ProcessFailure('file_gen()', error)
            except Exception as error:
                if error.returncode == 1:
                    raise kerri.InvalidInput("file_gen()", "You must create at least 1 file!")
                raise kerri.Unknown('file_gen()', error)

    def randig(self, x=1, *args):
        """
        Generate Random Digits Of Specified Length
        """

        if len(args) >= 1:
            raise kerri.ExcessArguments("randig()", 1)
        range_start = 10**(x-1)
        range_end = (10**x)-1
        return random.randint(range_start, range_end)

    def randbyte(self, x, *args):
        """ Generates (x) random bytes (suitable for
            cryptographic use) """

        if len(args) >= 1:
            raise kerri.ExcessArguments("randbytes()", 1)
        try:
            bytes = os.urandom(x)
            return bytes
        except Exception as error:
            raise kerri.Unknown("randbyte()", error)


#########
# INITs #
########

gen = Generator()
pass_gen = gen.pass_gen
file_gen = gen.file_gen
randbyte = gen.randbyte
randig = gen.randig
