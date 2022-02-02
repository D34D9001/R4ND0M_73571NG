#!/usr/bin/python3

__author__ = "D34D9001"
__license__ = "MIT"
__version__ = "1.0.1"
__maintainer__ = "D34D9001"
__status__ = "Prototype"

"""
This is a very basic script that shows the last (n) lines of a series of log files.
The files shown can be changed below as well as the log directory used.
The number of lines to show can be changed with the -l or --lines flags and
the amount of time each is shown can be adjusted with the -t or --time flags.
"""

import getopt
import subprocess
import sys
import time

# These variables can be modified to reflect the log files you wish to display.
log_dir = "/var/log"
log_list = ['messages', 'cron', 'secure']

###############################
# DO NOT EDIT BELOW THIS LINE #
###############################

argv = sys.argv[1:]

index = 0
line_cnt = 10
disp_time = 5

options, args = getopt.getopt(argv, "l:t:h",
                           ["lines=",
                            "time=",
                            "help"])

for name, value in options:
    if name in ['-l', '--lines']:
        line_cnt = int(value)

    if name in ['-t', '--time']:
        disp_time = int(value)

    if name in ['-h', '--help']:
        print("./pylog.py -l/--line [line count] -t/--time [display time]")
        sys.exit()

while True:
    if index >= 3:
        index = 0
    subprocess.call(['clear'])
    print("\n\n             %s\n#######################################\n"
          % log_list[index])
    with open('%s/%s' % (log_dir, log_list[index])) as log:
        data = log.readlines()
        output = data[-int(line_cnt):]
        for item in output:
            print(item + "\n")
        index += 1
        time.sleep(int(disp_time))
