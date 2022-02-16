#!/usr/bin/env python3

import getopt
import sys
from termcolor import colored

USAGE = """
./numerologist.py -f [first_name] -m [middle_name] -l [last_name] -d [dob {dd/mm/yyyy}]
"""

alpha = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':1,
         'K':2, 'L':3, 'M':4, 'N':5, 'O':6, 'P':7, 'Q':8, 'R':9, 'S':1, 'T':2,
         'U':3, 'V':4, 'W':5, 'X':6, 'Y':7, 'Z':8}

fname = None
fname_int = 0
mname = None
mname_int = 0
lname = None
lname_int = 0
dob = None
dob_int = 0
life_path = 0
lp_karma = 0
lp_k = ""
expression = 0
ex_karma = 0
ex_k = ""
personality = 0
pers_karma = 0
per_k = ""
hearts_desire = 0
hd_karma = 0
hd_k = ""
bday = 0
birth_day = 0
b_karma = 0
b_k = ""
maturity = 0
alignment = 0
challenge_1 = 0
challenge_2 = 0
challenge_3 = 0
challenge_4 = 0
le_bridge = 0
hp_bridge = 0
lb_bridge = 0

argv = sys.argv[1:]

options, args = getopt.getopt(argv, "f:m:l:d:h",
                           ["fname=",
                            "mname=",
                            "lname=",
                            "dob=",
                            "help"])

for name, value in options:

    if name in ['-f', '--fname']:
        fname = value

    if name in ['-m', '--mname']:
        mname = value

    if name in ['-l', '--lname']:
        lname = value

    if name in ['-d', '--dob']:
        dob = value

    if name in ['-h', '--help']:
        print(USAGE)
        sys.exit()


###################################
## Life Path
dob = dob.replace('/', '')
for item in str(dob):
    dob_int = dob_int + int(item)
for item in str(dob_int):
    life_path = life_path + int(item)
while len(str(life_path)) > 1 or life_path == 11 or life_path == 22 or life_path == 33:
    if life_path == 13 or life_path == 14 or life_path == 16 or life_path == 19:
        lp_karma = life_path
    tmp = 0
    for item in str(life_path):
        tmp = tmp + int(item)
    life_path = tmp

if lp_karma > 0:
    lp_k = "%i/%i" % (life_path, lp_karma)

###################################
## Expression/Destiny
conv = 0
for item in fname:
    conv = conv + alpha[item.upper()]
result = 0
for item in str(conv):
    result = result + int(item)
fname_int = result
while len(str(fname_int)) > 1:
    fni = 0
    for item in str(fname_int):
        fni = fni + int(item)
        fname_int = fni

conv = 0
for item in mname:
    conv = conv + alpha[item.upper()]
result = 0
for item in str(conv):
    result = result + int(item)
mname_int = result
while len(str(mname_int)) > 1:
    mni = 0
    for item in str(mname_int):
        mni = mni + int(item)
        mname_int = mni

conv = 0
for item in lname:
    conv = conv + alpha[item.upper()]
result = 0
for item in str(conv):
    result = result + int(item)
lname_int = result
while len(str(lname_int)) > 1:
    lni = 0
    for item in str(lname_int):
        lni = lni + int(item)
        lname_int = lni


path_init = fname_int + mname_int + lname_int
for item in str(path_init):
    expression = expression + int(item)
while len(str(expression)) > 1:
    if expression == 13 or expression == 14 or expression == 16 or expression == 19:
        ex_karma = expression
    exp = 0
    for item in str(expression):
        exp = exp + int(item)
        expression = exp
if ex_karma > 0:
    ex_k = "%i/%i" % (expression, ex_karma)

###################################
## Personality
cons_fname = ""
cf_int = 0
cons_mname = ""
cm_int = 0
cons_lname = ""
cl_int = 0
for item in fname.upper():
    if item != 'A' and item != 'E' and item != "I" and item != 'O' and item != "U":
        cons_fname = cons_fname + item
for item in mname.upper():
    if item != 'A' and item != 'E' and item != "I" and item != 'O' and item != "U":
        cons_mname = cons_mname + item
for item in lname.upper():
    if item != 'A' and item != 'E' and item != "I" and item != 'O' and item != "U":
        cons_lname = cons_lname + item
conv = 0
for item in cons_fname:
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
#print("cons_fname: %s\ncf_int: %i" % (cons_fname, cf_int))
conv = 0
for item in cons_mname:
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
#print("cons_mname: %s\ncm_int: %i" % (cons_mname, cm_int))
conv = 0
for item in cons_lname:
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
#print("cons_lname: %s\ncl_int: %i" % (cons_lname, cl_int))
init_pers = ""
for item in str(cf_int):
    init_pers = str(init_pers) + str(item)
#print(init_pers)
for item in str(cm_int):
    init_pers = str(init_pers) + str(item)
#print(init_pers)
for item in str(cl_int):
    init_pers = str(init_pers) + str(item)
#print(init_pers)
pers_num = 0
for item in str(init_pers):
    pers_num = pers_num + int(item)
while len(str(pers_num)) > 1 or pers_num == 11 or pers_num == 22 or pers_num == 33:
    if pers_num == 13 or pers_num == 14 or pers_num == 16 or pers_num == 19:
        pers_karma = pers_num

    tmp = 0
    for item in str(pers_num):
        tmp = tmp + int(item)
    pers_num = tmp
personality = pers_num
#print("init_pers: ", init_pers)

if pers_karma > 0:
    per_k = "%i/%i" % (pers_num, pers_karma)

###################################
## Hearts Desire
vow_fname = ""
vf_int = 0
vow_mname = ""
vm_int = 0
vow_lname = ""
vl_int = 0
for item in fname.upper():
    if item == 'A' or item == 'E' or item == "I" or item == 'O' or item == "U":
        vow_fname = vow_fname + item
for item in mname.upper():
    if item == 'A' or item == 'E' or item == "I" or item == 'O' or item == "U":
        vow_mname = vow_mname + item
for item in lname.upper():
    if item == 'A' or item == 'E' or item == "I" or item == 'O' or item == "U":
        vow_lname = vow_lname + item
conv = 0
for item in vow_fname:
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
for item in vow_mname:
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
for item in vow_lname:
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
#print(init_hd)
for item in str(vm_int):
    init_hd = str(init_hd) + str(item)
#print(init_hd)
for item in str(vl_int):
    init_hd = str(init_hd) + str(item)
#print(init_hd)
hd_num = 0
for item in str(init_hd):
    hd_num = hd_num + int(item)
while len(str(hd_num)) > 1 or hd_num == 11 or hd_num == 22 or hd_num == 33:
    if hd_num == 13 or hd_num == 14 or hd_num == 16 or hd_num == 19:
        hd_karma = hd_num
    tmp = 0
    for item in str(hd_num):
        tmp = tmp + int(item)
    hd_num = tmp
hearts_desire = hd_num
#print("init_hd: ", init_hd)
if hd_karma > 0:
    hd_k = "%i/%i" % (hearts_desire, hd_karma)

###################################
## Birth day

bd = dob[:-4]
bday = bd[-2:]

while len(str(bday)) > 1:
    if int(bday) == 11 or int(bday) == 13 or int(bday) == 14 or int(bday) == 16 or int(bday) == 19 or int(bday) == 22 or int(bday) == 33:
        b_karma = int(bday)
        for item in str(bday):
            birth_day = birth_day + int(item)
            bday = birth_day
    else:
        d = 0
        for item in str(bday):
            d = d + int(item)
        birth_day = int(d)
        bday = birth_day

if b_karma > 0:
    b_k = "%i/%i" % (birth_day, b_karma)

###################################
## Maturity
mat = int(life_path) + int(expression)
while len(str(mat)) > 1:
    tmp = 0
    for item in str(mat):
        tmp = tmp + int(item)
    mat = tmp
maturity = int(mat)


## Alignment
bm = dob[:-6]
alg = int(bm) + int(birth_day)
while len(str(alg)) > 1:
    tmp = 0
    for item in str(alg):
        tmp = tmp + int(item)
    alg = tmp
alignment = int(alg)


###################################
## Challenge 1

b_day = birth_day
#print(b_day)
while len(str(b_day)) > 1:
    tmp = 0
    for item in str(b_day):
        tmp = tmp + int(item)
    b_day = tmp
#print(b_day)
b_mon = bm
#print(b_mon)
while len(str(b_mon)) > 1 or b_mon == 11:
    tmp = 0
    for item in str(b_mon):
        tmp = tmp + int(item)
    b_mon = tmp
#print(b_mon)

if int(b_day) > int(b_mon):
#    print('using if')
    chal_1 = int(b_day) - int(b_mon)
#    print(chal_1)

else:
#    print('using else')
    chal_1 = int(b_mon) - int(b_day)
#    print(chal_1)

while len(str(chal_1)) > 1:
    tmp = 0
    for item in str(chal_1):
        tmp = tmp + int(item)
    chal_1 = tmp
challenge_1 = int(chal_1)

###################################
## Challenge 2
b_year = dob[4:]
while len(str(b_year)) > 1:
    tmp = 0
    for item in str(b_year):
        tmp = tmp + int(item)
    b_year = tmp
#print(b_year)
if int(b_day) > int(b_year):
#    print('using if')
    chal_2 = int(b_day) - int(b_year)
#    print(chal_2)

else:
#    print('using else')
    chal_2 = int(b_year) - int(b_day)
#    print(chal_2)

challenge_2 = chal_2

###################################
## Challenge 3
if int(challenge_1) > int(challenge_2):
#    print('using if')
    chal_3 = int(challenge_1) - int(challenge_2)
#    print(chal_3)
    challenge_3 = chal_3

else:
#    print('using else')
    chal_3 = int(challenge_2) - int(challenge_1)
#    print(chal_3)
    challenge_3 = chal_3

###################################
## Challenge 4
if int(b_mon) > int(b_year):
#    print('using if')
    chal_4 = int(b_mon) - int(b_year)
#    print(chal_4)

else:
#    print('using else')
    chal_4 = int(b_year) - int(b_mon)
#    print(chal_4)

challenge_4 = chal_4


######################
## Life Path / Expression Bridge
if int(life_path) > int(expression):
    le_bridge = int(life_path) - int(expression)
else:
    le_bridge = int(expression) - int(life_path)


######################
## Heart's Desire / Personality Bridge
if int(hearts_desire) > int(personality):
    hp_bridge = int(hearts_desire) - int(personality)
else:
    hp_bridge = int(personality) - int(hearts_desire)


######################
## Life Path / Birthday Bridge
if int(life_path) > int(birth_day):
    lb_bridge = int(life_path) - int(birth_day)
else:
    lb_bridge = int(birth_day) - int(life_path)

######################
## Karmic Debt
if len(lp_k) > 1:
    life_path = lp_kd
if len(ex_k) > 1:
    expression = ex_k
if len(per_k) > 1:
    personality = per_k
if len(hd_k) > 1:
    hearts_desire = hd_k
if len(b_k) > 1:
    birth_day = b_k


print("\n\nFirst Name:\n   %s : %s\n" % (fname, colored(fname_int, 'blue', attrs=['bold'])))
print("Middle Name:\n   %s : %s\n" % (mname, colored(mname_int, 'blue', attrs=['bold'])))
print("Last Name:\n   %s : %s\n" % ( lname, colored(lname_int, 'blue', attrs=['bold'])))
print(colored("        CORE\n#####################", 'yellow', attrs=['bold']))
print(colored("#  ", 'yellow', attrs=['bold']) + colored("Life Path: %s" % life_path, 'blue', attrs=['bold']))
print(colored("#  ", 'yellow', attrs=['bold']) + colored("Expression: %s" % expression, 'blue', attrs=['bold']))
print(colored("#  ", 'yellow', attrs=['bold']) + colored("Personality: %s" % personality, 'blue', attrs=['bold']))
print(colored("#  ", 'yellow', attrs=['bold']) + colored("Hearts Desire: %s" % hearts_desire, 'blue', attrs=['bold']))
print(colored("#  ", 'yellow', attrs=['bold']) + colored("Birthday: %s" % birth_day, 'blue', attrs=['bold']))
print(colored("#####################", 'yellow', attrs=['bold']))
print("\n")
print(colored(" - Maturity: %s" % maturity, 'blue', attrs=['bold']))
print(colored(" - Alignment: %s" % alignment, 'blue', attrs=['bold']))
print("\n")
print(colored(" - Challenge 1: %s" % challenge_1, 'blue', attrs=['bold']))
print(colored(" - Challenge 2: %s" % challenge_2, 'blue', attrs=['bold']))
print(colored(" - Challenge 3: %s" % challenge_3, 'blue', attrs=['bold']))
print(colored(" - Challenge 4: %s" % challenge_4, 'blue', attrs=['bold']))
print("\n")
print(colored(" - Life Path/Expression Bridge: %i" % le_bridge, 'blue', attrs=['bold']))
print(colored(" - Hearts Desire/Personality Bridge: %i" % hp_bridge, 'blue', attrs=['bold']))
print(colored(" - Life Path/Birthday Bridge: %i" % lb_bridge, 'blue', attrs=['bold']))


print("\n")
