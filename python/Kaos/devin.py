#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Created: Aug 2017

    @author: D34D9001@9R0GR4M13
"""

import kerri
import ktime
import ksys
import os
import subprocess
# from termcolor import colored

class Devin(object):
    """ This Class Handles Development Integration For Multiple Languages.
        Use This Class To Interactively Create And Run Scripts In Multiple
        Languages Directly From Kaos. Scripts Are Securely Removed After Execution
        With "secure remove {srm}" Unless The 'delete' Parameter Is Set To 0.

        Currenty Available Languages:
                                        Bash
                                        Perl
                                        Python
                                        Ruby"""
    def ruby(self, delete=1, ruby_loc="/usr/bin/ruby", *args):
        """ Write Then Execute A Ruby Script From Kaos """

        if len(args) >= 1:
            raise kerri.ExcessArguments("ruby()")
        else:
            try:
                program = "ruby"
                if str(os.path.isfile("/usr/bin/%s" % program)) == "True":
                    if str(os.access("/usr/bin/%s" % program,
                                     os.X_OK)) == "True":
                        tmp_script = "/tmp/k_ruby.rb"
                        prog = ruby_loc
                        header = """#!/usr/bin/ruby -w
# encode: ISO_8859_1

        """
                        with open(tmp_script, 'w') as script:
                            script.write("%s\n" % header)
                            index = 0
                            print("[*] Add A Blank Line To Stop:\n-----------------------------")
                            print(header)
                            while True:
                                text = raw_input(">>> ")
                                if len(text) >= 1:
                                    script.write("%s\n" % text)
                                    index += 1
                                else:
                                    if index == 0:
                                        print("No Data Was Added To The Script")
                                    else:
                                        print("Data Successfully Added To The Script")
                                    break
                            script.close()
                        print("Running The Ruby Script Now...\n")
                        ktime.wait(.5)
                        subprocess.call([prog, tmp_script])
                        if delete == 0:
                            del_conf = raw_input("\nWould You Like To Save Your Script?\n[Y/N]: ")
                            if del_conf == "Y" or del_conf == "y" or del_conf == "Yes" or del_conf == "yes" or del_conf == "YES":
                                location = raw_input("Where Would You Like To Save Your File?\n[Save Location]: ")
                                try:
                                    subprocess.call(["mv", tmp_script, location])
                                except subprocess.CalledProcessError:
                                    try:
                                        subprocess.call(["cp", tmp_script, location])
                                        ksys.srem(tmp_script)
                                    except subprocess.CalledProcessError:
                                        ksys.srem(tmp_script)
                                        raise kerri.ProcessFailure("python()", "Script Could Not Be Saved!")
                            else:
                                ksys.srem(tmp_script)
                        if delete == 1:
                            ksys.srem(tmp_script)
                    else:
                        return "The Ruby File Exists But Is Not Executable..."
                else:
                    return "Ruby Is Not Installed"
            except OSError as e:
                if e.errno == 2:
                    return "Ruby Is Not Installed On This System!!!"
                else:
                    return "Ruby Installation Status Unknown"
            except subprocess.CalledProcessError:
                raise kerri.ProcessFailure("ruby()")
            except Exception as error:
                raise kerri.Unknown("ruby()", error)

    def perl(self, delete=1, perl_loc="/usr/bin/perl", *args):
        """ Write Then Execute A Perl Script From Kaos """

        if len(args) >= 1:
            raise kerri.ExcessArguments("perl()")
        else:
            try:
                program = "perl"
                if str(os.path.isfile("/usr/bin/%s" % program)) == "True":
                    if str(os.access("/usr/bin/%s" % program,
                                     os.X_OK)) == "True":
                        tmp_script = "/tmp/k_perl.pl"
                        prog = perl_loc
                        header = "#!/usr/bin/perl"
                        with open(tmp_script, 'w') as script:
                            script.write("%s\n" % header)
                            index = 0
                            print("[*] Add A Blank Line To Stop:\n-----------------------------")
                            print(header)
                            while True:
                                text = raw_input(">>> ")
                                if len(text) >= 1:
                                    script.write("%s\n" % text)
                                    index += 1
                                else:
                                    if index == 0:
                                        print("No Data Was Added To The Script")
                                    else:
                                        print("Data Successfully Added To The Script")
                                    break
                            script.close()
                        print("Running The Perl Script Now...\n")
                        ktime.wait(.5)
                        subprocess.call([prog, tmp_script])
                        if delete == 0:
                            del_conf = raw_input("\nWould You Like To Save Your Script?\n[Y/N]: ")
                            if del_conf == "Y" or del_conf == "y" or del_conf == "Yes" or del_conf == "yes" or del_conf == "YES":
                                location = raw_input("Where Would You Like To Save Your File?\n[Save Location]: ")
                                try:
                                    subprocess.call(["mv", tmp_script, location])
                                except subprocess.CalledProcessError:
                                    try:
                                        subprocess.call(["cp", tmp_script, location])
                                        ksys.srem(tmp_script)
                                    except subprocess.CalledProcessError:
                                        ksys.srem(tmp_script)
                                        raise kerri.ProcessFailure("perl()", "Script Could Not Be Saved!")
                            else:
                                ksys.srem(tmp_script)
                        if delete == 1:
                            ksys.srem(tmp_script)
                    else:
                        return "The Perl File Exists But Is Not Executable..."
                else:
                    return "Perl Is Not Installed"
            except OSError as e:
                if e.errno == 2:
                    return "Perl Is Not Installed On This System!!!"
                else:
                    return "Perl Installation Status Unknown"
            except subprocess.CalledProcessError:
                raise kerri.ProcessFailure("perl()")
            except Exception as error:
                raise kerri.Unknown("perl()", error)

    def python(self, delete=1, version="2.7", *args):
        """ Write Then Execute A Python Script From Kaos
            Only Versions 2.7 And 3.6 Are Supported."""

        if len(args) >= 1:
            raise kerri.ExcessArguments("python()")
        else:
            try:
                program = "python%s" % version
                if str(os.path.isfile("/usr/bin/%s" % program)) == "True":
                    if str(os.access("/usr/bin/%s" % program,
                                     os.X_OK)) == "True":
                        tmp_script = "/tmp/k_python.py"
                        if version == "2.7":
                            py_loc = "/usr/bin/python2.7"
                        elif version == "3.6":
                            py_loc = "/usr/bin/python3.6"
                        else:
                            raise kerri.InvalidInput("python()", "Only Versions 2.7 and 3.6 Are Supported!")
                        prog = py_loc
                        header = """#!%s
# -*- coding: utf-8 -*-

        """ % py_loc
                        with open(tmp_script, 'w') as script:
                            script.write("%s\n" % header)
                            index = 0
                            print("[*] Add A Blank Line To Stop:\n-----------------------------")
                            print(header)
                            while True:
                                text = raw_input(">>> ")
                                if len(text) >= 1:
                                    script.write("%s\n" % text)
                                    index += 1
                                else:
                                    if index == 0:
                                        print("No Data Was Added To The Script")
                                    else:
                                        print("Data Successfully Added To The Script")
                                    break
                            script.close()
                        print("Running The Python Script Now...\n")
                        ktime.wait(.5)
                        subprocess.call([prog, tmp_script])
                        if delete == 0:
                            del_conf = raw_input("\nWould You Like To Save Your Script?\n[Y/N]: ")
                            if del_conf == "Y" or del_conf == "y" or del_conf == "Yes" or del_conf == "yes" or del_conf == "YES":
                                location = raw_input("Where Would You Like To Save Your File?\n[Save Location]: ")
                                try:
                                    subprocess.call(["mv", tmp_script, location])
                                except subprocess.CalledProcessError:
                                    try:
                                        subprocess.call(["cp", tmp_script, location])
                                        ksys.srem(tmp_script)
                                    except subprocess.CalledProcessError:
                                        ksys.srem(tmp_script)
                                        raise kerri.ProcessFailure("python()", "Script Could Not Be Saved!")
                            else:
                                ksys.srem(tmp_script)
                        if delete == 1:
                            ksys.srem(tmp_script)
                    else:
                        return "The Python%s File Exists But Is Not Executable..." % version
                else:
                    return "Python%s Is Not Installed" % version
            except OSError as e:
                if e.errno == 2:
                    return "Python%s Is Not Installed On This System!!!" % version
                else:
                    return "Python%s Installation Status Unknown" % version
            except subprocess.CalledProcessError:
                raise kerri.ProcessFailure("python()")
            except Exception as error:
                raise kerri.Unknown("python()", error)

    def bash(self, delete=1, bash_loc="/bin/bash", *args):
        """ Write Then Execute A Bash Script From Kaos """

        if len(args) >= 1:
            raise kerri.ExcessArguments("bash()")
        else:
            try:
                program = "bash"
                if str(os.path.isfile("/bin/%s" % program)) == "True":
                    if str(os.access("/bin/%s" % program,
                                     os.X_OK)) == "True":
                        tmp_script = "/tmp/k_bash.sh"
                        prog = bash_loc
                        header = "#!/usr/bin/env bash"
                        with open(tmp_script, 'w') as script:
                            script.write("%s\n" % header)
                            index = 0
                            print("[*] Add A Blank Line To Stop:\n-----------------------------")
                            print(header)
                            while True:
                                text = raw_input(">>> ")
                                if len(text) >= 1:
                                    script.write("%s\n" % text)
                                    index += 1
                                else:
                                    if index == 0:
                                        print("No Data Was Added To The Script")
                                    else:
                                        print("Data Successfully Added To The Script")
                                    break
                            script.close()
                        print("Running The Bash Script Now...\n")
                        ktime.wait(.5)
                        subprocess.call([prog, tmp_script])
                        if delete == 0:
                            del_conf = raw_input("\nWould You Like To Save Your Script?\n[Y/N]: ")
                            if del_conf == "Y" or del_conf == "y" or del_conf == "Yes" or del_conf == "yes" or del_conf == "YES":
                                location = raw_input("Where Would You Like To Save Your File?\n[Save Location]: ")
                                try:
                                    subprocess.call(["mv", tmp_script, location])
                                except subprocess.CalledProcessError:
                                    try:
                                        subprocess.call(["cp", tmp_script, location])
                                        ksys.srem(tmp_script)
                                    except subprocess.CalledProcessError:
                                        ksys.srem(tmp_script)
                                        raise kerri.ProcessFailure("bash()", "Script Could Not Be Saved!")
                            else:
                                ksys.srem(tmp_script)
                        if delete == 1:
                            ksys.srem(tmp_script)
                    else:
                        return "The Bash File Exists But Is Not Executable..."
                else:
                    return "Bash Is Not Installed"
            except OSError as e:
                if e.errno == 2:
                    return "Bash Is Not Installed On This System!!!"
                else:
                    return "Bash Installation Status Unknown"
            except subprocess.CalledProcessError:
                raise kerri.ProcessFailure("bash()")
            except Exception as error:
                raise kerri.Unknown("bash()", error)

#########
# INITs #
#########

devin = Devin()
ruby = devin.ruby
perl = devin.perl
python = devin.python
bash = devin.bash
