#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created: Aug 2017

    @author: D34D9001@9R0GR4M13
"""
import kerri
import os
import subprocess
import symbo
import sys
import random
import requests
import webbrowser
from bs4 import BeautifulSoup as bs
from termcolor import colored

######################
# FAKE ID GENERATION #
######################

class FakeID(object):
    """ This class gets information from http://www.fakenamegenerator.com
        to generate a completely usable fake id quickly """

    global nameset
    nameset = {"American":"us", "Arabic":"ar", "Brazil":"br", "Chechen":"celat",
               "Chinese":"ch", "Chinese-Traditional":"zhtw", "Croation":"hr",
               "Czech":"cs", "Danish":"dk", "Dutch":"nl", "England Wales":"en",
               "Eritrean":"er", "Finnish":"fi", "French":"fr", "German":"gr",
               "Greenland":"gl", "Hispanic":"sp", "Hobbit":"hobbit",
               "Hungarian":"hu", "Icelandic":"is", "Igbo":"ig", "Italian":"it",
               "Japanese":"jpja", "Japanese-Anglicized":"jp", "Ninja":"ninja",
               "Norwegian":"no", "Persian":"fa", "Polish":"pl", "Russian":"ru",
               "Russian-Cyrillic":"rucyr", "Scottish":"gd", "Slovenian":"sl",
               "Swedish":"sw", "Thai":"th", "Vietnamese":"vn"}

    global country
    country = {"Australia":"au", "Austria":"as", "Belgium":"bg", "Brazil":"br",
               "Canada":"ca", "Cyprus Anglicized":"cyen", "Cyprus Greek":"cygk",
               "Czech Republic":"cz", "Denmark":"dk", "Estonia":"ee", "Finland":"fi",
               "France":"fr", "Germany":"gr", "Greenland":"gl", "Hungarian":"hu",
               "Iceland":"is", "Italy":"it", "Netherlands":"nl", "New Zealand":"nz",
               "Norway":"no", "Poland":"pl", "Portugal":"pt", "Slovenia":"sl",
               "South Africa":"za", "Spain":"sp", "Sweden":"sw", "Switzerland":"sz",
               "Tunisia":"tn", "United Kingdom":"uk", "United States":"us",
               "Uruguay":"uy"}

    def __str__(self):
        return """ Controls Kaos' FakeID Generation Operations """

    def id_gen(self, nset=nameset["American"], cntry=country["United States"], sex="random", out=None, *args):
        """ Generate a fake id """

        if len(args) >= 1:
            raise kerri.ExcessArguments("id_gen()", 4)
        else:
            def srem_temp():
                """ Deletes temporary files created by id_gen() """
                if str(os.path.isfile("/tmp/fakeid")) == "False":
                    pass
                else:
                    subprocess.call(["srm", "-f", "/tmp/fakeid"])
                if str(os.path.isfile("/tmp/fakemail")) == "False":
                    pass
                else:
                    subprocess.call(["srm", "-f", "/tmp/fakemail"])
                if str(os.path.isfile("/tmp/fakessn")) == "False":
                    pass
                else:
                    subprocess.call(["srm", "-f", "/tmp/fakessn"])
                if str(os.path.isfile("/tmp/numfile")) == "False":
                    pass
                else:
                    subprocess.call(["srm", "-f", "/tmp/numfile"])

        fake_init2 = open("/tmp/fakeid", 'w')
        fake_init2.write("Started\n")
        fake_init2.close()
        if nset != nameset["American"]:
            try:
                name_set = nameset[nset]
                nset = name_set
            except KeyError:
                sys.stderr.write("%s is not a valid nameset option...\nUsing default option instead...\n" % nset)
                nset = nameset["American"]
        fake_init2 = open("/tmp/fakeid", 'a')
        fake_init2.write("Nameset Set\n")
        fake_init2.close()
        if cntry != country["United States"]:
            try:
                home_land = country[cntry]
                cntry = home_land
            except KeyError:
                sys.stderr.write("%s is not a valid country option...\nUsing default option instead...\n" % cntry)
        fake_init2 = open("/tmp/fakeid", 'a')
        fake_init2.write("Country Set\n")
        fake_init2.close()
        id_sex = sex.lower()
        sex = id_sex
        if sex != "male" and sex != "female" and sex != "random":
            sys.stderr.write("%s is not a valid sex option...\nUsing default option instead...\n" % sex)
            sex = "random"
        if out == None:
            try:
                data = []
                headers = {"User-Agent": "my web scraping program. contact me at admin@domain.com"}
                page = requests.get("https://www.fakenamegenerator.com/gen-%s-%s-%s.php" % (sex, nset, cntry), headers=headers)
                soup = bs(page.content, 'html.parser')
                fake_init2 = open("/tmp/fakeid", 'a')
                fake_init2.write("Website Found\n")
                fake_init2.close()
                list = soup.find_all('div', class_='info')[0].get_text().rstrip()
                fake_init2 = open("/tmp/fakeid", 'a')
                fake_init2.write("List Created\n")
                fake_init2.close()
                try:
                    link = soup.find_all('div', class_='adtl')[1]
                    fake_init2 = open("/tmp/fakeid", 'a')
                    fake_init2.write("Links Found\n")
                    fake_init2.close()
                except IndexError as error:
                    return "THERE WAS A PROBLEM! \n PLEASE SELECT DIFFERENT OPTIONS AND TRY AGAIN"
                info = list.strip()
                fake_init = open("/tmp/fakeid", 'w')
                fake_init.write("\n")
                fake_init.close()
                fakefile = open("/tmp/fakeid", 'a')
                fakefile.write("%s" % info)
                fakefile.close()
                try:
                    with open("/tmp/fakemail", 'w') as fakemail:
                        fakemail.write(str(link))
                        fakemail.close()
                except Exception as error:
                    return error

                finance = subprocess.check_output(["grep", "-A", "12", "-i", "finance", "/tmp/fakeid"])
                birthday = subprocess.check_output(["grep", "-A", "9", "-i", "birthday", "/tmp/fakeid"])
                name = subprocess.check_output(["sed", "-n", "2p", "/tmp/fakeid"])
                address = subprocess.check_output(["sed", "-n", "4p", "/tmp/fakeid"])
                adr = address.strip()
                maiden = subprocess.check_output(["grep", "-A", "1", "-i", "mother", "/tmp/fakeid"])
                phone = subprocess.check_output(["grep", "-A", "5", "-i", "phone", "/tmp/fakeid"])
                online = subprocess.check_output(["grep", "-A", "19", "Online", "/tmp/fakeid"])
                employment = subprocess.check_output(["grep", "-A", "7", "Employment", "/tmp/fakeid"])
                charics = subprocess.check_output(["grep", "-A", "11", "Physical", "/tmp/fakeid"])
                tracking = subprocess.check_output(["grep", "-A", "11", "Tracking", "/tmp/fakeid"])
                color = subprocess.check_output(["grep", "-A", "2", "Favorite", "/tmp/fakeid"])
                vehicle = subprocess.check_output(["grep", "-A", "2", "Vehicle", "/tmp/fakeid"])
                guid = subprocess.check_output(["grep", "-A", "2", "GUID", "/tmp/fakeid"])
                geo = subprocess.check_output(["grep", "-A", "1", "Geo", "/tmp/fakeid"])
#                print "%s\n%s" % (symbo.SEP, symbo.SEP)
#                print "Name: %s" % name
                data.append("%s" % name.decode())
#                print symbo.SEP
#                print "SSN:"
                os.system("grep -o -P '.{0,0}SSN.{0,11}' /tmp/fakeid | cut -f2- -dN | head -1 > /tmp/fakessn")
                social = subprocess.check_output(["cat", "/tmp/fakessn"])
                if len(social) > 3:
                    social = social[:7]
#                    os.system("echo $((1000 + RANDOM % 9999)) > /tmp/numfile")
#                    end = subprocess.check_output(["cat", "/tmp/numfile"])
                    end = random.randint(1000,9999)
                    ssn = social.decode() + str(end)
#                    print ssn
                    data.append("SSN: %s" % ssn)
                else:
#                    print "N/A"
                    data.append("N/A")
#                    print symbo.SEP
#                print "Address: %s" % adr
                data.append("%s\n" % adr.decode())
#                print symbo.SEP
#                print geo
                data.append("%s" % geo.decode())
#                print symbo.SEP
#                print phone
                data.append("%s" % phone.decode())
#                print symbo.SEP
#                print birthday
                data.append("%s" % birthday.decode())
#                print symbo.SEP
#                print charics
                data.append("%s" % charics.decode())
#                print symbo.SEP
#                print color
                data.append("%s" % color.decode())
#                print symbo.SEP
#                print "%s" % maiden
                data.append("%s" % maiden.decode())
#                print symbo.SEP
#                print vehicle
                data.append("%s" % vehicle.decode())
#                print symbo.SEP
#                print employment
                data.append("%s" % employment.decode())
#                print symbo.SEP
#                print finance
                data.append("%s" % finance.decode())
#                print symbo.SEP
#                print online
                data.append("%s" % online.decode())
#                print colored("[*] Here Is The Link To Your Email [*]", symbo.out_color, attrs=['bold'])
#                try:
#                    os.system("""grep -Eoi '<a [^>]+>' /tmp/fakemail | grep  -Eo 'href="[^\"]+"'""")
#                except Exception:
#                    print colored("N/A: ", symbo.out_color, attrs=['bold'])
#                print symbo.SEP
#                print tracking
                data.append("%s" % tracking.decode())
#                print symbo.SEP
#                print guid
                data.append("%s" % guid.decode())
#                print symbo.SEP
                complete_data = ""
                for item in data:
                    complete_data = complete_data + "%s \n" % item
#                srem_temp()
                return complete_data
            except requests.ConnectionError:
                raise kerri.INetFailure("id_gen()")
            except Exception as error:
                return error
        else:
            try:
                page = requests.get("https://www.fakenamegenerator.com/gen-%s-%s-%s.php" % (sex, nset, cntry))
                soup = bs(page.content, 'html.parser')
                list = soup.find_all('div', class_='info')[0].get_text().rstrip()
                try:
                    link = soup.find_all('div', class_='adtl')[1]
                except IndexError as error:
                    raise error
                info = list.strip()
                with open("/tmp/fakeid", 'w') as fakefile:
                    fakefile.write("%s" % info)
                    fakefile.close()
                try:
                    with open("/tmp/fakemail", 'w') as fakemail:
                        fakemail.write(str(link))
                        fakemail.close()
                except Exception as error:
                    raise error

                finance = subprocess.check_output(["grep", "-A", "12", "-i", "finance", "/tmp/fakeid"])
                birthday = subprocess.check_output(["grep", "-A", "9", "-i", "birthday", "/tmp/fakeid"])
                name = subprocess.check_output(["sed", "-n", "1p", "/tmp/fakeid"])
                address = subprocess.check_output(["sed", "-n", "4p", "/tmp/fakeid"])
                adr = address.strip()
                maiden = subprocess.check_output(["grep", "-A", "1", "-i", "mother", "/tmp/fakeid"])
                phone = subprocess.check_output(["grep", "-A", "5", "-i", "phone", "/tmp/fakeid"])
                online = subprocess.check_output(["grep", "-A", "19", "Online", "/tmp/fakeid"])
                employment = subprocess.check_output(["grep", "-A", "7", "Employment", "/tmp/fakeid"])
                charics = subprocess.check_output(["grep", "-A", "11", "Physical", "/tmp/fakeid"])
                tracking = subprocess.check_output(["grep", "-A", "11", "Tracking", "/tmp/fakeid"])
                color = subprocess.check_output(["grep", "-A", "2", "Favorite", "/tmp/fakeid"])
                vehicle = subprocess.check_output(["grep", "-A", "2", "Vehicle", "/tmp/fakeid"])
                guid = subprocess.check_output(["grep", "-A", "2", "GUID", "/tmp/fakeid"])
                geo = subprocess.check_output(["grep", "-A", "1", "Geo", "/tmp/fakeid"])
                with open("%s/%s" % (out, name.rstrip()), 'w') as kfile:
                    kfile.write("%s\n%s\n" % (symbo.SEP, symbo.SEP))
                    kfile.write("Name: %s\n" % name)
                    kfile.write("%s\n" % symbo.SEP)
                    kfile.write("SSN:\n")
                    os.system("grep -o -P '.{0,0}SSN.{0,11}' /tmp/fakeid | cut -f2- -dN | head -1 > /tmp/fakessn")
                    social = subprocess.check_output(["cat", "/tmp/fakessn"])
                    if len(social) > 3:
                        social = social[:7]
#                        os.system("echo $((1000 + RANDOM % 9999)) > /tmp/numfile")
                        last4 = ''.join(random.sample('0123456789', 4))
                        with open("/tmp/numfile", 'w') as outfile:
                            outfile.write(int(last4))
                            outfile.close()
                        end = subprocess.check_output(["cat", "/tmp/numfile"])
                        ssn = str(social) + str(end)
                        kfile.write("%s\n" % ssn)
                    else:
                        kfile.write("N/A\n")
                    kfile.write("%s\n" % symbo.SEP)
                    kfile.write("Address: %s\n" % adr)
                    kfile.write("%s\n" % symbo.SEP)
                    kfile.write("%s\n" % geo)
                    kfile.write("%s\n" % symbo.SEP)
                    kfile.write("%s\n" % phone)
                    kfile.write("%s\n" % symbo.SEP)
                    kfile.write("%s\n" % birthday)
                    kfile.write("%s\n" % symbo.SEP)
                    kfile.write("%s\n" % charics)
                    kfile.write("%s\n" % symbo.SEP)
                    kfile.write("%s\n" % color)
                    kfile.write("%s\n" % symbo.SEP)
                    kfile.write("%s\n" % maiden)
                    kfile.write("%s\n" % symbo.SEP)
                    kfile.write("%s\n" % vehicle)
                    kfile.write("%s\n" % symbo.SEP)
                    kfile.write("%s\n" % employment)
                    kfile.write("%s\n" % symbo.SEP)
                    kfile.write("%s\n" % finance)
                    kfile.write("%s\n" % symbo.SEP)
                    kfile.write("%s\n" % online)
                    kfile.write("[*] Here Is The Link To Your Email [*]\n")
                    try:
#                        os.system("""grep -Eoi '<a [^>]+>' /tmp/fakemail | grep  -Eo 'href="[^\"]+"'""") # This will only print the email to stdout. It will not write it to the file
                        new_name = name.lower().replace(" ", "").replace(".", "")
                        providers = ('dayrep.com', 'armyspy.com', 'cuvox.de', 'einrot.com', 'fleckens.hu', 'gustr.com', 'jourrapide.com', 'rhyta.com', 'supperito.com', 'teleworm.us')
                        email_address = "%s/%s" % (str(random.choice(providers)), new_name)
                        kfile.write("https://fakemailgenerator.com/#/%s" % email_address)
                    except Exception:
                        kfile.write("N/A\n")
                    kfile.write("%s\n" % symbo.SEP)
                    kfile.write("%s\n" % tracking)
                    kfile.write("%s\n" % symbo.SEP)
                    kfile.write("%s\n" % guid)
                    kfile.write("%s\n" % symbo.SEP)
                    kfile.close()

            except requests.ConnectionError:
                raise kerri.INetFailure("id_gen()")
            except subprocess.CalledProcessError:
                raise kerri.ProcessFailure("id_gen()")
            except Exception as error:
                pass

#        try:
#            srem_temp()
#        except subprocess.CalledProcessError:
#            sys.stderr.write(str("%s\nCould Not Remove Temp Files" % symbo.SEP))
#            return
#        except Exception as error:
#            sys.stderr.write(str("%s\nCould Not Remove Temp Files: %s %s" % (symbo.SEP, symbo.E_Sym, error)))
#            return

    def id_gen_opts(self, *args):
        """ Lists options available to use with id_gen() """

        if len(args) >= 1:
            raise kerri.ExcessArguments("id_gen_opts()", 0)
        else:
            nameset_list = nameset.keys()
            country_list = country.keys()
#            print colored("\nAvailable NameSets:", symbo.out_color, attrs=['bold'])
#            print colored("%s\n%s\n" % (nameset_list, symbo.SEP), symbo.alt_color, attrs=['bold'])
#            print colored("Available Countries:", symbo.out_color, attrs=['bold'])
#            print colored("%s\n%s\n" % (country_list, symbo.SEP), symbo.alt_color, attrs=['bold'])
#            print colored("Sex: {male} || {female} || {random}", symbo.out_color, attrs=['bold'])
            avail_opts = "NAMESETS:\n"
            for item in nameset_list:
                avail_opts = avail_opts + "%s  | " % item
            avail_opts = avail_opts + "\n\nCOUNTRIES:\n"
            for item in country_list:
                avail_opts = avail_opts + "%s | " % item
            return avail_opts

    def chk_fkmail(self, email, *args):
        """ Check Email Created By FakeID """
        if len(args) > 1:
            raise kerri.ExcessArguments("chk_fkmail()", 1)
        else:
            addr = str(email)
            ext = addr.split('@')[1]
            un = addr.split('@')[0]
#            print("ext: %s\nun: %s" % (ext, un))
#            webbrowser.get("/usr/bin/chromium-nosand").open("http://www.fakemailgenerator.com/#/%s/%s/" % (ext, un))


#            os.system("/usr/bin/chromium --no-sandbox http://www.fakemailgenerator.com/#/%s/%s/" % (ext, un))

#            os.system("/usr/bin/firefox http://www.fakemailgenerator.com/#/%s/%s/" % (ext, un))
            subprocess.Popen(["/usr/bin/firefox", "http://www.fakemailgenerator.com/#/%s/%s/" % (ext, un)])
#########
# INITs #
#########

fakeid = FakeID()
id_gen = fakeid.id_gen
id_gen_opts = fakeid.id_gen_opts
check_fmail = fakeid.chk_fkmail
