#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created: Aug 2017

    @author: D34D9001@9R0GR4M13
"""
import kerri
import konst
import os
import subprocess
import shlex
import sys
import time
from termcolor import colored

# Current Directory

global pwd

# THIS WILL SET THE CURRENT WORKING DIRECTORY AT TIME OF KAOS IMPORT
# IF THE DIRECTORY IS CHANGED AFTER KAOS IS IMPORTED, THIS VARIABLE
# WILL NOT CHANGE AUTOMATICALLY, BUT IT CAN BE CHANGED MANUALLY BY:
#   pwd = \'new/directory/path/\'

pwd = konst.pwd

#####################
# SYSTEM MANAGEMENT #
#####################

class System(object):
    """ Controls system operations """

    def __str__(self):
        return """ Controls All System Operations Performed By Kaos """

    def op_sys(self, *args):
        if len(args) >= 1:
            raise kerri.ExcessArguments("vers_chk()", 0)
        else:
            try:
                op_system = subprocess.Popen(["uname", "-r"],
                                                  stdout=subprocess.PIPE,
                                                  stderr=subprocess.PIPE)
                std_out, std_err = op_system.communicate()
                if len(std_err) != 0:
                    sys.stderr.write(std_err.decode())
                if len(std_out) != 0:
                    return std_out
            except subprocess.CalledProcessError:
                raise kerri.ProcessFailure("op_sys()")
            except Exception as error:
                raise kerri.Unknown("op_sys()", error)

    def get_host(self, *args):
        if len(args) >= 1:
            raise kerri.ExcessArguments("get_host()", 0)
        else:
            try:
#                hostname = subprocess.check_output(["hostname"])
                hostname = subprocess.Popen(["hostname"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                if len(std_out) >= 1:
                    return std_out.decode()
                else:
                    return std_err.decode()
            except Exception as error:
                raise kerri.Unknown("get_host()", error)

    def get_user(self, *args):
        if len(args) >= 1:
            raise kerri.ExcessArguments("get_user()", 0)
        else:
            try:
                username = subprocess.Popen(["whoami"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                std_out, std_err = username.communicate()
                if len(std_out) >= 1:
                    output = std_out
                else:
                    output = std_err
                return output.decode()
            except Exception as error:
                raise kerri.Unknown("get_user()", error)

#   #######################
#   # HARDWARE MANAGEMENT #
#   #######################

    class Hardware(object):
        """Controls hardware operations """

        def __str__(self):
            return """ Controls All Hardware Operations Preformed By Kaos """

        def battery(self, *args):
            """ Check battery information """

            if len(args) >= 1:
                raise kerri.ExcessArguments("battery()", 0)

            else:

                try:
                    usable_os = "kali"
                    actual_os = subprocess.check_output(["uname", "-r"])
                    # Check To See If The User Is Running Kali Linux
                    if usable_os in actual_os.decode():
                        bat_info = subprocess.Popen(["upower", "-i", "/org/freedesktop/UPower/devices/battery_BAT0"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        std_out, std_err = bat_info.communicate()
                        if len(std_out) >= 1:
                            return std_out
                        else:
                            return std_err

                    # If The User Is Not Running Kali Linux, The Arch 'Equivalent' Is Executed
                    else:
                        bat_info = subprocess.Popen(["acpi", "-V"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        std_out, std_err = bat_info.communicate()

                        if len(std_out) >= 1:
                            return std_out
                        else:
                            return std_err

                except subprocess.CalledProcessError as error:
                    raise kerri.ProcessFailure('battery()')
#                    return error

                except Exception as error:
#                    raise kerri.Unknown("battery()", error)
                    return error

        def shutdown(self, option='h', itime=None, wall=None, *args):
            """ Shutdown the entire system (default time is (1) minute)
                Or cancel an active shutdown """

            if len(args) >= 1:
                raise kerri.ExcessArguments("shutdown()", 1)
            else:
                try:
                    if itime == None:
                        if wall != None:
                            itime = '1'
                            pipes = subprocess.Popen(["shutdown", "-%s" % option, "%s" % itime, "%s" % wall],
                                                       stdout=subprocess.PIPE,
                                                       stderr=subprocess.PIPE)
                            std_out, std_err = pipes.communicate()
                        else:
                            pipes = subprocess.Popen(["shutdown", "--no-wall", "-%s" % option],
                                                       stdout=subprocess.PIPE,
                                                       stderr=subprocess.PIPE)
                            std_out, std_err = pipes.communicate()
                    else:
                        if wall != None:
                            pipes = subprocess.Popen(["shutdown", "-%s" % option, "%s" % itime, "%s" % wall],
                                                       stdout=subprocess.PIPE,
                                                       stderr=subprocess.PIPE)
                            std_out, std_err = pipes.communicate()
                        else:
                            pipes = subprocess.Popen(["shutdown", "--no-wall", "-%s" % option, "%s" % itime],
                                                       stdout=subprocess.PIPE,
                                                       stderr=subprocess.PIPE)
                            std_out, std_err = pipes.communicate()
                    if len(std_out) != 0:
                        sys.stdout.write(std_out)
                    if len(std_err) != 0:
                        sys.stderr.write(std_err)
                except subprocess.CalledProcessError as error:
                    raise kerri.ProcessFailure('shutdown()', error)
                except Exception as error:
                    raise kerri.Unknown("shutdown()", error)

#   #   ##############
#   #   # MICROAUDIO #
#   #   ##############

        class MicroAudio(object):
            """ Controls microphone recording and audio playback """

            def __str__(self):
                return """ Controls All Microphone Interactions As Well As
All Audio Playback Processes Preformed By Kaos"""

            def record(self, file_name, duration=0, *args):
                """ Record audio with default builtin microphone for (n) seconds
                    A duration of 0 will record for infinity or until you hit ctrl^c """

                if len(args) >= 1:
                    raise kerri.ExcessArguments("record()", 2)
                else:
                    try:
                        if "kali" in subprocess.check_output(["uname", "-r"]):
                            if duration != 0:
                                print(colored("record() Will Run For %s seconds..." % str(duration), 'blue', attrs=['bold']))
                                subprocess.call(["parecord", "-rv", "%s" % file_name], timeout=duration)
                            else:
                                subprocess.call(["parecord", "-rv", "%s" % file_name])
                        else:
                            pipes = subprocess.Popen(["arecord", "-q",
                                                      "--duration=%s" % duration],
                                                       stdout=subprocess.PIPE,
                                                       stderr=subprocess.PIPE)
                            std_out, std_err = pipes.communicate()
                    except subprocess.TimeoutExpired:
                        return "Recording Was Saved @ %s" % file_name
                    except subprocess.CalledProcessError:
                        raise kerri.ProcessFailure('record()')
                    except Exception:
                        raise kerri.Unknown('record()', 6, std_err)

            def play(self, file_name, *args):
                """ Play a specified audio file """

                if len(args) >= 1:
                    raise kerri.ExcessArguments("play()", 1)
                else:
                    try:
                        if "kali" in subprocess.check_output(["uname", "-r"]):
                            subprocess.call(["parecord", "-pv", file_name])
                        else:
                            play_file = subprocess.Popen(["aplay", "-q", file_name], stderr=subprocess.PIPE)
                            std_err = play_file.communicate()
                            if len(std_err) != 0:
                                sys.stderr.write(std_err)
                    except KeyboardInterrupt:
                        raise kerri.UsrInt('play(%s)' % file_name)
                    except subprocess.CalledProcessError:
                        raise kerri.ProcessFailure('play()', std_err)
                    except Exception as error:
                        raise kerri.Unknown('play()', error)

            def tonegen(self, time=276447231, wave="sine", freq=1000, *args):
                """ Generate a tone with {x} freq and {y} waveform for {t} secs """

                if len(args) >= 1:
                    raise kerri.ExcessArguments("tonegen()")
                else:
                    try:
                        subprocess.call(["altonegen", "-t", str(time), "-w",
                                          str(wave), "-f", str(freq)])
                    except KeyboardInterrupt:
                        raise kerri.UsrInt("tonegen()")
                    except subprocess.CalledProcessError:
                        raise kerri.ProcessFailure("tonegen()")
                    except Exception as error:
                        raise kerri.Unknown("tonegen()", error)

            def static(self, time=276447231, *args):
                """ Generate WhiteNoise """

                if len(args) >= 1:
                    raise kerri.ExcessArguments("whitenoise()")
                else:
                    try:
                        subprocess.call(["altonegen", "-t", str(time), "-w",
                                         "noise"])
                    except KeyboardInterrupt:
                        raise kerri.UsrInt("static()")
                    except subprocess.CalledProcessError:
                        raise kerri.ProcessFailure("static()")
                    except Exception as error:
                        raise kerri.Unknown("static()", error)

#   ##########################
#   # FILE SYSTEM MANAGEMENT #
#   ##########################

    class FS_Man(object):
        """ Filesystem management """

        def __str__(self):
            return """ Controls All File System Operations Preformed By Kaos
Except For Reading, Writing, And Editing Files.

See: kaos.System.File """

        def cd(self, directory="/root", *args):
            """ Change to specified directory """

            if len(args) >= 1:
                raise kerri.ExcessArguments("cd()", 1)
            else:
                try:
                    if str(os.path.isfile(directory)) == "False":
                        if str(os.path.isdir(directory)) == "False":
                            raise kerri.FSError("cd()")
                        else:
                            os.chdir(directory)
                    else:
                        raise kerri.FSError("cd()")
                except Exception as error:
                    if error.returncode == 3:
                        raise kerri.FSError("cd(%s)" % directory, "%s Is A File, Not A Directory!" % (directory))
                    else:
                        raise kerri.Unknown("cd()", error)

        def dcon(self, path=None, *args):
            """ Lists the contents of a directory """

            if len(args) >= 1:
                raise kerri.ExcessArguments("dir_con()", 1)
            else:
                if path == None:
                    path = os.getcwd()
                if str(os.path.isdir(path)) == "False":
                    raise kerri.FSError('dir_con')
                else:
                    try:
                        contents = subprocess.Popen(["ls", "-A", "--author", path],
                                                     stdout=subprocess.PIPE,
                                                     stderr=subprocess.PIPE)
                        std_out, std_err = contents.communicate()
                        if len(std_out) != 0:
#                            return shlex.split(std_out.rstrip())
                            output = ""
                            for item in std_out.split():
                                output = output + "\n" + item.decode()
#                            return std_out.split()
                            return output
                    except subprocess.CalledProcessError as error:
                        raise kerri.ProcessFailure('dir_con()', error)
                    except Exception as error:
                        raise kerri.Unknown('dir_con()', error)

        def rcon(self, directory, start, end, *args):
            """ List Directory Contents In Range(start_range, end_range)
                Useful for viewing large directories in tty or other limited
                scroll back environment"""

            if len(args) >= 1:
                raise kerri.ExcessArguments('rcon()', 3)
            elif str(os.path.isdir(directory)) == "False":
                raise kerri.FSError('rcon()')
            else:
                try:
                    contents = shlex.split(subprocess.check_output(["ls", "-A",
                                                                    directory]))
                    cons = []
                    for name in range(start, end):
                        cons.append(contents[name])
                    return cons
                except subprocess.CalledProcessError:
                    raise kerri.FSError("lcon()")
                except IndexError:
                    raise kerri.OutOfRange("lcon()")
                except Exception as error:
                    raise kerri.Unknown("lcon()", error)

        def inc_con(self, directory, *args):
            """ Incremental Directory Contents Listing
                Useful with tty's and other limited scroll back displays """

            if len(args) >= 1:
                raise kerri.ExcessArguments('inc_con()', 1)
            elif str(os.path.isdir(directory)) == "False":
                raise kerri.FSError('inc_con()')
            else:
                try:
                    stuff = subprocess.check_output(["ls", "-A",
                                                                    directory])
                    contents = stuff.split("/n")
                except subprocess.CalledProcessError:
                    raise kerri.FSError("inc_con()")
                ints = {'a':0, 'b':23}
                while True:
                    try:
                        for name in range(ints['a'], ints['b']):
                            if os.path.isdir("%s/%s" % (directory,
                                                        contents[name])) == True:
                                print(colored(contents[name], 'blue', attrs=['bold']))
                            elif os.access("%s/%s" % (directory,
                                                      contents[name]),
                                                      os.X_OK) == True:
                                print(colored(contents[name], 'red', attrs=['bold']))
                            else:
                                print(colored(contents[name], 'white', attrs=['bold']))
                        for integers in ints:
                            ints[integers] += 25
                    except IndexError:
                        print(colored("""\n### [END] ###""", 'red'))
                        break
                    except KeyboardInterrupt:
                        raise kerri.UsrInt("inc_con()")
                    except Exception as error:
                        raise kerri.Unknown("inc_con()", error)

        def cont_info(self, path=pwd, *args):
            """ Show information about content in a directory """

            if len(args) >= 1:
                raise kerri.ExcessArguments("cont_info()", 1)
            if str(os.path.isdir(path)) == "False":
                raise kerri.FSError('cont_info()')
            else:
                try:
                    contents = subprocess.check_output(["ls", "-ARgh", path])
                    return contents
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFailure('cont_info()')
                except Exception as error:
                    raise kerri.Unknown('cont_info()', error)

        def srem(self, file_name, verbose=1, *args):
            """ Securely remove files generated by your programs
            {THIS WILL FORCE A DELETION. IT WILL NOT ASK FOR
            APPROVAL. * USE WITH CAUTION *}
            [DELETION IS IRREVERSABLE!!!]"""

            if len(args) >= 1:
                raise kerri.ExcessArguments("srem()", 1)
            elif str(os.path.isfile(file_name)) == "False":
                raise kerri.FSError('srem()')
            else:
                try:
                    if verbose == 0:
                        srm = subprocess.Popen(["srm", "-r", file_name],
                                                stdout=subprocess.PIPE,
                                                stderr=subprocess.PIPE)
                        std_out, std_err = srm.communicate()
                    elif verbose == 1:
                        srm = subprocess.Popen(["srm", "-rv", file_name],
                                                stdout=subprocess.PIPE,
                                                stderr=subprocess.PIPE)
                        std_out, std_err = srm.communicate()
                    else:
                        raise kerri.InvalidInput("srem()", "The \'verbose\' parameter must be either a 1{on:default} or a 0{off}")
                    if len(std_out) != 0:
                        return std_out
                    else:
                        if len(std_err) != 0:
                            return std_err
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFailure('srem()')
                except Exception as error:
                    raise kerri.Unknown('srem()', error)

        def rem(self, file_name, *args):
            """ Recursively force deletion of files or directories
                {This will not ask you to approve the deletion. It is
                automatic and silent
                * USE WITH CAUTION *} """

            if len(args) >= 1:
                raise kerri.ExcessArguments("rem()", 1)
            elif str(os.path.isfile(file_name)) == "False":
                raise kerri.FSError('rem()')
            else:
                try:
                    subprocess.call(["rm", "-rf", file_name])
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFailure('rem()')
                except Exception as error:
                    raise kerri.Unknown('rem()', error)

        def mk_dir(self, path, *args):
            """ Creates a directory at specified path """

            if len(args) >= 1:
                raise kerri.ExcessArguments("mk_dir()", 1)
            elif str(os.path.isdir(path)) == "True":
                raise kerri.DuplicationError("mk_dir()", "%s Already Exists!!! Can Not Create Another One!" % path)
            else:
                try:
                    subprocess.call(["mkdir", path])
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFailure('mk_dir')
                except Exception as error:
                    raise kerri.Unknown('mk_dir', error)

        def mdirs(self, path, mode='0777', *args):
            """ Create specified directory and all parent directories needed """

            if len(args) >= 1:
                raise kerri.ExcessArguments('mk_dirs()', 1)
            else:
                try:
                    os.makedirs(path, int(mode))
                except Exception as error:
                    raise kerri.Unknown("mk_dirs()", error)

        def chk_file(self, path, *args):
            """ Check to see if file or directory exists """

            if len(args) >= 1:
                raise kerri.ExcessArguments("chk_file", 1)
            else:
                try:
                    if os.path.exists(path) == True:
                        if os.path.isdir(path):
                            return colored('%s is a directory' % path, 'green', attrs=['bold'])
                        else:
                            return colored('True', 'green', attrs=['bold'])
                    elif os.path.exists(path) == False:
                        return colored('False', 'red', attrs=['bold'])
                    else:
                        return colored('UnKnown', 'yellow', attrs=['bold'])
                except Exception as error:
                    raise kerri.Unknown('chk_file()', error)

        def chk_del(self, *args):
            """ Check for deleted but still open files
            These types of files are not properly
            removed and can easily be recovered by ANYONE """

            if len(args) >= 1:
                raise kerri.ExcessArguments("chk_del()", 0)
            else:
                try:
                    lsof = subprocess.Popen("lsof -s -X".split(),
                                            stdout=subprocess.PIPE)
                    grep = subprocess.Popen("grep deleted".split(),
                                            stdin=lsof.stdout,
                                            stdout=subprocess.PIPE)
                    lsof.stdout.close()
                    output = grep.communicate()[0]
                    lsof.wait()
                    return output
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFailure("chk_del()")
                except Exception as error:
                    raise kerri.Unknown('chk_del()', error)

#   ###################
#   # DISK MANAGEMENT #
#   ###################

    class Disk_Man(object):
        """ Disk Management """

        def __str__(self):
            return """ Controls All Disk Operations Preformed By Kaos """

        def mk_boot(self, dest, source, bs='512K', *args):
            """ Create Bootable Drive With dd """

            if len(args) >= 1:
                raise kerri.ExcessArguments("mk_boot()", 3)
            else:
                try:
                    subprocess.call(["dd", "status=progress", "if=%s" % source,
                                     "of=%s" % dest, "bs=%s" % bs])
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFailure('mk_boot()')
                except Exception as error:
                    raise kerri.Unknown('mk_boot()', error)

        def mount(self, disk, location, *args):
            """ Mount A Disk At Specified Location """

            if len(args) >= 1:
                raise kerri.ExcessArguments("mount()", 2)
            else:
                try:
                    mount = subprocess.Popen(["mount", "%s" % disk,
                                              "%s" % location],
                                              stdout=subprocess.PIPE,
                                              stderr=subprocess.PIPE)
                    std_out, std_err = mount.communicate()
                    if len(std_err) != 0:
                        sys.stderr.write(std_err)
                    if len(std_out) != 0:
                        return std_out
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFailure('mount()')
                except Exception as error:
                    raise kerri.Unknown('mount()', error)

        def memc(self, *args):
            """ Check Disk Usage """

            if len(args) >= 1:
                raise kerri.ExcessArguments("mem()", 0)
            else:
                try:
                    memory_stats = subprocess.Popen(["df", "-ah"],
                                                    stdout=subprocess.PIPE,
                                                    stderr=subprocess.PIPE)
                    std_out, std_err = memory_stats.communicate()
                    if len(std_err) != 0:
                        sys.stderr.write(std_err)
                    if len(std_out) != 0:
                        return std_out
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFailure("memc()")
                except Exception as error:
                    raise kerri.Unknown("memc()", error)

#   ###################
#   # FILE MANAGEMENT #
#   ###################

    class File_Man(object):
        """ Manage File {read/write} Operations """

        def __str__(self):
            return """ Controls All Read/Write File Operations Preformed By Kaos """

        def scribe(self, file_name, message, *args):
            """ Append a line of text to specified file """

            if len(args) >= 1:
                raise kerri.ExcessArguments("scribe()", 2)
            else:
                try:
                    with open(file_name, 'a') as edit:
                        edit.write(message)
                        edit.close()
                except Exception as error:
                    raise kerri.Unknown("scribe()", error)

        def book(self, file_name, *args):
            """ Add Text To A File From A Recursive Loop
                Add A Blank Line To Terminate Loop """

            if len(args) >= 1:
                raise kerri.ExcessArguments("book()", 1)
            else:
                try:
                    print(colored("[*] Add A Blank Line To Stop:\n-----------------------------", 'yellow', attrs=['bold']))
                    index = 0
                    while True:
                        text = raw_input(">>> ")
                        if len(text) >= 1:
                            with open(file_name, 'a') as out:
                                out.write("%s\n" % text)
                                out.close()
                            index += 1
                        else:
                            if index == 0:
                                print(colored("No Data Was Added To %s" % file_name, 'red', attrs=['bold']))
                            else:
                                print(colored("Data Successfully Added To %s" % file_name, 'green', attrs=['bold']))
                            break
                except KeyboardInterrupt:
                    print(" ")
                    sys.stderr.write("Using CTRL^C Could Cause This Function To Have Adverse Side Effects!!!")
                    raise kerri.UsrInt("book()", "You Should Add A Blank Line To Stop book() Instead Of CTRL^C")
                except Exception as error:
                    raise kerri.Unknown("book()", error)

        def alt_scribe(self, file, message, option='a', *args):
            """ Add text to file based on write mode option.
            The default option will append the text """

            if len(args) >= 1:
                raise kerri.ExcessArguments("alt_scribe()", 3)
            else:
                try:
                    with open(file, option) as edit:
                        edit.write(message)
                        edit.close()
                except Exception as error:
                    raise kerri.Unknown("alt_scribe()", error)

        def gander(self, file, *args):
            """ Read a file without adding, removing,
            or changing any of the existing content
            Output is returned as a list """

            if len(args) >= 1:
                raise kerri.ExcessArguments("gander()", 1)
            else:
                try:
                    with open(file, 'r') as read_it:
                        data = read_it.readlines()
                        output = []
                        for item in data:
                            output.append(item.strip())
                        return output
                        read_it.close()
                except IOError:
                    raise kerri.FSError('gander(%s)' % file)
                except Exception as error:
                   raise kerri.Unknown("gander()", error)

        def nano(self, file_name, *args):
            """ Edit A File Using The Nano Editor """

            if len(args) >= 1:
                raise kerri.ExcessArguments("nano()", 1)
            else:
                try:
                    subprocess.call(["nano", file_name])
                    subprocess.call(["clear"])
                except IOError:
                    raise kerri.FSError("nano(%s)" % file_name)
                except Exception as error:
                    raise kerri.Unknown("nano(%s)" % file_name, error)

        def ext_read(self, path, *args):
            """ Read a file using the 'less' program """

            if len(args) >= 1:
                raise kerri.ExcessArguments("ext_read()", 1)
            else:
                try:
                    subprocess.call(["less", path])
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFailure('ext_read()')
                except Exception as error:
                    raise kerri.Unknown('ext_read()', error)

#   #####################
#   # SYSTEM OPERATIONS #
#   #####################

    class Sys_Op(object):
        """ System Operation Management """

        def __str__(self):
            return """ Controls All System Operations Preformed By Kaos """

        def watch_log(self, log_file, refresh_rate, *args):
            if len(args) >= 1:
                raise kerri.ProcessFailure("watch_log()")
            else:
                r_rate = int(refresh_rate)
                try:
                    print("Hit CTRL^C To Quit...")
                    time.sleep(1)
                    subprocess.call(["watch", "-n", str(r_rate), "less",
                                     log_file])
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFailure("watch_log()")
                except TypeError as error:
                    raise kerri.InvalidInput("watch_log()", error)
                except Exception as error:
                    raise kerri.Unknown("watch_log()", error)

        def serv_ls(self, *args):
            """
            List All Available Sevices On The System
            """

            if len(args) >= 1:
                raise kerri.ExcessArguments('serv_chk', 0)
            else:
                try:
                    services = []
                    pipes = subprocess.Popen(["systemctl", "-at", "service"],
                                              stdout=subprocess.PIPE,
                                              stderr=subprocess.PIPE)
                    std_out, std_err = pipes.communicate()
                    if len(std_err) == 0:
#                        data = std_out.replace("     ", "").split("\n")
                        data = std_out.split("\n").strip()
                        for item in data:
                            services.append(item)
                        return services
                except subprocess.CalledProcessError:
                    raise kerri.ProcessError('serv_chk()')
                except Exception as error:
                    raise kerri.Unknown('serv_chk()', error)

        def chmod(self, opts, file_name, *args):
            """ Change permissions of a file """

            if len(args) >= 1:
                raise kerri.ExcessArguments('chmod()', 2)
            else:
                try:
                    if str(os.path.isdir(file_name)) == "False":
                        if str(os.path.isfile(file_name)) == "True":
                            subprocess.Popen(["chmod", opts, file_name])
                        else:
                            raise kerri.FSError('chmod(%s)' % file_name)
                    else:
                        subprocess.Popen(["chmod", opts, file_name])
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFailure('chmod()')
                except Exception as error:
                    if str(os.path.isdir(file_name)) == "False" and str(os.path.isfile(file_name)) == "False":
                        raise kerri.FSError('chmod()')
                    else:
                        raise kerri.Unknown("chmod()", error)

        def chk_out(self, command, *args):
            """
            Checks The Output Of A Shell Command
            """

            if len(args) >= 1:
                raise kerri.ExcessArguments("chk_out()", 1)
            else:
                argus = shlex.split(command)
                try:
                    output = subprocess.check_output(argus)
                    return output
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFailure('chk_out()')
                except Exception as error:
                    raise kerri.Unknown('chk_out()', error)

        def ex(self, command, *args):
            """
            Executes A Shell Command
            """

            if len(args) >= 1:
                raise kerri.ExcessArguments("ex()", 1)
            else:
                argus = shlex.split(command)
                try:
                    output = subprocess.Popen(argus, stdout=subprocess.PIPE,
                                              stderr=subprocess.PIPE)
                    std_out, std_err = output.communicate()
                    if len(std_out) != 0:
                        return std_out
                    else:
                        return std_err
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFailure('ex()')
                except Exception as error:
                    raise kerri.Unknown('ex()', error)

        def silent_ex(self, command, *args):
            """
            Executes A Shell Command
            """

            if len(args) >= 1:
                raise kerri.ExcessArguments("ex()", 1)
            else:
                argus = shlex.split(command)
                try:
                    output = subprocess.Popen(argus, stdout=subprocess.PIPE,
                                              stderr=subprocess.PIPE)
                    std_out, std_err = output.communicate()
                    if len(std_err) != 0:
                        return std_err
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFailure('ex()')
                except Exception as error:
                    raise kerri.Unknown('ex()', error)

        def os_ex(self, command, *args):
            """
            Executes A Shell Command
            """

            if len(args) >= 1:
                raise kerri.ExcessArguments("ex()", 1)
            else:
                try:
                    os.system(command)
                except Exception as error:
                    raise kerri.Unknown('ex()', error)

        def ex_chk(self, path, *args):
            """ Check To See If A File Is Executable """

            if len(args) >= 1:
                raise kerri.ExcessArguments("ex_chk()", 1)
            else:
                status = os.access(path, os.X_OK)
                return status

        def prog_chk(self, program, *args):
            """ Check To See If A Program Is Installed """

            if len(args) >= 1:
                raise kerri.ExcessArguments("prog_chk()", 1)
            else:
                self.status = None
                self.stat_num = None
                try:
                    if str(os.path.isfile("/usr/bin/%s" % program)) == "True":
                        if str(os.access("/usr/bin/%s" % program,
                                         os.X_OK)) == "True":
                            self.stat_num = 1
                            self.status = "Program Is Installed"
                        else:
                            self.stat_num = 0
                            self.status = "The File Exists But Is Not Executable..."
                    else:
                        self.stat_num = 0
                        self.status = "Program Not Installed"

                except OSError as e:
                    if e.errno == 2:
                        self.stat_num = 0
                        self.status = "Program Not Installed"
                    else:
                        self.stat_num = 2
                        self.status = "Program Installation Status Unknown"
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFailure('prog_chk()')
                except Exception as error:
                    raise kerri.Unknown('prog_chk()', error)
                return "[%i]: %s" % (self.stat_num, self.status)

        def pac_install(self, app, silent='Y', *args):
            """ Install Application Using PacMan """

            if len(args) >= 1:
                raise kerri.ExcessArguments("pac_install()", 1)
            if silent != "N" and silent != "n" and silent != "Y" and silent != "y":
                raise kerri.InvalidInput("pac_install()", "silent can only be \"Y\" or \"N\" ")
            else:
                try:
                    pipes = subprocess.Popen(["pacman", "--noconfirm", "-S",
                                              app], stdout=subprocess.PIPE,
                                              stderr=subprocess.PIPE)
                    std_out, std_err = pipes.communicate()
                    if silent == "N" or silent == "n":
                        return std_out
                    else:
                        pass
                except OSError:
                    raise kerri.FSError('pac_install', "\'pacman\' Does Not Appear To Be Installed On This System!")
                except KeyboardInterrupt:
                    raise kerri.UsrInt("pac_install()")
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFailure('pac_install()')
                except Exception:
                    raise kerri.Unknown('pac_install()', std_err)


        def apt_install(self, app, silent='Y', *args):
            """ Install Application Using Apt """

            if len(args) >= 1:
                raise kerri.ExcessArguments("apt_install()", 1)
            if silent != "N" and silent != "n" and silent != "Y" and silent != "y":
                raise kerri.InvalidInput("apt_install()", "silent can only be \"Y\" or \"N\" ")
            else:
                try:
                    pipes = subprocess.Popen(["apt-get", "install", app],
                                              stdout=subprocess.PIPE,
                                              stderr=subprocess.PIPE)
                    std_out, std_err = pipes.comminucate()
                    if silent == "N" or silent == "n":
                        return std_out
                    else:
                        pass
                except OSError:
                    raise kerri.FSError('apt_install', "\'apt\' Does Not Appear To Be Installed On This System!")
                except KeyboardInterrupt:
                    raise kerri.UsrInt("apt_install()")
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFailure('apt_install()')
                except Exception as error:
                    raise kerri.Unknown('apt_install', error)


        def pip_install(self, mod, silent='Y', *args):
            """ Install a python module or program with pip """

            if len(args) >= 1:
                raise kerri.ExcessArguments('pip_install()', 1)
            if silent != "N" and silent != "n" and silent != "Y" and silent != "y":
                raise kerri.InvalidInput("pip_install()", "silent can only be \"Y\" or \"N\" ")
            else:
                try:
                    pipes = subprocess.Popen(["pip", "install", mod],
                                              stdout=subprocess.PIPE,
                                              stderr=subprocess.PIPE)
                    std_out, std_err = pipes.communicate()
                    if silent == "N" or silent == "n":
                        return std_out
                    else:
                        pass
                except OSError:
                    raise kerri.FSError('pip_install', "\'pip\' Does Not Appear To Be Installed On This System!")
                except KeyboardInterrupt:
                    raise kerri.UsrInt("pip_install()")
                except subprocess.CalledProcessError:
                    raise kerri.ProcessFailure('pip_install()')
                except Exception as error:
                    raise kerri.Unknown('pip_install', error)

#   #######################
#   # CSV FILE OPERATIONS #
#   #######################
    class CSV(object):
        """ Manipulate CSV Files """

        def __str__(self):
            return """ Controls All CSV File Manipulation Preformed By Kaos """

        def read_cols(self, csv_file, key_col, val_1, val_2=None, val_3=None, val_4=None, val_5=None, val_6=None, val_7=None, val_8=None, val_9=None, *args):
            """ Return (up to 10) columns from a CSV file
                IF YOU ARE USING THIS TO EVALUATE AN AIRLOG FILE,
                THE COLUMN FORMAT IS:

                [0]:BSSID, [1]:First Time Seen, [2]:Last Time Seen
                [3]:Channel, [4]:Speed, [5]:Privacy, [6]:Cipher
                [7]:Authentication, [8]:Power, [9]:# of Beacons
                [10]:# IV, [11]:LAN IP, [12]:ID-Length
                [13]:ESSID, [14]:Key """

            if len(args) >= 1:
                raise kerri.ExcessArguments("read_cols()", 10)
            else:
                try:
                    with open(csv_file) as csvf:
                        reader = csv.reader(csvf)
                        output = {}
                        for row in reader:
                            try:
                                if val_1 != None and val_2 == None and val_3 == None and val_4 == None and val_5 == None and val_6 == None and val_7 == None and val_8 == None and val_9 == None:
                                    output[str(row[key_col])] = row[val_1]
                                elif val_1 != None and val_2 != None and val_3 == None and val_4 == None and val_5 == None and val_6 == None and val_7 == None and val_8 == None and val_9 == None:
                                    output[str(row[key_col])] = (row[val_1], row[val_2])
                                elif val_1 != None and val_2 != None and val_3 != None and val_4 == None and val_5 == None and val_6 == None and val_7 == None and val_8 == None and val_9 == None:
                                    output[str(row[key_col])] = (row[val_1], row[val_2], row[val_3])
                                elif val_1 != None and val_2 != None and val_3 != None and val_4 != None and val_5 == None and val_6 == None and val_7 == None and val_8 == None and val_9 == None:
                                    output[str(row[key_col])] = (row[val_1], row[val_2], row[val_3], row[val_4])
                                elif val_1 != None and val_2 != None and val_3 != None and val_4 != None and val_5 != None and val_6 == None and val_7 == None and val_8 == None and val_9 == None:
                                    output[str(row[key_col])] = (row[val_1], row[val_2], row[val_3], row[val_4], row[val_5])
                                elif val_1 != None and val_2 != None and val_3 != None and val_4 != None and val_5 != None and val_6 != None and val_7 == None and val_8 == None and val_9 == None:
                                    output[str(row[key_col])] = (row[val_1], row[val_2], row[val_3], row[val_4], row[val_5], row[val_6])
                                elif val_1 != None and val_2 != None and val_3 != None and val_4 != None and val_5 != None and val_6 != None and val_7 != None and val_8 == None and val_9 == None:
                                    output[str(row[key_col])] = (row[val_1], row[val_2], row[val_3], row[val_4], row[val_5], row[val_6], row[val_7])
                                elif val_1 != None and val_2 != None and val_3 != None and val_4 != None and val_5 != None and val_6 != None and val_7 != None and val_8 != None and val_9 == None:
                                    output[str(row[key_col])] = (row[val_1], row[val_2], row[val_3], row[val_4], row[val_5], row[val_6], row[val_7], row[val_8])
                                elif val_1 != None and val_2 != None and val_3 != None and val_4 != None and val_5 != None and val_6 != None and val_7 != None and val_8 != None and val_9 != None:
                                    output[str(row[key_col])] = (row[val_1], row[val_2], row[val_3], row[val_4], row[val_5], row[val_6], row[val_7], row[val_8], row[val_9])
                                else:
                                    raise kerri.ProcessFailure("read_cols()")
                            except IndexError:
                                return output
                                pass
                except Exception as error:
                    raise kerri.Unknown("read_cols()", error)

#########
# INITs #
#########

ksys = System()
op_sys = ksys.op_sys
get_host = ksys.get_host
get_user = ksys.get_user

hware = ksys.Hardware()
battery = hware.battery
shutdown = hware.shutdown

m_audio = hware.MicroAudio()
record = m_audio.record
play = m_audio.play
tonegen = m_audio.tonegen
static = m_audio.static

fsman = ksys.FS_Man()
cd = fsman.cd
dcon = fsman.dcon
rcon = fsman.rcon
inc_con = fsman.inc_con
cont_info = fsman.cont_info
srem = fsman.srem
rem = fsman.rem
mkdir = fsman.mk_dir
mdirs = fsman.mdirs
chk_file = fsman.chk_file
chk_del = fsman.chk_del

dman = ksys.Disk_Man()
mk_boot = dman.mk_boot
mount = dman.mount
memc = dman.memc

fman = ksys.File_Man()
scrbe = fman.scribe
book = fman.book
alt_scribe = fman.alt_scribe
gander = fman.gander
nano = fman.nano
ext_read = fman.ext_read

sys_op = ksys.Sys_Op()
watch_log = sys_op.watch_log
serv_ls = sys_op.serv_ls
chmod = sys_op.chmod
chk_out = sys_op.chk_out
os_ex = sys_op.os_ex
ex = sys_op.chk_out
ex_chk = sys_op.ex_chk
prog_chk = sys_op.prog_chk
pac_install = sys_op.pac_install
apt_install = sys_op.apt_install
pip_install = sys_op.pip_install

csv = ksys.CSV()
read_cols = csv.read_cols
