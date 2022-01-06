#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created: Aug 2017

    @author: 73RM1N41@9R0GR4M13
"""
import os
import random  # Used to generate a random name for Tk() objects
import string  # Used to generate a random name for Tk() objects
import tkinter as tk  # Used to create the gui
from tkinter import ttk
import subprocess
from PIL import Image as pImage
from PIL import ImageTk as pitk
from tkinter import *  # Used to create the gui
from tkinter import messagebox  # Used to create message boxes
import anon, ap_maker, konst, ksys, fakeid, iface, recon, spyder, stalker  # used for Kaos functions within the gui app
import playbook as pb
import requests
from bs4 import BeautifulSoup as bs


# These fields are used for config of Kaos functions later in the program
tfields = konst.tfields
device_info = konst.device_info
site_info = konst.site_info
tshark_fields = konst.tshark_fields


class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.Canvas(self, width=995, height = 250)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        s = ttk.Style()
        s.configure('default.TFrame', background='#000000')
        self.scrollable_frame = ttk.Frame(canvas, style="default.TFrame")

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")


def save_file(data):
    def get_data(winName, _data):
        window = winName
        fname = info.get()
        try:
            ksys.scrbe(fname, _data)
            window.destroy()

        except Exception as error:
            window.destroy()
            msgbx("ERROR", error)

    _data = data
    newWin = Toplevel()
    newWin.geometry("500x100")
    newWin.title("Save File")
    newWin.configure(background='black')
    info = Label(newWin, text = "Save As: ", bg="black", fg="lime")
    info.place(x = 15, y = 10)
    info = StringVar()
    info_entry = Entry(newWin, textvariable = info, width = "30", bg="black", fg="lime")
    info_entry.insert(0, "ex: /home/Documents/doc.txt")
    info_entry.bind("<Button-1>", lambda event: clear_entry(event, info_entry))
    info_entry.place(x = 150, y = 10)
    b1 = Button(newWin, text="Save", bg="black", fg="lime",
                command=lambda : get_data(newWin, _data))
    b1.place(x=15,y=55)
    b2 = Button(newWin, text="Cancel", bg="black", fg="lime",
                command=newWin.destroy)
    b2.place(x=150, y=55)


root = Tk()  # Main window for Kaos

try:
    logo = PhotoImage(file=konst.logo_loc)
except Exception as error:
    print("%s" % error)
    print("The Kaos Logo Failed To Load...\n Kali Logo Will Be Used Instead!")
    logo = PhotoImage(file=konst.logo_loc_bak)

root.geometry("650x375+1+1")

# KAOS VERSION
root.title(konst.KAOS_VERSION)  # Title for main window

# Create Frames

topFrame = Frame(root) #, highlightbackground="lime", highlightcolor="lime", highlightthickness=3, width=100, height=100, bd= 0)
topFrame.configure(bg="black")
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

leftFrame = Frame(root)
leftFrame.pack(side=LEFT)

rightFrame = Frame(root)
rightFrame.pack(side=RIGHT)


def donothing():
        x = 0


def msgbx(title, message):
    messagebox.showinfo(title, message)


def msgbx2():
    msgbx("`(:", "It Worked!!!\nGreat Job!!!")

def dev_msgbx():
    messagebox.showinfo("DISABLED", "THIS FUNCTION HAS BEEN DISABLED BY THE DEVELOPER.")

def rand_nm(length=7):
    return ''.join(random.choice(string.ascii_lowercase +
                                 string.digits) for _ in range(length))


def clear_entry(event, entry):
    entry.delete(0, END)

# ANON
###########################################################################################
def anon_main():

    def histoclr(nWin):
    #    msgbx("WARNING", "This will clear the \'/root/.bash_history\' file and wipe all history currently stored")
        msgbx("WARNING", "THIS FUNCTION DOES NOT CURRENTLY WORK CORRRECTLY")
        b1 = Button(root, text="Clear \'/root/.bash_history\'", bg="black",
                    fg="lime", command=donothing)
        b1.pack(side=LEFT, padx=5, pady=5)
        b2 = Button(root, text='Cancel', bg="black", fg="lime", command=root.quit)
        b2.pack(side=LEFT, padx=5, pady=5)


    def watergate(nWin):
        for widget in topFrame.winfo_children():
            widget.destroy()
        msgbx("WARNING", "This will permenantly delete important log files. If this is what you want to do, please be sure to double check that all expected files were removed")
        b1 = Button(root, text='W193 7H47 5H17!', bg="black", fg="lime",
                    command=donothing)
        b1.pack(side=LEFT, padx=5, pady=5)
        b2 = Button(root, text='Hell Nah Dude!', bg="black", fg="lime",
                    command=root.quit)
        b2.pack(side=LEFT, padx=5, pady=5)


    def blkhole(nWin):
        msgbx("WARNING", "This will send all future bash commands to \'/dev/null\' instead of \'/root/.bash_history\'")
        b1 = Button(root, text="Send All CMDs to \'/dev/null\'", bg="black",
                    fg="lime", command=donothing)
        b1.pack(side=LEFT, padx=5, pady=5)
        b2 = Button(root, text='Cancel', bg="black", fg="lime", command=root.quit)
        b2.pack(side=LEFT, padx=5, pady=5)


    def anoid(nWin):
        msgbx("ANOID", "This will start Anoid from the Kaos module")
        b1 = Button(root, text="Start Anoid", bg="black", fg="lime",
                    command=anon.anoid)
        b1.pack(side=LEFT, padx=5, pady=5)
        b2 = Button(root, text='Cancel', bg="black", fg="lime", command=root.quit)
        b2.pack(side=LEFT, padx=5, pady=5)


# Chk_Fkmail

    def ck_fmail(winName):
        def check_mail(winName):
            email = info.get()
            winName.destroy()
            fakeid.check_fmail(email)

        winName = Toplevel()
        winName.geometry("500x95+1+1")
        winName.title("Fakemail")
        winName.attributes('-topmost', True)
        winName.configure(background="black")
        msg = Label(winName, text = "Enter The Email Address Generated By FakeID", bg="black", fg="lime")
        info = Label(winName, text = "Email Address: ", bg="black", fg="lime")
        msg.place(x = 15, y = 10)
        info.place(x = 15, y = 30)
        info = StringVar()
        info_entry = Entry(winName, textvariable = info, width = "30", bg="black", fg="lime")
        info_entry.place(x = 150, y = 30)
        b1 = Button(winName, text="See Email", bg="black", fg="lime",
                    command=lambda : check_mail(winName))
        b1.place(x=15,y=55)
        b2 = Button(winName, text="Cancel", bg="black", fg="lime",
                    command=winName.destroy)
        b2.place(x=150, y=55)

    def _fakeid(nWin):
        def save_id_file(data):
            def get_data(winName, id_info):
                window = winName
                fname = info.get()
                ksys.scrbe(fname, id_info)
                window.destroy()
            id_data = data
            newWin = Toplevel()
            newWin.geometry("500x100")
            newWin.title("Save FakeID")
            newWin.configure(background='black')
            info = Label(newWin, text = "Save As: ", bg="black", fg="lime")
            info.place(x = 15, y = 10)
            info = StringVar()
            info_entry = Entry(newWin, textvariable = info, width = "30", bg="black", fg="lime")
            info_entry.insert(0, "ex: /home/Documents/fake_id.txt")
            info_entry.bind("<Button-1>", lambda event: clear_entry(event, info_entry))
            info_entry.place(x = 150, y = 10)
            b1 = Button(newWin, text="Save ID", bg="black", fg="lime",
                        command=lambda : get_data(newWin, id_data))
            b1.place(x=15,y=55)
            b2 = Button(newWin, text="Cancel", bg="black", fg="lime",
                        command=newWin.destroy)
            b2.place(x=150, y=55)
        def get_id(winName):
            name_set = nset.get()
            country_name = country.get()
            sex = _sex.get()
            winName.destroy()
            optWin.destroy()
            try:
                output = fakeid.id_gen(name_set, country_name, sex)
            except Exception:
                print("[!] There Was An Error With Your Options...\nDefault Options Being Used")
                output = fakeid.id_gen("American", "United States", "random")
            newWin = Toplevel()
            newWin.geometry("500x500+1-1")
            newWin.title("FakeID")

            menubar = Menu(root)
            savemenu = Menu(menubar, tearoff=0)
            savemenu.add_command(label="Save ID", command=lambda: save_id_file(output))
            menubar.add_cascade(label="File", menu=savemenu)

            emailmenu = Menu(menubar, tearoff=0)
            emailmenu.add_command(label="Check Email", command=lambda: ck_fmail(newWin))
            menubar.add_cascade(label="Email", menu=emailmenu)

            newWin.configure(background='black', menu=menubar)

            T = Text(newWin, height=750, width=350, bg="black", fg="lime")
            T.pack()
            T.insert(END, output)
        def killWins():
            winName.destroy()
            optWin.destroy()

        winName = Toplevel()
        winName.title("FakeID")
        winName.geometry("500x120+1+1")
        winName.attributes('-topmost', True)
        winName.config(background="black")

        nset = Label(winName, text = "NameSet: ", bg="black", fg="lime")
        country = Label(winName, text = "Country: ", bg="black", fg="lime")
        _sex = Label(winName, text = "Sex: ", bg="black", fg="lime")

        nset.place(x = 15, y = 10)
        country.place(x = 15, y = 30)
        _sex.place(x = 15, y = 50)

        nset = StringVar()
        country = StringVar()
        _sex = StringVar()

        nset_entry = Entry(winName, textvariable = nset, width = "30", bg="black", fg="lime")
        country_entry = Entry(winName, textvariable = country, width = "30", bg="black", fg="lime")
        _sex_entry = Entry(winName, textvariable = _sex, width = "30", bg="black", fg="lime")

        nset_entry.place(x = 150, y = 10)
        country_entry.place(x = 150, y = 30)
        _sex_entry.place(x = 150, y = 50)

        optWin = Tk()
        optWin.geometry("500x530+1-1")
        optWin.title("Options")
    #    optWin.attributes('-topmost', True)
        optWin.config(background="black")
        output = fakeid.id_gen_opts()

        T = Text(optWin, height=750, width=350, bg="black", fg="lime")
        T.pack()
        T.insert(END, output)

        b1 = Button(winName, text="Generate FakeID", bg="black", fg="lime",
                    command=lambda : get_id(winName))
        b1.place(x=150, y = 75)
        b2 = Button(winName, text='Cancel', bg="black", fg="lime",
                    command=killWins)
        b2.place(x = 350, y = 75)

    def dishis(nWin):
        def disable_history():
            MsgBox = tk.messagebox.askquestion ('Continue?','THIS FUNCTION MAY NOT WORK AS EXPECTED!!!\nThis Will Disable The Bash History File...\nDo you wish to continue?',icon = 'warning')
            if MsgBox == 'yes':
                newWin = Toplevel()
                newWin.geometry("500x500")
                newWin.title("Disable HIstory")
                newWin.attributes('-topmost', True)
                T = Text(newWin, height=75, width=250, bg="black", fg="lime")
                T.pack()
                T.insert(END, "Okey Dokey :)\nDisabling Bash History Now...")
                output = anon.dishist()
                T.insert(END, output)
            else:
                tk.messagebox.showinfo('DISHIST TERMINATED!!!','DISHIST WAS STOPPED BY USER!')

        disable_history()


## Anon WINDOW LAYOUT

    def anon_window():
        nWin = Toplevel()
        nWin.geometry("550x125-1+1")
        nWin.title("Anon")
        nWin.configure(background="black")
        info = Label(nWin, text = "Available Anon Funcs.: ", bg="black", fg="lime")
        info.grid(row = 1, column = 0, padx=3, pady=3)
#
        b1 = Button(nWin, text="Histoclear", bg="black", fg="#ff0000",
                    command=lambda : dev_msgbx())
        b1.grid(row = 2 ,column=1, padx=3, pady=3)
#
        b2 = Button(nWin, text="Watergate", bg="black", fg="#ff0000",
                    command=lambda : dev_msgbx())
        b2.grid(row = 2, column = 2, padx=3, pady=3)
#
        b3 = Button(nWin, text="Blackhole", bg="black", fg="#ff0000",
                    command=lambda : dev_msgbx())
        b3.grid(row = 2, column = 3, padx=3, pady=3)
#
        b4 = Button(nWin, text="Anoid", bg="black", fg="#ff0000",
                    command=lambda : dev_msgbx())
        b4.grid(row = 2, column = 4, padx=3, pady=3)

        b5 = Button(nWin, text="Dis. History", bg="black", fg="#ff0000",
                    command=lambda : dev_msgbx())
        b5.grid(row = 3, column = 1, padx=3, pady=3)

        b6 = Button(nWin, text="Fake ID", bg="black", fg="lime",
                    command=lambda : _fakeid(nWin))
        b6.grid(row = 3, column = 2, padx=3, pady=3)


        b7 = Button(nWin, text="FakeMail", bg="black", fg="lime",
                    command=lambda : ck_fmail(nWin))
        b7.grid(row = 3, column = 3, padx=3, pady=3)
##
#        b8 = Button(nWin, text="", bg="black", fg="lime",
#                    command=lambda : (nWin))
#        b8.grid(row = 3, column = 4, padx=3, pady=3)
##
#        b9 = Button(nWin, text="", bg="black", fg="lime",
#                    command=lambda : (nWin))
#        b9.grid(row = 4, column = 1, padx=3, pady=3)
##
#        b10 = Button(nWin, text="", bg="black", fg="lime",
#                    command=lambda : (nWin))
#        b10.grid(row = 4, column = 2, padx=3, pady=3)
##
#        b11 = Button(nWin, text="", bg="black", fg="lime",
#                    command=lambda : (nWin))
#        b11.grid(row = 4, column = 3, padx=3, pady=3)
##
#        b12 = Button(nWin, text="", bg="black", fg="lime",
#                    command=lambda : (nWin))
#        b12.grid(row = 4, column = 4, padx=3, pady=3)
##
#        b13 = Button(nWin, text="", bg="black", fg="lime",
#                    command=lambda : (nWin))
#        b13.grid(row = 5, column = 1, padx=3, pady=3)
##
#        b14 = Button(nWin, text="", bg="black", fg="lime",
#                    command=lambda : (nWin))
#        b14.grid(row = 5, column = 2, padx=3, pady=3)
##
#        b15 = Button(nWin, text="", bg="black", fg="lime",
#                    command=lambda : (nWin))
#        b15.grid(row = 5, column = 3, padx=3, pady=3)
##
#        b16 = Button(nWin, text="", bg="black", fg="lime",
#                    command=lambda : (nWin))
#        b16.grid(row = 5, column = 4, padx=3, pady=3)

    anon_window()


# RECON
###########################################################################################
def recon_main():
    # Stalker
    def init_recon(winName):
        # Add popup dialog box asking for target info
        def save_info(window):
            first_name = firstname.get()
            middle_name = middlename.get()
            last_name = lastname.get()
            city_info = city.get()
            state_info = state.get()
            window.destroy()
#           print("[*] Searching For: %s %s %s In %s, %s" % (str(first_name), str(middle_name), str(last_name), str(city_info), str(state_info)))
            stalker.stalk(first_name, middle_name, last_name, city_info, state_info, save=0, gui=1, bypass=1)

        winName = Toplevel()
        winName.geometry("400x175")
        winName.title("Stalker")
        winName.configure(background="black")


        logo_image = Label(winName, bg="black", image=logo)
        firstname = Label(winName, text = "First Name: ", bg="black", fg="lime")
        middlename = Label(winName, text = "Middle Name: ", bg="black", fg="lime")
        lastname = Label(winName, text = "Last Name: ", bg="black", fg="lime")
        city = Label(winName, text = "City: ", bg="black", fg="lime")
        state = Label(winName, text = "State: ", bg="black", fg="lime")

        logo_image.place(x = 0, y = 0)
        firstname.place(x = 15, y = 10)
        middlename.place(x = 15, y = 30)
        lastname.place(x = 15, y = 50)
        city.place(x = 15, y = 70)
        state.place(x = 15, y = 90)

        firstname = StringVar()
        middlename = StringVar()
        lastname = StringVar()
        city = StringVar()
        state = StringVar()

        firstname_entry = Entry(winName, textvariable = firstname, width = "30", bg="black", fg="lime")
        middlename_entry = Entry(winName, textvariable = middlename, width = "30", bg="black", fg="lime")
        lastname_entry = Entry(winName, textvariable = lastname, width = "30", bg="black", fg="lime")
        city_entry = Entry(winName, textvariable = city, width = "30", bg="black", fg="lime")
        state_entry = Entry(winName, textvariable = state, width = "30", bg="black", fg="lime")

        firstname_entry.place(x = 150, y = 10)
        middlename_entry.place(x = 150, y = 30)
        lastname_entry.place(x = 150, y = 50)
        city_entry.place(x = 150, y = 70)
        state_entry.place(x = 150, y = 90)

        b1 = Button(winName, text='Search', bg="black", fg="lime", command=lambda: save_info(winName))
        b1.place(x = 15, y = 130)
        b2 = Button(winName, text='Cancel', bg="black", fg="lime",
                    command=winName.destroy)
        b2.place(x=100, y=130)

# DRIFTNET

    def driftnet(winName):
        def drift(winName):
            interface = inter.get()
            router = route_ip.get()
            local = local_ip.get()
            winName.destroy()
            try:
                recon.drift(interface, router, local)
            except Exception as error:
                msgbx(error)
        winName = Toplevel()
        winName.title("Driftnet")
        winName.geometry("450x120")
        winName.attributes('-topmost', True)
        winName.config(background="black")

        inter = Label(winName, text = "Interface: ", bg="black", fg="lime")
        route_ip = Label(winName, text = "Router IP: ", bg="black", fg="lime")
        local_ip = Label(winName, text = "Local IP: ", bg="black", fg="lime")

        inter.place(x = 15, y = 10)
        route_ip.place(x = 15, y = 30)
        local_ip.place(x = 15, y = 50)

        inter = StringVar()
        route_ip = StringVar()
        local_ip = StringVar()

        inter_entry = Entry(winName, textvariable = inter, width = "30", bg="black", fg="lime")
        route_ip_entry = Entry(winName, textvariable = route_ip, width = "30", bg="black", fg="lime")
        local_ip_entry = Entry(winName, textvariable = local_ip, width = "30", bg="black", fg="lime")

        inter_entry.place(x = 150, y = 10)
        route_ip_entry.place(x = 150, y = 30)
        local_ip_entry.place(x = 150, y = 50)

        b1 = Button(winName, text="Start Driftnet", bg="black", fg="lime",
                    command=lambda : drift(winName))
        b1.place(x=150, y = 75)
        b2 = Button(winName, text='Cancel', bg="black", fg="lime",
                    command=winName.destroy)
        b2.place(x = 350, y = 75)

# WHOIS

    def whois(winName):

        def save_file(data):
            def get_data(winName, _data):
                window = winName
                fname = info.get()
                ksys.scrbe(fname, _data)
                window.destroy()
            _data = data
            newWin = Toplevel()
            newWin.geometry("500x100")
            newWin.title("Save File")
            newWin.configure(background='black')
            info = Label(newWin, text = "Save As: ", bg="black", fg="lime")
            info.place(x = 15, y = 10)
            info = StringVar()
            info_entry = Entry(newWin, textvariable = info, width = "30", bg="black", fg="lime")
            info_entry.insert(0, "ex: /home/Documents/doc.txt")
            info_entry.bind("<Button-1>", lambda event: clear_entry(event, info_entry))
            info_entry.place(x = 150, y = 10)
            b1 = Button(newWin, text="Save", bg="black", fg="lime",
                        command=lambda : get_data(newWin, _data.decode()))
            b1.place(x=15,y=55)
            b2 = Button(newWin, text="Cancel", bg="black", fg="lime",
                        command=newWin.destroy)
            b2.place(x=150, y=55)

        def whodat(winName):
            whois_target = info.get()
            winName.destroy()
            newWin = Toplevel()
            newWin.geometry("500x500")
            newWin.title("WhoIs")
            newWin.attributes('-topmost', True)
            output = recon.whois(whois_target)

            menubar = Menu(root)
            savemenu = Menu(menubar, tearoff=0)
            savemenu.add_command(label="Save", command=lambda: save_file(output))
            menubar.add_cascade(label="File", menu=savemenu)
            newWin.configure(background='black', menu=menubar)

            T = Text(newWin, height=500, width=250, bg="black", fg="lime")
            T.pack()
            T.insert(END, output)

        winName = Toplevel()
        winName.geometry("400x75")
        winName.title("WhoIs")
        winName.attributes('-topmost', True)
        winName.configure(background="black")
        info = Label(winName, text = "Domain / IP: ", bg="black", fg="lime")
        info.place(x = 15, y = 10)
        info = StringVar()
        info_entry = Entry(winName, textvariable = info, width = "30", bg="black", fg="lime")
        info_entry.place(x = 150, y = 10)
        b1 = Button(winName, text="WhoIs", bg="black", fg="lime",
                    command=lambda : whodat(winName))
        b1.place(x=15,y=35)
        b2 = Button(winName, text="Cancel", bg="black", fg="lime",
                    command=winName.destroy)
        b2.place(x=150, y=35)

# IP_LOCATE

    def iploc(winName):

        def save_file(data):
            def get_data(winName, _data):
                window = winName
                fname = info.get()
                ksys.scrbe(fname, _data)
                window.destroy()
            _data = data
            newWin = Toplevel()
            newWin.geometry("500x100")
            newWin.title("Save File")
            newWin.configure(background='black')
            info = Label(newWin, text = "Save As: ", bg="black", fg="lime")
            info.place(x = 15, y = 10)
            info = StringVar()
            info_entry = Entry(newWin, textvariable = info, width = "30", bg="black", fg="lime")
            info_entry.insert(0, "ex: /home/Documents/doc.txt")
            info_entry.bind("<Button-1>", lambda event: clear_entry(event, info_entry))
            info_entry.place(x = 150, y = 10)
            b1 = Button(newWin, text="Save", bg="black", fg="lime",
                        command=lambda : get_data(newWin, _data.decode()))
            b1.place(x=15,y=55)
            b2 = Button(newWin, text="Cancel", bg="black", fg="lime",
                        command=newWin.destroy)
            b2.place(x=150, y=55)

        def locator(winName):
            output = ""
            target = info.get()
            winName.destroy()
            newWin = Toplevel()
            newWin.geometry("500x500")
            newWin.title("IP Locator")
            newWin.attributes('-topmost', True)
            data = recon.iploc(target)
            for item in data:
                output += "%s  %s\n" % (item, data["%s" % item])
            menubar = Menu(root)
            savemenu = Menu(menubar, tearoff=0)
            savemenu.add_command(label="Save", command=lambda: save_file(output))
            menubar.add_cascade(label="File", menu=savemenu)
            newWin.configure(background='black', menu=menubar)

            T = Text(newWin, height=500, width=250, bg="black", fg="lime")
            T.pack()
            T.insert(END, output)

        winName = Toplevel()
        winName.geometry("400x75")
        winName.title("IP Locator")
        winName.attributes('-topmost', True)
        winName.configure(background="black")
        info = Label(winName, text = "IP Address: ", bg="black", fg="lime")
        info.place(x = 15, y = 10)
        info = StringVar()
        info_entry = Entry(winName, textvariable = info, width = "30", bg="black", fg="lime")
        info_entry.place(x = 150, y = 10)
        b1 = Button(winName, text="IP Locator", bg="black", fg="lime",
                    command=lambda : locator(winName))
        b1.place(x=15,y=35)
        b2 = Button(winName, text="Cancel", bg="black", fg="lime",
                    command=winName.destroy)
        b2.place(x=150, y=35)


# WafW00f

    def wafw00f(winName):
        def waf(winName):
            waf_target = info.get()
            winName.destroy()
            newWin = Toplevel()
            newWin.geometry("500x500")
            newWin.title("WafW00f")
            newWin.attributes('-topmost', True)
            output = recon.wafw00f(waf_target)
            T = Text(newWin, height=500, width=250, bg="black", fg="lime")
            T.pack()
            T.insert(END, output)

        winName = Toplevel()
        winName.geometry("400x75")
        winName.title("Wafw00f")
        winName.configure(background="black")
        info = Label(winName, text = "Target URL: ", bg="black", fg="lime")
        info.place(x = 15, y = 10)
        info = StringVar()
        info_entry = Entry(winName, textvariable = info, width = "30", bg="black", fg="lime")
        info_entry.place(x = 150, y = 10)
        b1 = Button(winName, text="Wafwoof", bg="black", fg="lime",
                    command=lambda : waf(winName))
        b1.place(x=15,y=35)
        b2 = Button(winName, text="Cancel", bg="black", fg="lime",
                    command=winName.destroy)
        b2.place(x=150, y=35)

    # p0f

    def p0f(winName):
        def get_data(winName):
            interface = info.get()
            out_file = out_f.get()
            winName.destroy()
            newWin = Toplevel()
            newWin.geometry("500x500")
            newWin.title("p0f")
            newWin.attributes('-topmost', True)
            try:
                output = recon.p0f(interface, out_file)
            except Exception as error:
                output = "THERE WAS A PROBLEM WITH p0f!!! ---\n                                  |\n                                  V\n\n%s" % error
            T = Text(newWin, height=500, width=250, bg="black", fg="lime")
            T.pack()
            T.insert(END, output)

        winName = Toplevel()
        winName.geometry("400x100")
        winName.title("p0f")
        winName.configure(background="black")
        info = Label(winName, text = "Interface: ", bg="black", fg="lime")
        info.place(x = 15, y = 10)
        info = StringVar()
        info_entry = Entry(winName, textvariable = info, width = "30", bg="black", fg="lime")
        info_entry.place(x = 150, y = 10)

        out_f = Label(winName, text = "Output File: ", bg="black", fg="lime")
        out_f.place(x = 15, y = 35)
        out_f = StringVar()
        out_f_entry = Entry(winName, textvariable = out_f, width = "30", bg="black", fg="lime")
        out_f_entry.place(x = 150, y = 35)

        b1 = Button(winName, text="Start p0f", bg="black", fg="lime",
                    command=lambda : get_data(winName))
        b1.place(x=15,y=65)
        b2 = Button(winName, text="Cancel", bg="black", fg="lime",
                    command=winName.destroy)
        b2.place(x=150, y=65)

    # arp_fprint

    def arp_fp(winName):
        def get_data(winName):
            interface = info.get()
            tgt = target.get()
            winName.destroy()
            try:
                output = recon.arp_fprint(interface, tgt)
            except Exception as error:
                output = "THERE WAS A PROBLEM WITH Arp Fingerprint!!! ---\n                                              |\n                                              V\n\n%s" % error
            newWin = Toplevel()
            newWin.geometry("500x500")
            newWin.title("Arp Fingerprint")
            newWin.attributes('-topmost', True)
            T = Text(newWin, height=500, width=250, bg="black", fg="lime")
            T.pack()
            T.insert(END, output)

        winName = Toplevel()
        winName.geometry("400x100")
        winName.title("Arp Fingerprint")
        winName.configure(background="black")
        info = Label(winName, text = "Interface: ", bg="black", fg="lime")
        target = Label(winName, text = "Target: ", bg="black", fg="lime")
        info.place(x = 15, y = 10)
        target.place(x = 15, y = 35)
        info = StringVar()
        target = StringVar()
        info_entry = Entry(winName, textvariable = info, width = "30", bg="black", fg="lime")
        target_entry = Entry(winName, textvariable = target, width = "30", bg="black", fg="lime")
        info_entry.place(x = 150, y = 10)
        target_entry.place(x = 150, y = 35)

        b1 = Button(winName, text="Fingerprint", bg="black", fg="lime",
                    command=lambda : get_data(winName))
        b1.place(x=15,y=65)
        b2 = Button(winName, text="Cancel", bg="black", fg="lime",
                    command=winName.destroy)
        b2.place(x=150, y=65)

    # DNSEnum

    def dnse(winName):

        def save_file(data):
            def get_data(winName, _data):
                window = winName
                fname = info.get()
                ksys.scrbe(fname, _data)
                window.destroy()
            _data = data
            newWin = Toplevel()
            newWin.geometry("500x100")
            newWin.title("Save File")
            newWin.configure(background='black')
            info = Label(newWin, text = "Save As: ", bg="black", fg="lime")
            info.place(x = 15, y = 10)
            info = StringVar()
            info_entry = Entry(newWin, textvariable = info, width = "30", bg="black", fg="lime")
            info_entry.insert(0, "ex: /home/Documents/doc.txt")
            info_entry.bind("<Button-1>", lambda event: clear_entry(event, info_entry))
            info_entry.place(x = 150, y = 10)
            b1 = Button(newWin, text="Save", bg="black", fg="lime",
                        command=lambda : get_data(newWin, _data.decode()))
            b1.place(x=15,y=55)
            b2 = Button(newWin, text="Cancel", bg="black", fg="lime",
                        command=newWin.destroy)
            b2.place(x=150, y=55)

        def get_data(winName):
            target = info.get()
            winName.destroy()
            output = recon.dnsenum(target)
            newWin = Toplevel()
            newWin.geometry("500x500")
            newWin.title("DNSEnum")
            newWin.attributes('-topmost', True)

            menubar = Menu(root)
            savemenu = Menu(menubar, tearoff=0)
            savemenu.add_command(label="Save", command=lambda: save_file(output))
            menubar.add_cascade(label="File", menu=savemenu)
            newWin.configure(background='black', menu=menubar)

            T = Text(newWin, height=500, width=250, bg="black", fg="lime")
            T.pack()
            T.insert(END, output)

        winName = Toplevel()
        winName.geometry("400x75")
        winName.title("DNSEnum")
        winName.configure(background="black")
        info = Label(winName, text = "URL: ", bg="black", fg="lime")
        info.place(x = 15, y = 10)
        info = StringVar()
        info_entry = Entry(winName, textvariable = info, width = "30", bg="black", fg="lime")
        info_entry.place(x = 150, y = 10)
        b1 = Button(winName, text="Enum", bg="black", fg="lime",
                    command=lambda : get_data(winName))
        b1.place(x=15,y=35)
        b2 = Button(winName, text="Cancel", bg="black", fg="lime",
                    command=winName.destroy)
        b2.place(x=150, y=35)

    # DNSMap

    def dnsmap(winName):

        def save_file(data):
            def get_data(winName, _data):
                window = winName
                fname = info.get()
                ksys.scrbe(fname, _data)
                window.destroy()
            _data = data
            newWin = Toplevel()
            newWin.geometry("500x100")
            newWin.title("Save File")
            newWin.configure(background='black')
            info = Label(newWin, text = "Save As: ", bg="black", fg="lime")
            info.place(x = 15, y = 10)
            info = StringVar()
            info_entry = Entry(newWin, textvariable = info, width = "30", bg="black", fg="lime")
            info_entry.insert(0, "ex: /home/Documents/doc.txt")
            info_entry.bind("<Button-1>", lambda event: clear_entry(event, info_entry))
            info_entry.place(x = 150, y = 10)
            b1 = Button(newWin, text="Save", bg="black", fg="lime",
                        command=lambda : get_data(newWin, _data.decode()))
            b1.place(x=15,y=55)
            b2 = Button(newWin, text="Cancel", bg="black", fg="lime",
                        command=newWin.destroy)
            b2.place(x=150, y=55)

        def get_data(winName):
            target = info.get()
            winName.destroy()
            try:
                output = recon.dnsmap(target)
            except Exception as error:
                output = "THERE WAS A PROBLEM WITH DNSMAP...\nPERHAPS THE URL WAS INVALID\nOR DNSMAP IS NOT INSTALLED?\n\n%s" % error
            newWin = Toplevel()
            newWin.geometry("500x500")
            newWin.title("DNSMap")

            menubar = Menu(root)
            savemenu = Menu(menubar, tearoff=0)
            savemenu.add_command(label="Save", command=lambda: save_file(output))
            menubar.add_cascade(label="File", menu=savemenu)
            newWin.configure(background='black', menu=menubar)

            T = Text(newWin, height=500, width=250, bg="black", fg="lime")
            T.pack()
            T.insert(END, output)

        winName = Toplevel()
        winName.geometry("400x75")
        winName.title("DNSMap")
        winName.configure(background="black")
        info = Label(winName, text = "Domain: ", bg="black", fg="lime")
        info.place(x = 15, y = 10)
        info = StringVar()
        info_entry = Entry(winName, textvariable = info, width = "30", bg="black", fg="lime")
        info_entry.place(x = 150, y = 10)
        b1 = Button(winName, text="Map", bg="black", fg="lime",
                    command=lambda : get_data(winName))
        b1.place(x=15,y=35)
        b2 = Button(winName, text="Cancel", bg="black", fg="lime",
                    command=winName.destroy)
        b2.place(x=150, y=35)

    # DNSTrace

    def dnst(winName):

        def save_file(data):
            def get_data(winName, _data):
                window = winName
                fname = info.get()
                ksys.scrbe(fname, _data)
                window.destroy()
            _data = data
            newWin = Toplevel()
            newWin.geometry("500x100")
            newWin.title("Save File")
            newWin.configure(background='black')
            info = Label(newWin, text = "Save As: ", bg="black", fg="lime")
            info.place(x = 15, y = 10)
            info = StringVar()
            info_entry = Entry(newWin, textvariable = info, width = "30", bg="black", fg="lime")
            info_entry.insert(0, "ex: /home/Documents/doc.txt")
            info_entry.bind("<Button-1>", lambda event: clear_entry(event, info_entry))
            info_entry.place(x = 150, y = 10)
            b1 = Button(newWin, text="Save", bg="black", fg="lime",
                        command=lambda : get_data(newWin, _data.decode()))
            b1.place(x=15,y=55)
            b2 = Button(newWin, text="Cancel", bg="black", fg="lime",
                        command=newWin.destroy)
            b2.place(x=150, y=55)

        def get_data(winName):
            target = info.get()
            winName.destroy()
            try:
                output = recon.dnstrace(target)
            except Exception as error:
                output = "THERE WAS A PROBLEM WITH DNSTRACER...\nPERHAPS THE URL WAS INVALID\nOR DNSTRACER IS NOT INSTALLED?\n\n%s" % error
            newWin = Toplevel()
            newWin.geometry("500x500")
            newWin.title("DNSTracer")

            menubar = Menu(root)
            savemenu = Menu(menubar, tearoff=0)
            savemenu.add_command(label="Save", command=lambda: save_file(output))
            menubar.add_cascade(label="File", menu=savemenu)
            newWin.configure(background='black', menu=menubar)

            T = Text(newWin, height=500, width=250, bg="black", fg="lime")
            T.pack()
            T.insert(END, output)

        winName = Toplevel()
        winName.geometry("400x75")
        winName.title("DNSTracer")
        winName.configure(background="black")
        info = Label(winName, text = "Domain: ", bg="black", fg="lime")
        info.place(x = 15, y = 10)
        info = StringVar()
        info_entry = Entry(winName, textvariable = info, width = "30", bg="black", fg="lime")
        info_entry.place(x = 150, y = 10)
        b1 = Button(winName, text="Trace", bg="black", fg="lime",
                    command=lambda : get_data(winName))
        b1.place(x=15,y=35)
        b2 = Button(winName, text="Cancel", bg="black", fg="lime",
                    command=winName.destroy)
        b2.place(x=150, y=35)

    # Golismero

    def golismero(winName):
        def get_data(winName):
            target = info.get()
            winName.destroy()
            output = recon.golismero(target)
            newWin = Toplevel()
            newWin.geometry("500x500")
            newWin.title("Golismero")
            T = Text(newWin, height=500, width=250, bg="black", fg="lime")
            T.pack()
            T.insert(END, output)

        winName = Toplevel()
        winName.geometry("400x75")
        winName.title("Golismero")
        winName.configure(background="black")
        info = Label(winName, text = "Target: ", bg="black", fg="lime")
        info.place(x = 15, y = 10)
        info = StringVar()
        info_entry = Entry(winName, textvariable = info, width = "30", bg="black", fg="lime")
        info_entry.place(x = 150, y = 10)
        b1 = Button(winName, text="WhoIs", bg="black", fg="lime",
                    command=lambda : get_data(winName))
        b1.place(x=15,y=35)
        b2 = Button(winName, text="Cancel", bg="black", fg="lime",
                    command=winName.destroy)
        b2.place(x=150, y=35)

    # Arpscan

    def arpscn(winName):

        def save_file(data):
            def get_data(winName, _data):
                window = winName
                fname = info.get()
                ksys.scrbe(fname, _data)
                window.destroy()
            _data = data
            newWin = Toplevel()
            newWin.geometry("500x100")
            newWin.title("Save File")
            newWin.configure(background='black')
            info = Label(newWin, text = "Save As: ", bg="black", fg="lime")
            info.place(x = 15, y = 10)
            info = StringVar()
            info_entry = Entry(newWin, textvariable = info, width = "30", bg="black", fg="lime")
            info_entry.insert(0, "ex: /home/Documents/doc.txt")
            info_entry.bind("<Button-1>", lambda event: clear_entry(event, info_entry))
            info_entry.place(x = 150, y = 10)
            b1 = Button(newWin, text="Save", bg="black", fg="lime",
                        command=lambda : get_data(newWin, _data.decode()))
            b1.place(x=15,y=55)
            b2 = Button(newWin, text="Cancel", bg="black", fg="lime",
                        command=newWin.destroy)
            b2.place(x=150, y=55)

        def get_data():
            output = recon.local_arp()
            newWin = Toplevel()
            newWin.geometry("750x500")
            newWin.title("Arpscan")

            menubar = Menu(root)
            savemenu = Menu(menubar, tearoff=0)
            savemenu.add_command(label="Save", command=lambda: save_file(output))
            menubar.add_cascade(label="File", menu=savemenu)
            newWin.configure(background='black', menu=menubar)

            T = Text(newWin, height=500, width=250, bg="black", fg="lime")
            T.pack()
            T.insert(END, output)

        get_data()

    # Dig
    def digem(winName):

        def save_file(data):
            def get_data(winName, _data):
                window = winName
                fname = info.get()
                ksys.scrbe(fname, _data)
                window.destroy()
            _data = data
            newWin = Toplevel()
            newWin.geometry("500x100")
            newWin.title("Save File")
            newWin.configure(background='black')
            info = Label(newWin, text = "Save As: ", bg="black", fg="lime")
            info.place(x = 15, y = 10)
            info = StringVar()
            info_entry = Entry(newWin, textvariable = info, width = "30", bg="black", fg="lime")
            info_entry.insert(0, "ex: /home/Documents/doc.txt")
            info_entry.bind("<Button-1>", lambda event: clear_entry(event, info_entry))
            info_entry.place(x = 150, y = 10)
            b1 = Button(newWin, text="Save", bg="black", fg="lime",
                        command=lambda : get_data(newWin, _data.decode()))
            b1.place(x=15,y=55)
            b2 = Button(newWin, text="Cancel", bg="black", fg="lime",
                        command=newWin.destroy)
            b2.place(x=150, y=55)

        def get_data(winName):
            target = info.get()
            winName.destroy()
            try:
                output = recon.dig(target)
                T.insert(END, output)
            except Exception:
                return 1
            newWin = Toplevel()
            newWin.geometry("750x750")
            newWin.title("Dig")

            menubar = Menu(root)
            savemenu = Menu(menubar, tearoff=0)
            savemenu.add_command(label="Save", command=lambda: save_file(output))
            menubar.add_cascade(label="File", menu=savemenu)
            newWin.configure(background='black', menu=menubar)

            T = Text(newWin, height=500, width=250, bg="black", fg="lime")
            T.pack()
        winName = Toplevel()
        winName.geometry("400x90")
        winName.title("Dig")
        winName.configure(background="black")
        MsgBox = tk.messagebox.askquestion ('Continue?','This function May Take While...\nDo you wish to continue?',icon = 'warning')
        if MsgBox == 'yes':
            info = Label(winName, text = "Target:", bg="black", fg="lime")
            info.place(x = 15, y = 10)
            info = StringVar()
            info_entry = Entry(winName, textvariable = info, width = "30", bg="black", fg="lime")
            info_entry.place(x = 150, y = 10)
            b1 = Button(winName, text="Dig", bg="black", fg="lime",
                        command=lambda : get_data(winName))
            b1.place(x=100,y=50)
            b2 = Button(winName, text="Cancel", bg="black", fg="lime",
                        command=winName.destroy)
            b2.place(x=250, y=50)
        else:
            tk.messagebox.showinfo("Dig Terminated!", "Dig was terminated by the user!")
            winName.destroy()


    # NSLOOKUP
    def nslook(winName):

        def save_file(data):
            def get_data(winName, _data):
                window = winName
                fname = info.get()
                ksys.scrbe(fname, _data)
                window.destroy()
            _data = data
            newWin = Toplevel()
            newWin.geometry("500x100")
            newWin.title("Save File")
            newWin.configure(background='black')
            info = Label(newWin, text = "Save As: ", bg="black", fg="lime")
            info.place(x = 15, y = 10)
            info = StringVar()
            info_entry = Entry(newWin, textvariable = info, width = "30", bg="black", fg="lime")
            info_entry.insert(0, "ex: /home/Documents/doc.txt")
            info_entry.bind("<Button-1>", lambda event: clear_entry(event, info_entry))
            info_entry.place(x = 150, y = 10)
            b1 = Button(newWin, text="Save", bg="black", fg="lime",
                        command=lambda : get_data(newWin, _data.decode()))
            b1.place(x=15,y=55)
            b2 = Button(newWin, text="Cancel", bg="black", fg="lime",
                        command=newWin.destroy)
            b2.place(x=150, y=55)

        def lookup(winName):
            target = info.get()
            winName.destroy()
            output = recon.nslookup(target)
            newWin = Toplevel()
            newWin.geometry("500x500")
            newWin.title("NSLookup")

            menubar = Menu(root)
            savemenu = Menu(menubar, tearoff=0)
            savemenu.add_command(label="Save", command=lambda: save_file(output))
            menubar.add_cascade(label="File", menu=savemenu)
            newWin.configure(background='black', menu=menubar)

            T = Text(newWin, height=500, width=250, bg="black", fg="lime")
            T.pack()
            T.insert(END, output)

        winName = Toplevel()
        winName.geometry("400x75")
        winName.title("NSLookup")
        winName.configure(background="black")
        info = Label(winName, text = "Target URL: ", bg="black", fg="lime")
        info.place(x = 15, y = 10)
        info = StringVar()
        info_entry = Entry(winName, textvariable = info, width = "30", bg="black", fg="lime")
        info_entry.place(x = 150, y = 10)
        b1 = Button(winName, text="Lookup", bg="black", fg="lime",
                    command=lambda : lookup(winName))
        b1.place(x=15,y=35)
        b2 = Button(winName, text="Cancel", bg="black", fg="lime",
                    command=winName.destroy)
        b2.place(x=150, y=35)

# NIKTO

    def nikto(winName):

        def get_data(winName):
            target = info.get()
            winName.destroy()
            newWin = Toplevel()
            newWin.geometry("500x500")
            newWin.title("Nikto")
            MsgBox = tk.messagebox.askquestion ('Continue?','Nikto can take a while...\nDo you wish to continue?',icon = 'warning')
            if MsgBox == 'yes':
                T = Text(newWin, height=500, width=250, bg="black", fg="lime")
                T.pack()
                T.insert(END, "Nikto Is Running... Please Wait :)")
                output = recon.nikto(target)
                T.insert(END, output)
            else:
                tk.messagebox.showinfo('Nikto Terminated','NIKTO WAS STOPPED BY USER!')

        winName = Toplevel()
        winName.geometry("400x75")
        winName.title("Nikto")
        winName.configure(background="black")
        info = Label(winName, text = "Target Address: ", bg="black", fg="lime")
        info.place(x = 15, y = 10)
        info = StringVar()
        info_entry = Entry(winName, textvariable = info, width = "30", bg="black", fg="lime")
        info_entry.place(x = 150, y = 10)
        b1 = Button(winName, text="Run Nikto", bg="black", fg="lime",
                    command=lambda : get_data(winName))
        b1.place(x=15,y=35)
        b2 = Button(winName, text="Cancel", bg="black", fg="lime",
                    command=winName.destroy)
        b2.place(x=150, y=35)


# ARPSPOOF

    def arpspoof(newWin):
        def get_data(winName):
            interface = info.get()
            dest_ip = d_ip.get()
            winName.destroy()
            try:
                output = recon.arpspoof(interface, dest_ip)
            except Exception as error:
                output = "THERE WAS A PROBLEM WITH ARPSPOOF!!!\n\n%s" % error
            newWin = Toplevel()
            newWin.geometry("500x500")
            newWin.title("Arpspoof")
            newWin.attributes('-topmost', True)
            T = Text(newWin, height=500, width=250, bg="black", fg="lime")
            T.pack()
            T.insert(END, output)

        winName = Toplevel()
        winName.geometry("400x100")
        winName.title("Arpspoof")
        winName.configure(background="black")
        info = Label(winName, text = "Interface: ", bg="black", fg="lime")
        info.place(x = 15, y = 10)
        info = StringVar()
        info_entry = Entry(winName, textvariable = info, width = "30", bg="black", fg="lime")
        info_entry.place(x = 150, y = 10)

        d_ip = Label(winName, text = "Destination IP: ", bg="black", fg="lime")
        d_ip.place(x = 15, y = 35)
        d_ip = StringVar()
        d_ip_entry = Entry(winName, textvariable = d_ip, width = "30", bg="black", fg="lime")
        d_ip_entry.place(x = 150, y = 35)

        b1 = Button(winName, text="Arpspoof", bg="black", fg="lime",
                    command=lambda : get_data(winName))
        b1.place(x=15,y=65)
        b2 = Button(winName, text="Cancel", bg="black", fg="lime",
                    command=winName.destroy)
        b2.place(x=150, y=65)

# SYSPRINT

    def sysprint(newWin):

        def save_file(data):
            def get_data(winName, _data):
                window = winName
                fname = info.get()
                ksys.scrbe(fname, _data)
                window.destroy()
            _data = data
            newWin = Toplevel()
            newWin.geometry("500x100")
            newWin.title("Save File")
            newWin.configure(background='black')
            info = Label(newWin, text = "Save As: ", bg="black", fg="lime")
            info.place(x = 15, y = 10)
            info = StringVar()
            info_entry = Entry(newWin, textvariable = info, width = "30", bg="black", fg="lime")
            info_entry.insert(0, "ex: /home/Documents/doc.txt")
            info_entry.bind("<Button-1>", lambda event: clear_entry(event, info_entry))
            info_entry.place(x = 150, y = 10)
            b1 = Button(newWin, text="Save", bg="black", fg="lime",
                        command=lambda : get_data(newWin, _data.decode()))
            b1.place(x=15,y=55)
            b2 = Button(newWin, text="Cancel", bg="black", fg="lime",
                        command=newWin.destroy)
            b2.place(x=150, y=55)

        def get_data(winName):
            interface = info.get()
            host_ip = host.get()
            winName.destroy()
            try:
                output = recon.sysprint(interface, host_ip)
            except Exception as error:
                output = "THERE WAS A PROBLEM WITH SYSPRINT!!!\n\n%s" % error
            newWin = Toplevel()
            newWin.geometry("500x500")
            newWin.title("Sysprint")
            newWin.attributes('-topmost', True)

            menubar = Menu(root)
            savemenu = Menu(menubar, tearoff=0)
            savemenu.add_command(label="Save", command=lambda: save_file(output))
            menubar.add_cascade(label="File", menu=savemenu)
            newWin.configure(background='black', menu=menubar)

            T = Text(newWin, height=500, width=250, bg="black", fg="lime")
            T.pack()
            T.insert(END, output)

        winName = Toplevel()
        winName.geometry("400x100")
        winName.title("Sysprint")
        winName.configure(background="black")
        info = Label(winName, text = "Interface: ", bg="black", fg="lime")
        info.place(x = 15, y = 10)
        info = StringVar()
        info_entry = Entry(winName, textvariable = info, width = "30", bg="black", fg="lime")
        info_entry.place(x = 150, y = 10)

        host = Label(winName, text = "Host IP: ", bg="black", fg="lime")
        host.place(x = 15, y = 35)
        host = StringVar()
        host_entry = Entry(winName, textvariable = host, width = "30", bg="black", fg="lime")
        host_entry.place(x = 150, y = 35)

        b1 = Button(winName, text="Sysprint", bg="black", fg="lime",
                    command=lambda : get_data(winName))
        b1.place(x=15,y=65)
        b2 = Button(winName, text="Cancel", bg="black", fg="lime",
                    command=winName.destroy)
        b2.place(x=150, y=65)

# WebInfo

    def webinfo(winName):

        def save_file(data):
            def get_data(winName, _data):
                window = winName
                fname = info.get()
                ksys.scrbe(fname, _data)
                window.destroy()
            _data = data
            newWin = Toplevel()
            newWin.geometry("500x100")
            newWin.title("Save File")
            newWin.configure(background='black')
            info = Label(newWin, text = "Save As: ", bg="black", fg="lime")
            info.place(x = 15, y = 10)
            info = StringVar()
            info_entry = Entry(newWin, textvariable = info, width = "30", bg="black", fg="lime")
            info_entry.insert(0, "ex: /home/Documents/doc.txt")
            info_entry.bind("<Button-1>", lambda event: clear_entry(event, info_entry))
            info_entry.place(x = 150, y = 10)
            b1 = Button(newWin, text="Save", bg="black", fg="lime",
                        command=lambda : get_data(newWin, _data.decode()))
            b1.place(x=15,y=55)
            b2 = Button(newWin, text="Cancel", bg="black", fg="lime",
                        command=newWin.destroy)
            b2.place(x=150, y=55)

        def get_data(winName):
            target = info.get()
            winName.destroy()
            newWin = Toplevel()
            newWin.geometry("500x500")
            newWin.title("WebInfo")
            MsgBox = tk.messagebox.askquestion ('Continue?','WebInfo can take a while...\nDo you wish to continue?',icon = 'warning')
            if MsgBox == 'yes':

                menubar = Menu(root)
                savemenu = Menu(menubar, tearoff=0)
                savemenu.add_command(label="Save", command=lambda: save_file(output))
                menubar.add_cascade(label="File", menu=savemenu)
                newWin.configure(background='black', menu=menubar)

                T = Text(newWin, height=500, width=250, bg="black", fg="lime")
                T.pack()
                T.insert(END, "WebInfo Is Running... Please Wait :)")
                output = recon.webinfo(target)
                T.insert(END, output)
            else:
                tk.messagebox.showinfo('WebInfo Terminated','WEBINFO WAS STOPPED BY USER!')

            button1 = tk.Button (root, text='Exit Application',command=tk.ExitApplication)
            winName.create_window(97, 270, window=button1)

        winName = Toplevel()
        winName.geometry("400x75")
        winName.title("WebInfo")
        winName.configure(background="black")
        info = Label(winName, text = "Target Address: ", bg="black", fg="lime")
        info.place(x = 15, y = 10)
        info = StringVar()
        info_entry = Entry(winName, textvariable = info, width = "30", bg="black", fg="lime")
        info_entry.place(x = 150, y = 10)
        b1 = Button(winName, text="Run WebInfo", bg="black", fg="lime",
                    command=lambda : get_data(winName))
        b1.place(x=15,y=35)
        b2 = Button(winName, text="Cancel", bg="black", fg="lime",
                    command=winName.destroy)
        b2.place(x=150, y=35)

# theHarvester
    def harvest(winName):
        def getter(winName):
            winName.destroy()
            target = _target.get()
            winName.destroy()
            msgbx("theHarvester", "Please Wait While\nWe Search For\nYour Target...")
            try:
                output = recon.harvester(target)
            except Exception as error:
                return error
            newWin = Toplevel()
            newWin.geometry("750x750")
            newWin.title("%s" % target)
            newWin.attributes('-topmost', True)
            menubar = Menu(root)
            savemenu = Menu(menubar, tearoff=0)
            savemenu.add_command(label="Save", command=lambda: save_file(output))
            menubar.add_cascade(label="File", menu=savemenu)
            newWin.configure(background='black')
            T = Text(newWin, height=500, width=250, bg="black", fg="lime")
            T.pack()
            T.insert(END, output)

        winName = Toplevel()
        winName.geometry("400x75")
        winName.title("theHarvester")
        winName.configure(background="black")
        _target = Label(winName, text = "Domain: ", bg="black", fg="lime")
        _target.place(x = 15, y = 10)
        _target = StringVar()
        _target_entry = Entry(winName, textvariable = _target, width = "30", bg="black", fg="lime")
        _target_entry.place(x = 150, y = 10)
        b1 = Button(winName, text="Search", bg="black", fg="lime",
                    command=lambda : getter(winName))
        b1.place(x=15,y=35)
        b2 = Button(winName, text="Cancel", bg="black", fg="lime",
                    command=winName.destroy)
        b2.place(x=150, y=35)



    ############################################################################
    # NMAP

    def nmap_main(winName):

        def save_file(data):
            def get_data(winName, _data):
                window = winName
                fname = info.get()
                ksys.scrbe(fname, _data)
                window.destroy()
            _data = data
            newWin = Toplevel()
            newWin.geometry("500x100")
            newWin.title("Save File")
            newWin.configure(background='black')
            info = Label(newWin, text = "Save As: ", bg="black", fg="lime")
            info.place(x = 15, y = 10)
            info = StringVar()
            info_entry = Entry(newWin, textvariable = info, width = "30", bg="black", fg="lime")
            info_entry.insert(0, "ex: /home/Documents/doc.txt")
            info_entry.bind("<Button-1>", lambda event: clear_entry(event, info_entry))
            info_entry.place(x = 150, y = 10)
            b1 = Button(newWin, text="Save", bg="black", fg="lime",
                        command=lambda : get_data(newWin, _data.decode()))
            b1.place(x=15,y=55)
            b2 = Button(newWin, text="Cancel", bg="black", fg="lime",
                        command=newWin.destroy)
            b2.place(x=150, y=55)

    ## STANDARD NMAP
        def get_std_data(winName):
            MsgBox = tk.messagebox.askquestion ('Continue?','NMap can take a long time...\nDo you wish to continue?', parent=winName ,icon = 'warning')
            if MsgBox == 'yes':
                target = info.get()
                winName.destroy()
                output = recon.std_map(target)
                newWin = Toplevel()
                newWin.geometry("500x500")
                newWin.title("NMap Standard Data")
                newWin.attributes('-topmost', True)
                menubar = Menu(root)
                savemenu = Menu(menubar, tearoff=0)
                savemenu.add_command(label="Save", command=lambda: save_file(output))
                menubar.add_cascade(label="File", menu=savemenu)
                newWin.configure(background='black', menu=menubar)
                T = Text(newWin, height=500, width=250, bg="black", fg="lime")
                T.pack()
                T.insert(END, "NMap Is Running... Please Wait :)")
                T.insert(END, output)
            else:
                tk.messagebox.showinfo('NMap Terminated','NMAP WAS STOPPED BY USER!')

        def std_map(winName):
            winName = Toplevel()
            winName.geometry("400x75")
            winName.title("Nmap")
            winName.attributes('-topmost', True)
            winName.configure(background="black")
            global info
            info = Label(winName, text = "Target Address: ", bg="black", fg="lime")
            info.place(x = 15, y = 10)
            info = StringVar()
            info_entry = Entry(winName, textvariable = info, width = "30", bg="black", fg="lime")
            info_entry.place(x = 150, y = 10)
            b1 = Button(winName, text="Start NMap", bg="black", fg="lime",
                        command=lambda : get_std_data(winName))
            b1.place(x=15,y=35)
            b2 = Button(winName, text="Cancel", bg="black", fg="lime",
                        command=winName.destroy)
            b2.place(x=150, y=35)

    ## CONNECT NMAP
        def get_con_data(winName):
            MsgBox = tk.messagebox.askquestion ('Continue?','NMap can take a long time...\nDo you wish to continue?', parent=winName ,icon = 'warning')
            if MsgBox == 'yes':
                target = conninfo.get()
                winName.destroy()
                output = recon.connect_map(target)
                newWin = Toplevel()
                newWin.geometry("500x500")
                newWin.title("NMap Connect Data")
                newWin.attributes('-topmost', True)
                menubar = Menu(root)
                savemenu = Menu(menubar, tearoff=0)
                savemenu.add_command(label="Save", command=lambda: save_file(output))
                menubar.add_cascade(label="File", menu=savemenu)
                newWin.configure(background='black', menu=menubar)
                T = Text(newWin, height=500, width=250, bg="black", fg="lime")
                T.pack()
                T.insert(END, "NMap Is Running... Please Wait :)")
                T.insert(END, output)
            else:
                tk.messagebox.showinfo('NMap Terminated','NMAP WAS STOPPED BY USER!')

        def conn_map(winName):
            winName = Toplevel()
            winName.geometry("400x75")
            winName.title("Nmap")
            winName.configure(background="black")
            global conninfo
            conninfo = Label(winName, text = "Target Address: ", bg="black", fg="lime")
            conninfo.place(x = 15, y = 10)
            conninfo = StringVar()
            conninfo_entry = Entry(winName, textvariable = info, width = "30", bg="black", fg="lime")
            conninfo_entry.place(x = 150, y = 10)
            b1 = Button(winName, text="Start NMap", bg="black", fg="lime",
                        command=lambda : get_con_data(winName))
            b1.place(x=15,y=35)
            b2 = Button(winName, text="Cancel", bg="black", fg="lime",
                        command=winName.destroy)
            b2.place(x=150, y=35)

    ## ACK NMAP
        def get_ack_data(winName):
            MsgBox = tk.messagebox.askquestion ('Continue?','NMap can take a long time...\nDo you wish to continue?', parent=winName ,icon = 'warning')
            if MsgBox == 'yes':
                target = ackinfo.get()
                winName.destroy()
                output = recon.ack_map(target)
                newWin = Toplevel()
                newWin.geometry("500x500")
                newWin.title("NMap ACK Data")
                newWin.attributes('-topmost', True)
                menubar = Menu(root)
                savemenu = Menu(menubar, tearoff=0)
                savemenu.add_command(label="Save", command=lambda: save_file(output))
                menubar.add_cascade(label="File", menu=savemenu)
                newWin.configure(background='black', menu=menubar)
                T = Text(newWin, height=500, width=250, bg="black", fg="lime")
                T.pack()
                T.insert(END, "NMap Is Running... Please Wait :)")
                T.insert(END, output)
            else:
                tk.messagebox.showinfo('NMap Terminated','NMAP WAS STOPPED BY USER!')

        def ack_map(winName):
            winName = Toplevel()
            winName.geometry("400x75")
            winName.title("Nmap")
            winName.configure(background="black")
            global ackinfo
            ackinfo = Label(winName, text = "Target Address: ", bg="black", fg="lime")
            ackinfo.place(x = 15, y = 10)
            ackinfo = StringVar()
            ackinfo_entry = Entry(winName, textvariable = ackinfo, width = "30", bg="black", fg="lime")
            ackinfo_entry.place(x = 150, y = 10)
            b1 = Button(winName, text="Start NMap", bg="black", fg="lime",
                        command=lambda : get_ack_data(winName))
            b1.place(x=15,y=35)
            b2 = Button(winName, text="Cancel", bg="black", fg="lime",
                        command=winName.destroy)
            b2.place(x=150, y=35)

    ## WINDOW NMAP
        def get_wndw_data(winName):
            MsgBox = tk.messagebox.askquestion ('Continue?','NMap can take a long time...\nDo you wish to continue?', parent=winName ,icon = 'warning')
            if MsgBox == 'yes':
                target = info.get()
                winName.destroy()
                output = recon.window_map(target)
                newWin = Toplevel()
                newWin.geometry("500x500")
                newWin.title("NMap Window Data")
                newWin.attributes('-topmost', True)
                menubar = Menu(root)
                savemenu = Menu(menubar, tearoff=0)
                savemenu.add_command(label="Save", command=lambda: save_file(output))
                menubar.add_cascade(label="File", menu=savemenu)
                newWin.configure(background='black', menu=menubar)
                T = Text(newWin, height=500, width=250, bg="black", fg="lime")
                T.pack()
                T.insert(END, "NMap Is Running... Please Wait :)")
                T.insert(END, output)
            else:
                tk.messagebox.showinfo('NMap Terminated','NMAP WAS STOPPED BY USER!')

        def wndw_map(winName):
            winName = Toplevel()
            winName.geometry("400x75")
            winName.title("Nmap")
            winName.configure(background="black")
            global info
            info = Label(winName, text = "Target Host: ", bg="black", fg="lime")
            info.place(x = 15, y = 10)
            info = StringVar()
            info_entry = Entry(winName, textvariable = info, width = "30", bg="black", fg="lime")
            info_entry.place(x = 150, y = 10)
            b1 = Button(winName, text="Start NMap", bg="black", fg="lime",
                        command=lambda : get_wndw_data(winName))
            b1.place(x=15,y=35)
            b2 = Button(winName, text="Cancel", bg="black", fg="lime",
                        command=winName.destroy)
            b2.place(x=150, y=35)

    ## MAIMON NMAP
        def get_mmn_data(winName):
            MsgBox = tk.messagebox.askquestion ('Continue?','NMap can take a long time...\nDo you wish to continue?', parent=winName ,icon = 'warning')
            if MsgBox == 'yes':
                target = info.get()
                winName.destroy()
                output = recon.maimon_map(target)
                newWin = Toplevel()
                newWin.geometry("500x500")
                newWin.title("NMap Maimon Data")
                newWin.attributes('-topmost', True)
                menubar = Menu(root)
                savemenu = Menu(menubar, tearoff=0)
                savemenu.add_command(label="Save", command=lambda: save_file(output))
                menubar.add_cascade(label="File", menu=savemenu)
                newWin.configure(background='black', menu=menubar)
                T = Text(newWin, height=500, width=250, bg="black", fg="lime")
                T.pack()
                T.insert(END, "NMap Is Running... Please Wait :)")
                T.insert(END, output)
            else:
                tk.messagebox.showinfo('NMap Terminated','NMAP WAS STOPPED BY USER!')

        def maimon_map(winName):
            winName = Toplevel()
            winName.geometry("400x75")
            winName.title("Nmap")
            winName.configure(background="black")
            global info
            info = Label(winName, text = "Target: ", bg="black", fg="lime")
            info.place(x = 15, y = 10)
            info = StringVar()
            info_entry = Entry(winName, textvariable = info, width = "30", bg="black", fg="lime")
            info_entry.place(x = 150, y = 10)
            b1 = Button(winName, text="Start NMap", bg="black", fg="lime",
                        command=lambda : get_mmn_data(winName))
            b1.place(x=15,y=35)
            b2 = Button(winName, text="Cancel", bg="black", fg="lime",
                        command=winName.destroy)
            b2.place(x=150, y=35)

    ## FAST NMAP
        def get_fast_data(winName):
            MsgBox = tk.messagebox.askquestion ('Continue?','NMap can take a long time...\nDo you wish to continue?', parent=winName ,icon = 'warning')
            if MsgBox == 'yes':
                target = info.get()
                winName.destroy()
                output = recon.fast_map(target)
                newWin = Toplevel()
                newWin.geometry("500x500")
                newWin.title("NMap Fast Data")
                newWin.attributes('-topmost', True)
                menubar = Menu(root)
                savemenu = Menu(menubar, tearoff=0)
                savemenu.add_command(label="Save", command=lambda: save_file(output))
                menubar.add_cascade(label="File", menu=savemenu)
                newWin.configure(background='black', menu=menubar)
                T = Text(newWin, height=500, width=250, bg="black", fg="lime")
                T.pack()
                T.insert(END, "NMap Is Running... Please Wait :)")
                T.insert(END, output)
            else:
                tk.messagebox.showinfo('NMap Terminated','NMAP WAS STOPPED BY USER!')

        def fast_map(winName):
            winName = Toplevel()
            winName.geometry("400x75")
            winName.title("Nmap")
            winName.configure(background="black")
            global info
            info = Label(winName, text = "Target: ", bg="black", fg="lime")
            info.place(x = 15, y = 10)
            info = StringVar()
            info_entry = Entry(winName, textvariable = info, width = "30", bg="black", fg="lime")
            info_entry.place(x = 150, y = 10)
            b1 = Button(winName, text="Start NMap", bg="black", fg="lime",
                        command=lambda : get_fast_data(winName))
            b1.place(x=15,y=35)
            b2 = Button(winName, text="Cancel", bg="black", fg="lime",
                        command=winName.destroy)
            b2.place(x=150, y=35)

    ## NETWORK NMAP
        def get_ntwk_data(winName):
            MsgBox = tk.messagebox.askquestion ('Continue?','NMap can take a long time...\nDo you wish to continue?', parent=winName ,icon = 'warning')
            if MsgBox == 'yes':
                target = info.get()
                range = rg.get()
                winName.destroy()
                output = recon.net_map(target, range)
                newWin = Toplevel()
                newWin.geometry("500x500")
                newWin.title("NMap Network Data")
                newWin.attributes('-topmost', True)
                menubar = Menu(root)
                savemenu = Menu(menubar, tearoff=0)
                savemenu.add_command(label="Save", command=lambda: save_file(output))
                menubar.add_cascade(label="File", menu=savemenu)
                newWin.configure(background='black', menu=menubar)
                T = Text(newWin, height=500, width=250, bg="black", fg="lime")
                T.pack()
                T.insert(END, "NMap Is Running... Please Wait :)")
                T.insert(END, output)
            else:
                tk.messagebox.showinfo('NMap Terminated','NMAP WAS STOPPED BY USER!')

        def ntwk_map(winName):
            winName = Toplevel()
            winName.geometry("400x120")
            winName.title("Nmap")
            winName.configure(background="black")
            global info
            info = Label(winName, text = "Target: ", bg="black", fg="lime")
            global rg
            rg = Label(winName, text = "Range [8/16/24]: ", bg="black", fg="lime")
            info.place(x = 15, y = 10)
            rg.place(x = 15, y = 35)
            info = StringVar()
            rg = StringVar()
            info_entry = Entry(winName, textvariable = info, width = "30", bg="black", fg="lime")
            rg_entry = Entry(winName, textvariable = rg, width = "30", bg="black", fg="lime")
            info_entry.place(x = 150, y = 10)
            rg_entry.place(x = 150, y = 35)
            b1 = Button(winName, text="Start NMap", bg="black", fg="lime",
                        command=lambda : get_ntwk_data(winName))
            b1.place(x=15,y=75)
            b2 = Button(winName, text="Cancel", bg="black", fg="lime",
                        command=winName.destroy)
            b2.place(x=150, y=75)

    ## PORT NMAP
        def get_port_data(winName):
            MsgBox = tk.messagebox.askquestion ('Continue?','NMap can take a long time...\nDo you wish to continue?', parent=winName ,icon = 'warning')
            if MsgBox == 'yes':
                target = info.get()
                winName.destroy()
                output = recon.port_map(target)
                newWin = Toplevel()
                newWin.geometry("500x500")
                newWin.title("NMap Port Data")
                newWin.attributes('-topmost', True)
                menubar = Menu(root)
                savemenu = Menu(menubar, tearoff=0)
                savemenu.add_command(label="Save", command=lambda: save_file(output))
                menubar.add_cascade(label="File", menu=savemenu)
                newWin.configure(background='black', menu=menubar)
                T = Text(newWin, height=500, width=250, bg="black", fg="lime")
                T.pack()
                T.insert(END, "NMap Is Running... Please Wait :)")
                T.insert(END, output)
            else:
                tk.messagebox.showinfo('NMap Terminated','NMAP WAS STOPPED BY USER!')

        def port_map(winName):
            winName = Toplevel()
            winName.geometry("400x75")
            winName.title("Nmap")
            winName.configure(background="black")
            global info
            info = Label(winName, text = "Target: ", bg="black", fg="lime")
            info.place(x = 15, y = 10)
            info = StringVar()
            info_entry = Entry(winName, textvariable = info, width = "30", bg="black", fg="lime")
            info_entry.place(x = 150, y = 10)
            b1 = Button(winName, text="Start NMap", bg="black", fg="lime",
                        command=lambda : get_port_data(winName))
            b1.place(x=15,y=35)
            b2 = Button(winName, text="Cancel", bg="black", fg="lime",
                        command=winName.destroy)
            b2.place(x=150, y=35)

    ## OS NMAP
        def get_os_data(winName):
            MsgBox = tk.messagebox.askquestion ('Continue?','NMap can take a long time...\nDo you wish to continue?', parent=winName ,icon = 'warning')
            if MsgBox == 'yes':
                target = info.get()
                winName.destroy()
                output = recon.port_map(target)
                newWin = Toplevel()
                newWin.geometry("500x500")
                newWin.title("NMap OS Data")
                newWin.attributes('-topmost', True)
                menubar = Menu(root)
                savemenu = Menu(menubar, tearoff=0)
                savemenu.add_command(label="Save", command=lambda: save_file(output))
                menubar.add_cascade(label="File", menu=savemenu)
                newWin.configure(background='black', menu=menubar)
                T = Text(newWin, height=500, width=250, bg="black", fg="lime")
                T.pack()
                T.insert(END, "NMap Is Running... Please Wait :)")
                T.insert(END, output)
            else:
                tk.messagebox.showinfo('NMap Terminated','NMAP WAS STOPPED BY USER!')

        def os_map(winName):
            winName = Toplevel()
            winName.geometry("400x75")
            winName.title("Nmap")
            winName.configure(background="black")
            global info
            info = Label(winName, text = "Target: ", bg="black", fg="lime")
            info.place(x = 15, y = 10)
            info = StringVar()
            info_entry = Entry(winName, textvariable = info, width = "30", bg="black", fg="lime")
            info_entry.place(x = 150, y = 10)
            b1 = Button(winName, text="Start NMap", bg="black", fg="lime",
                        command=lambda : get_os_data(winName))
            b1.place(x=15,y=35)
            b2 = Button(winName, text="Cancel", bg="black", fg="lime",
                        command=winName.destroy)
            b2.place(x=150, y=35)

    ## VERS NMAP
        def get_vers_data(winName):
            MsgBox = tk.messagebox.askquestion ('Continue?','NMap can take a long time...\nDo you wish to continue?', parent=winName ,icon = 'warning')
            if MsgBox == 'yes':
                target = info.get()
                winName.destroy()
                output = recon.vers_map(target)
                newWin = Toplevel()
                newWin.geometry("500x500")
                newWin.title("NMap Version Data")
                newWin.attributes('-topmost', True)
                menubar = Menu(root)
                savemenu = Menu(menubar, tearoff=0)
                savemenu.add_command(label="Save", command=lambda: save_file(output))
                menubar.add_cascade(label="File", menu=savemenu)
                newWin.configure(background='black', menu=menubar)
                T = Text(newWin, height=500, width=250, bg="black", fg="lime")
                T.pack()
                T.insert(END, "NMap Is Running... Please Wait :)")
                T.insert(END, output)
            else:
                tk.messagebox.showinfo('NMap Terminated','NMAP WAS STOPPED BY USER!')

        def vers_map(winName):
            winName = Toplevel()
            winName.geometry("400x75")
            winName.title("Nmap")
            winName.configure(background="black")
            global info
            info = Label(winName, text = "Target: ", bg="black", fg="lime")
            info.place(x = 15, y = 10)
            info = StringVar()
            info_entry = Entry(winName, textvariable = info, width = "30", bg="black", fg="lime")
            info_entry.place(x = 150, y = 10)
            b1 = Button(winName, text="Start NMap", bg="black", fg="lime",
                        command=lambda : get_vers_data(winName))
            b1.place(x=15,y=35)
            b2 = Button(winName, text="Cancel", bg="black", fg="lime",
                        command=winName.destroy)
            b2.place(x=150, y=35)

    ## FIRE NMAP
        def get_fire_data(winName):
            MsgBox = tk.messagebox.askquestion ('Continue?','NMap can take a long time...\nDo you wish to continue?', parent=winName ,icon = 'warning')
            if MsgBox == 'yes':
                target = info.get()
                winName.destroy()
                output = recon.vers_map(target)
                newWin = Toplevel()
                newWin.geometry("500x500")
                newWin.title("NMap Firewall Data")
                newWin.attributes('-topmost', True)
                menubar = Menu(root)
                savemenu = Menu(menubar, tearoff=0)
                savemenu.add_command(label="Save", command=lambda: save_file(output))
                menubar.add_cascade(label="File", menu=savemenu)
                newWin.configure(background='black', menu=menubar)
                T = Text(newWin, height=500, width=250, bg="black", fg="lime")
                T.pack()
                T.insert(END, "NMap Is Running... Please Wait :)")
                T.insert(END, output)
            else:
                tk.messagebox.showinfo('NMap Terminated','NMAP WAS STOPPED BY USER!')

        def fire_map(winName):
            winName = Toplevel()
            winName.geometry("400x75")
            winName.title("Nmap")
            winName.configure(background="black")
            global info
            info = Label(winName, text = "Target: ", bg="black", fg="lime")
            info.place(x = 15, y = 10)
            info = StringVar()
            info_entry = Entry(winName, textvariable = info, width = "30", bg="black", fg="lime")
            info_entry.place(x = 150, y = 10)
            b1 = Button(winName, text="Start NMap", bg="black", fg="lime",
                        command=lambda : get_fire_data(winName))
            b1.place(x=15,y=35)
            b2 = Button(winName, text="Cancel", bg="black", fg="lime",
                        command=winName.destroy)
            b2.place(x=150, y=35)

    ## NP NMAP
        def get_np_data(winName):
            MsgBox = tk.messagebox.askquestion ('Continue?','NMap can take a long time...\nDo you wish to continue?', parent=winName ,icon = 'warning')
            if MsgBox == 'yes':
                target = info.get()
                winName.destroy()
                output = recon.vers_map(target)
                newWin = Toplevel()
                newWin.geometry("500x500")
                newWin.title("NMap NoPing Data")
                newWin.attributes('-topmost', True)
                menubar = Menu(root)
                savemenu = Menu(menubar, tearoff=0)
                savemenu.add_command(label="Save", command=lambda: save_file(output))
                menubar.add_cascade(label="File", menu=savemenu)
                newWin.configure(background='black', menu=menubar)
                T = Text(newWin, height=500, width=250, bg="black", fg="lime")
                T.pack()
                T.insert(END, "NMap Is Running... Please Wait :)")
                T.insert(END, output)
            else:
                tk.messagebox.showinfo('NMap Terminated','NMAP WAS STOPPED BY USER!')

        def np_map(winName):
            winName = Toplevel()
            winName.geometry("400x75")
            winName.title("Nmap")
            winName.configure(background="black")
            global info
            info = Label(winName, text = "Target: ", bg="black", fg="lime")
            info.place(x = 15, y = 10)
            info = StringVar()
            info_entry = Entry(winName, textvariable = info, width = "30", bg="black", fg="lime")
            info_entry.place(x = 150, y = 10)
            b1 = Button(winName, text="Start NMap", bg="black", fg="lime",
                        command=lambda : get_np_data(winName))
            b1.place(x=15,y=35)
            b2 = Button(winName, text="Cancel", bg="black", fg="lime",
                        command=winName.destroy)
            b2.place(x=150, y=35)

    ## STEALTH NMAP
        def get_stealth_data(winName):
            MsgBox = tk.messagebox.askquestion ('Continue?','NMap can take a long time...\nDo you wish to continue?', parent=winName ,icon = 'warning')
            if MsgBox == 'yes':
                target = info.get()
                winName.destroy()
                output = recon.stealth_map(target)
                newWin = Toplevel()
                newWin.geometry("500x500")
                newWin.title("NMap Stealth Data")
                newWin.attributes('-topmost', True)
                menubar = Menu(root)
                savemenu = Menu(menubar, tearoff=0)
                savemenu.add_command(label="Save", command=lambda: save_file(output))
                menubar.add_cascade(label="File", menu=savemenu)
                newWin.configure(background='black', menu=menubar)
                T = Text(newWin, height=500, width=250, bg="black", fg="lime")
                T.pack()
                T.insert(END, "NMap Is Running... Please Wait :)")
                T.insert(END, output)
            else:
                tk.messagebox.showinfo('NMap Terminated','NMAP WAS STOPPED BY USER!')

        def stealth_map(winName):
            winName = Toplevel()
            winName.geometry("400x75")
            winName.title("Nmap")
            winName.configure(background="black")
            global info
            info = Label(winName, text = "Target: ", bg="black", fg="lime")
            info.place(x = 15, y = 10)
            info = StringVar()
            info_entry = Entry(winName, textvariable = info, width = "30", bg="black", fg="lime")
            info_entry.place(x = 150, y = 10)
            b1 = Button(winName, text="Start NMap", bg="black", fg="lime",
                        command=lambda : get_stealth_data(winName))
            b1.place(x=15,y=35)
            b2 = Button(winName, text="Cancel", bg="black", fg="lime",
                        command=winName.destroy)
            b2.place(x=150, y=35)

    ## UDP NMAP
        def get_udp_data(winName):
            MsgBox = tk.messagebox.askquestion ('Continue?','NMap can take a long time...\nDo you wish to continue?', parent=winName ,icon = 'warning')
            if MsgBox == 'yes':
                target = info.get()
                winName.destroy()
                output = recon.udp_map(target)
                newWin = Toplevel()
                newWin.geometry("500x500")
                newWin.title("NMap UDP Data")
                newWin.attributes('-topmost', True)
                menubar = Menu(root)
                savemenu = Menu(menubar, tearoff=0)
                savemenu.add_command(label="Save", command=lambda: save_file(output))
                menubar.add_cascade(label="File", menu=savemenu)
                newWin.configure(background='black', menu=menubar)
                T = Text(newWin, height=500, width=250, bg="black", fg="lime")
                T.pack()
                T.insert(END, "NMap Is Running... Please Wait :)")
                T.insert(END, output)
            else:
                tk.messagebox.showinfo('NMap Terminated','NMAP WAS STOPPED BY USER!')

        def udp_map(winName):
            winName = Toplevel()
            winName.geometry("400x75")
            winName.title("Nmap")
            winName.configure(background="black")
            global info
            info = Label(winName, text = "Target: ", bg="black", fg="lime")
            info.place(x = 15, y = 10)
            info = StringVar()
            info_entry = Entry(winName, textvariable = info, width = "30", bg="black", fg="lime")
            info_entry.place(x = 150, y = 10)
            b1 = Button(winName, text="Start NMap", bg="black", fg="lime",
                        command=lambda : get_udp_data(winName))
            b1.place(x=15,y=35)
            b2 = Button(winName, text="Cancel", bg="black", fg="lime",
                        command=winName.destroy)
            b2.place(x=150, y=35)

    ## TCP NMAP
        def get_tcp_data(winName):
            MsgBox = tk.messagebox.askquestion ('Continue?','NMap can take a long time...\nDo you wish to continue?', parent=winName ,icon = 'warning')
            if MsgBox == 'yes':
                target = info.get()
                winName.destroy()
                output = recon.tcp_map(target)
                newWin = Toplevel()
                newWin.geometry("500x500")
                newWin.title("NMap TCP Data")
                newWin.attributes('-topmost', True)
                menubar = Menu(root)
                savemenu = Menu(menubar, tearoff=0)
                savemenu.add_command(label="Save", command=lambda: save_file(output))
                menubar.add_cascade(label="File", menu=savemenu)
                newWin.configure(background='black', menu=menubar)
                T = Text(newWin, height=500, width=250, bg="black", fg="lime")
                T.pack()
                T.insert(END, "NMap Is Running... Please Wait :)")
                T.insert(END, output)
            else:
                tk.messagebox.showinfo('NMap Terminated','NMAP WAS STOPPED BY USER!')

        def tcp_map(winName):
            winName = Toplevel()
            winName.geometry("400x75")
            winName.title("Nmap")
            winName.configure(background="black")
            global info
            info = Label(winName, text = "Target: ", bg="black", fg="lime")
            info.place(x = 15, y = 10)
            info = StringVar()
            info_entry = Entry(winName, textvariable = info, width = "30", bg="black", fg="lime")
            info_entry.place(x = 150, y = 10)
            b1 = Button(winName, text="Start NMap", bg="black", fg="lime",
                        command=lambda : get_tcp_data(winName))
            b1.place(x=15,y=35)
            b2 = Button(winName, text="Cancel", bg="black", fg="lime",
                        command=winName.destroy)
            b2.place(x=150, y=35)

    ## AUTO NMAP
        def get_auto_data(winName):
            MsgBox = tk.messagebox.askquestion ('Continue?','NMap can take a long time...\nDo you wish to continue?', parent=winName ,icon = 'warning')
            if MsgBox == 'yes':
                target = info.get()
                winName.destroy()
                try:
                    output = recon.def_target(target)
                except Exception as error:
                    output = "Something Went Wrong...\nPlease Check The Target Address And Try Again.\n\n%s" % error
                newWin = Toplevel()
                newWin.geometry("500x500")
                newWin.title("NMap Auto Data")
                newWin.attributes('-topmost', True)
                menubar = Menu(root)
                savemenu = Menu(menubar, tearoff=0)
                savemenu.add_command(label="Save", command=lambda: save_file(output))
                menubar.add_cascade(label="File", menu=savemenu)
                newWin.configure(background='black', menu=menubar)
                T = Text(newWin, height=500, width=250, bg="black", fg="lime")
                T.pack()
                T.insert(END, "NMap Is Running... Please Wait :)")
                T.insert(END, output)
            else:
                tk.messagebox.showinfo('NMap Terminated','NMAP WAS STOPPED BY USER!')

        def auto_map(winName):
            winName = Toplevel()
            winName.geometry("400x75")
            winName.title("Nmap")
            winName.configure(background="black")
            global info
            info = Label(winName, text = "Target: ", bg="black", fg="lime")
            info.place(x = 15, y = 10)
            info = StringVar()
            info_entry = Entry(winName, textvariable = info, width = "30", bg="black", fg="lime")
            info_entry.place(x = 150, y = 10)
            b1 = Button(winName, text="Start NMap", bg="black", fg="lime",
                        command=lambda : get_auto_data(winName))
            b1.place(x=15,y=35)
            b2 = Button(winName, text="Cancel", bg="black", fg="lime",
                        command=winName.destroy)
            b2.place(x=150, y=35)

    ## NMAP WINDOW LAYOUT
        def nmap_window():
            nWin = Toplevel()
            nWin.geometry("550x175-1+1")
            nWin.title("NMap")
            nWin.configure(background="black")
            info = Label(nWin, text = "Available Nmap Funcs.: ", bg="black", fg="lime")
            info.grid(row = 1, column = 0, padx=3, pady=3)
    # STD
            b1 = Button(nWin, text="Standard", bg="black", fg="lime",
                        command=lambda : std_map(nWin))
            b1.grid(row = 2 ,column=1, padx=3, pady=3)
    # CONN
            b2 = Button(nWin, text="Connect", bg="black", fg="lime",
                        command=lambda : conn_map(nWin))
            b2.grid(row = 2, column = 2, padx=3, pady=3)
    # ACK
            b3 = Button(nWin, text="ACK", bg="black", fg="lime",
                        command=lambda : ack_map(nWin))
            b3.grid(row = 2, column = 3, padx=3, pady=3)
    # MAIMON
            b4 = Button(nWin, text="Maimon", bg="black", fg="lime",
                        command=lambda : maimon_map(nWin))
            b4.grid(row = 2, column = 4, padx=3, pady=3)
    # FAST
            b5 = Button(nWin, text="Fast", bg="black", fg="lime",
                        command=lambda : fast_map(nWin))
            b5.grid(row = 3, column = 1, padx=3, pady=3)
    # NETWORK
            b6 = Button(nWin, text="Network", bg="black", fg="lime",
                        command=lambda : ntwk_map(nWin))
            b6.grid(row = 3, column = 2, padx=3, pady=3)
    # PORT
            b7 = Button(nWin, text="Port", bg="black", fg="lime",
                        command=lambda : port_map(nWin))
            b7.grid(row = 3, column = 3, padx=3, pady=3)
    # OS
            b8 = Button(nWin, text="OS", bg="black", fg="lime",
                        command=lambda : os_map(nWin))
            b8.grid(row = 3, column = 4, padx=3, pady=3)
    # VERS
            b9 = Button(nWin, text="Version", bg="black", fg="lime",
                        command=lambda : vers_map(nWin))
            b9.grid(row = 4, column = 1, padx=3, pady=3)
    # FIRE
            b10 = Button(nWin, text="Firewall", bg="black", fg="lime",
                        command=lambda : fire_map(nWin))
            b10.grid(row = 4, column = 2, padx=3, pady=3)
    # NOPING
            b11 = Button(nWin, text="No Ping", bg="black", fg="lime",
                        command=lambda : np_map(nWin))
            b11.grid(row = 4, column = 3, padx=3, pady=3)
    # STEALTH
            b12 = Button(nWin, text="Stealth", bg="black", fg="lime",
                        command=lambda : stealth_map(nWin))
            b12.grid(row = 4, column = 4, padx=3, pady=3)
    # NO_DNS
            b13 = Button(nWin, text="No DNS", bg="black", fg="lime",
                        command=lambda : no_dns_map(nWin))
            b13.grid(row = 5, column = 1, padx=3, pady=3)
    # UDP
            b14 = Button(nWin, text="UDP", bg="black", fg="lime",
                        command=lambda : udp_map(nWin))
            b14.grid(row = 5, column = 2, padx=3, pady=3)
    # TCP
            b15 = Button(nWin, text="TCP", bg="black", fg="lime",
                        command=lambda : tcp_map(nWin))
            b15.grid(row = 5, column = 3, padx=3, pady=3)
    # AUTO
            b16 = Button(nWin, text="Auto Map", bg="black", fg="lime",
                        command=lambda : auto_map(nWin))
            b16.grid(row = 5, column = 4, padx=3, pady=3)

        nmap_window()


## Recon WINDOW LAYOUT

    def recon_window():
        nWin = Toplevel()
        nWin.geometry("620x210-1+1")
        nWin.title("Recon")
        nWin.configure(background="black")
        info = Label(nWin, text = "Available Recon Funcs.: ", bg="black", fg="lime")
        info.grid(row = 1, column = 0, padx=3, pady=3)
#
        b1 = Button(nWin, text="Stalker", bg="black", fg="lime",
                    command=lambda : init_recon(nWin))
        b1.grid(row = 2 ,column=1, padx=3, pady=3)
#
        b2 = Button(nWin, text="Driftnet", bg="black", fg="lime",
                    command=lambda : driftnet(nWin))
        b2.grid(row = 2, column = 2, padx=3, pady=3)
#
        b3 = Button(nWin, text="WhoIs", bg="black", fg="lime",
                    command=lambda : whois(nWin))
        b3.grid(row = 2, column = 3, padx=3, pady=3)
#
        b4 = Button(nWin, text="Nmap", bg="black", fg="lime",
                    command=lambda : nmap_main(nWin))
        b4.grid(row = 2, column = 4, padx=3, pady=3)

        b5 = Button(nWin, text="Wafw00f", bg="black", fg="lime",
                    command=lambda : wafw00f(nWin))
        b5.grid(row = 3, column = 1, padx=3, pady=3)

        b6 = Button(nWin, text="p0f", bg="black", fg="lime",
                    command=lambda : p0f(nWin))
        b6.grid(row = 3, column = 2, padx=3, pady=3)

        b7 = Button(nWin, text="Arp Fingerprint", bg="black", fg="lime",
                    command=lambda : arp_fp(nWin))
        b7.grid(row = 3, column = 3, padx=3, pady=3)

        b8 = Button(nWin, text="DNSEnum", bg="black", fg="lime",
                    command=lambda : dnse(nWin))
        b8.grid(row = 3, column = 4, padx=3, pady=3)

        b9 = Button(nWin, text="DNSmap", bg="black", fg="lime",
                    command=lambda : dnsmap(nWin))
        b9.grid(row = 4, column = 1, padx=3, pady=3)

        b10 = Button(nWin, text="DNSTrace", bg="black", fg="lime",
                    command=lambda : dnst(nWin))
        b10.grid(row = 4, column = 2, padx=3, pady=3)

        b11 = Button(nWin, text="Golismero", bg="black", fg="#ff0000",
                    command=lambda : dev_msgbx())
        b11.grid(row = 4, column = 3, padx=3, pady=3)

        b12 = Button(nWin, text="ArpScan", bg="black", fg="lime",
                    command=lambda : arpscn(nWin))
        b12.grid(row = 4, column = 4, padx=3, pady=3)

        b13 = Button(nWin, text="Dig", bg="black", fg="lime",
                    command=lambda : digem(nWin))
        b13.grid(row = 5, column = 1, padx=3, pady=3)

        b14 = Button(nWin, text="NSLookup", bg="black", fg="lime",
                    command=lambda : nslook(nWin))
        b14.grid(row = 5, column = 2, padx=3, pady=3)

        b15 = Button(nWin, text="Nikto", bg="black", fg="lime",
                    command=lambda : nikto(nWin))
        b15.grid(row = 5, column = 3, padx=3, pady=3)

        b16 = Button(nWin, text="Arpspoof", bg="black", fg="lime",
                    command=lambda : arpspoof(nWin))
        b16.grid(row = 5, column = 4, padx=3, pady=3)

        b17 = Button(nWin, text="SysPrint", bg="black", fg="lime",
                    command=lambda : sysprint(nWin))
        b17.grid(row = 5, column = 4, padx=3, pady=3)

        b18 = Button(nWin, text="WebInfo", bg="black", fg="lime",
                    command=lambda : webinfo(nWin))
        b18.grid(row = 5, column = 4, padx=3, pady=3)

        b19 = Button(nWin, text="theHarvester", bg="black", fg="lime",
                    command=lambda : harvest(nWin))
        b19.grid(row = 5, column = 4, padx=3, pady=3)

        b20 = Button(nWin, text="IP Locator", bg="black", fg="lime",
                    command=lambda : iploc(nWin))
        b20.grid(row = 6, column = 1, padx=3, pady=3)

#        b20 = Button(nWin, text="", bg="black", fg="lime",
#                    command=lambda : (nWin))
#        b20.grid(row = 5, column = 4, padx=3, pady=3)


    recon_window()


# WEBSITE CONTROL
###########################################################################################
def wsc_main():

    def save_file(data):
        def get_data(winName, _data):
            window = winName
            fname = info.get()
            ksys.scrbe(fname, _data)
            window.destroy()
        _data = data
        newWin = Toplevel()
        newWin.geometry("500x100+1+1")
        newWin.title("Save File")
        newWin.configure(background='#000000')
        info = Label(newWin, text = "Save As: ", bg="black", fg="lime")
        info.place(x = 15, y = 10)
        info = StringVar()
        info_entry = Entry(newWin, textvariable = info, width = "30", bg="black", fg="lime")
        info_entry.insert(0, "ex: /home/Documents/doc.txt")
        info_entry.bind("<Button-1>", lambda event: clear_entry(event, info_entry))
        info_entry.place(x = 150, y = 10)
        b1 = Button(newWin, text="Save", bg="black", fg="lime",
                    command=lambda : get_data(newWin, _data.decode()))
        b1.place(x=15,y=55)
        b2 = Button(newWin, text="Cancel", bg="black", fg="lime",
                    command=newWin.destroy)
        b2.place(x=150, y=55)

# Save Site
    def get_site(winName):
        def getter(winName):
            url_addr = _url.get()
            winName.destroy()
            cur_dir = os.path.abspath(os.curdir)
            spyder.save_site(url=str(url_addr), filename="%s" % str(url_addr.replace("http://",
                             '').replace('https://', '').replace('/', '[fs]')))
            msgbx("Website Downloader", "Website Saved To %s/%s" %
                  (cur_dir, url_addr.replace('http://', '').replace('https://', '').replace('/', '[fs]')))

        winName = Toplevel()
        winName.geometry("400x75")
        winName.title("Website Downloader")
        winName.configure(background="black")
        _url = Label(winName, text = "URL: ", bg="black", fg="lime")
        _url.place(x = 15, y = 10)
        _url = StringVar()
        _url_entry = Entry(winName, textvariable = _url, width = "30", bg="black", fg="lime")
        _url_entry.place(x = 150, y = 10)
        b1 = Button(winName, text="Download", bg="black", fg="lime",
                    command=lambda : getter(winName))
        b1.place(x=15,y=35)
        b2 = Button(winName, text="Cancel", bg="black", fg="lime",
                    command=winName.destroy)
        b2.place(x=150, y=35)

# Print Site
    def print_site(winName):
        def getter(winName):
            winName.destroy()
            url = _url.get()
            winName.destroy()
            try:
                output = spyder.print_site(url)
            except Exception as error:
                return error
            newWin = Toplevel()
            newWin.geometry("750x750")
            newWin.title("%s" % url)
            newWin.attributes('-topmost', True)
            menubar = Menu(root)
            savemenu = Menu(menubar, tearoff=0)
            savemenu.add_command(label="Save", command=lambda: save_file(output))
            menubar.add_cascade(label="File", menu=savemenu)
            newWin.configure(background='black', menu=menubar)
            T = Text(newWin, height=500, width=250, bg="black", fg="lime")
            T.pack()
            T.insert(END, output)

        winName = Toplevel()
        winName.geometry("400x75")
        winName.title("Website Printer")
        winName.configure(background="black")
        _url = Label(winName, text = "URL: ", bg="black", fg="lime")
        _url.place(x = 15, y = 10)
        _url = StringVar()
        _url_entry = Entry(winName, textvariable = _url, width = "30", bg="black", fg="lime")
        _url_entry.place(x = 150, y = 10)
        b1 = Button(winName, text="Show Site", bg="black", fg="lime",
                    command=lambda : getter(winName))
        b1.place(x=15,y=35)
        b2 = Button(winName, text="Cancel", bg="black", fg="lime",
                    command=winName.destroy)
        b2.place(x=150, y=35)


## WSC WINDOW LAYOUT

    def wsc_window():
        nWin = Toplevel()
        nWin.geometry("600x75-1+1")
        nWin.title("Website Control")
        nWin.configure(background="black")
        info = Label(nWin, text = "Avail. Website Ctrl. Funcs.: ", bg="black", fg="lime")
        info.grid(row = 1, column = 0, padx=3, pady=3)
#
        b1 = Button(nWin, text="DL Website", bg="black", fg="lime",
                    command=lambda : get_site(nWin))
        b1.grid(row = 2 ,column=1, padx=3, pady=3)
#
        b2 = Button(nWin, text="Print Website", bg="black", fg="lime",
                    command=lambda : print_site(nWin))
        b2.grid(row = 2, column = 2, padx=3, pady=3)
##
#        b3 = Button(nWin, text="", bg="black", fg="lime",
#                    command=lambda : (nWin))
#        b3.grid(row = 2, column = 3, padx=3, pady=3)
##
#        b4 = Button(nWin, text="", bg="black", fg="lime",
#                    command=lambda : (nWin))
#        b4.grid(row = 2, column = 4, padx=3, pady=3)
#
#        b5 = Button(nWin, text="", bg="black", fg="lime",
#                    command=lambda : (nWin))
#        b5.grid(row = 3, column = 1, padx=3, pady=3)
#
#        b6 = Button(nWin, text="", bg="black", fg="lime",
#                    command=lambda : (nWin))
#        b6.grid(row = 3, column = 2, padx=3, pady=3)
#
#        b7 = Button(nWin, text="", bg="black", fg="lime",
#                    command=lambda : (nWin))
#        b7.grid(row = 3, column = 3, padx=3, pady=3)
#
#        b8 = Button(nWin, text="", bg="black", fg="lime",
#                    command=lambda : (nWin))
#        b8.grid(row = 3, column = 4, padx=3, pady=3)
##
#        b9 = Button(nWin, text="", bg="black", fg="lime",
#                    command=lambda : (nWin))
#        b9.grid(row = 4, column = 1, padx=3, pady=3)
##
#        b10 = Button(nWin, text="", bg="black", fg="lime",
#                    command=lambda : (nWin))
#        b10.grid(row = 4, column = 2, padx=3, pady=3)
##
#        b11 = Button(nWin, text="", bg="black", fg="lime",
#                    command=lambda : (nWin))
#        b11.grid(row = 4, column = 3, padx=3, pady=3)
##
#        b12 = Button(nWin, text="", bg="black", fg="lime",
#                    command=lambda : (nWin))
#        b12.grid(row = 4, column = 4, padx=3, pady=3)
##
#        b13 = Button(nWin, text="", bg="black", fg="lime",
#                    command=lambda : (nWin))
#        b13.grid(row = 5, column = 1, padx=3, pady=3)
##
#        b14 = Button(nWin, text="", bg="black", fg="lime",
#                    command=lambda : (nWin))
#        b14.grid(row = 5, column = 2, padx=3, pady=3)
##
#        b15 = Button(nWin, text="", bg="black", fg="lime",
#                    command=lambda : (nWin))
#        b15.grid(row = 5, column = 3, padx=3, pady=3)
##
#        b16 = Button(nWin, text="", bg="black", fg="lime",
#                    command=lambda : (nWin))
#        b16.grid(row = 5, column = 4, padx=3, pady=3)

    wsc_window()

######################################################################
# Network Ctrl.
def main_nwkctl():

    def save_file(data):
        def get_data(winName, _data):
            window = winName
            fname = info.get()
            ksys.scrbe(fname, _data)
            window.destroy()
        _data = data
        newWin = Toplevel()
        newWin.geometry("500x100")
        newWin.title("Save File")
        newWin.configure(background='black')
        info = Label(newWin, text = "Save As: ", bg="black", fg="lime")
        info.place(x = 15, y = 10)
        info = StringVar()
        info_entry = Entry(newWin, textvariable = info, width = "30", bg="black", fg="lime")
        info_entry.insert(0, "ex: /home/Documents/doc.txt")
        info_entry.bind("<Button-1>", lambda event: clear_entry(event, info_entry))
        info_entry.place(x = 150, y = 10)
        b1 = Button(newWin, text="Save", bg="black", fg="lime",
                    command=lambda : get_data(newWin, _data.decode()))
        b1.place(x=15,y=55)
        b2 = Button(newWin, text="Cancel", bg="black", fg="lime",
                    command=newWin.destroy)
        b2.place(x=150, y=55)

    def netdiscover(winName):
        def get_data(winName):
            interface = info.get()
            winName.destroy()
            try:
                output = recon.netdiscover(interface)
            except Exception as error:
                return error
            newWin = Toplevel()
            newWin.geometry("750x750")
            newWin.title("Netdiscover")
            newWin.attributes('-topmost', True)
            menubar = Menu(root)
            savemenu = Menu(menubar, tearoff=0)
            savemenu.add_command(label="Save", command=lambda: save_file(output))
            menubar.add_cascade(label="File", menu=savemenu)
            newWin.configure(background='black', menu=menubar)
            T = Text(newWin, height=500, width=250, bg="black", fg="lime")
            T.pack()
            T.insert(END, output.decode())
        MsgBox = tk.messagebox.askquestion ('Continue?','This function may cause a buffer overflow...\nDo you wish to continue?',icon = 'warning')
        if MsgBox == 'yes':
            winName = Toplevel()
            winName.geometry("450x75")
            winName.title("Netdiscover")
            winName.attributes('-topmost', True)
            winName.configure(background="black")
            info = Label(winName, text = "Interface:", bg="black", fg="lime")
            info.place(x = 15, y = 10)
            info = StringVar()
            info_entry = Entry(winName, textvariable = info, width = "30", bg="black", fg="lime")
            info_entry.place(x = 170, y = 10)
            b1 = Button(winName, text="Netdiscover", bg="black", fg="lime",
                        command=lambda : get_data(winName))
            b1.place(x=100,y=35)
            b2 = Button(winName, text="Cancel", bg="black", fg="lime",
                        command=winName.destroy)
            b2.place(x=250, y=35)
        else:
            tk.messagebox.showinfo("Netdiscover Terminated!", "Netdiscover was terminated by the user!")
            winName.destroy()

# Ifconfig Data
    def i_con(winName):
        """ Show data from ifconfig -a """
        def ifconfig():
            data = subprocess.Popen(["ifconfig", "-a"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            std_out, std_err = data.communicate()
            if len(std_err) >= 1:
                return std_err
            else:
                return std_out

        def ifcon():
            newWin = Toplevel()
            newWin.geometry("750x750")
            newWin.title("Ifconfig")
            menubar = Menu(root)
            savemenu = Menu(menubar, tearoff=0)
            savemenu.add_command(label="Save", command=lambda: save_file(output))
            menubar.add_cascade(label="File", menu=savemenu)
            newWin.configure(background='black', menu=menubar)
            T = Text(newWin, height=500, width=250, bg="black", fg="lime")
            T.pack()
            output = ifconfig()
            T.insert(END, output.decode())

        ifcon()

    def ls_ap(winName):
        """ List running access points """
        def get_data():
            output = ap_maker.ls_aps()
            newWin = Toplevel()
            newWin.geometry("750x500")
            newWin.title("Currently Running APs")

            menubar = Menu(root)
            savemenu = Menu(menubar, tearoff=0)
            savemenu.add_command(label="Save", command=lambda: save_file(output))
            menubar.add_cascade(label="File", menu=savemenu)
            newWin.configure(background='black', menu=menubar)

            T = Text(newWin, height=500, width=250, bg="black", fg="lime")
            T.pack()
            T.insert(END, output)

        get_data()

    def stopap(winName):
        """Stop a running access point"""
        def get_data(winName):
            interface = info.get()
            winName.destroy()
            try:
                output = ap_maker.stop_ap(interface)
            except Exception as error:
                output = "THERE WAS A PROBLEM STOPPING THE ACCESS POINT!!!\n\n%s" % error
            newWin = Toplevel()
            newWin.geometry("500x500")
            newWin.title("STOP AP")
            newWin.attributes('-topmost', True)

            menubar = Menu(root)
            savemenu = Menu(menubar, tearoff=0)
            savemenu.add_command(label="Save", command=lambda: save_file(output))
            menubar.add_cascade(label="File", menu=savemenu)
            newWin.configure(background='black', menu=menubar)

            T = Text(newWin, height=500, width=250, bg="black", fg="lime")
            T.pack()
            T.insert(END, output)

        winName = Toplevel()
        winName.geometry("400x100")
        winName.title("Stop AP")
        winName.configure(background="black")
        info = Label(winName, text = "Interface: ", bg="black", fg="lime")
        info.place(x = 15, y = 10)
        info = StringVar()
        info_entry = Entry(winName, textvariable = info, width = "30", bg="black", fg="lime")
        info_entry.place(x = 150, y = 10)

        b1 = Button(winName, text="Stop AP", bg="black", fg="lime",
                    command=lambda : get_data(winName))
        b1.place(x=15,y=65)
        b2 = Button(winName, text="Cancel", bg="black", fg="lime",
                    command=winName.destroy)
        b2.place(x=150, y=65)

    def lsc(winName):
        """List clients connected to specified access point"""
        def get_data(winName):
            id = info.get()
            winName.destroy()
            try:
                output = ap_maker.ls_clients(id)
            except Exception as error:
                msgbx("ERROR!","THERE WAS A PROBLEM GETTING THE AP CLIENTS!!!\n\n%s" % error)
            newWin = Toplevel()
            newWin.geometry("500x500")
            newWin.title("AP Clients")
            newWin.attributes('-topmost', True)

            menubar = Menu(root)
            savemenu = Menu(menubar, tearoff=0)
            savemenu.add_command(label="Save", command=lambda: save_file(output))
            menubar.add_cascade(label="File", menu=savemenu)
            newWin.configure(background='black', menu=menubar)

            T = Text(newWin, height=500, width=250, bg="black", fg="lime")
            T.pack()
            T.insert(END, output)

        winName = Toplevel()
        winName.geometry("400x100")
        winName.title("AP Clients")
        winName.configure(background="black")
        info = Label(winName, text = "Interface/ID: ", bg="black", fg="lime")
        info.place(x = 15, y = 10)
        info = StringVar()
        info_entry = Entry(winName, textvariable = info, width = "30", bg="black", fg="lime")
        info_entry.place(x = 150, y = 10)

        b1 = Button(winName, text="Get Clients", bg="black", fg="lime",
                    command=lambda : get_data(winName))
        b1.place(x=15,y=65)
        b2 = Button(winName, text="Cancel", bg="black", fg="lime",
                    command=winName.destroy)
        b2.place(x=150, y=65)

    def opap(winName):
        """Create 'open' access point [No Password Protection]"""
        def get_data(winName):
            apinterface = api.get()
            i_interface = ii.get()
            ap_name = apname.get()
            winName.destroy()
            try:
                output = ap_maker.open_ap(apinterface, i_interface, ap_name)
            except Exception as error:
                output = error

                newWin = Toplevel()
                newWin.geometry("750x750")
                newWin.title("Open AP Error")
                newWin.attributes('-topmost', True)
                menubar = Menu(root)
                savemenu = Menu(menubar, tearoff=0)
                savemenu.add_command(label="Save", command=lambda: save_file(output))
                menubar.add_cascade(label="File", menu=savemenu)
                newWin.configure(background='black', menu=menubar)
                T = Text(newWin, height=500, width=250, bg="black", fg="lime")
                T.pack()
                T.insert(END, output.decode())

        winName = Toplevel()
        winName.geometry("450x135")
        winName.title("Create Open AP")
        winName.attributes('-topmost', True)
        winName.configure(background="black")
        api = Label(winName, text = "AP Interface:", bg="black", fg="lime")
        ii = Label(winName, text = "Inet Interface:", bg="black", fg="lime")
        apname = Label(winName, text = "AP Name:", bg="black", fg="lime")
        api.place(x = 15, y = 10)
        ii.place(x = 15, y = 35)
        apname.place(x = 15, y = 55)
        api = StringVar()
        ii = StringVar()
        apname = StringVar()
        api_entry = Entry(winName, textvariable = api, width = "30", bg="black", fg="lime")
        ii_entry = Entry(winName, textvariable = ii, width = "30", bg="black", fg="lime")
        apname_entry = Entry(winName, textvariable = apname, width = "30", bg="black", fg="lime")
        api_entry.place(x = 170, y = 10)
        ii_entry.place(x = 170, y = 35)
        apname_entry.place(x = 170, y = 55)
        b1 = Button(winName, text="Create AP", bg="black", fg="lime",
                    command=lambda : get_data(winName))
        b1.place(x=100,y=100)
        b2 = Button(winName, text="Cancel", bg="black", fg="lime",
                    command=winName.destroy)
        b2.place(x=250, y=100)

    def ppap(winName):
        """Standard password protected access point"""
        def get_data(winName):
            apinterface = api.get()
            i_interface = ii.get()
            password = pswd.get()
            ap_name = apname.get()
            isolate = CheckVar1.get()
            hidden = CheckVar2.get()
            winName.destroy()
            if isolate == 1:
                iso = 1
            else:
                iso = 0
            if hidden == 1:
                hid = 1
            else:
                hid = 0
            try:
                output = ap_maker.std_ap(apinterface, i_interface, ap_name, password, iso, hid)

            except Exception as error:
                output = error

            newWin = Toplevel()
            newWin.geometry("750x750")
            newWin.title("AP")
            newWin.attributes('-topmost', True)
            menubar = Menu(root)
            savemenu = Menu(menubar, tearoff=0)
            savemenu.add_command(label="Save", command=lambda: save_file(output))
            menubar.add_cascade(label="File", menu=savemenu)
            newWin.configure(background='black', menu=menubar)
            T = Text(newWin, height=500, width=250, bg="black", fg="lime")
            T.pack()
            T.insert(END, output)

        winName = Toplevel()
        winName.geometry("450x180")
        winName.title("Create Pwd. Prot. AP")
        winName.attributes('-topmost', True)
        winName.configure(background="black")
        api = Label(winName, text = "AP Interface:", bg="black", fg="lime")
        ii = Label(winName, text = "Inet Interface:", bg="black", fg="lime")
        pswd = Label(winName, text = "Password:", bg="black", fg="lime")
        apname = Label(winName, text = "AP Name:", bg="black", fg="lime")
        api.place(x = 15, y = 10)
        ii.place(x = 15, y = 35)
        pswd.place(x = 15, y = 55)
        apname.place(x = 15, y = 75)
        api = StringVar()
        ii = StringVar()
        pswd = StringVar()
        apname = StringVar()
        api_entry = Entry(winName, textvariable = api, width = "30", bg="black", fg="lime")
        ii_entry = Entry(winName, textvariable = ii, width = "30", bg="black", fg="lime")
        pswd_entry = Entry(winName, textvariable = pswd, width = "30", bg="black", fg="lime")
        apname_entry = Entry(winName, textvariable = apname, width = "30", bg="black", fg="lime")
        api_entry.place(x = 170, y = 10)
        ii_entry.place(x = 170, y = 35)
        pswd_entry.place(x = 170, y = 55)
        apname_entry.place(x = 170, y = 75)
        CheckVar1 = IntVar()
        CheckVar2 = IntVar()
        C1 = Checkbutton(winName, text = "Isolate Clients", variable = CheckVar1, \
                         onvalue = 1, offvalue = 0, height=1, \
                         width = 20, bg = "black", fg = "lime")
        C2 = Checkbutton(winName, text = "Hidden Network", variable = CheckVar2, \
                         onvalue = 1, offvalue = 0, height=1, \
                         width = 20, bg = "black", fg = "lime")
        C1.place(x = 170, y = 98)
        C2.place(x = 170, y = 118)
        b1 = Button(winName, text="Create AP", bg="black", fg="lime",
                    command=lambda : get_data(winName))
        b1.place(x=100,y=145)
        b2 = Button(winName, text="Cancel", bg="black", fg="lime",
                    command=winName.destroy)
        b2.place(x=250, y=145)

    def net_list(winName):
        """List nearby wifi networks"""
        def get_data(winName):
            interface = api.get()
            net_list = iface.simple_iw(interface)
            newWin = Toplevel()
            newWin.geometry("750x750")
            newWin.title("Nearby Networks")
            newWin.attributes('-topmost', True)
            menubar = Menu(root)
            savemenu = Menu(menubar, tearoff=0)
            savemenu.add_command(label="Save", command=lambda: save_file(output))
            menubar.add_cascade(label="File", menu=savemenu)
            newWin.configure(background='black', menu=menubar)
            T = Text(newWin, height=500, width=250, bg="black", fg="lime")
            T.pack()
            T.insert(END, netlist)

        winName = Toplevel()
        winName.geometry("450x75")
        winName.title("Nearby Networks")
        winName.configure(background='black')
        api = Label(winName, text = "Interface:", bg="black", fg="lime")
        api.place(x = 15, y = 10)
        api = StringVar()
        api_entry = Entry(winName, textvariable = api, width = "30", bg="black", fg="lime")
        api_entry.place(x = 150, y = 10)
        b1 = Button(winName, text="Search", bg="black", fg="lime",
                    command=lambda : get_data(winName))
        b1.place(x=100,y=50)
        b2 = Button(winName, text="Cancel", bg="black", fg="lime",
                    command=winName.destroy)
        b2.place(x=250, y=50)


    def nwctrl_window():
        """Network Control Window"""
        nWin = Toplevel()
        nWin.geometry("620x120-1+1")
        nWin.title("Network Control")
        nWin.configure(background="black")
        info = Label(nWin, text = "Avail. Network Ctrl. Funcs.: ", bg="black", fg="lime")
        info.grid(row = 1, column = 0, padx=3, pady=3)
#
        b1 = Button(nWin, text="Netdiscover", bg="black", fg="lime",
                    command=lambda : netdiscover(nWin))
        b1.grid(row = 2 ,column=1, padx=3, pady=3)

        b2 = Button(nWin, text="Ifconfig", bg="black", fg="lime",
                    command=lambda : i_con(nWin))
        b2.grid(row = 2, column = 2, padx=3, pady=3)
#
        b3 = Button(nWin, text="List APs", bg="black", fg="lime",
                    command=lambda : ls_ap(nWin))
        b3.grid(row = 2, column = 3, padx=3, pady=3)
#
        b4 = Button(nWin, text="List AP Clients", bg="black", fg="lime",
                    command=lambda : lsc(nWin))
        b4.grid(row = 2, column = 4, padx=3, pady=3)
#
        b5 = Button(nWin, text="Stop AP", bg="black", fg="lime",
                    command=lambda : stopap(nWin))
        b5.grid(row = 3, column = 1, padx=3, pady=3)
#
        b6 = Button(nWin, text="Open AP", bg="black", fg="lime",
                    command=lambda : opap(nWin))
        b6.grid(row = 3, column = 2, padx=3, pady=3)
#
        b7 = Button(nWin, text="Pwd AP", bg="black", fg="lime",
                    command=lambda : ppap(nWin))
        b7.grid(row = 3, column = 3, padx=3, pady=3)
#
        b8 = Button(nWin, text="Nearby Wifi", bg="black", fg="red",
                    command=lambda : dev_msgbx())
        b8.grid(row = 3, column = 4, padx=3, pady=3)
##
#        b9 = Button(nWin, text="", bg="black", fg="lime",
#                    command=lambda : (nWin))
#        b9.grid(row = 4, column = 1, padx=3, pady=3)
##
#        b10 = Button(nWin, text="", bg="black", fg="lime",
#                    command=lambda : (nWin))
#        b10.grid(row = 4, column = 2, padx=3, pady=3)
##
#        b11 = Button(nWin, text="", bg="black", fg="lime",
#                    command=lambda : (nWin))
#        b11.grid(row = 4, column = 3, padx=3, pady=3)
##
#        b12 = Button(nWin, text="", bg="black", fg="lime",
#                    command=lambda : (nWin))
#        b12.grid(row = 4, column = 4, padx=3, pady=3)
##
#        b13 = Button(nWin, text="", bg="black", fg="lime",
#                    command=lambda : (nWin))
#        b13.grid(row = 5, column = 1, padx=3, pady=3)
##
#        b14 = Button(nWin, text="", bg="black", fg="lime",
#                    command=lambda : (nWin))
#        b14.grid(row = 5, column = 2, padx=3, pady=3)
##
#        b15 = Button(nWin, text="", bg="black", fg="lime",
#                    command=lambda : (nWin))
#        b15.grid(row = 5, column = 3, padx=3, pady=3)
##
#        b16 = Button(nWin, text="", bg="black", fg="lime",
#                    command=lambda : (nWin))
#        b16.grid(row = 5, column = 4, padx=3, pady=3)

    nwctrl_window()

# Offense
###########################################################################################
def offense_main():

    def save_file(data):
        def get_data(winName, _data):
            window = winName
            fname = info.get()
            ksys.scrbe(fname, _data)
            window.destroy()
        _data = data
        newWin = Toplevel()
        newWin.geometry("500x100")
        newWin.title("Save File")
        newWin.configure(background='black')
        info = Label(newWin, text = "Save As: ", bg="black", fg="lime")
        info.place(x = 15, y = 10)
        info = StringVar()
        info_entry = Entry(newWin, textvariable = info, width = "30", bg="black", fg="lime")
        info_entry.insert(0, "ex: /home/Documents/doc.txt")
        info_entry.bind("<Button-1>", lambda event: clear_entry(event, info_entry))
        info_entry.place(x = 150, y = 10)
        b1 = Button(newWin, text="Save", bg="black", fg="lime",
                    command=lambda : get_data(newWin, _data.decode()))
        b1.place(x=15,y=55)
        b2 = Button(newWin, text="Cancel", bg="black", fg="lime",
                    command=newWin.destroy)
        b2.place(x=150, y=55)

    def wash(winName):
        def getter(winName):
            winName.destroy()
            interface = _int.get()
            winName.destroy()
            try:
                print(interface)
                print("Starting Wash...")
                output = bad_ideas.wash(interface)
                print(output)
            except Exception as error:
                return error
            newWin = Toplevel()
            newWin.geometry("750x750")
            newWin.title("Wash")
            newWin.attributes('-topmost', True)
            menubar = Menu(root)
            savemenu = Menu(menubar, tearoff=0)
            savemenu.add_command(label="Save", command=lambda: save_file(output))
            menubar.add_cascade(label="File", menu=savemenu)
            newWin.configure(background='black', menu=menubar)
            T = Text(newWin, height=500, width=250, bg="black", fg="lime")
            T.pack()
            T.insert(END, output)

        winName = Toplevel()
        winName.geometry("400x75")
        winName.title("Wash")
        winName.configure(background="black")
        _int = Label(winName, text = "Interface: ", bg="black", fg="lime")
        _int.place(x = 15, y = 10)
        _int = StringVar()
        _int_entry = Entry(winName, textvariable = _int, width = "30", bg="black", fg="lime")
        _int_entry.place(x = 150, y = 10)
        b1 = Button(winName, text="Wash It", bg="black", fg="lime",
                    command=lambda : getter(winName))
        b1.place(x=15,y=35)
        b2 = Button(winName, text="Cancel", bg="black", fg="lime",
                    command=winName.destroy)
        b2.place(x=150, y=35)

    def off_window():
        nWin = Toplevel()
        nWin.geometry("600x75-1+1")
        nWin.title("0FF3N53")
        nWin.configure(background="black")
        info = Label(nWin, text = "Avail. Offensive Funcs.: ", bg="black", fg="lime")
        info.grid(row = 1, column = 0, padx=3, pady=3)
#
        b1 = Button(nWin, text="Wash", bg="black", fg="lime",
                    command=lambda : wash(nWin))
        b1.grid(row = 2 ,column=1, padx=3, pady=3)
#
#        b2 = Button(nWin, text="", bg="black", fg="lime",
#                    command=lambda : (nWin))
#        b2.grid(row = 2, column = 2, padx=3, pady=3)
##
#        b3 = Button(nWin, text="", bg="black", fg="lime",
#                    command=lambda : (nWin))
#        b3.grid(row = 2, column = 3, padx=3, pady=3)
##
#        b4 = Button(nWin, text="", bg="black", fg="lime",
#                    command=lambda : (nWin))
#        b4.grid(row = 2, column = 4, padx=3, pady=3)
#
#        b5 = Button(nWin, text="", bg="black", fg="lime",
#                    command=lambda : (nWin))
#        b5.grid(row = 3, column = 1, padx=3, pady=3)
#
#        b6 = Button(nWin, text="", bg="black", fg="lime",
#                    command=lambda : (nWin))
#        b6.grid(row = 3, column = 2, padx=3, pady=3)
#
#        b7 = Button(nWin, text="", bg="black", fg="lime",
#                    command=lambda : (nWin))
#        b7.grid(row = 3, column = 3, padx=3, pady=3)
#
#        b8 = Button(nWin, text="", bg="black", fg="lime",
#                    command=lambda : (nWin))
#        b8.grid(row = 3, column = 4, padx=3, pady=3)
##
#        b9 = Button(nWin, text="", bg="black", fg="lime",
#                    command=lambda : (nWin))
#        b9.grid(row = 4, column = 1, padx=3, pady=3)
##
#        b10 = Button(nWin, text="", bg="black", fg="lime",
#                    command=lambda : (nWin))
#        b10.grid(row = 4, column = 2, padx=3, pady=3)
##
#        b11 = Button(nWin, text="", bg="black", fg="lime",
#                    command=lambda : (nWin))
#        b11.grid(row = 4, column = 3, padx=3, pady=3)
##
#        b12 = Button(nWin, text="", bg="black", fg="lime",
#                    command=lambda : (nWin))
#        b12.grid(row = 4, column = 4, padx=3, pady=3)
##
#        b13 = Button(nWin, text="", bg="black", fg="lime",
#                    command=lambda : (nWin))
#        b13.grid(row = 5, column = 1, padx=3, pady=3)
##
#        b14 = Button(nWin, text="", bg="black", fg="lime",
#                    command=lambda : (nWin))
#        b14.grid(row = 5, column = 2, padx=3, pady=3)
##
#        b15 = Button(nWin, text="", bg="black", fg="lime",
#                    command=lambda : (nWin))
#        b15.grid(row = 5, column = 3, padx=3, pady=3)
##
#        b16 = Button(nWin, text="", bg="black", fg="lime",
#                    command=lambda : (nWin))
#        b16.grid(row = 5, column = 4, padx=3, pady=3)

    off_window()

# Defense
###########################################################################################


# Misc.
###########################################################################################
def main_misc():

    def flck(file_name):
        ck = subprocess.Popen(["ruby", "bin/flck", "%s" % file_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        std_out, std_err = ck.communicate()
        if len(str(std_err)) >= 1:
            return std_err
        else:
            return std_out

    def ck_file(winName):
        def get_data(winName):
            file_name = info.get()
            winName.destroy()
            newWin = Toplevel()
            newWin.geometry("750x750")
            newWin.title("File Check")
            menubar = Menu(root)
            savemenu = Menu(menubar, tearoff=0)
            savemenu.add_command(label="Save", command=lambda: save_file(output))
            menubar.add_cascade(label="File", menu=savemenu)
            newWin.configure(background='black', menu=menubar)
            T = Text(newWin, height=500, width=250, bg="black", fg="lime")
            T.pack()
            output = flck(file_name)
            T.insert(END, output)

        winName = Toplevel()
        winName.geometry("400x75")
        winName.title("File Check")
        winName.configure(background="black")
        info = Label(winName, text = "File Name: ", bg="black", fg="lime")
        info.place(x = 15, y = 10)
        info = StringVar()
        info_entry = Entry(winName, textvariable = info, width = "30", bg="black", fg="lime")
        info_entry.place(x = 150, y = 10)
        b1 = Button(winName, text="Check File", bg="black", fg="lime",
                    command=lambda : get_data(winName))
        b1.place(x=15,y=35)
        b2 = Button(winName, text="Cancel", bg="black", fg="lime",
                    command=winName.destroy)
        b2.place(x=150, y=35)

    def os_info(winName):
        newWin = Toplevel()
        newWin.geometry("750x750")
        newWin.title("OS Information")
        menubar = Menu(root)
        savemenu = Menu(menubar, tearoff=0)
        savemenu.add_command(label="Save", command=lambda: save_file(output))
        menubar.add_cascade(label="File", menu=savemenu)
        newWin.configure(background='black', menu=menubar)
        T = Text(newWin, height=500, width=250, bg="black", fg="lime")
        T.pack()
        output = subprocess.Popen(["bin/os_check.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        std_out, std_err = output.communicate()
        if len(std_out) >= 1:
            T.insert(END, std_out)
        else:
            T.insert(END, std_err)

    def ck_serv(service):
        ck = subprocess.Popen(["sudo", "systemctl", "status", "%s" % service], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        std_out, std_err = ck.communicate()
        if len(str(std_err)) >= 1:
            return std_err
        else:
            return std_out

    def serv_stat(winName):
        def get_data(winName):
            service_name = info.get()
            winName.destroy()
            newWin = Toplevel()
            newWin.geometry("750x750")
            newWin.title("Service Check")
            menubar = Menu(root)
            savemenu = Menu(menubar, tearoff=0)
            savemenu.add_command(label="Save", command=lambda: save_file(output))
            menubar.add_cascade(label="File", menu=savemenu)
            newWin.configure(background='black', menu=menubar)
            T = Text(newWin, height=500, width=250, bg="black", fg="lime")
            T.pack()
            output = ck_serv(service_name)
            T.insert(END, output)

        winName = Toplevel()
        winName.geometry("400x75")
        winName.title("Service Check")
        winName.configure(background="black")
        info = Label(winName, text = "Service Name: ", bg="black", fg="lime")
        info.place(x = 15, y = 10)
        info = StringVar()
        info_entry = Entry(winName, textvariable = info, width = "30", bg="black", fg="lime")
        info_entry.place(x = 150, y = 10)
        b1 = Button(winName, text="Check Service", bg="black", fg="lime",
                    command=lambda : get_data(winName))
        b1.place(x=15,y=35)
        b2 = Button(winName, text="Cancel", bg="black", fg="lime",
                    command=winName.destroy)
        b2.place(x=150, y=35)

    def ck_dir(path):
        ck = subprocess.Popen(["ls", "%s" % path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        std_out, std_err = ck.communicate()
        if len(str(std_err)) >= 1:
            return std_err
        else:
            return std_out

    def d_con(winName):
        def get_data(winName):
            dir_path = info.get()
            winName.destroy()
            newWin = Toplevel()
            newWin.geometry("750x750")
            newWin.title("Directory Check")
            menubar = Menu(root)
            savemenu = Menu(menubar, tearoff=0)
            savemenu.add_command(label="Save", command=lambda: save_file(output))
            menubar.add_cascade(label="File", menu=savemenu)
            newWin.configure(background='black', menu=menubar)
            T = Text(newWin, height=500, width=250, bg="black", fg="lime")
            T.pack()
            output = ksys.dcon(dir_path)
            T.insert(END, output)

        winName = Toplevel()
        winName.geometry("400x75")
        winName.title("Directory Check")
        winName.configure(background="black")
        info = Label(winName, text = "Directory Path: ", bg="black", fg="lime")
        info.place(x = 15, y = 10)
        info = StringVar()
        info_entry = Entry(winName, textvariable = info, width = "30", bg="black", fg="lime")
        info_entry.place(x = 150, y = 10)
        b1 = Button(winName, text="Check Directory", bg="black", fg="lime",
                    command=lambda : get_data(winName))
        b1.place(x=15,y=35)
        b2 = Button(winName, text="Cancel", bg="black", fg="lime",
                    command=winName.destroy)
        b2.place(x=150, y=35)

    # Get_User

    def gt_user(winName):

        def get_data():
            newWin = Toplevel()
            newWin.geometry("300x50")
            newWin.title("Get User")
            menubar = Menu(root)
            savemenu = Menu(menubar, tearoff=0)
            savemenu.add_command(label="Save", command=lambda: save_file(output))
            menubar.add_cascade(label="File", menu=savemenu)
            newWin.configure(background='black', menu=menubar)
            T = Text(newWin, height=500, width=250, bg="black", fg="lime")
            T.pack()
            username = ksys.get_user()
            output = "Your Username Is:   " + str(username).strip()
            T.insert(END, output)

        get_data()

    # Check Battery

    def batt_info(winName):
        def get_data():
            newWin = Toplevel()
            newWin.geometry("500x500")
            newWin.title("Battery Status")
            menubar = Menu(root)
            savemenu = Menu(menubar, tearoff=0)
            savemenu.add_command(label="Save", command=lambda: save_file(output))
            menubar.add_cascade(label="File", menu=savemenu)
            newWin.configure(background='black', menu=menubar)
            T = Text(newWin, height=500, width=250, bg="black", fg="lime")
            T.pack()
            output = ksys.battery()
            T.insert(END, output)

        get_data()

    # Check Memory
    def mem_ck(winName):
        def get_data():
            output = ksys.memc()
            data = subprocess.Popen(["free", "-h"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            std_out, std_err = data.communicate()
            if len(std_out) >= 1:
                d_out = std_out
            else:
                d_out = std_err
            newWin = Toplevel()
            newWin.geometry("750x500")
            newWin.title("Memory")
            menubar = Menu(root)
            savemenu = Menu(menubar, tearoff=0)
            savemenu.add_command(label="Save", command=lambda: save_file(output))
            menubar.add_cascade(label="File", menu=savemenu)
            newWin.configure(background='black', menu=menubar)
            T = Text(newWin, height=500, width=500, bg="black", fg="lime")
            T.pack()
            _Win = Toplevel()
            _Win.geometry("750x75")
            _Win.title("Memory")
            _Win.configure(background='black', menu=menubar)
            D = Text(_Win, height=500, width=500, bg="black", fg="lime")
            D.pack()
            T.insert(END, output.decode())
            D.insert(END, d_out.decode())

        get_data()

    # Service List
    def sv_lst(winName):
        def get_data():
            services = []
            pipes = subprocess.Popen(["systemctl", "-at", "service"],
                                      stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE)
            std_out, std_err = pipes.communicate()
            if len(std_err) == 0:
                data = std_out.decode().split("\n")
            svcs = ""
            for item in data:
                svcs = svcs + "\n" + item
            newWin = Toplevel()
            newWin.geometry("750x750")
            newWin.title("Service List")
            menubar = Menu(root)
            savemenu = Menu(menubar, tearoff=0)
            savemenu.add_command(label="Save", command=lambda: save_file(output))
            menubar.add_cascade(label="File", menu=savemenu)
            newWin.configure(background='black', menu=menubar)
            T = Text(newWin, height=500, width=250, bg="black", fg="lime")
            T.pack()
            T.insert(END, svcs)

        get_data()

    def kali_help(winName):

        def open_page(prog_name, url):
#                subprocess.Popen(["/usr/bin/firefox", "%s" % url])
            headers = {"User-Agent": "my web scraping program. contact me at admin@domain.com"}
            page = requests.get(url, headers=headers)
            soup = bs(page.content, 'html.parser')
            info = soup.find("section", {"id": "content"}).get_text().rstrip()
            try:
                newWin = Toplevel()
                newWin.geometry("750x750")
                newWin.title(prog_name)
                menubar = Menu(root)
                savemenu = Menu(menubar, tearoff=0)
                savemenu.add_command(label="Save", command=lambda: save_file(info))
                menubar.add_cascade(label="File", menu=savemenu)
                newWin.configure(background='black', menu=menubar)
                T = Text(newWin, height=500, width=250, bg="black", fg="lime")
                T.pack()
                T.insert(END, info)

            except Exception as error:
                newWin = Toplevel()
                newWin.geometry("500x500")
                newWin.title("ERROR")
                newWin.configure(background='black')
                T = Text(newWin, height=500, width=250, bg="black", fg="lime")
                T.pack()
                T.insert(END, "%s\n%s" % (info, error))

        _window = Toplevel()
        _window.configure(background='black')
        popCanv = ScrollableFrame(_window)
        # winName.title("Kali Tools Help")
        # ksbar=Scrollbar(winName, orient=VERTICAL)
        # ksbar.grid(row=0, column=1, sticky="ns")
        #
        # popCanv = Canvas(winName, width=875, height = 250, scrollregion=(0,0,875,1600)) #width=1256, height = 1674)
        # popCanv.grid(row=0, column=0, sticky=NSEW) #added sticky
        # ksbar.config(command=popCanv.yview)
#        popCanv.config(background="black")
        # winName.configure(background="black")

        info = Label(popCanv.scrollable_frame, text = "Kali Tools: ", bg="black", fg="lime")
        info.grid(row = 1, column = 0, padx=3, pady=3)

        a_label = Label(popCanv.scrollable_frame, text = "--- A ---", bg="black", fg="lime")
        a_label.grid(row = 2, column = 6, padx=3, pady=3)

        a1 = Button(popCanv.scrollable_frame, text="0trace", bg="black", fg="lime",
                    command=lambda : open_page("0trace","https://www.kali.org/tools/0trace/"))
        a1.grid(row = 3, column = 1, padx=3, pady=3)

        a2 = Button(popCanv.scrollable_frame, text="abootimg", bg="black", fg="lime",
                    command=lambda : open_page("abootimg","https://www.kali.org/tools/abootimg/"))
        a2.grid(row = 3, column = 2, padx=3, pady=3)

        a3 = Button(popCanv.scrollable_frame, text="aesfix", bg="black", fg="lime",
                    command=lambda : open_page("aesfix","https://www.kali.org/tools/aesfix/"))
        a3.grid(row = 3, column = 3, padx=3, pady=3)

        a4 = Button(popCanv.scrollable_frame, text="aeskeyfind", bg="black", fg="lime",
                    command=lambda : open_page("aeskeyfind","https://www.kali.org/tools/aeskeyfind/"))
        a4.grid(row = 3, column = 4, padx=3, pady=3)

        a5 = Button(popCanv.scrollable_frame, text="afflib", bg="black", fg="lime",
                    command=lambda : open_page("afflib","https://www.kali.org/tools/afflib/"))
        a5.grid(row = 3, column = 5, padx=3, pady=3)

        a6 = Button(popCanv.scrollable_frame, text="aflplusplus", bg="black", fg="lime",
                    command=lambda : open_page("aflplusplus","https://www.kali.org/tools/aflplusplus/"))
        a6.grid(row = 4, column = 1, padx=3, pady=3)

        a7 = Button(popCanv.scrollable_frame, text="aircrack-ng", bg="black", fg="lime",
                    command=lambda : open_page("aircrack-ng","https://www.kali.org/tools/aircrack-ng/"))
        a7.grid(row = 4, column = 2, padx=3, pady=3)

        a8 = Button(popCanv.scrollable_frame, text="airgeddon", bg="black", fg="lime",
                    command=lambda : open_page("airgeddon","https://www.kali.org/tools/airgeddon/"))
        a8.grid(row = 4, column = 3, padx=3, pady=3)

        a9 = Button(popCanv.scrollable_frame, text="altdns", bg="black", fg="lime",
                    command=lambda : open_page("altdns","https://www.kali.org/tools/altdns/"))
        a9.grid(row = 4, column = 4, padx=3, pady=3)

        a10 = Button(popCanv.scrollable_frame, text="amap", bg="black", fg="lime",
                    command=lambda : open_page("amap","https://www.kali.org/tools/amap/"))
        a10.grid(row = 4, column = 5, padx=3, pady=3)

        a11 = Button(popCanv.scrollable_frame, text="amass", bg="black", fg="lime",
                    command=lambda : open_page("amass","https://www.kali.org/tools/amass/"))
        a11.grid(row = 5, column = 1, padx=3, pady=3)

        a12 = Button(popCanv.scrollable_frame, text="android-sdk", bg="black", fg="lime",
                    command=lambda : open_page("android-sdk","https://www.kali.org/tools/android-sdk/"))
        a12.grid(row = 5, column = 2, padx=3, pady=3)

        a13 = Button(popCanv.scrollable_frame, text="apache-users", bg="black", fg="lime",
                    command=lambda : open_page("apache-users","https://www.kali.org/tools/apache-users/"))
        a13.grid(row = 5, column = 3, padx=3, pady=3)

        a14 = Button(popCanv.scrollable_frame, text="apache2", bg="black", fg="lime",
                    command=lambda : open_page("apache2","https://www.kali.org/tools/apache2/"))
        a14.grid(row = 5, column = 4, padx=3, pady=3)

        a15 = Button(popCanv.scrollable_frame, text="apktool", bg="black", fg="lime",
                    command=lambda : open_page("apktool","https://www.kali.org/tools/apktool/"))
        a15.grid(row = 5, column = 5, padx=3, pady=3)

        a16 = Button(popCanv.scrollable_frame, text="arjun", bg="black", fg="lime",
                    command=lambda : open_page("arjun","https://www.kali.org/tools/arjun/"))
        a16.grid(row = 6, column = 1, padx=3, pady=3)

        a17 = Button(popCanv.scrollable_frame, text="armitage", bg="black", fg="lime",
                    command=lambda : open_page("armitage","https://www.kali.org/tools/armitage/"))
        a17.grid(row = 6, column = 2, padx=3, pady=3)

        a18 = Button(popCanv.scrollable_frame, text="arp-scan", bg="black", fg="lime",
                    command=lambda : open_page("arp-scan","https://www.kali.org/tools/arp-scan/"))
        a18.grid(row = 6, column = 3, padx=3, pady=3)

        a19 = Button(popCanv.scrollable_frame, text="arping", bg="black", fg="lime",
                    command=lambda : open_page("arping","https://www.kali.org/tools/arping/"))
        a19.grid(row = 6, column = 4, padx=3, pady=3)

        a20 = Button(popCanv.scrollable_frame, text="arpwatch", bg="black", fg="lime",
                    command=lambda : open_page("arpwatch","https://www.kali.org/tools/arpwatch/"))
        a20.grid(row = 6, column = 5, padx=3, pady=3)

        a21 = Button(popCanv.scrollable_frame, text="asleap", bg="black", fg="lime",
                    command=lambda : open_page("asleap","https://www.kali.org/tools/asleap/"))
        a21.grid(row = 7, column = 1, padx=3, pady=3)

        a22 = Button(popCanv.scrollable_frame, text="assetfinder", bg="black", fg="lime",
                    command=lambda : open_page("assetfinder","https://www.kali.org/tools/assetfinder/"))
        a22.grid(row = 7, column = 2, padx=3, pady=3)

        a23 = Button(popCanv.scrollable_frame, text="atftp", bg="black", fg="lime",
                    command=lambda : open_page("atftp","https://www.kali.org/tools/atftp/"))
        a23.grid(row = 7, column = 3, padx=3, pady=3)

        a24 = Button(popCanv.scrollable_frame, text="autopsy", bg="black", fg="lime",
                    command=lambda : open_page("autopsy","https://www.kali.org/tools/autopsy/"))
        a24.grid(row = 7, column = 4, padx=3, pady=3)

        a25 = Button(popCanv.scrollable_frame, text="axel", bg="black", fg="lime",
                    command=lambda : open_page("axel","https://www.kali.org/tools/axel/"))
        a25.grid(row = 7, column = 5, padx=3, pady=3)

        b_label = Label(popCanv.scrollable_frame, text = "--- B ---", bg="black", fg="lime")
        b_label.grid(row = 8, column = 6, padx=3, pady=3)

        b1 = Button(popCanv.scrollable_frame, text="backdoor-factory", bg="black", fg="lime",
                    command=lambda : open_page("backdoor-factory","https://www.kali.org/tools/backdoor-factory/"))
        b1.grid(row = 9, column = 1, padx=3, pady=3)

        b2 = Button(popCanv.scrollable_frame, text="bed", bg="black", fg="lime",
                    command=lambda : open_page("bed","https://www.kali.org/tools/bed/"))
        b2.grid(row = 9, column = 2, padx=3, pady=3)

        b3 = Button(popCanv.scrollable_frame, text="beef-xss", bg="black", fg="lime",
                    command=lambda : open_page("beef-xss","https://www.kali.org/tools/beef-xss/"))
        b3.grid(row = 9, column = 3, padx=3, pady=3)

        b4 = Button(popCanv.scrollable_frame, text="berate-ap", bg="black", fg="lime",
                    command=lambda : open_page("berate-ap","https://www.kali.org/tools/berate-ap/"))
        b4.grid(row = 9, column = 4, padx=3, pady=3)

        b5 = Button(popCanv.scrollable_frame, text="bettercap", bg="black", fg="lime",
                    command=lambda : open_page("bettercap","https://www.kali.org/tools/bettercap/"))
        b5.grid(row = 9, column = 5, padx=3, pady=3)

        b6 = Button(popCanv.scrollable_frame, text="bind9", bg="black", fg="lime",
                    command=lambda : open_page("bind9","https://www.kali.org/tools/bind9/"))
        b6.grid(row = 10, column = 1, padx=3, pady=3)

        b7 = Button(popCanv.scrollable_frame, text="bing-ip2hosts", bg="black", fg="lime",
                    command=lambda : open_page("bing-ip2hosts","https://www.kali.org/tools/bing-ip2hosts/"))
        b7.grid(row = 10, column = 2, padx=3, pady=3)

        b8 = Button(popCanv.scrollable_frame, text="binwalk", bg="black", fg="lime",
                    command=lambda : open_page("binwalk","https://www.kali.org/tools/binwalk/"))
        b8.grid(row = 10, column = 3, padx=3, pady=3)

        b9 = Button(popCanv.scrollable_frame, text="bloodhound", bg="black", fg="lime",
                    command=lambda : open_page("bloodhound","https://www.kali.org/tools/bloodhound/"))
        b9.grid(row = 10, column = 4, padx=3, pady=3)

        b10 = Button(popCanv.scrollable_frame, text="bluelog", bg="black", fg="lime",
                    command=lambda : open_page("bluelog","https://www.kali.org/tools/bluelog/"))
        b10.grid(row = 10, column = 5, padx=3, pady=3)

        b11 = Button(popCanv.scrollable_frame, text="blueranger", bg="black", fg="lime",
                    command=lambda : open_page("blueranger","https://www.kali.org/tools/blueranger/"))
        b11.grid(row = 11, column = 1, padx=3, pady=3)

        b12 = Button(popCanv.scrollable_frame, text="bluesnarfer", bg="black", fg="lime",
                    command=lambda : open_page("bluesnarfer","https://www.kali.org/tools/bluesnarfer/"))
        b12.grid(row = 11, column = 2, padx=3, pady=3)

        b13 = Button(popCanv.scrollable_frame, text="bluez", bg="black", fg="lime",
                    command=lambda : open_page("bluez","https://www.kali.org/tools/bluez/"))
        b13.grid(row = 11, column = 3, padx=3, pady=3)

        b14 = Button(popCanv.scrollable_frame, text="braa", bg="black", fg="lime",
                    command=lambda : open_page("braa","https://www.kali.org/tools/braa/"))
        b14.grid(row = 11, column = 4, padx=3, pady=3)


        b15 = Button(popCanv.scrollable_frame, text="bruteforce-salted-openssl", bg="black", fg="lime",
                    command=lambda : open_page("bruteforce-salted-openssl","https://www.kali.org/tools/bruteforce-salted-openssl/"))
        b15.grid(row = 11, column = 5, padx=3, pady=3)

        b16 = Button(popCanv.scrollable_frame, text="brutespray", bg="black", fg="lime",
                    command=lambda : open_page("brutespray","https://www.kali.org/tools/brutespray/"))
        b16.grid(row = 12, column = 1, padx=3, pady=3)


        b17 = Button(popCanv.scrollable_frame, text="btscanner", bg="black", fg="lime",
                    command=lambda : open_page("btscanner","https://www.kali.org/tools/btscanner/"))
        b17.grid(row = 12, column = 2, padx=3, pady=3)

        b18 = Button(popCanv.scrollable_frame, text="bulk-extractor", bg="black", fg="lime",
                    command=lambda : open_page("bulk-extractor","https://www.kali.org/tools/bulk-extractor/"))
        b18.grid(row = 12, column = 3, padx=3, pady=3)

        b19 = Button(popCanv.scrollable_frame, text="bully", bg="black", fg="lime",
                    command=lambda : open_page("bully","https://www.kali.org/tools/bully/"))
        b19.grid(row = 12, column = 4, padx=3, pady=3)

        b20 = Button(popCanv.scrollable_frame, text="burpsuite", bg="black", fg="lime",
                    command=lambda : open_page("burpsuite","https://www.kali.org/tools/burpsuite/"))
        b20.grid(row = 12, column = 5, padx=3, pady=3)

        b21 = Button(popCanv.scrollable_frame, text="bytecode-viewer", bg="black", fg="lime",
                    command=lambda : open_page("bytecode-viewer","https://www.kali.org/tools/bytecode-viewer/"))
        b21.grid(row = 13, column = 3, padx=3, pady=3)

        c_label = Label(popCanv.scrollable_frame, text = "--- C ---", bg="black", fg="lime")
        c_label.grid(row = 14, column = 6, padx=3, pady=3)

        c1= Button(popCanv.scrollable_frame, text="cabextract", bg="black", fg="lime",
                    command=lambda : open_page("cabextract","https://www.kali.org/tools/cabextract/"))
        c1.grid(row = 15, column = 1, padx=3, pady=3)

        c2 = Button(popCanv.scrollable_frame, text="cadaver", bg="black", fg="lime",
                    command=lambda : open_page("cadaver","https://www.kali.org/tools/cadaver/"))
        c2.grid(row = 15, column = 2, padx=3, pady=3)

        c3 = Button(popCanv.scrollable_frame, text="caldera", bg="black", fg="lime",
                    command=lambda : open_page("caldera","https://www.kali.org/tools/caldera/"))
        c3.grid(row = 15, column = 3, padx=3, pady=3)

        c4 = Button(popCanv.scrollable_frame, text="capstone", bg="black", fg="lime",
                    command=lambda : open_page("capstone","https://www.kali.org/tools/capstone/"))
        c4.grid(row = 15, column = 4, padx=3, pady=3)

        c5 = Button(popCanv.scrollable_frame, text="ccrypt", bg="black", fg="lime",
                    command=lambda : open_page("ccrypt","https://www.kali.org/tools/ccrypt/"))
        c5.grid(row =15 , column = 5, padx=3, pady=3)

        c6 = Button(popCanv.scrollable_frame, text="certgraph", bg="black", fg="lime",
                    command=lambda : open_page("certgraph","https://www.kali.org/tools/certgraph/"))
        c6.grid(row = 16, column = 1, padx=3, pady=3)

        c7 = Button(popCanv.scrollable_frame, text="cewl", bg="black", fg="lime",
                    command=lambda : open_page("cewl","https://www.kali.org/tools/cewl/"))
        c7.grid(row = 16, column = 2, padx=3, pady=3)

        c8 = Button(popCanv.scrollable_frame, text="changeme", bg="black", fg="lime",
                    command=lambda : open_page("changeme","https://www.kali.org/tools/changeme/"))
        c8.grid(row = 16, column = 3, padx=3, pady=3)

        c9 = Button(popCanv.scrollable_frame, text="chaosreader", bg="black", fg="lime",
                    command=lambda : open_page("chaosreader","https://www.kali.org/tools/chaosreader/"))
        c9.grid(row = 16, column = 4, padx=3, pady=3)

        c10 = Button(popCanv.scrollable_frame, text="cherrytree", bg="black", fg="lime",
                    command=lambda : open_page("cherrytree","https://www.kali.org/tools/cherrytree/"))
        c10.grid(row = 16, column = 5, padx=3, pady=3)

        c11 = Button(popCanv.scrollable_frame, text="chirp", bg="black", fg="lime",
                    command=lambda : open_page("chirp","https://www.kali.org/tools/chirp/"))
        c11.grid(row = 17, column = 1, padx=3, pady=3)

        c12 = Button(popCanv.scrollable_frame, text="chisel", bg="black", fg="lime",
                    command=lambda : open_page("chisel","https://www.kali.org/tools/chisel/"))
        c12.grid(row = 17, column = 2, padx=3, pady=3)

        c13 = Button(popCanv.scrollable_frame, text="chkrootkit", bg="black", fg="lime",
                    command=lambda : open_page("chkrootkit","https://www.kali.org/tools/chkrootkit/"))
        c13.grid(row = 17, column = 3, padx=3, pady=3)

        c14 = Button(popCanv.scrollable_frame, text="chntpw", bg="black", fg="lime",
                    command=lambda : open_page("chntpw","https://www.kali.org/tools/chntpw/"))
        c14.grid(row = 17, column = 4, padx=3, pady=3)

        c15 = Button(popCanv.scrollable_frame, text="chromium", bg="black", fg="lime",
                    command=lambda : open_page("chromium","https://www.kali.org/tools/chromium/"))
        c15.grid(row = 17, column = 5, padx=3, pady=3)

        c16 = Button(popCanv.scrollable_frame, text="cifs-utils", bg="black", fg="lime",
                    command=lambda : open_page("cifs-utils","https://www.kali.org/tools/cifs-utils/"))
        c16.grid(row = 18, column = 1, padx=3, pady=3)

        c17 = Button(popCanv.scrollable_frame, text="cisco-auditing-tool", bg="black", fg="lime",
                    command=lambda : open_page("cisco-auditing-tool","https://www.kali.org/tools/cisco-auditing-tool/"))
        c17.grid(row = 18, column = 2, padx=3, pady=3)

        c18 = Button(popCanv.scrollable_frame, text="cisco-global-exploiter", bg="black", fg="lime",
                    command=lambda : open_page("cisco-global-exploiter","https://www.kali.org/tools/cisco-global-exploiter/"))
        c18.grid(row = 18, column = 3, padx=3, pady=3)

        c19 = Button(popCanv.scrollable_frame, text="cisco-ocs", bg="black", fg="lime",
                    command=lambda : open_page("cisco-ocs","https://www.kali.org/tools/cisco-ocs/"))
        c19.grid(row = 18, column = 4, padx=3, pady=3)

        c20 = Button(popCanv.scrollable_frame, text="cisco-torch", bg="black", fg="lime",
                    command=lambda : open_page("cisco-torch","https://www.kali.org/tools/cisco-torch/"))
        c20.grid(row = 18, column = 5, padx=3, pady=3)

        c21 = Button(popCanv.scrollable_frame, text="cloud-enum", bg="black", fg="lime",
                    command=lambda : open_page("cloud-enum","https://www.kali.org/tools/cloud-enum/"))
        c21.grid(row = 19, column = 1, padx=3, pady=3)

        c22 = Button(popCanv.scrollable_frame, text="cloudbrute", bg="black", fg="lime",
                    command=lambda : open_page("cloudbrute","https://www.kali.org/tools/cloudbrute/"))
        c22.grid(row = 19, column = 2, padx=3, pady=3)

        c23 = Button(popCanv.scrollable_frame, text="cmospwd", bg="black", fg="lime",
                    command=lambda : open_page("cmospwd","https://www.kali.org/tools/cmospwd/"))
        c23.grid(row = 19, column = 3, padx=3, pady=3)

        c24 = Button(popCanv.scrollable_frame, text="cmseek", bg="black", fg="lime",
                    command=lambda : open_page("cmseek","https://www.kali.org/tools/cmseek/"))
        c24.grid(row = 19, column = 4, padx=3, pady=3)

        c25 = Button(popCanv.scrollable_frame, text="code-oss", bg="black", fg="lime",
                    command=lambda : open_page("code-oss","https://www.kali.org/tools/code-oss/"))
        c25.grid(row = 19, column = 5, padx=3, pady=3)

        c26 = Button(popCanv.scrollable_frame, text="command-not-found", bg="black", fg="lime",
                    command=lambda : open_page("command-not-found","https://www.kali.org/tools/command-not-found/"))
        c26.grid(row = 20, column = 1, padx=3, pady=3)

        c27 = Button(popCanv.scrollable_frame, text="commix", bg="black", fg="lime",
                    command=lambda : open_page("commix","https://www.kali.org/tools/commix/"))
        c27.grid(row = 20, column = 2, padx=3, pady=3)

        c28 = Button(popCanv.scrollable_frame, text="copy-router-config", bg="black", fg="lime",
                    command=lambda : open_page("copy-router-config","https://www.kali.org/tools/copy-router-config/"))
        c28.grid(row = 20, column = 3, padx=3, pady=3)

        c29 = Button(popCanv.scrollable_frame, text="covenant-kbx", bg="black", fg="lime",
                    command=lambda : open_page("covenant-kbx","https://www.kali.org/tools/covenant-kbx/"))
        c29.grid(row = 20, column = 4, padx=3, pady=3)

        c30 = Button(popCanv.scrollable_frame, text="cowpatty", bg="black", fg="lime",
                    command=lambda : open_page("cowpatty","https://www.kali.org/tools/cowpatty/"))
        c30.grid(row = 20, column = 5, padx=3, pady=3)

        c31 = Button(popCanv.scrollable_frame, text="crack", bg="black", fg="lime",
                    command=lambda : open_page("crack","https://www.kali.org/tools/crack/"))
        c31.grid(row = 21, column = 1, padx=3, pady=3)

        c32 = Button(popCanv.scrollable_frame, text="crackle", bg="black", fg="lime",
                    command=lambda : open_page("crackle","https://www.kali.org/tools/crackle/"))
        c32.grid(row = 21, column = 2, padx=3, pady=3)

        c33 = Button(popCanv.scrollable_frame, text="creddump7", bg="black", fg="lime",
                    command=lambda : open_page("creddump7","https://www.kali.org/tools/creddump7/"))
        c33.grid(row = 21, column = 3, padx=3, pady=3)

        c34 = Button(popCanv.scrollable_frame, text="crowbar", bg="black", fg="lime",
                    command=lambda : open_page("crowbar","https://www.kali.org/tools/crowbar/"))
        c34.grid(row = 21, column = 4, padx=3, pady=3)

        c35 = Button(popCanv.scrollable_frame, text="crunch", bg="black", fg="lime",
                    command=lambda : open_page("crunch","https://www.kali.org/tools/crunch/"))
        c35.grid(row = 21, column = 5, padx=3, pady=3)

        c36 = Button(popCanv.scrollable_frame, text="cryptcat", bg="black", fg="lime",
                    command=lambda : open_page("cryptcat","https://www.kali.org/tools/cryptcat/"))
        c36.grid(row = 22, column = 1, padx=3, pady=3)

        c37 = Button(popCanv.scrollable_frame, text="cryptsetup", bg="black", fg="lime",
                    command=lambda : open_page("cryptsetup","https://www.kali.org/tools/cryptsetup/"))
        c37.grid(row = 22, column = 2, padx=3, pady=3)

        c38 = Button(popCanv.scrollable_frame, text="cryptsetup-nuke-password", bg="black", fg="lime",
                    command=lambda : open_page("cryptsetup-nuke-password","https://www.kali.org/tools/cryptsetup-nuke-password/"))
        c38.grid(row = 22, column = 3, padx=3, pady=3)

        c39 = Button(popCanv.scrollable_frame, text="curlftpfs", bg="black", fg="lime",
                    command=lambda : open_page("curlftpfs","https://www.kali.org/tools/curlftpfs/"))
        c39.grid(row = 22, column = 4, padx=3, pady=3)

        c40 = Button(popCanv.scrollable_frame, text="cutecom", bg="black", fg="lime",
                    command=lambda : open_page("cutecom","https://www.kali.org/tools/cutecom/"))
        c40.grid(row = 22, column = 5, padx=3, pady=3)

        c41 = Button(popCanv.scrollable_frame, text="cutycapt", bg="black", fg="lime",
                    command=lambda : open_page("cutycapt","https://www.kali.org/tools/cutycapt/"))
        c41.grid(row = 23, column = 1, padx=3, pady=3)

        c42 = Button(popCanv.scrollable_frame, text="cymothoa", bg="black", fg="lime",
                    command=lambda : open_page("cymothoa","https://www.kali.org/tools/cymothoa/"))
        c42.grid(row = 23, column = 2, padx=3, pady=3)

        d_label = Label(popCanv.scrollable_frame, text = "--- D ---", bg="black", fg="lime")
        d_label.grid(row = 24, column = 6, padx=3, pady=3)

        #  = Button(popCanv.scrollable_frame, text="", bg="black", fg="lime",
        #             command=lambda : open_page("","https://www.kali.org/tools//"))
        # .grid(row = , column = , padx=3, pady=3)
        #
        #  = Button(popCanv.scrollable_frame, text="", bg="black", fg="lime",
        #             command=lambda : open_page("","https://www.kali.org/tools//"))
        # .grid(row = , column = , padx=3, pady=3)

        #  = Button(popCanv.scrollable_frame, text="", bg="black", fg="lime",
        #             command=lambda : open_page("","https://www.kali.org/tools//"))
        # .grid(row = , column = , padx=3, pady=3)
        #
        #  = Button(popCanv.scrollable_frame, text="", bg="black", fg="lime",
        #             command=lambda : open_page("","https://www.kali.org/tools//"))
        # .grid(row = , column = , padx=3, pady=3)
        #
        #  = Button(popCanv.scrollable_frame, text="", bg="black", fg="lime",
        #             command=lambda : open_page("","https://www.kali.org/tools//"))
        # .grid(row = , column = , padx=3, pady=3)
        #
        #  = Button(popCanv.scrollable_frame, text="", bg="black", fg="lime",
        #             command=lambda : open_page("","https://www.kali.org/tools//"))
        # .grid(row = , column = , padx=3, pady=3)

        #  = Button(popCanv.scrollable_frame, text="", bg="black", fg="lime",
        #             command=lambda : open_page("","https://www.kali.org/tools//"))
        # .grid(row = , column = , padx=3, pady=3)
        #
        #  = Button(popCanv.scrollable_frame, text="", bg="black", fg="lime",
        #             command=lambda : open_page("","https://www.kali.org/tools//"))
        # .grid(row = , column = , padx=3, pady=3)

        #  = Button(popCanv.scrollable_frame, text="", bg="black", fg="lime",
        #             command=lambda : open_page("","https://www.kali.org/tools//"))
        # .grid(row = , column = , padx=3, pady=3)
        #
        #  = Button(popCanv.scrollable_frame, text="", bg="black", fg="lime",
        #             command=lambda : open_page("","https://www.kali.org/tools//"))
        # .grid(row = , column = , padx=3, pady=3)

        #  = Button(popCanv.scrollable_frame, text="", bg="black", fg="lime",
        #             command=lambda : open_page("","https://www.kali.org/tools//"))
        # .grid(row = , column = , padx=3, pady=3)
        #
        #  = Button(popCanv.scrollable_frame, text="", bg="black", fg="lime",
        #             command=lambda : open_page("","https://www.kali.org/tools//"))
        # .grid(row = , column = , padx=3, pady=3)

        #  = Button(popCanv.scrollable_frame, text="", bg="black", fg="lime",
        #             command=lambda : open_page("","https://www.kali.org/tools//"))
        # .grid(row = , column = , padx=3, pady=3)
        #
        #  = Button(popCanv.scrollable_frame, text="", bg="black", fg="lime",
        #             command=lambda : open_page("","https://www.kali.org/tools//"))
        # .grid(row = , column = , padx=3, pady=3)

        #  = Button(popCanv.scrollable_frame, text="", bg="black", fg="lime",
        #             command=lambda : open_page("","https://www.kali.org/tools//"))
        # .grid(row = , column = , padx=3, pady=3)
        #
        #  = Button(popCanv.scrollable_frame, text="", bg="black", fg="lime",
        #             command=lambda : open_page("","https://www.kali.org/tools//"))
        # .grid(row = , column = , padx=3, pady=3)

        #  = Button(popCanv.scrollable_frame, text="", bg="black", fg="lime",
        #             command=lambda : open_page("","https://www.kali.org/tools//"))
        # .grid(row = , column = , padx=3, pady=3)
        #
        #  = Button(popCanv.scrollable_frame, text="", bg="black", fg="lime",
        #             command=lambda : open_page("","https://www.kali.org/tools//"))
        # .grid(row = , column = , padx=3, pady=3)

        #  = Button(popCanv.scrollable_frame, text="", bg="black", fg="lime",
        #             command=lambda : open_page("","https://www.kali.org/tools//"))
        # .grid(row = , column = , padx=3, pady=3)
        #
        #  = Button(popCanv.scrollable_frame, text="", bg="black", fg="lime",
        #             command=lambda : open_page("","https://www.kali.org/tools//"))
        # .grid(row = , column = , padx=3, pady=3)

        #  = Button(popCanv.scrollable_frame, text="", bg="black", fg="lime",
        #             command=lambda : open_page("","https://www.kali.org/tools//"))
        # .grid(row = , column = , padx=3, pady=3)
        #
        #  = Button(popCanv.scrollable_frame, text="", bg="black", fg="lime",
        #             command=lambda : open_page("","https://www.kali.org/tools//"))
        # .grid(row = , column = , padx=3, pady=3)

        #  = Button(popCanv.scrollable_frame, text="", bg="black", fg="lime",
        #             command=lambda : open_page("","https://www.kali.org/tools//"))
        # .grid(row = , column = , padx=3, pady=3)
        #
        #  = Button(popCanv.scrollable_frame, text="", bg="black", fg="lime",
        #             command=lambda : open_page("","https://www.kali.org/tools//"))
        # .grid(row = , column = , padx=3, pady=3)

        #  = Button(popCanv.scrollable_frame, text="", bg="black", fg="lime",
        #             command=lambda : open_page("","https://www.kali.org/tools//"))
        # .grid(row = , column = , padx=3, pady=3)
        #
        #  = Button(popCanv.scrollable_frame, text="", bg="black", fg="lime",
        #             command=lambda : open_page("","https://www.kali.org/tools//"))
        # .grid(row = , column = , padx=3, pady=3)

        #  = Button(popCanv.scrollable_frame, text="", bg="black", fg="lime",
        #             command=lambda : open_page("","https://www.kali.org/tools//"))
        # .grid(row = , column = , padx=3, pady=3)
        #
        #  = Button(popCanv.scrollable_frame, text="", bg="black", fg="lime",
        #             command=lambda : open_page("","https://www.kali.org/tools//"))
        # .grid(row = , column = , padx=3, pady=3)

        #  = Button(popCanv.scrollable_frame, text="", bg="black", fg="lime",
        #             command=lambda : open_page("","https://www.kali.org/tools//"))
        # .grid(row = , column = , padx=3, pady=3)
        #
        #  = Button(popCanv.scrollable_frame, text="", bg="black", fg="lime",
        #             command=lambda : open_page("","https://www.kali.org/tools//"))
        # .grid(row = , column = , padx=3, pady=3)

        #  = Button(popCanv.scrollable_frame, text="", bg="black", fg="lime",
        #             command=lambda : open_page("","https://www.kali.org/tools//"))
        # .grid(row = , column = , padx=3, pady=3)
        #
        #  = Button(popCanv.scrollable_frame, text="", bg="black", fg="lime",
        #             command=lambda : open_page("","https://www.kali.org/tools//"))
        # .grid(row = , column = , padx=3, pady=3)

        #  = Button(popCanv.scrollable_frame, text="", bg="black", fg="lime",
        #             command=lambda : open_page("","https://www.kali.org/tools//"))
        # .grid(row = , column = , padx=3, pady=3)
        #
        #  = Button(popCanv.scrollable_frame, text="", bg="black", fg="lime",
        #             command=lambda : open_page("","https://www.kali.org/tools//"))
        # .grid(row = , column = , padx=3, pady=3)

        #  = Button(popCanv.scrollable_frame, text="", bg="black", fg="lime",
        #             command=lambda : open_page("","https://www.kali.org/tools//"))
        # .grid(row = , column = , padx=3, pady=3)
        #
        #  = Button(popCanv.scrollable_frame, text="", bg="black", fg="lime",
        #             command=lambda : open_page("","https://www.kali.org/tools//"))
        # .grid(row = , column = , padx=3, pady=3)
        #
        #  = Button(popCanv.scrollable_frame, text="", bg="black", fg="lime",
        #             command=lambda : open_page("","https://www.kali.org/tools//"))
        # .grid(row = , column = , padx=3, pady=3)
        #
        #  = Button(popCanv.scrollable_frame, text="", bg="black", fg="lime",
        #             command=lambda : open_page("","https://www.kali.org/tools//"))
        # .grid(row = , column = , padx=3, pady=3)

        #  = Button(popCanv.scrollable_frame, text="", bg="black", fg="lime",
        #             command=lambda : open_page("","https://www.kali.org/tools//"))
        # .grid(row = , column = , padx=3, pady=3)
        #
        #  = Button(popCanv.scrollable_frame, text="", bg="black", fg="lime",
        #             command=lambda : open_page("","https://www.kali.org/tools//"))
        # .grid(row = , column = , padx=3, pady=3)

        #  = Button(popCanv.scrollable_frame, text="", bg="black", fg="lime",
        #             command=lambda : open_page("","https://www.kali.org/tools//"))
        # .grid(row = , column = , padx=3, pady=3)
        #
        #  = Button(popCanv.scrollable_frame, text="", bg="black", fg="lime",
        #             command=lambda : open_page("","https://www.kali.org/tools//"))
        # .grid(row = , column = , padx=3, pady=3)

        #  = Button(popCanv.scrollable_frame, text="", bg="black", fg="lime",
        #             command=lambda : open_page("","https://www.kali.org/tools//"))
        # .grid(row = , column = , padx=3, pady=3)
        #
        #  = Button(popCanv.scrollable_frame, text="", bg="black", fg="lime",
        #             command=lambda : open_page("","https://www.kali.org/tools//"))
        # .grid(row = , column = , padx=3, pady=3)

        #  = Button(popCanv.scrollable_frame, text="", bg="black", fg="lime",
        #             command=lambda : open_page("","https://www.kali.org/tools//"))
        # .grid(row = , column = , padx=3, pady=3)
        #
        #  = Button(popCanv.scrollable_frame, text="", bg="black", fg="lime",
        #             command=lambda : open_page("","https://www.kali.org/tools//"))
        # .grid(row = , column = , padx=3, pady=3)

        #  = Button(popCanv.scrollable_frame, text="", bg="black", fg="lime",
        #             command=lambda : open_page("","https://www.kali.org/tools//"))
        # .grid(row = , column = , padx=3, pady=3)
        #
        #  = Button(popCanv.scrollable_frame, text="", bg="black", fg="lime",
        #             command=lambda : open_page("","https://www.kali.org/tools//"))
        # .grid(row = , column = , padx=3, pady=3)

        #  = Button(popCanv.scrollable_frame, text="", bg="black", fg="lime",
        #             command=lambda : open_page("","https://www.kali.org/tools//"))
        # .grid(row = , column = , padx=3, pady=3)
        #
        #  = Button(popCanv.scrollable_frame, text="", bg="black", fg="lime",
        #             command=lambda : open_page("","https://www.kali.org/tools//"))
        # .grid(row = , column = , padx=3, pady=3)

        #  = Button(popCanv.scrollable_frame, text="", bg="black", fg="lime",
        #             command=lambda : open_page("","https://www.kali.org/tools//"))
        # .grid(row = , column = , padx=3, pady=3)
        #
        #  = Button(popCanv.scrollable_frame, text="", bg="black", fg="lime",
        #             command=lambda : open_page("","https://www.kali.org/tools//"))
        # .grid(row = , column = , padx=3, pady=3)

        #  = Button(popCanv.scrollable_frame, text="", bg="black", fg="lime",
        #             command=lambda : open_page("","https://www.kali.org/tools//"))
        # .grid(row = , column = , padx=3, pady=3)
        #
        #  = Button(popCanv.scrollable_frame, text="", bg="black", fg="lime",
        #             command=lambda : open_page("","https://www.kali.org/tools//"))
        # .grid(row = , column = , padx=3, pady=3)

        #  = Button(popCanv.scrollable_frame, text="", bg="black", fg="lime",
        #             command=lambda : open_page("","https://www.kali.org/tools//"))
        # .grid(row = , column = , padx=3, pady=3)
        #
        #  = Button(popCanv.scrollable_frame, text="", bg="black", fg="lime",
        #             command=lambda : open_page("","https://www.kali.org/tools//"))
        # .grid(row = , column = , padx=3, pady=3)

        #  = Button(popCanv.scrollable_frame, text="", bg="black", fg="lime",
        #             command=lambda : open_page("","https://www.kali.org/tools//"))
        # .grid(row = , column = , padx=3, pady=3)
        #
        #  = Button(popCanv.scrollable_frame, text="", bg="black", fg="lime",
        #             command=lambda : open_page("","https://www.kali.org/tools//"))
        # .grid(row = , column = , padx=3, pady=3)

        #  = Button(popCanv.scrollable_frame, text="", bg="black", fg="lime",
        #             command=lambda : open_page("","https://www.kali.org/tools//"))
        # .grid(row = , column = , padx=3, pady=3)
        #
        #  = Button(popCanv.scrollable_frame, text="", bg="black", fg="lime",
        #             command=lambda : open_page("","https://www.kali.org/tools//"))
        # .grid(row = , column = , padx=3, pady=3)

        #  = Button(popCanv.scrollable_frame, text="", bg="black", fg="lime",
        #             command=lambda : open_page("","https://www.kali.org/tools//"))
        # .grid(row = , column = , padx=3, pady=3)
        #
        #  = Button(popCanv.scrollable_frame, text="", bg="black", fg="lime",
        #             command=lambda : open_page("","https://www.kali.org/tools//"))
        # .grid(row = , column = , padx=3, pady=3)

        #  = Button(popCanv.scrollable_frame, text="", bg="black", fg="lime",
        #             command=lambda : open_page("","https://www.kali.org/tools//"))
        # .grid(row = , column = , padx=3, pady=3)
        #
        #  = Button(popCanv.scrollable_frame, text="", bg="black", fg="lime",
        #             command=lambda : open_page("","https://www.kali.org/tools//"))
        # .grid(row = , column = , padx=3, pady=3)

        popCanv.pack()

    def misc_window():
        nWin = Toplevel()
        nWin.geometry("625x150-1+1")
        nWin.title("Misc. Controls")
        nWin.configure(background="black")
        info = Label(nWin, text = "Available Misc. Funcs.: ", bg="black", fg="lime")
        info.grid(row = 1, column = 0, padx=3, pady=3)
#
        b1 = Button(nWin, text="Check File", bg="black", fg="lime",
                    command=lambda : ck_file(nWin))
        b1.grid(row = 2 ,column=1, padx=3, pady=3)
#
        b2 = Button(nWin, text="OS Info", bg="black", fg="lime",
                    command=lambda : os_info(nWin))
        b2.grid(row = 2, column = 2, padx=3, pady=3)
#
        b3 = Button(nWin, text="Serv. Status", bg="black", fg="lime",
                    command=lambda : serv_stat(nWin))
        b3.grid(row = 2, column = 3, padx=3, pady=3)
#
        b4 = Button(nWin, text="Dir. Content", bg="black", fg="lime",
                    command=lambda : d_con(nWin))
        b4.grid(row = 2, column = 4, padx=3, pady=3)
#
        b5 = Button(nWin, text="Get User", bg="black", fg="lime",
                    command=lambda : gt_user(nWin))
        b5.grid(row = 3, column = 1, padx=3, pady=3)
#
        b6 = Button(nWin, text="Batt. Info", bg="black", fg="lime",
                    command=lambda : batt_info(nWin))
        b6.grid(row = 3, column = 2, padx=3, pady=3)
#
        b7 = Button(nWin, text="Memory Check", bg="black", fg="lime",
                    command=lambda : mem_ck(nWin))
        b7.grid(row = 3, column = 3, padx=3, pady=3)
#
        b8 = Button(nWin, text="Serv. List", bg="black", fg="lime",
                    command=lambda : sv_lst(nWin))
        b8.grid(row = 3, column = 4, padx=3, pady=3)
#
        b9 = Button(nWin, text="Kali Help", bg="black", fg="lime",
                    command=lambda : kali_help(nWin))
        b9.grid(row = 4, column = 1, padx=3, pady=3)
##
#        b10 = Button(nWin, text="", bg="black", fg="lime",
#                    command=lambda : (nWin))
#        b10.grid(row = 4, column = 2, padx=3, pady=3)
##
#        b11 = Button(nWin, text="", bg="black", fg="lime",
#                    command=lambda : (nWin))
#        b11.grid(row = 4, column = 3, padx=3, pady=3)
##
#        b12 = Button(nWin, text="", bg="black", fg="lime",
#                    command=lambda : (nWin))
#        b12.grid(row = 4, column = 4, padx=3, pady=3)
##
#        b13 = Button(nWin, text="", bg="black", fg="lime",
#                    command=lambda : (nWin))
#        b13.grid(row = 5, column = 1, padx=3, pady=3)
##
#        b14 = Button(nWin, text="", bg="black", fg="lime",
#                    command=lambda : (nWin))
#        b14.grid(row = 5, column = 2, padx=3, pady=3)
##
#        b15 = Button(nWin, text="", bg="black", fg="lime",
#                    command=lambda : (nWin))
#        b15.grid(row = 5, column = 3, padx=3, pady=3)
##
#        b16 = Button(nWin, text="", bg="black", fg="lime",
#                    command=lambda : (nWin))
#        b16.grid(row = 5, column = 4, padx=3, pady=3)

    misc_window()

##GOOGLE
###########################################################################################
def main_google():

    def operators(newWin):
        def get_data():
            g_ops = pb.g_opers
            newWin = Toplevel()
            newWin.geometry("750x750")
            newWin.title("Google Search Operators")
            T = Text(newWin, height=500, width=250, bg="black", fg="lime")
            T.pack()
            output = g_ops
            T.insert(END, output)
        get_data()

    def g_window():
        nWin = Toplevel()
        nWin.geometry("500x75-1+1")
        nWin.title("G00G13")
        nWin.configure(background="black")
        info = Label(nWin, text = "Avail. Options: ", bg="black", fg="lime")
        info.grid(row = 1, column = 0)
        b1 = Button(nWin, text="Search Ops", bg="black", fg="lime",
                    command=lambda : operators(nWin))
        b1.grid(row = 2 ,column=1)

    g_window()

##PLAYBOOK
###########################################################################################
def main_playbk():


  # HELP
  ##########################################################
    def help_menu():

    ### HELP

    # cron_help

        def cron_help(newWin):
            def get_data():
                _cron_help = pb.cron
                newWin = Toplevel()
                newWin.geometry("750x350")
                newWin.title("cron Help")
                T = Text(newWin, height=500, width=250, bg="black", fg="lime")
                T.pack()
                output = _cron_help
                T.insert(END, output)
            get_data()

    # chmod_help
        def chmod_help(newWin):
            def get_data():
                _chmod_help = pb.chmod
                newWin = Toplevel()
                newWin.geometry("750x400")
                newWin.title("chmod Help")
                T = Text(newWin, height=500, width=250, bg="black", fg="lime")
                T.pack()
                output = _chmod_help
                T.insert(END, output)

            get_data()

    # mysql_help
        def mysql_help(newWin):
            def get_data():
                _mysql_help = pb.mysql
                newWin = Toplevel()
                newWin.geometry("800x750")
                newWin.title("MySQL Help")
                T = Text(newWin, height=500, width=250, bg="black", fg="lime")
                T.pack()
                output = _mysql_help
                T.insert(END, output)

            get_data()

    # basic_help
        def basic_conf(newWin):
            def get_data():
                basic_help = pb.basic_conf
                newWin = Toplevel()
                newWin.geometry("800x275")
                newWin.title("Basic Configuration")
                T = Text(newWin, height=500, width=250, bg="black", fg="lime")
                T.pack()
                output = basic_help
                T.insert(END, output)

            get_data()

    # jbsrv
        def jbsrv(newWin):
            def get_data():
                jobsrv = pb.jbsrv
                newWin = Toplevel()
                newWin.geometry("550x750")
                newWin.title("Jobs And Services")
                T = Text(newWin, height=500, width=250, bg="black", fg="lime")
                T.pack()
                output = jobsrv
                T.insert(END, output)

            get_data()

    # kbh
        def kbh(newWin):
            def get_data():
                kerboohw = pb.kbh
                newWin = Toplevel()
                newWin.geometry("550x750")
                newWin.title("Kernel - Boot - Hardware")
                T = Text(newWin, height=500, width=250, bg="black", fg="lime")
                T.pack()
                output = kerboohw
                T.insert(END, output)

            get_data()

    # sftwr_mgmt
        def sftwrmgmt(newWin):
            def get_data():
                info = pb.sftwr_mgmt
                newWin = Toplevel()
                newWin.geometry("550x750")
                newWin.title("Software Management")
                T = Text(newWin, height=500, width=250, bg="black", fg="lime")
                T.pack()
                output = info
                T.insert(END, output)

            get_data()

    # user_mgmt
        def usrmgmt(newWin):
            def get_data():
                info = pb.user_mgmt
                newWin = Toplevel()
                newWin.geometry("550x750")
                newWin.title("User Management")
                T = Text(newWin, height=500, width=250, bg="black", fg="lime")
                T.pack()
                output = info
                T.insert(END, output)

            get_data()

    # fsvd
        def fsvd(newWin):
            def get_data():
                info = pb.FSVolsDsks
                newWin = Toplevel()
                newWin.geometry("550x750")
                newWin.title("File Systems - Volumes - Disks")
                T = Text(newWin, height=500, width=250, bg="black", fg="lime")
                T.pack()
                output = info
                T.insert(END, output)

            get_data()

    # linux directroy structure
        def lds(newWin):
            def get_data():
                info = pb.lds
                newWin = Toplevel()
                newWin.geometry("550x750")
                newWin.title("Linux Directory Structure")
                T = Text(newWin, height=500, width=250, bg="black", fg="lime")
                T.pack()
                output = info
                T.insert(END, output)

            get_data()

    # networking
        def netking(newWin):
            def get_data():
                info = pb.networking
                newWin = Toplevel()
                newWin.geometry("550x750")
                newWin.title("Networking")
                T = Text(newWin, height=500, width=250, bg="black", fg="lime")
                T.pack()
                output = info
                T.insert(END, output)

            get_data()

    # secid
        def secid(newWin):
            def get_data():
                info = pb.secid
                newWin = Toplevel()
                newWin.geometry("550x550")
                newWin.title("Security & Identity")
                T = Text(newWin, height=550, width=250, bg="black", fg="lime")
                T.pack()
                output = info
                T.insert(END, output)

            get_data()

    # recman
        def recmanage(newWin):
            def get_data():
                info = pb.recman
                newWin = Toplevel()
                newWin.geometry("550x750")
                newWin.title("Resource Management")
                T = Text(newWin, height=750, width=550, bg="black", fg="lime")
                T.pack()
                output = info
                T.insert(END, output)

            get_data()

    # apache2
        def apache_help(newWin):
            def get_data():
                info = pb.apache2
                newWin = Toplevel()
                newWin.geometry("550x750")
                newWin.title("Apache2")
                T = Text(newWin, height=750, width=550, bg="black", fg="lime")
                T.pack()
                output = info
                T.insert(END, output)
            get_data()

        def help_window():
            nWin = Toplevel()
            nWin.geometry("650x300-1+1")
            nWin.title("Help")
            nWin.configure(background="black")
            info = Label(nWin, text = "Avail. Help.: ", bg="black", fg="lime")
            info.grid(row = 1, column = 0)

            b1 = Button(nWin, text="Basic Conf.", bg="black", fg="lime",
                        command=lambda : basic_conf(nWin))
            b1.grid(row = 2, column = 1)

            b2 = Button(nWin, text="Kern./Boot/Hrdwr", bg="black", fg="lime",
                        command=lambda : kbh(nWin))
            b2.grid(row = 2, column = 2)

            b3 = Button(nWin, text="Jobs/Srvs.", bg="black", fg="lime",
                        command=lambda : jbsrv(nWin))
            b3.grid(row = 2, column = 3)

            b4 = Button(nWin, text="Sftwr. Mgmt.", bg="black", fg="lime",
                        command=lambda : sftwrmgmt(nWin))
            b4.grid(row = 2, column = 4)

            b5 = Button(nWin, text="User Mgmt.", bg="black", fg="lime",
                        command=lambda : usrmgmt(nWin))
            b5.grid(row = 3, column = 1)

            b6 = Button(nWin, text="F.S., Vols., Disks", bg="black", fg="lime",
                        command=lambda : fsvd(nWin))
            b6.grid(row = 3, column = 1)

            b7 = Button(nWin, text="Networking", bg="black", fg="lime",
                        command=lambda : netking(nWin))
            b7.grid(row = 3, column = 2)

            b8 = Button(nWin, text="Security & Identity", bg="black", fg="lime",
                        command= lambda: secid(nWin))
            b8.grid(row=3, column=3)

            b9 = Button(nWin, text="Resrc Man.", bg="black", fg="lime",
                        command= lambda: recmanage(nWin))
            b9.grid(row=3, column=4)

            b10 = Button(nWin, text="Linux Dir. Struct.", bg="black", fg="lime",
                        command=lambda : lds(nWin))
            b10.grid(row = 4, column = 1)

            b11 = Button(nWin, text="Cron", bg="black", fg="lime",
                        command=lambda : cron_help(nWin))
            b11.grid(row = 4 ,column=2)

            b12 = Button(nWin, text="Chmod", bg="black", fg="lime",
                        command=lambda : chmod_help(nWin))
            b12.grid(row = 4, column = 3)

            b13 = Button(nWin, text="MySQL", bg="black", fg="lime",
                        command=lambda : mysql_help(nWin))
            b13.grid(row = 4, column = 4)

            b14 = Button(nWin, text="Apache2", bg="black", fg="lime",
                         command=lambda : apache_help(nWin))
            b14.grid(row = 5, column = 1)

        help_window()

    def off_menu():

        def off_win():
            nWin = Toplevel()
            nWin.geometry("650x300")
            nWin.title("Offense")
            nWin.configure(background="black")
            info = Label(nWin, text = "Avail. Help.: ", bg="black", fg="lime")
            info.grid(row = 1, column = 0)

        off_win()

    def de_menu():

        def de_win():
            nWin = Toplevel()
            nWin.geometry("650x300")
            nWin.title("Defense")
            nWin.configure(background="black")
            info = Label(nWin, text = "Avail. Help.: ", bg="black", fg="lime")
            info.grid(row = 1, column = 0)

        de_win()

    def se_menu():

        def examp(newWin):
            def get_data():
                newWin = Toplevel()
                newWin.geometry("750x750")
                newWin.title("Examples")
                canv = Canvas(newWin, width=750, height=750, bg='black')
                canv.grid(row=1, column=1)
                canv.pack()
                img = PhotoImage(file="/media/kali/d60b209f-ad43-4f46-8e04-dc6371f98578/Development/media/se/graphology/example.gif")
                _pic = Label(newWin, image=img)
                _pic.place(x = 0, y = 0)
            get_data()

        def graph_win(newWin):
            nWin = Toplevel()
            nWin.geometry("650x300")
            nWin.title("Graphology")
            nWin.configure(background="black")
            info = Label(nWin, text = "Avail. Help.: ", bg="black", fg="lime")
            info.grid(row = 1, column = 0)

            b1 = Button(nWin, text = "Examples", bg="black", fg="lime",
                        command=lambda : examp(nWin))
            b1.grid(row = 2, column = 1)

        def liar(newWin):
            def get_data():
                info = pb.lies
                newWin = Toplevel()
                newWin.geometry("750x550")
                newWin.title("Lie Indicators")
                T = Text(newWin, height=250, width=250, bg="black", fg="lime")
                T.pack()
                output = info
                T.insert(END, output)
            get_data()

        def se_win():
            nWin = Toplevel()
            nWin.geometry("650x300")
            nWin.title("Social Engineering")
            nWin.configure(background="black")
            info = Label(nWin, text = "Avail. Help.: ", bg="black", fg="lime")
            info.grid(row = 1, column = 0)

            b1 = Button(nWin, text = "Lie Indicators", bg="black", fg="lime",
                        command=lambda : liar(nWin))
            b1.grid(row = 2, column = 1)

            b4 = Button(nWin, text = "Graphology", bg="black", fg="lime",
                        command=lambda : graph_win(nWin))
            b4.grid(row = 3, column = 1)

        se_win()

    def plybk_window():
        nWin = Toplevel()
        nWin.geometry("500x75-1+1")
        nWin.title("914Y800K")
        nWin.configure(background="black")
        info = Label(nWin, text = "Avail. Options: ", bg="black", fg="lime")
        info.grid(row = 1, column = 0)
        b1 = Button(nWin, text="Cmd Help", bg="black", fg="lime",
                    command=lambda : help_menu())
        b1.grid(row = 2 ,column=1)
        b2 = Button(nWin, text="Offense", bg="black", fg="lime",
                    command=lambda : off_menu())
        b2.grid(row = 2, column = 2)
        b3 = Button(nWin, text="Defense", bg="black", fg="lime",
                    command=lambda : de_menu())
        b3.grid(row = 2, column = 3)
        b4 = Button(nWin, text="Soc. Eng.", bg="black", fg="lime",
                    command=lambda : se_menu())
        b4.grid(row = 2, column = 4)

    plybk_window()
