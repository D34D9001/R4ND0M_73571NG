#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created: Aug 2017

    @author: D34D9001@9R0GR4M13
"""
import kerri

#############
# VERIFIERS #
#############

class Verifier(object):
    """ Verify Formatting Of Various User Input Variables """

    def __init__(self):
        self.ip_classes = {"A":"0.0.0.0 - 127.255.255.255",
                           "B":"128.0.0.0 - 191.255.255.255",
                           "C":"192.0.0.0 - 223.225.225.225",
                           "D":"224.0.0.0 - 239.255.255.255",
                           "E":"240.0.0.0 - 255.255.255.255"}

        self.classes = []
        for item in self.ip_classes:
            self.classes.append("%s: %s" % (item, self.ip_classes[item]))

    def __str__(self):
        return """This Class Checks To See If The Format Of User Input Variables Are Valid.

                  ver_ip():
                           If The IP Is Valid, The IP Address Class And Input IP
                           Are Returned. \nClasses: %s

                  ver_ssn():
                            If The SSN Is Of A Valid Format, The SSN Is Returned
                            With A \"Valid Format\" Status """ % (self.ip_classes)

    def ver_ip(self, ip_address, *args):
        """ This Function DOES NOT validate IP Addresses. It Simply Checks To
            See If The User Input IP Address Is Of A Valid Format And Within
            Range Of Valid IP Addresses """

        if len(args) >= 1:
            raise kerri.ExcessArguments("ver_ip()", 1)
        else:
            try:
                eval_address = ()
                ip = ip_address.split(".")
                for item in ip:
                    if item.isdigit():
                        if int(item) >= 0 and int(item) <= 255:
                            eval_address = eval_address + (item, )
                        else:
                            raise kerri.InvalidInput("IP Addresses Cannot Contain Numbers Higher Than 255 Or Less Than 0", returncode=13)
                    else:
                        raise kerri.InvalidInput("ver_ip()", "IP Addresses Do Not Contain Letters Or Special Characters!!!", returncode=14)
                if int(eval_address[0].strip()) in range(240, 256):
                    ip_class = "E"
                elif int(eval_address[0].strip()) in range(224, 240):
                    ip_class = "D"
                elif int(eval_address[0].strip()) in range(192, 224):
                    ip_class = "C"
                elif int(eval_address[0].strip()) in range(128, 192):
                    ip_class = "B"
                elif int(eval_address[0].strip()) in range(0, 128):
                    ip_class = "A"
                else:
                    address = eval_address[0]+"."+eval_address[1]+"."+eval_address[2]+"."+eval_address[3]
       	            raise kerri.InvalidInput("ip_ver()", "%s: This Is Not A Valid IP Address" % address.strip())

                if int(eval_address[0].strip()) == 192:
                    if int(eval_address[1].strip()) == 168:
                        ip_class = "Private C"
                elif int(eval_address[0].strip()) == 172:
                    if int(eval_address[1].strip()) in range(16, 32):
                        ip_class = "Private B"
                elif int(eval_address[0].strip()) == 127:
                    if int(eval_address[1].strip()) in range(0, 256):
                        ip_class = "Private A {LOOPBACK ADDRESS}"
                elif int(eval_address[0].strip()) == 10:
                    if int(eval_address[1].strip()) in range(0, 256):
                        ip_class = "Private A"
                address = eval_address[0]+"."+eval_address[1]+"."+eval_address[2]+"."+eval_address[3]
                return ip_class, address
            except Exception as error:
                if error.returncode == 1:
                    raise kerri.InvalidInput("ver_ip()", "IP Address Is INVALID!")
                elif error.returncode == 13:
                    raise kerri.InvalidInput("ver_ip()","IP Addresses Cannot Contain Numbers Higher Than 255", 13)
                elif error.returncode == 14:
                    raise kerri.InvalidInput("ver_ip()", "IP Addresses Do Not Contain Letters!!!", 14)
                else:
                    raise kerri.Unknown("ver_ip()", error)

    def ver_ssn(self, ssn, *args):
        """ This Function DOES NOT validate Social Security Numbers. It Simply
            Checks To See If The User Input SSN Is The Correct Format """

        if len(args) >= 1:
            raise kerri.ExcessArguments("ver_ssn()", 1)
        else:
            try:
                if ssn.isdigit():
                    if len(ssn) == 9:
                        return "[Valid Format]: %s" % ssn
                    elif len(ssn) < 9:
                        raise kerri.InvalidInput("ver_ssn()", "SSN Is Too Short!!!", returncode=14)
                    elif len(ssn) > 9:
                        raise kerri.InvalidInput("ver_ssn()", "SSN Is Too Long!!!", returncode=13)
                else:
                    raise kerri.InvalidInput("ver_ssn()", "Social Security Numbers Can Only Contain Numbers...")
            except Exception as error:
                if error.returncode == 1:
                    raise kerri.InvalidInput("ver_ssn()", "Social Security Numbers Contain Only Numbers...")
                elif error.returncode == 13:
                    raise kerri.InvalidInput("ver_ssn()", "SSN Is Too Long!!!", returncode=13)
                elif error.returncode == 14:
                    raise kerri.InvalidInput("ver_ssn()", "SSN Is Too Short!!!", returncode=13)
                else:
                    raise kerri.Unknown("ver_ssn()", error)

#########
# INITs #
#########

verifier = Verifier()
ver_ip = verifier.ver_ip
ver_ssn = verifier.ver_ssn
