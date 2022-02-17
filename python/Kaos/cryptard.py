#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Created: Aug 2017

    @author: D34D9001@9R0GR4M13
"""

import kerri
import gnupg
import subprocess
import sys
from Crypto.Cipher import AES
from Crypto import Random

###
# GNUPG
###
gnupg._parsers.Verify.TRUST_LEVELS["ENCRYPTION_COMPLIANCE_MODE"] = 23
gpg = gnupg.GPG(homedir="/root", keyring="/root/.gnupg/pubring.kbx")
gpg.encoding = 'utf-8'

####################################
# ENCRYPTION/DECRYPTION OPERATIONS #
####################################

class Cryptard(object):
    """ This class handles encryption and decryption operations """

    def __str__(self):
        return """ Controls Kaos' Encryption/Decryption Operations """

    def en_file(self, recipient, file_name, *args):
        """ Encrypt The Specified File """

        if len(args) >= 1:
            raise kerri.ExcessArguments("e_file()", 2)
        else:
            pass
        try:
            pipes = subprocess.Popen(["gpg", "-r", recipient, "-e", file_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            std_out, std_err = pipes.communicate()
            try:
                pipes_two = subprocess.Popen(["srm", "-f", file_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                std_out_two , std_err_two = pipes_two.communicate()
            except Exception:
                sys.stderr.write(std_err_two)
                return
        except IOError:
            raise kerri.FSError('en_file()')
        except subprocess.CalledProcessError:
            raise kerri.ProcessFailure('en_file', std_err)
        except Exception:
            raise kerri.Unknown('en_file', std_err)

    def de_file(self, recipient, file_name, output, *args):
        """ Decrypt The Specified File """

        if len(args) >= 1:
            raise kerri.ExcessArguments("de_file()", 3)
        else:
            pass
        try:
            pipes = subprocess.Popen(["gpg", "-r", recipient, "-o", output, "-d", file_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            std_out, std_err = pipes.communicate()
            try:
                pipes_two = subprocess.Popen(["srm", "-f", file_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                std_out_two , std_err_two = pipes_two.communicate()
            except Exception:
                sys.stderr.write(std_err_two)
                return
        except IOError:
            raise kerri.FSError('de_file()', std_err)
        except subprocess.CalledProcessError:
            raise kerri.ProcessFailure('de_file', std_err)
        except Exception:
            raise kerri.Unknown('de_file', std_err)

    def key_gen(self, *args):
        """ Generate A New GPG Key """

        if len(args) >= 1:
            raise kerri.ExcessArguments('key_gen()', 0)
        else:
            try:
                pipes = subprocess.Popen(["gpg", "--gen-key"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                std_out, std_err = pipes.communicate()
                if pipes.returncode != 0:
                    raise kerri.ProcessFailure('key_gen()', 4, std_err)
                else:
                    pass
            except KeyboardInterrupt:
                raise kerri.UsrInt('key_gen()')
            except subprocess.CalledProcessError:
                raise kerri.ProcessFailure("key_gen()")
            except Exception as error:
                raise kerri.Unknown("key_gen()", error)

    def pub_keys(self, *args):
        """ List Public Keys In '/root/.gnupg' Directory """

        if len(args) >= 1:
            return kerri.ExcessArguments("list_keys()", 0)
        else:
            try:
                pub_keys = gpg.list_keys()
                return pub_keys
            except Exception as error:
                raise kerri.Unknown("list_keys()", error)

    def del_pub(self, fingerprint, *args):
        """ This will only delete public keys """

        if len(args) >= 1:
            raise kerri.ExcessArguments("del_pub()", 1)
        else:
            try:
                gpg.delete_keys(fingerprint)
            except Exception as error:
                raise kerri.Unknown("del_pub()", error)

    def beta_en(self, data, recipient, *args):
        """ Encypt Data {Still In Beta Testing} """

        if len(args) >= 1:
            raise kerri.ExcessArguments("beta_en()")
        else:
            try:
                en_data = gpg.encrypt(data, recipient)
                return en_data
            except Exception as error:
                raise kerri.Unknown("beta_en()", error)

    def aes_msg(self, msg, key, *args):
        if len(args) >= 1:
            raise kerri.ExcessArguments("", )
        else:
            key = b'"%s"' % key
            iv = Random.new().read(AES.block_size)
            cipher = AES.new(key, AES.MODE_CFB, iv)
            message = iv + cipher.encrypt(b'"%s"' % msg)
            return message

#########
# INITs #
#########

cryptard = Cryptard()
en_file = cryptard.en_file
de_file = cryptard.de_file
key_gen = cryptard.key_gen
pub_keys = cryptard.pub_keys
del_pub = cryptard.del_pub
beta_en = cryptard.beta_en
aes_msg = cryptard.aes_msg
