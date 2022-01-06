#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created: Aug 2017

    @author: 73RM1N41@9R0GR4M13
"""

from tkinter import Button, Label, Menu  # Used to create the gui
import __init__
import gui_kFuncs as gkf

# MAIN MENU

menubar = Menu(gkf.root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=gkf.root.quit)
menubar.add_cascade(label="File", menu=filemenu)

# HELP MENU

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=gkf.donothing)
helpmenu.add_command(label="About", command=gkf.msgbx2)
menubar.add_cascade(label="Help", menu=helpmenu)

gkf.root.config(menu=menubar, background="black")

# Spacer
space = Label(gkf.topFrame, text="", bg="black")
space.grid(row=0, column=0, padx=0, pady=5)

# ANON
a_main = Button(gkf.topFrame, text="Anon", bg="black", fg="#33ff33", font=("Arial Bold", 12), highlightthickness=1, highlightbackground="#33ff33", command=gkf.anon_main)
a_main.grid(row=2, column=1, padx=5, pady=5)

# RECON
rwin = Button(gkf.topFrame, text="Recon", bg="black", fg="#33ff33", font=("Arial Bold", 12), highlightthickness=1, highlightbackground="#33ff33", command=gkf.recon_main)
rwin.grid(row=2, column=2, padx=5, pady=5)

# REPORTING
repwin = Button(gkf.topFrame, text="Reporting", bg="black", fg="#33ff33", font=("Arial Bold", 12), highlightthickness=1, highlightbackground="#33ff33", command=gkf.dev_msgbx)
repwin.grid(row=2, column=3, padx=5, pady=5)

# Website
wsc = Button(gkf.topFrame, text="Website Ctrl.", bg="black", fg="#ffffff", font=("Arial Bold", 12), highlightthickness=1, highlightbackground="#ffffff", command=gkf.wsc_main)
wsc.grid(row=3, column=1, padx=5, pady=5)

# Network Ctrl
main_nwctl = Button(gkf.topFrame, text="Network Ctrl.", bg="black", fg="#ffffff", font=("Arial Bold", 12), highlightthickness=1, highlightbackground="#ffffff", command=gkf.main_nwkctl)
main_nwctl.grid(row=3, column=2, padx=5, pady=5)

# Offense
offense = Button(gkf.topFrame, text="Offense", bg="black", fg="#ff0000", font=("Arial Bold", 12), highlightthickness=1, highlightbackground="#ff0000", command=gkf.offense_main)
offense.grid(row=4, column=1, padx=5, pady=5)

# Defense
defense = Button(gkf.topFrame, text="Defense", bg="black", fg="#ff0000", font=("Arial Bold", 12), highlightthickness=1, highlightbackground="#ff0000", command=gkf.dev_msgbx)
defense.grid(row=4, column=2, padx=5, pady=5)

# Misc
misc_main = Button(gkf.topFrame, text="Misc.", bg="black", fg="#00ffc1", font=("Arial Bold", 12), highlightthickness=1, highlightbackground="#00ffc1", command=gkf.main_misc)
misc_main.grid(row=5, column=1, padx=5, pady=5)

# Google
main_g = Button(gkf.topFrame, text="G00G13", bg="black", fg="#00ffc1", font=("Arial Bold", 12), highlightthickness=1, highlightbackground="#00ffc1", command=gkf.main_google)
main_g.grid(row=5, column=2, padx=5, pady=5)

# Playbook
main_plybk = Button(gkf.topFrame, text="914Y800K", bg="black", fg="#00ffc1", font=("Arial Bold", 12), highlightthickness=1, highlightbackground="#00ffc1", command=gkf.main_playbk)
main_plybk.grid(row=5, column=3, padx=5, pady=5)

# LOGO
logo_label = Label(gkf.bottomFrame, bg="black", image=gkf.logo)
logo_label.grid(row=6, column=2, padx = 0, pady = 0)

### MAIN LOOP
gkf.root.mainloop()
