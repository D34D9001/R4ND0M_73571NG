#!/usr/bin/env python3
__author__ = "D34D9001"
__license__ = "MIT"

__version__ = "1.0.2"
__maintainer__ = "D34D9001"
__status__ = "Prototype"

import qrcode
import getopt
import sys

debug = 1

USAGE = """
[USAGE]:
           $ ./qrgen.py -i [input] -f [filename]
    {or}   $  ./qrgen.py [input] [filename]
    """

def invalid(section=None):
    if debug == 1:
        if section != None:
            print("[section]: %s" % section)

    print("[!] INVALID INPUT!!!")
    print(USAGE)
    sys.exit()

input = None
fname = None

argv = sys.argv[1:]

if len(sys.argv) == 1 or len(sys.argv) > 5:
    invalid()

options, args = getopt.getopt(argv, "i:f:h",
                           ["input=",
                            "fname=",
                            "help"])

for name, value in options:

    if name in ['-i', '--input']:
        input = value

    if name in ['-f', '--fname']:
        fname = value

    if name in ['-h', '--help']:
        print(USAGE)
        sys.exit()

try:

    if input == None:
        if len(sys.argv[1]) >= 1:
            input = sys.argv[1]
        else:
            invalid("input.secondary")
    if fname == None:
        if len(sys.argv[2]) >= 1:
            fname = sys.argv[2]
        else:
            invalid("fname.secondary")

    fname = fname.replace('.png', '')

    img = qrcode.make(input)
    img.save("%s.png" % fname)

except Exception as error:
    print(error)
    sys.exit()
