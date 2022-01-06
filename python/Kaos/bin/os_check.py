#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 19:19:37 2017

@author: 73RM1N41
"""

#!/usr/bin/env python
import platform
profile = [
platform.architecture(),

## Depricated in 3.5
#platform.dist(),

platform.libc_ver(),
platform.mac_ver(),
platform.machine(),
platform.node(),
platform.platform(),
platform.processor(),
platform.python_build(),
platform.python_compiler(),
platform.python_version(),
platform.system(),
platform.uname(),
platform.version(),
]

if len(platform.architecture()) >= 1:
    try:
        print("Architecture:")
        for item in platform.architecture():
            print(" 	%s" % item)
    except Exception:
        pass
    print("#############################\n")

## DEPRICATED IN 3.5

#if len(platform.dist()) >= 1:
#    try:
#        print("Distribution:")
#        for item in platform.dist():
#            print(" 	%s" % item)
#    except Exception:
#        pass
#    print("#############################\n")

if len(platform.libc_ver()) >= 1:
    try:
        print("libc Version:")
        for item in platform.libc_ver():
            print("	       	%s" % item)
    except Exception:
        pass
if len(platform.mac_ver()) >= 1:
    print("#############################\n")
    try:
        print("mac Version:")
        for item in platform.mac_ver():
            print(" 	%s" % item)
    except Exception:
        pass
if len(platform.machine()) >= 1:
    print("#############################\n")
    try:
        print("Machine:")
        print(" 	%s" % platform.machine())
    except Exception:
        pass
    print("#############################\n")
if len(platform.platform()) >= 1:
    try:
        print("Node:")
        print(" 	%s" % platform.platform())
    except Exception:
        pass
    print("#############################\n")
if len(platform.processor()) >= 1:
    try:
        print("Processor:")
        for item in platform.processor():
            print(" 	%s" % item)
    except Exception:
        pass
    print("#############################\n")
if len(platform.python_build()) >= 1:
    try:
        print("Python Build:")
        print(" 	%s" % platform.python_build())
    except Exception:
        pass
    print("#############################\n")
if len(platform.python_compiler()) >= 1:
    try:
        print("Python Compiler:")
        print(" 	%s" % platform.python_compiler())
    except Exception:
        pass
    print("#############################\n")
if len(platform.python_version()) >= 1:
    try:
        print("Python Version:")
        print(" 	%s" % platform.python_version())
    except Exception:
        pass
    print("#############################\n")
if len(platform.system()) >= 1:
    try:
        print("System:")
        print(" 	%s" % platform.system())
    except Exception:
        pass
    print("#############################\n")
if len(platform.uname()) >= 1:
    try:
        print("Uname:")
        for item in platform.uname():
            print(" 	%s" % item)
    except Exception:
        pass
    print("#############################\n")
if len(platform.version()) >= 1:
    try:
        print("Version:")
        print(" 	%s" % platform.version())
    except Exception:
        pass
    print("#############################\n")
