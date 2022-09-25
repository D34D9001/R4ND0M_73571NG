#!/usr/bin/env python3

__author__ = "D34D9001"
__copyright__ = "Copyleft 2022"
__license__ = "GPL"
__version__ = "1.2.5"
__maintainer__ = "D34D9001@9R0GR4M13"
__email__ = "program13@protonamil.com"
__status__ = "Beta"

# Delphi modules

import getopt
import sys
import numdic as nd
import operator
import subprocess
from termcolor import colored

# Astrology modules
import getopt
import sys
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos
from flatlib import const
from flatlib.protocols.temperament import Temperament
from flatlib.protocols import behavior
from flatlib.predictives import returns


USAGE = """
./delphi.py -f [first_name] -m [middle_name] -l [last_name] -d [dob {dd/mm/yyyy}] -t ["01:30"] -z ["-06:00"] -n ["36n50"] -w ["86w88"] [-x (optional)]
"""

_bdate = "" # EX: 2020/01/30
_btime = "" # EX: 15:00
_tzone = "" # EX: -06:00
coor_n = "" # N Coords
coor_w = "" # W Coords

logo = """
    ...    :::::::..    :::.       .,-:::::   :::    .,::::::  
 .;;;;;;;. ;;;;``;;;;   ;;`;;    ,;;;'````\'   ;;;    ;;;;\'\'\'\'  
,[[     \[[,[[[,/[[[\'  ,[[ \'[[,  [[[          [[[     [[cccc   
$$$,     $$$$$$$$$c   c$$$cc$$$c $$$          $$\'     $$\"\"\"\"   
\"888,_ _,88P888b \"88bo,888   888,`88bo,__,o, o88oo,.__888oo,__ 
  \"YMMMMMP\" MMMM   \"W\" YMM   \"\"`   \"YUMMMMMP\"\"\"\"\"YUMMM\"\"\"\"YUMMM
              :::. ::::::::::::                                
              ;;`;;;;;;;;;;\'\'\'\'                                
             ,[[ \'[[,   [[                                     
            c$$$cc$$$c  $$                                     
             888   888, 88,                                    
             YMM   ""`  MMM                                    
:::::::-.  .,::::::   :::  ::::::::::.  ::   .:  :::           
 ;;,   `\';,;;;;\'\'\'\'   ;;;   `;;;```.;;;,;;   ;;, ;;;           
 `[[     [[ [[cccc    [[[    `]]nnn]]\',[[[,,,[[[ [[[           
  $$,    $$ $$\"\"\"\"    $$\'     $$$\"\"   \"$$$\"\"\"$$$ $$$           
  888_,o8P\' 888oo,__ o88oo,.__888o     888   \"88o888           
  MMMMP\"`   \"\"\"\"YUMMM\"\"\"\"YUMMMYMMMb    MMM    YMMMMM           
"""
alpha = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':1,
         'K':2, 'L':3, 'M':4, 'N':5, 'O':6, 'P':7, 'Q':8, 'R':9, 'S':1, 'T':2,
         'U':3, 'V':4, 'W':5, 'X':6, 'Y':7, 'Z':8}

report = {"fname": None, "fname_int": 0, "mname": None, "mname_int": 0, "lname": None, "lname_int": 0, "dob": None, "dob_int": 0,
 "life_path": 0, "lp_karma": 0, "lp_k": 0, "expression": 0, "ex_karma": 0, "ex_k": 0, "personality": 0, "pers_karma": 0, "per_k": 0,
 "hearts_desire": 0, "hd_karma": 0,"hd_k": 0, "bday": 0, "birth_day": 0, "b_karma": 0, "b_k": 0, "maturity": 0, "alignment": 0,
 "challenge_1": 0, "challenge_2": 0, "challenge_3": 0, "challenge_4": 0, "le_bridge": 0, "hp_bridge": 0, "lb_bridge": 0, "detailed": False,
 "first_name": "", "middle_name": "", "last_name": "", "life_mstr": 0, "dob_int": 0, "db": 0, "dayofbirth": 0, "vow_fname": None,
 "vow_mname": "", "vow_lname": "", "cons_fname": "", "cons_mname": "", "cons_lname": "", "balance": 0, "fullname": None, "subcon_self": 0,
 "ex_two": 0, "b_mon": 0, "first_cycle": 0, "second_cycle": 0, "third_cycle": 0, "fourth_cycle": 0, "b_year": 0, "birth_year": 0}

argv = sys.argv[1:]

options, args = getopt.getopt(argv, "f:m:l:d:t:z:n:w:xh",
                           ["fname=",
                            "mname=",
                            "lname=",
                            "dob=",
                            "time=",
                            "timezone=",
                            "north=",
                            "west="
                            "x",
                            "help"])

for name, value in options:

    if name in ['-f', '--fname']:
        report["fname"] = str(value).replace("-", "")
        report["first_name"] = value

    if name in ['-m', '--mname']:
        report["mname"] = str(value).replace("-", "")
        report["middle_name"] = value

    if name in ['-l', '--lname']:
        report["lname"] = str(value).replace("-", "")
        last_name = value

    if name in ['-d', '--dob']:
        report["dob"] = value

    if name in ['-t', '--time']:
        _btime = value

    if name in ['-z', '--timezone']:
        _tzone = value

    if name in ['-n', '--north']:
        coor_n = value

    if name in ['-w', '--west']:
        coor_w = value

    if name in ['-x', '--detailed']:
        report["detailed"] = True

    if name in ['-h', '--help']:
        print(USAGE)
        sys.exit()


###################################
## Life Path

report["dob_int"] = report["dob"].replace('/', '')
report["life_mstr"] = 0

    # Add numbers of birthday
for item in str(report["dob_int"]):
    report["dob_int"] = int(report["dob_int"]) + int(item)
    # Generate Life Path number
for item in str(report["dob_int"]):
    report["life_path"] = report["life_path"] + int(item)
    # Check if Life Path is a master number
if len(str(report["life_path"])) > 1 and int(report["life_path"]) == 11 or int(report["life_path"]) == 22 or int(report["life_path"]) == 33:
    report["life_mstr"] = int(report["life_path"])
    # Check if Life Path has Karmic debt number
elif int(report["life_path"]) == 13 or int(report["life_path"]) == 14 or int(report["life_path"]) == 16 or int(report["life_path"]) == 19:
    report["lp_karma"] = int(report["life_path"])

else:
    pass
    # Convert Life Path to 1 digit if it isn't already
report["tmp"] = 0
for item in str(report["life_path"]):
    report["tmp"] = int(report["tmp"]) + int(item)
report["life_path"] = report["tmp"]
    # If a Karmic Debt number was generated, move it to another variable
if int(report["lp_karma"]) > 0:
    report["lp_k"] = report["lp_karma"]

###################################
## Birth day

report["bd"] = str(report["dob_int"])[:-4]

report["bday"] = str(report["bd"])[:-2]

if int(report["bday"]) == 13 or int(report["bday"]) == 14 or int(report["bday"]) == 16 or int(report["bday"]) == 19:
    report["b_karma"] = int(report["bday"])

report["tmp"] = 0
birthday = int(report["bday"])
for item in str(birthday):
    report["tmp"] = int(report["tmp"]) + int(item)

t2 =0
if len(str(report["tmp"])) > 1:
    while len(str(report["tmp"])) > 1:
        for item in str(t2):
            t2 = int(item) + t2
report["dayofbirth"] = str(report["tmp"])

###################################
## Balance

report["balance"] = 0
initials = [report["fname"][0].upper(), report["mname"][0].upper(), report["lname"][0].upper()]

ins = 0

for item in initials:
    ins = ins + int(alpha[item.upper()])

if len(str(ins)) > 1:
    while len(str(ins)) > 1:
        temp = 0
        for item in str(ins):
            temp = temp + int(item)
        ins = int(temp)

report["balance"] = int(ins)


###################################
## Cornerstone, Capstone, First Vowel


cornerstone = str(report["fname"])[0].upper()
corner_int = int(alpha[str(cornerstone.upper())])
capstone = str(report["fname"])[-1:].upper()
cap_int = int(alpha[str(capstone.upper())])
first_vowel = ""
fv_int = 0


for item in report["fname"].upper():
    if item != "A" and item != "E" and item != "I" and item != "O" and item != "U":
        pass
    else:
        first_vowel = str(item.upper())
        fv_int = int(alpha[first_vowel.upper()])
        break

key_num = 0
report["tmp"] = 0

for item in report["fname"].upper():
    report["tmp"] = int(report["tmp"]) + int(alpha[str(item.upper())])

key_num = int(report["tmp"])


while len(str(key_num)) > 1:
    report["tmp"] = 0
    for item in str(key_num):
        report["tmp"] = int(int(report["tmp"])) + int(item)
    key_num = int(report["tmp"])


###################################
## Planes of Expression

report["fullname"] = str(report["fname"]) + str(report["mname"]) + str(report["lname"])

counter = {
"planes": {
"physical": {"pc": 0, "pv": 0, "pg": 0},
"mental": {"mc": 0, "mv": 0, "mg": 0 },
"emotional": {"ec": 0, "ev": 0, "eg": 0},
"intuitive": {"ic": 0, "iv": 0, "ig": 0}}}


PoE = tuple(('planes',('physical',('pc',('E',),),('pv',('W',),),('pg',('D','M'),),),
('mental',('mc',('A'),), ('mv',('H', 'J', 'N', 'P',),), ('mg',('G', 'L',),), ),
('emotional',('ec',('I', 'O', 'R', 'Z'),), ('ev',('B','S','T','X'),),('eg',(None,),),),
('intuitive',('ic',('K',),), ('iv',('F', 'Q', 'U', 'Y'),), ('ig',('C','V'),),),
))

expres = {'physical': 0, 'mental': 0, 'emotional': 0, 'intuitive': 0, 'creative': 0, 'vacillating': 0, 'grounded': 0}


for item in report["fullname"].upper():
    if item in PoE[1][1][1]:
        counter['planes']['physical']['pc'] += int(alpha[item.upper()])
        expres['physical'] += int(alpha[item.upper()])
        expres['creative'] += int(alpha[item.upper()])
    elif item in PoE[1][2][1]:
        counter['planes']['physical']['pv'] += int(alpha[item.upper()])
        expres['physical'] += int(alpha[item.upper()])
        expres['vacillating'] += int(alpha[item.upper()])
    elif item in PoE[1][3][1]:
        counter['planes']['physical']['pg'] += int(alpha[item.upper()])
        expres['physical'] += int(alpha[item.upper()])
        expres['grounded'] += int(alpha[item.upper()])

    elif item in PoE[2][1][1]:
        counter['planes']['mental']['mc'] += int(alpha[item.upper()])
        expres['mental'] += int(alpha[item.upper()])
        expres['creative'] += int(alpha[item.upper()])
    elif item in PoE[2][2][1]:
        counter['planes']['mental']['mv'] += int(alpha[item.upper()])
        expres['mental'] += int(alpha[item.upper()])
        expres['vacillating'] += int(alpha[item.upper()])
    elif item in PoE[2][3][1]:
        counter['planes']['mental']['mg'] += int(alpha[item.upper()])
        expres['mental'] += int(alpha[item.upper()])
        expres['grounded'] += int(alpha[item.upper()])

    elif item in PoE[3][1][1]:
        counter['planes']['emotional']['ec'] += int(alpha[item.upper()])
        expres['emotional'] += int(alpha[item.upper()])
        expres['creative'] += int(alpha[item.upper()])
    elif item in PoE[3][2][1]:
        counter['planes']['emotional']['ev'] += int(alpha[item.upper()])
        expres['emotional'] += int(alpha[item.upper()])
        expres['vacillating'] += int(alpha[item.upper()])
    elif item in PoE[3][3][1]:
        counter['planes']['emotional']['eg'] += int(alpha[item.upper()])
        expres['emotional'] += int(alpha[item.upper()])
        expres['grounded'] += int(alpha[item.upper()])

    elif item in PoE[4][1][1]:
        counter['planes']['intuitive']['ic'] += int(alpha[item.upper()])
        expres['intuitive'] += int(alpha[item.upper()])
        expres['creative'] += int(alpha[item.upper()])
    elif item in PoE[4][2][1]:
        counter['planes']['intuitive']['iv'] += int(alpha[item.upper()])
        expres['intuitive'] += int(alpha[item.upper()])
        expres['vacillating'] += int(alpha[item.upper()])
    elif item in PoE[4][3][1]:
        counter['planes']['intuitive']['ig'] += int(alpha[item.upper()])
        expres['intuitive'] += int(alpha[item.upper()])
        expres['grounded'] += int(alpha[item.upper()])
    else:
        print("%s could not be located!" % item)


exp_list = {1: "physical", 2: "mental", 3: "emotional", 4: "intuitive", 5: "creative", 6: "vacillating", 7: "grounded"}
exp_kList = {1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: ""}
plane_list = {"physical": 1, "mental": 2, "emotional": 3, "intuitive": 4, "creative": 5, "vacillating": 6, "grounded": 7}
#karma_list = {"": ,"": ,)}
## Add karmic numbers to poe

index = 1
for item in exp_list:
    mykey = exp_list[index]
    value = expres["%s" % mykey]
    while len(str(value)) > 1:
        poe_k = int(value)
        if int(value) == 11 or int(value) == 22:
            expres[mykey] = int(value)
        elif len(str(value)) == 2 and len(str(exp_kList[index])) == 0:
            exp_kList[index] = value
        else:
            pass
        report["tmp"] = 0
        for item in str(value):
            report["tmp"] = int(report["tmp"]) + int(item)
        value = int(report["tmp"])
        if expres[mykey] != 11 and expres[mykey] != 22:
            if len(str(expres[mykey])) >= 2:
                temp = 0
                for item in str(expres[mykey]):
                    temp = int(temp) + int(item)
                expres[mykey] = temp
            else:
                expres[mykey] = report["tmp"]
    if index <= 6:
        index += 1
    else:
        break

######################
### Number frequency

nct = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
for item in report["fullname"].upper():
    if alpha[item.upper()] in nct:
        nct[alpha[item.upper()]] += 1
    else:
        nct[alpha[item.upper()]] = 1


mI = max(nct)

hidden_passion_list = []
for item in nct:

#    print(item, nct[item])
    if int(nct[item]) == nct[mI]:
        hidden_passion_list.append(item)
    else:
        pass

####################################
### Rational Thought Number


full_int = 0
fn_int = 0

for item in report["fname"].upper():
    fn_int = fn_int + int(alpha[str(item).upper()])

if len(str(fn_int)) > 1:
    while len(str(fn_int)) > 1:
        tempo = 0
        for item in str(fn_int):
            tempo = tempo + int(item)
        fn_int = int(tempo)

rtn = 0
report["tmp"] = 0
var = 0
rtn_k = 0

var = int(fn_int)
for item in str(fn_int):
    rtn = rtn + int(item)
for item in str(report["dayofbirth"]):
    rtn = rtn + int(item)


if len(str(rtn)) > 1:
    rtn_k = rtn
    while len(str(rtn)) > 1:
        tp = 0
        for item in str(rtn):
            tp = tp + int(item)
        rtn = tp
    rtn = int(tp) + int(report["dayofbirth"])

if len(str(rtn)) > 1:
    while len(str(rtn)) > 1:
        temp = 0
        for item in str(rtn):
            temp = temp + int(item)
        rtn = int(temp)


###################################
## Expression/Destiny
conv = 0

for item in report["fname"]:
    conv = conv + alpha[item.upper()]
result = 0
for item in str(conv):
    result = result + int(item)
report["fname_int"] = result
while len(str(report["fname_int"])) > 1:
    fni = 0
    for item in str(report["fname_int"]):
        fni = fni + int(item)
        report["fname_int"] = fni

conv = 0
for item in report["mname"]:
    conv = conv + alpha[item.upper()]
result = 0
for item in str(conv):
    result = result + int(item)
    report["mname_int"] = result
while len(str(report["mname_int"])) > 1:
    mni = 0
    for item in str(report["mname_int"]):
        mni = mni + int(item)
        report["mname_int"] = mni

conv = 0
for item in report["lname"]:
    conv = conv + alpha[item.upper()]
result = 0
for item in str(conv):
    result = result + int(item)
report["lname_int"] = result
while len(str(report["lname_int"])) > 1:
    lni = 0
    for item in str(report["lname_int"]):
        lni = lni + int(item)
        report["lname_int"] = lni

master_ex = 0

path_init = str(report["fname_int"]) + str(report["mname_int"]) + str(report["lname_int"])

nameint = 0

for item in str(path_init):
    nameint = nameint + int(item)
path_init = nameint

if int(path_init) == 11 or int(path_init) == 22 or int(path_init) == 33:
    master_ex = int(path_init)

if path_init == 13 or path_init == 14 or path_init == 16 or path_init == 19:
    report["ex_karma"] = int(path_init)

for item in str(path_init):
    report["expression"] = report["expression"] + int(item)

while len(str(report["expression"])) > 1:
    exp = 0
    report["ex_two"] = report["expression"]
    for item in str(report["expression"]):
        exp = exp + int(item)
        report["expression"] = exp

if report["ex_karma"] > 0:
    report["ex_k"] = report["ex_karma"]

###################################
## Personality
report["cons_fname"] = ""
cf_int = 0
report["cons_fname"] = ""
cm_int = 0
report["cons_lname"] = ""
cl_int = 0
master_pers = 0
for item in report["fname"].upper():
    if item != 'A' and item != 'E' and item != "I" and item != 'O' and item != "U":
        report["cons_fname"] = str(report["cons_fname"]) + item
for item in report["mname"].upper():
    if item != 'A' and item != 'E' and item != "I" and item != 'O' and item != "U":
        report["cons_mname"] = str(report["cons_mname"]) + item
for item in report["lname"].upper():
    if item != 'A' and item != 'E' and item != "I" and item != 'O' and item != "U":
        report["cons_lname"] = str(report["cons_lname"]) + item
conv = 0

for item in report["cons_fname"]:
    conv = conv + alpha[item.upper()]
result = 0

for item in str(conv):
    result = result + int(item)

while len(str(result)) > 1:
    res = 0
    for item in str(result):
        res = res + int(item)
        result = res
cf_int = result
conv = 0


for item in report["cons_mname"]:
    conv = conv + alpha[item.upper()]
result = 0
for item in str(conv):
    result = result + int(item)


while len(str(result)) > 1:
    res = 0
    for item in str(result):
        res = res + int(item)
    result = res
cm_int = result
conv = 0


for item in report["cons_lname"]:
    conv = conv + alpha[item.upper()]
result = 0
for item in str(conv):
    result = result + int(item)
while len(str(result)) > 1:
    res = 0
    for item in str(result):
        res = res + int(item)
    result = res
cl_int = result


init_pers = ""

for item in str(cf_int):
    init_pers = str(init_pers) + str(item)
for item in str(cm_int):
    init_pers = str(init_pers) + str(item)
for item in str(cl_int):
    init_pers = str(init_pers) + str(item)
pers_num = 0


for item in str(init_pers):
    pers_num = pers_num + int(item)
    pers_twodig = int(pers_num)


if int(pers_twodig) == 11 or int(pers_twodig) == 22 or int(pers_twodig) == 33:
    master_pers = int(pers_twodig)

if len(str(pers_num)) > 1:
    if pers_num == 13 or pers_num == 14 or pers_num == 16 or pers_num == 19:
        report["pers_karma"] = int(pers_num)

    else:
        report["tmp"] = 0
        for item in str(pers_num):
            report["tmp"] = int(report["tmp"]) + int(item)
        pers_num = report["tmp"]
report["personality"] = pers_num

if report["pers_karma"] > 0:
    report["per_k"] = report["pers_karma"]

if len(str(report["personality"])) > 1:
    while len(str(report["personality"])) > 1:
        report["tmp"] = 0
        for item in str(report["personality"]):
            report["tmp"] = int(report["tmp"]) + int(item)
        report["personality"] = report["tmp"]

###################################
## Hearts Desire
report["vow_fname"] = ""
vf_int = 0
report["vow_mname"] = ""
vm_int = 0
report["vow_lname"] = ""
vl_int = 0
for item in report["fname"].upper():
    if item == 'A' or item == 'E' or item == "I" or item == 'O' or item == "U":
        report["vow_fname"] = str(report["vow_fname"]) + item
for item in report["mname"].upper():
    if item == 'A' or item == 'E' or item == "I" or item == 'O' or item == "U":
        report["vow_mname"] = str(report["vow_mname"]) + item
for item in report["lname"].upper():
    if item == 'A' or item == 'E' or item == "I" or item == 'O' or item == "U":
        report["vow_lname"] = str(report["vow_lname"]) + item
conv = 0
for item in report["vow_fname"]:
    conv = conv + alpha[item.upper()]
result = 0
for item in str(conv):
    result = result + int(item)
if len(str(result)) > 1:
    res = 0
    for item in str(result):
        res = res + int(item)
        result = res
vf_int = result
#print("vow_fname: %s\nvf_int: %i" % (vow_fname, vf_int))
conv = 0
for item in str(report["vow_mname"]):
    conv = conv + alpha[item.upper()]
result = 0
for item in str(conv):
    result = result + int(item)
if len(str(result)) > 1:
    res = 0
    for item in str(result):
        res = res + int(item)
        result = res
vm_int = result
#print("vow_mname: %s\nvm_int: %i" % (vow_mname, vm_int))
conv = 0
for item in str(report["vow_lname"]):
    conv = conv + alpha[item.upper()]
result = 0
for item in str(conv):
    result = result + int(item)
if len(str(result)) > 1:
    res = 0
    for item in str(result):
        res = res + int(item)
        result = res
vl_int = result
#print("vow_lname: %s\nvl_int: %i" % (vow_lname, vl_int))
init_hd = ""
for item in str(vf_int):
    init_hd = str(init_hd) + str(item)
for item in str(vm_int):
    init_hd = str(init_hd) + str(item)
for item in str(vl_int):
    init_hd = str(init_hd) + str(item)

hd_num = 0

for item in str(init_hd):
    hd_num = hd_num + int(item)

while len(str(hd_num)) > 1 or int(hd_num) == 11 or int(hd_num) == 22 or int(hd_num) == 33:
    if hd_num == 13 or hd_num == 14 or hd_num == 16 or hd_num == 19:
        report["hd_karma"] = hd_num
    report["tmp"] = 0
    for item in str(hd_num):
        report["tmp"] = int(report["tmp"]) + int(item)
    hd_num = report["tmp"]


report["hearts_desire"] = int(hd_num)

if report["hd_karma"] > 0:
    report["hd_k"] = "%i / %i" % (int(report["hearts_desire"]), int(report["hd_karma"]))

else:
    report["hd_k"] = int(report["hearts_desire"])

###################################
## Maturity
mat = int(report["life_path"]) + int(report["expression"])
mat2 = 0

if len(str(mat)) > 1:
    mat2 = int(mat)

while len(str(mat)) > 1:
    report["tmp"] = 0
    for item in str(mat):
        report["tmp"] = int(report["tmp"]) + int(item)
    mat = report["tmp"]
report["maturity"] = int(mat)


## Alignment

bm = str(report["dob_int"])[:-4]
bm = bm[-2:]
alg = int(bm) + int(report["bday"])
# Store 2 digit number for later use
if len(str(alg)) > 1:
    alg_kd = int(alg)
else:
    pass
# Add digits together until left with a single digit
while len(str(alg)) > 1:
    report["tmp"] = 0
    for item in str(alg):
        report["tmp"] = int(report["tmp"]) + int(item)
    alg = report["tmp"]

report["alignment"] = int(alg)


###################################
## Challenge 1
b_day = int(report["bday"])

red_b_day = int(report["bday"])

while len(str(red_b_day)) > 1:
    report["tmp"] = 0
    for item in str(red_b_day):
        report["tmp"] = int(report["tmp"]) + int(item)
    red_b_day = report["tmp"]

report["b_mon"] = bm
#print(report["b_mon"])
while len(str(report["b_mon"])) > 1 or report["b_mon"] == 11:
    report["tmp"] = 0
    for item in str(report["b_mon"]):
        report["tmp"] = int(report["tmp"]) + int(item)
    report["b_mon"] = report["tmp"]
#print(report["b_mon"])

if int(b_day) > int(report["b_mon"]):
#    print('using if')
    chal_1 = int(b_day) - int(report["b_mon"])
#    print(chal_1)

else:
#    print('using else')
    chal_1 = int(report["b_mon"]) - int(b_day)
#    print(chal_1)

while len(str(chal_1)) > 1:
    report["tmp"] = 0
    for item in str(chal_1):
        report["tmp"] = int(report["tmp"]) + int(item)
    chal_1 = report["tmp"]
report["challenge_1"] = int(chal_1)


while len(str(report["challenge_1"])) > 1:
    temp = 0
    for item in str(report["challenge_1"]):
        temp = temp + int(item)
    report["challenge_1"] = temp

###################################
## Challenge 2
report["b_year"] = str(report["dob_int"])[4:]
while len(str(report["b_year"])) > 1:
    report["tmp"] = 0
    for item in str(report["b_year"]):
        report["tmp"] = int(report["tmp"]) + int(item)
    report["b_year"] = report["tmp"]
#print(report["b_year"])
if int(b_day) > int(report["b_year"]):
#    print('using if')
    chal_2 = int(b_day) - int(report["b_year"])
#    print(chal_2)

else:
#    print('using else')
    chal_2 = int(report["b_year"]) - int(b_day)
#    print(chal_2)

report["challenge_2"] = chal_2

while len(str(report["challenge_2"])) > 1:
    temp = 0
    for item in str(report["challenge_2"]):
        temp = temp + int(item)
    report["challenge_2"] = temp
###################################
## Challenge 3
if int(report["challenge_1"]) > int(report["challenge_2"]):
#    print('using if')
    chal_3 = int(report["challenge_1"]) - int(report["challenge_2"])
#    print(chal_3)
    report["challenge_3"] = chal_3

else:
#    print('using else')
    chal_3 = int(report["challenge_2"]) - int(report["challenge_1"])
#    print(chal_3)
    report["challenge_3"] = chal_3

while len(str(report["challenge_3"])) > 1:
    temp = 0
    for item in str(report["challenge_3"]):
        temp = temp + int(item)
    report["challenge_3"] = temp
###################################
## Challenge 4
if int(report["b_mon"]) > int(report["b_year"]):
#    print('using if')
    chal_4 = int(report["b_mon"]) - int(report["b_year"])
#    print(chal_4)

else:
#    print('using else')
    chal_4 = int(report["b_year"]) - int(report["b_mon"])
#    print(chal_4)

report["challenge_4"] = chal_4

while len(str(report["challenge_4"])) > 1:
    temp = 0
    for item in str(report["challenge_4"]):
        temp = temp + int(item)
    report["challenge_4"] = temp

######################
## Life Path / Expression Bridge
if int(report["life_path"]) > int(report["expression"]):
    report["le_bridge"] = int(report["life_path"]) - int(report["expression"])
else:
    report["le_bridge"] = int(report["expression"]) - int(report["life_path"])


######################
## Heart's Desire / Personality Bridge
if int(report["hearts_desire"]) > int(report["personality"]):
    report["hp_bridge"] = int(report["hearts_desire"]) - int(report["personality"])
else:
    report["hp_bridge"] = int(report["personality"]) - int(report["hearts_desire"])


######################
## Life Path / Birthday Bridge

while len(str(b_day)) > 1:
    temp = 0
    for item in str(b_day):
        temp = temp + int(item)
    b_day = int(temp)
if int(report["life_path"]) > int(b_day):
    report["lb_bridge"] = int(report["life_path"]) - int(b_day)
else:
    report["lb_bridge"] = int(b_day) - int(report["life_path"])

######################
### Karmic Debt

if int(report["b_karma"]) > 0:
    report["b_k"] = report["b_karma"]


######################
### Period Cycles

per_cyc = {"cycles": {"1": {"1/2": "26/27", "2/3": "53/54"}, "2": {"1/2": "25/26", "2/3": "52/53"}, "3": {"1/2": "33/34", "2/3": "60/61"}, "4": {"1/2": "32/33", "2/3": "59/60"}, "5": {"1/2": "31/32", "2/3": "58/59"}, "6": {"1/2": "30/31", "2/3": "57/58"}, "7": {"1/2": "29/30", "2/3": "56/57"}, "8": {"1/2": "28/29", "2/3": "55/56"}, "9": {"1/2": "27/28", "2/3": "54/55"}, "11": {"1/2": "25/26", "2/3": "52/53"}, "22": {"1/2": "32/33", "2/3": "59/60"}}}

p_cycle1 = 0
for item in str(report["b_mon"]):
    p_cycle1 = p_cycle1 + int(item)

p_cycle2 = 0
for item in str(report["bday"]):
    p_cycle2 = p_cycle2 + int(item)

p_cycle3 = 0
for item in str(report["b_year"]):
    p_cycle3 = p_cycle3 + int(item)

######################
### Pinnacle Cycles

pin_cyc = {"paths":{
1: {"1st_cycle": "0-35", "2nd_cycle": "35-44", "3rd_cycle": "44-53", "4th_cycle": "53->"},
2: {"1st_cycle": "0-34", "2nd_cycle": "34-43", "3rd_cycle": "43-52", "4th_cycle": "52->"},
3: {"1st_cycle": "0-33", "2nd_cycle": "33-42", "3rd_cycle": "42-51", "4th_cycle": "51->"},
4: {"1st_cycle": "0-32", "2nd_cycle": "32-41", "3rd_cycle": "41-50", "4th_cycle": "50->"},
5: {"1st_cycle": "0-31", "2nd_cycle": "31-40", "3rd_cycle": "40-49", "4th_cycle": "49->"},
6: {"1st_cycle": "0-30", "2nd_cycle": "30-39", "3rd_cycle": "39-48", "4th_cycle": "48->"},
7: {"1st_cycle": "0-29", "2nd_cycle": "29-38", "3rd_cycle": "38-47", "4th_cycle": "47->"},
8: {"1st_cycle": "0-28", "2nd_cycle": "28-37", "3rd_cycle": "37-46", "4th_cycle": "46->"},
9: {"1st_cycle": "0-27", "2nd_cycle": "27-36", "3rd_cycle": "36-45", "4th_cycle": "45->"},
11: {"1st_cycle": "0-34", "2nd_cycle": "34-43", "3rd_cycle": "43-52", "4th_cycle": "52->"},
22: {"1st_cycle": "0-32", "2nd_cycle": "32-41", "3rd_cycle": "41-50", "4th_cycle": "50->"}}}

report["first_cycle"] = int(report["b_mon"]) + int(report["bday"])
if len(str(report["first_cycle"])) > 1:
    if int(report["first_cycle"]) == 11 or int(report["first_cycle"]) == 22:
        pass
    else:
        while len(str(report["first_cycle"])) > 1:
            report["tmp"] = 0
            for item in str(int(report["first_cycle"])):
                report["tmp"] = int(report["tmp"]) + int(item)
            report["first_cycle"] = report["tmp"]
            report["tmp"] = 0

report["second_cycle"] = int(report["bday"]) + int(report["b_year"])
if len(str(report["second_cycle"])) > 1:
    if int(report["second_cycle"]) == 11 or int(report["second_cycle"]) == 22:
        pass
    else:
        while len(str(report["second_cycle"])) > 1:
            report["tmp"] = 0
            for item in str(int(report["second_cycle"])):
                report["tmp"] = int(report["tmp"]) + int(item)
            report["second_cycle"] = report["tmp"]
            report["tmp"] = 0

report["third_cycle"] = int(report["first_cycle"]) + int(report["second_cycle"])
if len(str(report["third_cycle"])) > 1:
    if int(report["third_cycle"]) == 11 or int(report["third_cycle"]) == 22:
        pass
    else:
        while len(str(report["third_cycle"])) > 1:
            report["tmp"] = 0
            for item in str(int(report["third_cycle"])):
                report["tmp"] = int(report["tmp"]) + int(item)
            report["third_cycle"] = report["tmp"]
            report["tmp"] = 0

report["fourth_cycle"] = int(report["b_mon"]) + int(report["b_year"])
if len(str(report["fourth_cycle"])) > 1:
    if int(report["fourth_cycle"]) == 11 or int(report["fourth_cycle"]) == 22:
        pass
    else:
        report["tmp"] = 0
        for item in str(int(report["fourth_cycle"])):
            report["tmp"] = int(report["tmp"]) + int(item)
        report["fourth_cycle"] = report["tmp"]
        report["tmp"] = 0

if len(str(_btime)) > 0 and len(str(_tzone)) > 0 and len(str(coor_n)) > 0 and len(str(coor_w)) > 0:
    ## Astrology
    report["birth_year"] = str(report["dob"]).split("/")[2]
    _bdate = str(report["birth_year"]) + "/" + str(report["b_mon"]) + "/" + str(report["bday"])

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
else:
    pass

######### OUTPUT #########

subprocess.Popen(["clear"])

if report["detailed"] == True:
    print("\n%s" % logo)
print("################################################################\n\n\n")

print("First Name:    %s :   %s\n" % (report["first_name"], report["fname_int"]))
print("Middle Name:   %s :   %s\n" % (report["middle_name"], report["mname_int"]))
print("Last Name:     %s :   %s\n" % (last_name, report["lname_int"]))
print("DoB:           %s :   %s \n" % (report["dob"], report["life_path"]))
print("#############################################")
# Core Numbers
print("             CORE NUMBERS\n" + "#############################################\n")


if report["detailed"] == True:

    if int(report["life_mstr"]) != 0:
        b_li = int(report["life_mstr"])
        lpn = int(report["life_path"])
        in_data = "%s / %s" % (str(lpn), str(b_li))

    elif int(report["lp_k"]) != 0:
        b_li = int(report["life_path"])
        lpn = int(report["lp_k"])
        in_data = "%s / %s" % (str(b_li), str(lpn))

    else:
        b_li = int(report["life_path"])
        in_data = "%s" % str(b_li)

    print(" Life Path: %s" % str(in_data))
    print(" -  Ideal Partners: " + nd.partners["%i" % int(report["life_path"])])
    print(nd.lp_dict["lp%s" % str(b_li)])
    print("\n\n\n#############################################")
else:
    if int(report["life_mstr"]) != 0:
        b_li = int(report["life_mstr"])
        lpn = int(report["life_path"])
        in_data = "%s / %s" % (str(lpn), str(b_li))

    elif int(report["lp_k"]) != 0:
        b_li = int(report["life_path"])
        lpn = int(report["lp_k"])
        in_data = "%s / %s" % (str(b_li), str(lpn))

    else:
        b_li = int(report["life_path"])
        in_data = "%s" % str(b_li)

    print("   Life Path:          %s" % str(in_data))
    print("   -  Ideal Partners:  " + nd.partners["%i" % int(report["life_path"])])


if report["detailed"] == True:
    if int(master_ex) > 0:
        a_ex = int(report["expression"])
        b_ex = int(master_ex)
        exp_karm = "%s / %s" % (str(a_ex), str(b_ex))

    elif int(report["ex_k"]) > 0:
        b_ex = int(report["expression"])
        a_ex = int(report["ex_k"])
        exp_karm = "%s / %s" % (str(b_ex), str(a_ex))

    else:
        b_ex = int(report["expression"])
        exp_karm = "%s" % (str(b_ex))


    print("   Expression/Destiny: %s" % str(exp_karm))
    print(nd.ex_dict["%s" % str(b_ex)])
    print("\n\n\n#############################################")
else:
    if int(master_ex) > 0:
        a_ex = int(report["expression"])
        b_ex = int(master_ex)
        exp_karm = "%s / %s" % (str(a_ex), str(b_ex))

    elif int(report["ex_k"]) > 0:
        b_ex = int(report["expression"])
        a_ex = int(report["ex_k"])
        exp_karm = "%s / %s" % (str(b_ex), str(a_ex))

    else:
        b_ex = int(report["expression"])
        exp_karm = "%s / %s" % (str(b_ex), str(report["ex_two"]))

    print("   Expression/Destiny: %s" % str(exp_karm))


a_pers = 0
b_pers = 0

if report["detailed"] == True:
    if int(master_pers) == 11 or int(master_pers) == 22 or int(master_pers) == 33:
        a_pers = int(report["personality"])
        b_pers = int(master_pers)
        t_pers = int(master_pers)
        persona = "%i / %i" % (int(a_pers), int(b_pers))
    elif len(str(pers_twodig)) > 1:
        a_pers = int(report["personality"])
        b_pers = int(pers_twodig)
        t_pers = int(report["personality"])
        persona = "%i / %i" % (int(a_pers), int(b_pers))
    else:
        a_pers = int(report["personality"])
        t_pers = int(report["personality"])
        persona = "%i" % int(a_pers)

    print("   Personality:" + " %s" % str(persona))
    print(nd.per_dict["%s" % t_pers])
    print("\n\n#############################################")
else:

    if int(master_pers) == 11 or int(master_pers) == 22 or int(master_pers) == 33:
        a_pers = int(report["personality"])
        b_pers = int(master_pers)
        t_pers = int(master_pers)
        persona = "%i / %i" % (int(a_pers), int(b_pers))
    elif len(str(pers_twodig)) > 1:
        a_pers = int(report["personality"])
        b_pers = int(pers_twodig)
        t_pers = int(report["personality"])
        persona = "%i / %i" % (int(a_pers), int(b_pers))
    else:
        a_pers = int(report["personality"])
        t_pers = int(report["personality"])
        persona = "%i" % int(a_pers)

    print("   Personality:       " + " %s" % str(persona))


if report["detailed"] == True:
    print("    Heart\'s Desire:" + " %s" % report["hd_k"])
    print(nd.heart_dict["%s" % report["hearts_desire"]])
    print("\n\n#############################################")
else:
    print("   Heart\'s Desire:    " + " %s" % report["hd_k"])


if report["detailed"] == True:
    if int(red_b_day) > 0:
        if int(red_b_day) == int(report["bday"]):
            birth = "%s" % str(report["dayofbirth"])
        else:
            birth = "%s / %s" % (red_b_day, report["bday"])
    else:
        birth = report["bday"]
    print("    Birthday:" + "  %s" % birth)
    print(nd.b_dict["%s" % report["bday"]])
    print("\n\n#############################################\n\n\n")
else:
    if int(red_b_day) > 0:
        birth = "%s / %s" % (red_b_day, report["bday"])
    else:
        birth = report["bday"]
    print("   Birthday:         " + "  %s" % birth)

### Period Cycles

print("\n##########################################\n##########################################\n##########################################")
if report["detailed"] == True:
    print("\n - Period Cycles:               End Current / Begin Next\n")
    print("First Period Cycle:     %s:                %s" % (p_cycle1, per_cyc["cycles"][str(report["life_path"])]["1/2"]))
    print("-------------------")
    print(nd.per_cyc1[str(p_cycle1)])
    print("Second Period Cycle:     %s:                %s" % (p_cycle2, per_cyc["cycles"][str(report["life_path"])]["2/3"]))
    print("-------------------")
    print(nd.per_cyc2[str(p_cycle2)])
    print("Third Period Cycle:     %s:                %s >>" % (p_cycle3, per_cyc["cycles"][str(report["life_path"])]["2/3"].split("/")[1]))
    print("-------------------")
    print(nd.per_cyc3[str(p_cycle3)])
else:
    print("\n - Period Cycles:               End Current / Begin Next\n")
    print("First Period Cycle:     %s:                %s" % (p_cycle1, per_cyc["cycles"][str(report["life_path"])]["1/2"]))
    print("Second Period Cycle:     %s:                %s" % (p_cycle2, per_cyc["cycles"][str(report["life_path"])]["2/3"]))
    print("Third Period Cycle:     %s:                %s >>" % (p_cycle3, per_cyc["cycles"][str(report["life_path"])]["2/3"].split("/")[1]))

print("\n")

print("\n##########################################\n##########################################\n##########################################")

print("   - Karmic Lessons / Hidden Passions Chart")
print("""
        1: %s      2: %s     3: %s
        4: %s      5: %s     6: %s
        7: %s      8: %s     9: %s
""" % (nct[1], nct[2],
 nct[3], nct[4],
 nct[5], nct[6],
 nct[7], nct[8],
 nct[9]))

print("\n##########################################\n")
print("           - Karmic Lessons:")

index = 0
for i in nct:
    if nct[i] == 0:
        print("                  ===")
        print("                   %s" % i)
        print("                  ===")
        if report["detailed"] == True:
            print(nd.k_less["%s" % str(i)])

        index += 1

print("\n##########################################\n")

report["subcon_self"] = 9 - int(index)

print("\n##########################################\n")

print(" - Subconscious Self:" + "  %s" % report["subcon_self"])
if report["detailed"] == True:
    print(nd.sub_self["%s" % str(report["subcon_self"])])
print("\n##########################################\n")

print(" - Hidden Passion:\n")
hpl = ""
for i in hidden_passion_list:
#    hpl = str(hpl) + "%s  " % i
    print("                     %s  " % str(i))
    if report['detailed'] == True:
        print(nd.h_pass["%s" % str(i)])
    else:
        print(nd.h_pass["%s" % str(i)])

if report["detailed"] == True:
    print("\n##########################################\n##########################################\n##########################################")
    if int(report["lp_k"]) > 0 or int(report["ex_k"]) > 0 or int(report["per_k"]) > 0 or int(report["hd_karma"]) > 0 or int(report["b_k"]) > 0:
        print("        - Karmic Debt: ")
        if int(report["lp_k"]) > 0:
            print("\n\n###############")
            print("   - Life Path Karmic Debt:" + "  %s" % report["lp_k"])
            print("###############")
            print(nd.karm_dict["%s" % report["lp_k"]])
        if int(report["ex_k"]) > 0:
            print("###############")
            print("   - Expression Karmic Debt:" + "  %s" % report["ex_k"])
            print("###############")
            print(nd.karm_dict["%s" % report["ex_k"]])
        if int(report["per_k"]) > 0:
            print("\n\n###############")
            print("   - Personality Karmic Debt:" + "  %s" % report["per_k"])
            print("###############")
            print(nd.karm_dict["%s" % report["per_k"]])
        if int(report["hd_karma"]) > 0:
            print("\n\n###############")
            print("   - Heart\'s Desire Karmic Debt:" + "  %s" % report["hd_karma"])
            print("###############")
            print(nd.karm_dict["%s" % report["hd_karma"]])
        if int(report["b_k"]) > 0:
            print("\n\n###############")
            print("   - Birth-Day Karmic Debt:" + "  %s" % report["b_k"])
            print("###############\n")
            print(nd.karm_dict["%s" % report["b_k"]])
    print("\n##########################################\n##########################################\n##########################################")

else:
    print("\n##########################################\n##########################################\n##########################################")


if report["detailed"] == True:
    print(" - Balance: " + " %i" % int(report["balance"]))
    print(nd.bal_dic["%i" % int(report["balance"])])
else:
    print(" - Balance:      " + "  %i" % int(report["balance"]))

    print("\n##########################################\n##########################################\n##########################################")

if report["detailed"] == True:
    print("#############################################")
    print(" - Cornerstone: " + " %s:%i" % (str(cornerstone.upper()), int(corner_int)))
    print(nd.ccv["%s" % str(cornerstone.upper())])
    print("#############################################")
    print(" - Capstone   : " + " %s:%s " % (str(capstone.upper()), str(cap_int)))
    print(nd.cs_num["%s" % str(capstone.upper())])
    print("#############################################")
    print(" - First Vowel: " + " %s:%i" % (str(first_vowel.upper()), int(fv_int)))
    print(nd.vowel["%s" % str(first_vowel.upper())])
    print("#############################################")
    print(" - Key:         " + " %i" % (int(key_num)))

else:
    print(" - Cornerstone:   " + " %s : %i" % (str(cornerstone.upper()), int(corner_int)))
    print(" - Capstone:      " + " %s : %i" % (str(capstone.upper()), int(cap_int)))
    print(" - First Vowel:   " + " %s : %i" % (str(first_vowel.upper()), int(fv_int)))
    print(" - Key:           " + " %i" % (int(key_num)))


print("\n##########################################\n##########################################\n##########################################")

if report["detailed"] == True:
    print(" - Rational Thought:" + "  %s" % int(rtn))
    print(nd.rt_num["%s" % str(rtn)])
    print("\n\n#############################################")
    print(" - Alignment:" + "  %s" % report["alignment"])
    print("\n##########################################\n##########################################\n##########################################")
    print("#############################################")
    print("#############################################\n")
    print("         Planes of Expression:\n")
    print("#############################################")
    if len(str(exp_kList[1])) > 1:
        print("     -  Physical:     " + "%s / %s"  % (expres['physical'], str(exp_kList[1])))
    else:
        print("     -  Physical:     " + "%s"  % expres['physical'])
    try:
        print(nd.poe_phy["%s" % expres['physical'] ])
    except KeyError:
        pass
    print("#############################################")
    if len(str(exp_kList[1])) > 1:
        print("     -  Mental:     " + "%s / %s"  % (expres['mental'], str(exp_kList[2])))
    else:
        print("     -  Mental:       " + "%s"  % expres['mental'])
    try:
        print(nd.poe_ment["%s" % expres['mental'] ])
    except KeyError:
        pass
    print("#############################################")
    if len(str(exp_kList[1])) > 1:
        print("     -  Emotional:     " + "%s / %s"  % (expres['emotional'], str(exp_kList[3])))
    else:
        print("     -  Emotional:    " + "%s"  % expres['emotional'])
    try:
        print(nd.poe_emo["%s" % expres['emotional'] ])
    except KeyError:
        pass
    print("#############################################")
    if len(str(exp_kList[1])) > 1:
        print("     -  Intuitive:     " + "%s / %s"  % (expres['intuitive'], str(exp_kList[4])))
    else:
        print("     -  Intuitive:    " + "%s"  % expres['intuitive'])
    try:
        print(nd.poe_intu["%s" % expres['intuitive'] ])
    except KeyError:
        pass
    print("#############################################\n")
    print("     -  Creative:     " + "%s"   % expres['creative'])
    print("     -  Vacillating:  " + "%s"  % expres['vacillating'])
    print("     -  Grounded:     " + "%s"  % expres['grounded'])
    print("#############################################")
    print("#############################################\n")
else:
    print(" - Rational Thought:" + "  %s" % int(rtn))
    print("\n\n#############################################")
    print(" - Alignment:" + "  %s" % report["alignment"])
    print("\n##########################################\n##########################################\n##########################################")
    print("#############################################")
    print("#############################################\n")
    print("         Planes of Expression:\n")
    print("#############################################")
    if len(str(exp_kList[1])) > 1:
        print("     -  Physical:     " + "%s / %s"  % (expres['physical'], str(exp_kList[1])))
    else:
        print("     -  Physical:     " + "%s"  % expres['physical'])
    print("#############################################")
    if len(str(exp_kList[1])) > 1:
        print("     -  Mental:     " + "%s / %s"  % (expres['mental'], str(exp_kList[2])))
    else:
        print("     -  Mental:       " + "%s"  % expres['mental'])
    print("#############################################")
    if len(str(exp_kList[1])) > 1:
        print("     -  Emotional:     " + "%s / %s"  % (expres['emotional'], str(exp_kList[3])))
    else:
        print("     -  Emotional:    " + "%s"  % expres['emotional'])
    print("#############################################")
    if len(str(exp_kList[1])) > 1:
        print("     -  Intuitive:     " + "%s / %s"  % (expres['intuitive'], str(exp_kList[4])))
    else:
        print("     -  Intuitive:    " + "%s"  % expres['intuitive'])
    print("#############################################\n")
    print("     -  Creative:     " + "%s"   % expres['creative'])
    print("     -  Vacillating:  " + "%s"  % expres['vacillating'])
    print("     -  Grounded:     " + "%s"  % expres['grounded'])
    print("#############################################")
    print("#############################################\n\n\n")

print("\n##########################################\n##########################################\n##########################################")

### Maturity

if int(mat2) > 0:
    ture = "%s / %s" % (report["maturity"], mat2)
else:
    ture = report["maturity"]

if report["detailed"] == True:
    print(" - Maturity:" + "  %s" % ture)
    print(nd.mat_num["%s" % report["maturity"]])
else:
    print(" - Maturity:" + "  %s" % ture)

print("\n##########################################\n##########################################\n##########################################")

if report["detailed"] == False:
    print(" - Challenge 1:" + "  %s" % report["challenge_1"])
    print(" - Challenge 2:" + "  %s" % report["challenge_2"])
    print(" - Challenge 3:" + "  %s" % report["challenge_3"])
    print(" - Challenge 4:" + "  %s" % report["challenge_4"])
else:
    print(" - Challenge 1:" + "  %s" % report["challenge_1"])
    print(nd.cnum["%s" % str(report["challenge_1"])])
    print("\n\n#############################################")
    print(" - Challenge 2:" + "  %s" % report["challenge_2"])
    print(nd.cnum["%s" % str(report["challenge_2"])])
    print("\n\n#############################################")
    print(" - Challenge 3:" + "  %s" % report["challenge_3"])
    print(nd.cnum["%s" % str(report["challenge_3"])])
    print("\n\n#############################################")
    print(" - Challenge 4:" + "  %s" % report["challenge_4"])
    print(nd.cnum["%s" % str(report["challenge_4"])])

print("\n##########################################\n##########################################\n##########################################")

if report["detailed"] == True:
    print(" - Life Path/Expression Bridge:" + "       %i" % report["le_bridge"])
    print(nd.bridge["%s" % str(report["le_bridge"])])

    print(" - Hearts Desire/Personality Bridge:" + "  %i" % report["hp_bridge"])
    print(nd.bridge["%s" % str(report["hp_bridge"])])

    print(" - Life Path/Birthday Bridge:" + "         %i" % report["lb_bridge"])
    print(nd.bridge["%s" % str(report["lb_bridge"])])

else:
    print(" - Life Path/Expression Bridge:" + "       %i" % report["le_bridge"])
    print(" - Hearts Desire/Personality Bridge:" + "  %i" % report["hp_bridge"])

### Pinnacle Cycles

print("\n##########################################\n##########################################\n##########################################")

if report["detailed"] == True:
    print(" - Pinnacle Cycles:\n")
    print("First Cycle:     %s:  %s" % (report["first_cycle"], pin_cyc["paths"][report["life_path"]]["1st_cycle"]))
    print(nd.pinnacle_cycle["%s" % str(report["first_cycle"])])
    print("Second Cycle:     %s:  %s" % (report["second_cycle"], pin_cyc["paths"][report["life_path"]]["2nd_cycle"]))
    print(nd.pinnacle_cycle["%s" % str(report["second_cycle"])])
    print("Third Cycle:     %s:  %s" % (report["third_cycle"], pin_cyc["paths"][report["life_path"]]["3rd_cycle"]))
    print(nd.pinnacle_cycle["%s" % str(report["third_cycle"])])
    print("Fourth Cycle:     %s:  %s" % (report["fourth_cycle"], pin_cyc["paths"][report["life_path"]]["4th_cycle"]))
    print(nd.pinnacle_cycle["%s" % str(report["fourth_cycle"])])
else:
    print("First Cycle:     %s:  %s" % (report["first_cycle"], pin_cyc["paths"][report["life_path"]]["1st_cycle"]))
    print("Second Cycle:     %s:  %s" % (report["second_cycle"], pin_cyc["paths"][report["life_path"]]["2nd_cycle"]))
    print("Third Cycle:     %s:  %s" % (report["third_cycle"], pin_cyc["paths"][report["life_path"]]["3rd_cycle"]))
    print("Fourth Cycle:     %s:  %s" % (report["fourth_cycle"], pin_cyc["paths"][report["life_path"]]["4th_cycle"]))

if len(str(_btime)) > 0 and len(str(_tzone)) > 0 and len(str(coor_n)) > 0 and len(str(coor_w)) > 0:
    stars = chart.getFixedStars()
    star_list = {}
    for item in stars:
        s_list = str(item).replace('<', '').replace('>', '').split()
        star_list[s_list[0]] = str(s_list[1])
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
    try:
        for factor in factors:
            print("     %s:     %s" % (factor[0], factor[1][0]))
    except Exception as error:
        pass
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
else:
    pass
