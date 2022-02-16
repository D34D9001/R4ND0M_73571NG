#!/usr/bin/env python3
import getopt
import sys
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos
from flatlib import const
from flatlib.protocols.temperament import Temperament
from flatlib.protocols import behavior
from flatlib.predictives import returns

USAGE = """
    ./astro.py -d [dob] -t [time] -z [timezone] -n [north_coords] -w [west_coords]
ex: ./astro.py -d "1991/03/13" -t "01:30" -z "-06:00" -n "36n50" -w "86w88"
"""

_bdate = "" # EX: 2020/01/30
_btime = "" # EX: 15:00
_tzone = "" # EX: -06:00
coor_n = "" # N Coords
coor_w = "" # W Coords

argv = sys.argv[1:]

options, args = getopt.getopt(argv, "d:t:z:n:w:h",
                           ["dob=",
                            "time=",
                            "timezone=",
                            "north=",
                            "west="
                            "help"])

for name, value in options:

    if name in ['-d', '--dob']:
        _bdate = value

    if name in ['-t', '--time']:
        _btime = value

    if name in ['-z', '--timezone']:
        _tzone = value

    if name in ['-n', '--north']:
        coor_n = value

    if name in ['-w', '--west']:
        coor_w = value

    if name in ['-h', '--help']:
        print(USAGE)
        sys.exit()


date = Datetime(_bdate, _btime, _tzone)
pos = GeoPos(coor_n, coor_w)

from flatlib.chart import Chart
chart = Chart(date, pos)

sun = chart.getObject(const.SUN)
moon = chart.getObject(const.MOON)
mercury = chart.getObject(const.MERCURY)
venus = chart.getObject(const.VENUS)
mars = chart.getObject(const.MARS)
jupiter = chart.getObject(const.JUPITER)
saturn = chart.getObject(const.SATURN)

stars = chart.getFixedStars()
star_list = {}
for item in stars:
    s_list = str(item).replace('<', '').replace('>', '').split()
    star_list[s_list[0]] = str(s_list[1])

# today = Datetime(_bdate, _btime, _tzone)
# srChart = returns.nextSolarReturn(chart, today)
# asc = str(srChart.get(const.ASC)).replace('<', '').replace('>', '').split()

print("\n")
# print("Solar Return:")
# print("             %s\n             %s\n             %s" % (asc[0], asc[1], asc[2]))
print("Planets:\n")
print("     Sun:")
print("             Sign: %s " % sun.sign)
print("             Gender: %s" % sun.gender())
print("             Element: %s" % sun.element())
print("\n")
print("     Moon:")
print("             Phase: %s " % chart.getMoonPhase())
print("             Sign: %s " % moon.sign)
print("             Gender: %s " % moon.gender())
print("             Element: %s " % moon.element())
print("\n")
print("     Mercury:")
print("             Sign: %s " % mercury.sign)
print("             Gender: %s " % mercury.gender())
print("             Element: %s " % mercury.element())
print("\n")
print("     Venus:")
print("             Sign: %s " % venus.sign)
print("             Gender: %s " % venus.gender())
print("             Element: %s " % venus.element())
print("\n")
print("     Mars:")
print("             Sign: %s " % mars.sign)
print("             Gender: %s " % mars.gender())
print("             Element: %s " % mars.element())
print("\n")
print("     Jupiter:")
print("             Sign: %s " % jupiter.sign)
print("             Gender: %s " % jupiter.gender())
print("             Element: %s " % jupiter.element())
print("\n")
print("     Saturn:")
print("             Sign: %s " % saturn.sign)
print("             Gender: %s " % saturn.gender())
print("             Element: %s " % saturn.element())
print("\n")

print("Houses:")
print("\n")
print("     House1: %s" % chart.get(const.HOUSE1).sign)
print("         Condition: %s\n         Gender: %s" % (chart.get(const.HOUSE1).condition(), chart.get(const.HOUSE1).gender()))
print("\n")
print("     House2: %s" % chart.get(const.HOUSE2).sign)
print("         Condition: %s\n         Gender: %s" % (chart.get(const.HOUSE2).condition(), chart.get(const.HOUSE2).gender()))
print("\n")
print("     House3: %s" % chart.get(const.HOUSE3).sign)
print("         Condition: %s\n         Gender: %s" % (chart.get(const.HOUSE3).condition(), chart.get(const.HOUSE3).gender()))
print("\n")
print("     House4: %s" % chart.get(const.HOUSE4).sign)
print("         Condition: %s\n         Gender: %s" % (chart.get(const.HOUSE4).condition(), chart.get(const.HOUSE4).gender()))
print("\n")
print("     House5: %s" % chart.get(const.HOUSE5).sign)
print("         Condition: %s\n         Gender: %s" % (chart.get(const.HOUSE5).condition(), chart.get(const.HOUSE5).gender()))
print("\n")
print("     House6: %s" % chart.get(const.HOUSE6).sign)
print("         Condition: %s\n         Gender: %s" % (chart.get(const.HOUSE6).condition(), chart.get(const.HOUSE6).gender()))
print("\n")
print("     House7: %s" % chart.get(const.HOUSE7).sign)
print("         Condition: %s\n         Gender: %s" % (chart.get(const.HOUSE7).condition(), chart.get(const.HOUSE7).gender()))
print("\n")
print("     House8: %s" % chart.get(const.HOUSE8).sign)
print("         Condition: %s\n         Gender: %s" % (chart.get(const.HOUSE8).condition(), chart.get(const.HOUSE8).gender()))
print("\n")
print("     House9: %s" % chart.get(const.HOUSE9).sign)
#print("         Condition: %s\n         Gender: %s" % (chart.get(const.HOUSE9).condition(), chart.get(const.HOUSE9).gender()))
print("         Condition: %s" % chart.get(const.HOUSE9).condition())
print("\n")
print("     House10: %s" % chart.get(const.HOUSE10).sign)
#print("         Condition: %s\n         Gender: %s" % (chart.get(const.HOUSE10).condition(), chart.get(const.HOUSE10).gender()))
print("         Condition: %s" % chart.get(const.HOUSE9).condition())
print("\n")
print("     House11: %s" % chart.get(const.HOUSE11).sign)
#print("         Condition: %s\n         Gender: %s" % (chart.get(const.HOUSE11).condition(), chart.get(const.HOUSE11).gender()))
print("         Condition: %s" % chart.get(const.HOUSE9).condition())
print("\n")
print("     House12: %s" % chart.get(const.HOUSE12).sign)
#print("         Condition: %s\n         Gender: %s" % (chart.get(const.HOUSE12).condition(), chart.get(const.HOUSE12).gender()))
print("         Condition: %s" % chart.get(const.HOUSE9).condition())
print("\n")

print("Fixed Stars:\n")
for item in star_list:
    print("     %s:     %s" % (item, star_list[item]))
print("\n")

factors = behavior.compute(chart)
print("Behavior:\n")
for factor in factors:
    print("     %s:     %s" % (factor[0], factor[1][0]))

# Temperament
temperament = Temperament(chart)

# Print temperament factors
factors = temperament.getFactors()
for factor in factors:
    fac_list = []
    try:
        fac_list.append("Factor: %s" % factor['factor'])
    except Exception:
        pass
    try:
        fac_list.append("               ID: %s" % factor['objID'])
    except Exception:
        pass
    try:
        fac_list.append("               Aspect: %s" % factor['aspect'])
    except Exception:
        pass
    try:
        fac_list.append("               Sign: %s" % factor['sign'])
    except Exception:
        pass
    try:
        fac_list.append("               Element: %s" % factor['element'])
    except Exception:
        pass
    try:
        fac_list.append("               Phase: %s" % factor['phase'])
    except Exception:
        pass
    try:
        fac_list.append("               Sun Season: %s" % factor['sunseason'])
    except Exception:
        pass
    fac_list.append("\n")
    for item in fac_list:
        print("%s" % item)


# == These functions are not currently used == #

# # Print temperament modifiers
# modifiers = temperament.getModifiers()
# for modifier in modifiers:
#     print(modifier)
#

# # Print temperament scores
# score = temperament.getScore()
# print(score)
