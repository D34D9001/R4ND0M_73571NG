#!/usr/bin/env python3

__author__ = "D34D9001"
__copyright__ = "Copyleft 2022"
__license__ = "GPL"
__version__ = "1.2.5"
__maintainer__ = "D34D9001@9R0GR4M13"
__email__ = "program13@protonamil.com"
__status__ = "Beta"

# Dictionaries

logo = {
"1": """    ...    :::::::..    :::.       .,-:::::   :::    .,::::::  """,
"2": """ .;;;;;;;. ;;;;``;;;;   ;;`;;    ,;;;'````\'   ;;;    ;;;;\'\'\'\'  """,
"3": """,[[     \[[,[[[,/[[[\'  ,[[ \'[[,  [[[          [[[     [[cccc   """,
"4": """$$$,     $$$$$$$$$c   c$$$cc$$$c $$$          $$\'     $$\"\"\"\"   """,
"5": """\"888,_ _,88P888b \"88bo,888   888,`88bo,__,o, o88oo,.__888oo,__ """,
"6": """  \"YMMMMMP\" MMMM   \"W\" YMM   \"\"`   \"YUMMMMMP\"\"\"\"\"YUMMM\"\"\"\"YUMMM""",
"7": """              :::. ::::::::::::                                """,
"8": """              ;;`;;;;;;;;;;\'\'\'\'                                """,
"9": """             ,[[ \'[[,   [[                                     """,
"10": """            c$$$cc$$$c  $$                                     """,
"11": """             888   888, 88,                                    """,
"12": """             YMM   ""`  MMM                                    """,
"13": """:::::::-.  .,::::::   :::  ::::::::::.  ::   .:  :::           """,
"14": """ ;;,   `\';,;;;;\'\'\'\'   ;;;   `;;;```.;;;,;;   ;;, ;;;           """,
"15": """ `[[     [[ [[cccc    [[[    `]]nnn]]\',[[[,,,[[[ [[[           """,
"16": """  $$,    $$ $$\"\"\"\"    $$\'     $$$\"\"   \"$$$\"\"\"$$$ $$$           """,
"17": """  888_,o8P\' 888oo,__ o88oo,.__888o     888   \"88o888           """,
"18": """  MMMMP\"`   \"\"\"\"YUMMM\"\"\"\"YUMMMYMMMb    MMM    YMMMMM           """}


alpha = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':1,
         'K':2, 'L':3, 'M':4, 'N':5, 'O':6, 'P':7, 'Q':8, 'R':9, 'S':1, 'T':2,
         'U':3, 'V':4, 'W':5, 'X':6, 'Y':7, 'Z':8}


report = {"fname": None, "fname_int": 0, "mname": None, "mname_int": 0, "lname": None, "lname_int": 0, "dob": None, "dob_int": 0,
 "life_path": 0, "lp_karma": 0, "lp_k": 0, "expression": 0, "ex_karma": 0, "ex_k": 0, "personality": 0, "pers_karma": 0, "per_k": 0,
 "hearts_desire": 0, "hd_karma": 0,"hd_k": 0, "bday": 0, "birth_day": 0, "b_karma": 0, "b_k": 0, "maturity": 0, "alignment": 0,
 "challenge_1": 0, "challenge_2": 0, "challenge_3": 0, "challenge_4": 0, "le_bridge": 0, "hp_bridge": 0, "lb_bridge": 0, "detailed": False,
 "first_name": "", "middle_name": "", "last_name": "", "life_mstr": 0, "dob_int": 0, "db": 0, "dayofbirth": 0, "vow_fname": None,
 "vow_mname": "", "vow_lname": "", "cons_fname": "", "cons_mname": "", "cons_lname": "", "balance": 0, "fullname": None, "subcon_self": 0,
 "ex_two": 0, "b_mon": 0, "first_cycle": 0, "second_cycle": 0, "third_cycle": 0, "fourth_cycle": 0, "b_year": 0, "birth_year": 0,
 "gf_name": "", "gm_name": "", "gl_name": "", "greek_fullname": "", "full_name": "", "greek_int": 0}

greek_num = {"Α": 1, "α": 1, "Β": 2, "β": 2, "Γ": 3, "γ": 3, "Δ": 4, "δ": 4, "Ε": 5, "ε": 5, "": 6, "": 6, "Ϛ": 6, "ϛ": 6, "Ζ": 7, "ζ": 7, "Η": 8, "η": 8,
 "Θ": 9, "θ": 9, "Ι": 10, "ι": 10, "Κ": 20, "κ": 20, "Λ": 30, "λ": 30, "Μ": 40, "μ": 40, "Ν": 50, "ν": 50, "Ξ": 60, "ξ": 60, "Ο": 70, "ο": 70, "Π": 80, "π": 80,
 "Ϙ": 90, "ϙ": 90, "Ρ": 100, "ρ": 100, "Σ": 200, "σ": 200, "T": 300, "τ": 300, "Υ": 400, "υ": 400, "Φ": 500, "φ": 500, "Χ": 600, "χ": 600, "Ψ": 700, "ψ": 700,
 "Ω": 800, "ω": 800, "Ϡ": 900, "ϡ": 900}

# Delphi modules

import getopt
import sys
import numdic as nd
import operator
import subprocess

# Astrology modules
import getopt
import sys
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos
from flatlib import const
from flatlib.protocols.temperament import Temperament
from flatlib.protocols import behavior
from flatlib.predictives import returns

## Isopsephy modules
#from google.cloud import translate_v2 as translate
#import unidecode


# Output Modules
import os
import string
from fpdf import FPDF
from termcolor import colored
#fpdf.set_global("SYSTEM_TTFONTS", os.path.join(os.path.dirname(__file__),'/usr/share/fonts/chromeos/noto'))

#pdf = fpdf.FPDF()
#pdf.add_font("NotoSans-Regular", style="", fname="NotoSans-Regular.ttf", uni=True)
#pdf.add_page()
#pdf.set_font("NotoSans-Regular", size = 12)




USAGE = """
./delphi.py -f [first_name] -m [middle_name] -l [report["last_name"]] -d [dob {dd/mm/yyyy}] -t ["01:30"] -z ["-06:00"] -n ["36n50"] -w ["86w88"] [-x (optional)]
"""

_bdate = "" # EX: 2020/01/30
_btime = "" # EX: 15:00
_tzone = "" # EX: -06:00
coor_n = "" # N Coords
coor_w = "" # W Coords

ws = string.whitespace

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

try:
    for name, value in options:
        if len(options) == 0:
            add_data(USAGE)
            sys.exit(1)
        if name in ['-f', '--fname']:
            report["fname"] = str(value).replace("-", "")
            report["first_name"] = value

        if name in ['-m', '--mname']:
            report["mname"] = str(value).replace("-", "")
            report["middle_name"] = value

        if name in ['-l', '--lname']:
            report["lname"] = str(value).replace("-", "")
            report["last_name"] = value

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
            add_data(USAGE)
            sys.exit()
except Exception as error:
    print(colored(error, 'red', attrs=['bold', 'underline', 'blink']))
    print("\n\n" + USAGE)
    sys.exit()


report["full_name"] = str(report["fname"]) + " " + str(report["mname"]) + " " +  str(report["lname"])
report["fullname"] = str(report["fname"]) + str(report["mname"]) + str(report["lname"])

filename = "/home/t3rm1n41/AstroNum/" + str(report['first_name']) + "_" + str(report["last_name"])

title = "%s %s Personality Profile" % (str(report['first_name']), str(report['last_name']))

class PDF(FPDF):
    def header(self):

        # Arial bold 15
        self.set_font('Arial', 'B', 9)
        # Calculate width of title and position
        w = self.get_string_width(title) + 6
        self.set_x((210 - w) / 2)
        # Colors of frame, background and text
        self.set_draw_color(0, 80, 180)
#        self.set_fill_color(230, 230, 0)
        self.set_text_color(220, 50, 50)
        # Thickness of frame (1 mm)
        self.set_line_width(1)
        # Title
        self.cell(w, 9, title, 1, 1, 'C', 1)
        # Line break
        self.ln(10)

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 7)
        # Text color in gray
        self.set_text_color(128)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

    def chapter_title(self, num, label):
        # Arial 12
        self.set_font('Arial', '', 15)
        # Background color
        self.set_fill_color(200, 220, 255)
        # Title
        self.cell(0, 6, 'Chapter %d : %s' % (num, label), 0, 1, 'C', 1)
        # Line break
        self.ln(4)

    def chapter_body(self, name):
        # Read text file
        with open(name, 'rb') as fh:
            txt = fh.read().decode('latin-1')
        # Times 12
        self.set_font('Times', '', 12)
        # Output justified text
        self.multi_cell(0, 5, txt, align = 'J')
        # Line break
        self.ln()
        # Mention in italics
        self.set_font('', 'I')
        self.cell(0, 5, '(end of chapter)', align = 'C')

    def print_chapter(self, num, title, name):
        self.add_page()
        self.chapter_title(num, title)
        self.chapter_body(name)

pdf = PDF()

#pdf.add_page()
#pdf.image('/home/t3rm1n41/R4ND0M_73571NG/python/Kaos/media/logo/13-1.png', 70, 100, 100, 100)

###############################################
tmp_files = []

def add_data(data, file):
    with open("/home/t3rm1n41/AstroNum/tmp/%s" % file, 'a') as f:
        f.write(str(data))
    f.close()

def create_txt_page(file):
    tmp_files.append("/home/t3rm1n41/AstroNum/tmp/%s" % file)
    with open("/home/t3rm1n41/AstroNum/tmp/%s" % file, 'w') as f:
        f.write("")
    f.close()


def del_tmp():
    for item in tmp_files:
#        print(item)
        deltmp = subprocess.Popen(["srm", "%s" % str(item)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    std_out, std_err = deltmp.communicate()
    if len(str(std_out)) >= 1:
#        print(std_out)
        sys.exit()

###############################################

def new_chap(chapter, chtitle, file):
    pdf.print_chapter(int(chapter), str(chtitle), "/home/t3rm1n41/AstroNum/tmp/%s" % str(file))


## Isopsephy Calculation


#def translate_text(target, text):
#    import six
#    from google.cloud import translate_v2 as translate
#
#    translate_client = translate.Client()
#
#    if isinstance(text, six.binary_type):
#        text = text.decode("utf-8")
#
#    result = translate_client.translate(text, target_language=target)
##    print(result)
#    report["greek_full"] = (u"{}".format(result["translatedText"]))
##    print(report["greek_full"])
#
#translate_text('el', str(report["full_name"]))
#
#g_int_lst = []
#for item in str(report["greek_full"]):
#    try:
#        if str(item) == str(greek_num[item]):
#            print(item)
#        else:
#            pass
#    except Exception as error:
#        print(str(error) + "\n")
##    g_int_lst.append(greek_num[item])
#
##for item in g_int_lst:
##    print(item)
##report["greek_int"] = 0
##print(report["greek_full"])
#
##for item in str(report["greek_full"]):
#
##    report["greek_int"] = int(report["greek_int"]) + int(greek_num[item])
#
##    print(report["greek_int"])
#
##for item in str(report["greek_full"]):
##    accented_string = u"%s" % str(item)
##    unaccented_string = unidecode.unidecode(accented_string)
##    item = str(unaccented_string)
##    report["greek_int"] = int(report["greek_int"]) + int(greek_num["%s" % str(item)])
#
##print(report["greek_int"])
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
        add_data("%s could not be located!" % item)


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


mI = max(nct.values())
hidden_passion_list = []
for item in nct:

#    add_data(item, nct[item])
    if int(nct[item]) == mI:
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
#add_data("vow_fname: %s\n\nvf_int: %i" % (vow_fname, vf_int))
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
#add_data("vow_mname: %s\n\nvm_int: %i" % (vow_mname, vm_int))
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
#add_data("vow_lname: %s\n\nvl_int: %i" % (vow_lname, vl_int))
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
#add_data(report["b_mon"])
while len(str(report["b_mon"])) > 1 or report["b_mon"] == 11:
    report["tmp"] = 0
    for item in str(report["b_mon"]):
        report["tmp"] = int(report["tmp"]) + int(item)
    report["b_mon"] = report["tmp"]
#add_data(report["b_mon"])

if int(b_day) > int(report["b_mon"]):
#    add_data('using if')
    chal_1 = int(b_day) - int(report["b_mon"])
#    add_data(chal_1)

else:
#    add_data('using else')
    chal_1 = int(report["b_mon"]) - int(b_day)
#    add_data(chal_1)

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
#add_data(report["b_year"])
if int(b_day) > int(report["b_year"]):
#    add_data('using if')
    chal_2 = int(b_day) - int(report["b_year"])
#    add_data(chal_2)

else:
#    add_data('using else')
    chal_2 = int(report["b_year"]) - int(b_day)
#    add_data(chal_2)

report["challenge_2"] = chal_2

while len(str(report["challenge_2"])) > 1:
    temp = 0
    for item in str(report["challenge_2"]):
        temp = temp + int(item)
    report["challenge_2"] = temp
###################################
## Challenge 3
if int(report["challenge_1"]) > int(report["challenge_2"]):
#    add_data('using if')
    chal_3 = int(report["challenge_1"]) - int(report["challenge_2"])
#    add_data(chal_3)
    report["challenge_3"] = chal_3

else:
#    add_data('using else')
    chal_3 = int(report["challenge_2"]) - int(report["challenge_1"])
#    add_data(chal_3)
    report["challenge_3"] = chal_3

while len(str(report["challenge_3"])) > 1:
    temp = 0
    for item in str(report["challenge_3"]):
        temp = temp + int(item)
    report["challenge_3"] = temp
###################################
## Challenge 4
if int(report["b_mon"]) > int(report["b_year"]):
#    add_data('using if')
    chal_4 = int(report["b_mon"]) - int(report["b_year"])
#    add_data(chal_4)

else:
#    add_data('using else')
    chal_4 = int(report["b_year"]) - int(report["b_mon"])
#    add_data(chal_4)

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

#subprocess.call(["clear"])

create_txt_page('core.txt')

add_data("First Name:    %s :   %s\n" % (report["first_name"], report["fname_int"]), 'core.txt')
add_data("Middle Name:   %s :   %s\n" % (report["middle_name"], report["mname_int"]), 'core.txt')
add_data("Last Name:     %s :   %s\n" % (report["last_name"], report["lname_int"]), 'core.txt')
add_data("DoB:           %s :   %s\n" % (report["dob"], report["life_path"]), 'core.txt')
add_data("\n#############################################\n", 'core.txt')
# Core Numbers

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

    add_data("\n - Life Path: %s\n  " % str(in_data), 'core.txt')
    add_data("\n   -  Ideal Partners: " + nd.partners["%i" % int(report["life_path"])]+ "\n\n", 'core.txt')
    add_data(nd.lp_dict["lp%s" % str(b_li)] + "\n", 'core.txt')
    add_data("\n#############################################\n\n", 'core.txt')
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

    add_data("\n - Life Path:          %s\n\n" % str(in_data), 'core.txt')
    add_data("   -  Ideal Partners:  " + nd.partners["%i" % int(report["life_path"])] + "\n", 'core.txt')
    add_data("\n#############################################\n\n", 'core.txt')


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


    add_data("\n - Expression/Destiny: %s\n\n" % str(exp_karm), 'core.txt')
    add_data(nd.ex_dict["%s" % str(b_ex)] + "\n", 'core.txt')
    add_data("\n#############################################\n\n", 'core.txt')
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

    add_data("\n - Expression/Destiny: %s\n\n" % str(exp_karm), 'core.txt')


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

    add_data("\n - Personality:" + " %s\n\n" % str(persona), 'core.txt')
    add_data(nd.per_dict["%s" % t_pers] + "\n", 'core.txt')
    add_data("\n#############################################\n\n", 'core.txt')
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

    add_data("\n - Personality:       " + " %s\n\n" % str(persona), 'core.txt')


if report["detailed"] == True:
    add_data("\n - Heart\'s Desire:" + " %s\n\n" % report["hd_k"], 'core.txt')
    add_data(nd.heart_dict["%s" % report["hearts_desire"]] + "\n", 'core.txt')
    add_data("\n#############################################\n\n", 'core.txt')
else:
    add_data("\n - Heart\'s Desire:    " + " %s\n\n" % report["hd_k"], 'core.txt')


if report["detailed"] == True:
    if int(red_b_day) > 0:
        if int(red_b_day) == int(report["bday"]):
            birth = "%s" % str(report["dayofbirth"])
        else:
            birth = "%s / %s" % (red_b_day, report["bday"])
    else:
        birth = report["bday"]
    add_data("\n - Birthday:" + "  %s\n\n" % birth, 'core.txt')
    add_data(nd.b_dict["%s" % report["bday"]] + "\n", 'core.txt')
    add_data("\n#############################################\n\n", 'core.txt')
else:
    if int(red_b_day) > 0:
        birth = "%s / %s" % (red_b_day, report["bday"])
    else:
        birth = report["bday"]
    add_data("\n - Birthday:         " + "  %s" % birth + "\n", 'core.txt')
    add_data("\n#############################################\n\n", 'core.txt')



### Period Cycles
create_txt_page('period_cycles.txt')


if report["detailed"] == True:
    add_data("Period Cycles:               End Current / Begin Next\n", 'period_cycles.txt')
    add_data("\n#############################################\n\n", 'period_cycles.txt')
    add_data("\n - First Period Cycle:     %s:                %s\n\n" % (p_cycle1, per_cyc["cycles"][str(report["life_path"])]["1/2"]), 'period_cycles.txt')
    add_data(nd.per_cyc1[str(p_cycle1)] + "\n", 'period_cycles.txt')
    add_data("\n#############################################\n\n", 'period_cycles.txt')
    add_data("\n - Second Period Cycle:     %s:                %s\n\n" % (p_cycle2, per_cyc["cycles"][str(report["life_path"])]["2/3"]), 'period_cycles.txt')
    add_data(nd.per_cyc2[str(p_cycle2)] + "\n", 'period_cycles.txt')
    add_data("\n#############################################\n\n", 'period_cycles.txt')
    add_data("\n - Third Period Cycle:     %s:                %s\n\n >>" % (p_cycle3, per_cyc["cycles"][str(report["life_path"])]["2/3"].split("/")[1]), 'period_cycles.txt')
    add_data(nd.per_cyc3[str(p_cycle3)] + "\n", 'period_cycles.txt')
else:
    add_data("\n#############################################\n\n", 'period_cycles.txt')
    add_data("\n - Period Cycles:               End Current / Begin Next\n\n", 'period_cycles.txt')
    add_data("\n - First Period Cycle:     %s:                %s\n\n" % (p_cycle1, per_cyc["cycles"][str(report["life_path"])]["1/2"]), 'period_cycles.txt')
    add_data("\n - Second Period Cycle:     %s:                %s\n\n" % (p_cycle2, per_cyc["cycles"][str(report["life_path"])]["2/3"]), 'period_cycles.txt')
    add_data("\n - Third Period Cycle:     %s:                %s\n\n >>" % (p_cycle3, per_cyc["cycles"][str(report["life_path"])]["2/3"].split("/")[1]), 'period_cycles.txt')

add_data("\n#############################################\n\n", 'period_cycles.txt')


create_txt_page('karma.txt')

add_data("                 Karmic Lessons / Hidden Passions Chart\n\n", 'karma.txt')
add_data("""
          MIND PLANE    ->      3: %s   |   6: %s   |   9: %s      <-    CONSCIOUS SELF
                                                _________________

          SOUL PLANE    ->      2: %s   |   5: %s   |   8: %s      <-    HIGH SELF
                                                _________________

           BASIC SELF    ->       1: %s   |   4: %s   |   7: %s      <-    PHYSICAL PLANE
""" % (nct[3], nct[6], nct[9], nct[2], nct[5], nct[8], nct[1], nct[4], nct[7]), 'karma.txt')

add_data("\n##########################################\n\n", 'karma.txt')
add_data("                                      Karmic Lessons:\n", 'karma.txt')

index = 0
if report["detailed"] == True:
    for i in nct:
        if nct[i] == 0:
            add_data("\n                                                ===\n", 'karma.txt')
            add_data("                                                   %s\n" % i, 'karma.txt')
            add_data("                                                ===\n\n", 'karma.txt')
            add_data(nd.k_less["%s" % str(i)] + "\n", 'karma.txt')
            add_data("\n##########################################\n\n", 'karma.txt')
else:
    for i in hidden_passion_list:
        add_data("\n                                                ===\n", 'karma.txt')
        add_data("                                                   %s\n" % i, 'karma.txt')
        add_data("                                                ===\n\n", 'karma.txt')
    add_data("\n##########################################\n\n", 'karma.txt')

report["subcon_self"] = 9 - int(index)


add_data("                                      Hidden Passions:\n", 'karma.txt')


for i in hidden_passion_list:
    add_data("\n                                                ===\n", 'karma.txt')
    add_data("                                                   %s\n\n" % i, 'karma.txt')
    add_data("                                                ===\n\n", 'karma.txt')
#    hpl = str(hpl) + "%s  " % i
#    add_data("                     %s\n\n  " % str(i))
    if report['detailed'] == True:
        add_data(nd.h_pass["%s" % str(i)] + "\n", 'karma.txt')
    else:
        pass

add_data("\n##########################################\n\n", 'karma.txt')
add_data("\n - Subconscious Self:" + "  %s\n\n" % report["subcon_self"] + "\n", 'karma.txt')
if report["detailed"] == True:
    add_data(nd.sub_self["%s" % str(report["subcon_self"])] + "\n", 'karma.txt')
add_data("\n##########################################\n\n", 'karma.txt')

if report["detailed"] == True:
    if int(report["lp_k"]) > 0 or int(report["ex_k"]) > 0 or int(report["per_k"]) > 0 or int(report["hd_karma"]) > 0 or int(report["b_k"]) > 0:
        add_data("                                      Karmic Debt: \n", 'karma.txt')
        add_data("\n##########################################\n\n", 'karma.txt')
        if int(report["lp_k"]) > 0:
            add_data("\n###############\n", 'karma.txt')
            add_data("   - Life Path Karmic Debt:" + "  %s" % report["lp_k"] + "\n\n", 'karma.txt')
            add_data(nd.karm_dict["%s" % report["lp_k"]] + "\n", 'karma.txt')
        if int(report["ex_k"]) > 0:
            add_data("\n###############\n", 'karma.txt')
            add_data("   - Expression Karmic Debt:" + "  %s" % report["ex_k"] + "\n\n", 'karma.txt')
            add_data(nd.karm_dict["%s" % report["ex_k"]] + "\n", 'karma.txt')
        if int(report["per_k"]) > 0:
            add_data("\n###############\n", 'karma.txt')
            add_data("   - Personality Karmic Debt:" + "  %s" % report["per_k"] + "\n\n", 'karma.txt')
            add_data(nd.karm_dict["%s" % report["per_k"]] + "\n", 'karma.txt')
        if int(report["hd_karma"]) > 0:
            add_data("\n###############\n", 'karma.txt')
            add_data("   - Heart\'s Desire Karmic Debt:" + "  %s" % report["hd_karma"] + "\n\n", 'karma.txt')
            add_data(nd.karm_dict["%s" % report["hd_karma"]] + "\n", 'karma.txt')
        if int(report["b_k"]) > 0:
            add_data("\n###############\n", 'karma.txt')
            add_data("   - Birth-Day Karmic Debt:" + "  %s" % report["b_k"] + "\n", 'karma.txt')
            add_data(nd.karm_dict["%s" % report["b_k"]] + "\n", 'karma.txt')
        add_data("\n#############################################\n\n", 'karma.txt')

else:
    add_data("\n#############################################\n\n", 'karma.txt')


create_txt_page('corner.txt')

if report["detailed"] == True:
    add_data("\n - Balance: " + " %i" % int(report["balance"]) + "\n\n", 'corner.txt')
    add_data(nd.bal_dic["%i" % int(report["balance"])] + "\n", 'corner.txt')

else:
    add_data("\n - Balance:      " + "  %i" % int(report["balance"]) + "\n\n", 'corner.txt')


if report["detailed"] == True:
    add_data("\n#############################################\n\n", 'corner.txt')
    add_data("\n - Cornerstone: " + " %s : %i\n\n" % (str(cornerstone.upper()), int(corner_int)), 'corner.txt')
    add_data(nd.ccv["%s" % str(cornerstone.upper())] + "\n", 'corner.txt')
    add_data("\n#############################################\n\n", 'corner.txt')
    add_data("\n - Capstone   : " + " %s : %s\n\n" % (str(capstone.upper()), str(cap_int)), 'corner.txt')
    add_data(nd.cs_num["%s" % str(capstone.upper())] + "\n", 'corner.txt')
    add_data("\n#############################################\n\n", 'corner.txt')
    add_data("\n - First Vowel: " + " %s : %i\n\n" % (str(first_vowel.upper()), int(fv_int)), 'corner.txt')
    add_data(nd.vowel["%s" % str(first_vowel.upper())] + "\n", 'corner.txt')
    add_data("\n#############################################\n\n", 'corner.txt')
    add_data("\n - Key:         " + " %i\n\n" % (int(key_num)), 'corner.txt')
    add_data("\n#############################################\n\n", 'corner.txt')

else:
    add_data("\n#############################################\n\n", 'corner.txt')
    add_data("\n - Cornerstone:   " + " %s : %i\n\n" % (str(cornerstone.upper()), int(corner_int)), 'corner.txt')
    add_data("\n - Capstone:      " + " %s : %i\n\n" % (str(capstone.upper()), int(cap_int)), 'corner.txt')
    add_data("\n - First Vowel:   " + " %s : %i\n\n" % (str(first_vowel.upper()), int(fv_int)), 'corner.txt')
    add_data("\n - Key:           " + " %i\n\n" % (int(key_num)), 'corner.txt')
    add_data("\n#############################################\n\n", 'corner.txt')


create_txt_page('poe.txt')

if report["detailed"] == True:
    add_data("\n - Rational Thought:" + "  %s\n\n" % int(rtn), 'corner.txt')
    add_data(nd.rt_num["%s" % str(rtn)] + "\n", 'corner.txt')
    add_data("\n#############################################\n\n", 'corner.txt')
    add_data("\n - Alignment:" + "  %s" % report["alignment"] + "\n\n", 'corner.txt')
    add_data("\n#############################################\n\n", 'corner.txt')



    add_data("                                      Planes of Expression:\n", 'poe.txt')
    add_data("\n#############################################\n\n", 'poe.txt')
    if len(str(exp_kList[1])) > 1:
        add_data("       -  Physical:     " + "%s / %s\n\n"  % (expres['physical'], str(exp_kList[1])), 'poe.txt')
    else:
        add_data("       -  Physical:     " + "%s\n\n"  % expres['physical'] + "\n", 'poe.txt')
    try:
        add_data(nd.poe_phy["%s" % expres['physical'] ] + "\n", 'poe.txt')
    except KeyError:
        pass
    add_data("\n#############################################\n\n", 'poe.txt')
    if len(str(exp_kList[2])) > 1:
        add_data("       -  Mental:     " + "%s / %s\n\n"  % (expres['mental'], str(exp_kList[2])), 'poe.txt')
    else:
        add_data("       -  Mental:       " + "%s\n\n"  % expres['mental'] + "\n", 'poe.txt')
    try:
        add_data(nd.poe_ment["%s" % expres['mental'] ] + "\n", 'poe.txt')
    except KeyError:
        pass
    add_data("\n#############################################\n\n", 'poe.txt')
    if len(str(exp_kList[3])) > 1:
        add_data("       -  Emotional:     " + "%s / %s\n\n"  % (expres['emotional'], str(exp_kList[3])), 'poe.txt')
    else:
        add_data("       -  Emotional:    " + "%s\n\n"  % expres['emotional'] + "\n", 'poe.txt')
    try:
        add_data(nd.poe_emo["%s" % expres['emotional'] ] + "\n", 'poe.txt')
    except KeyError:
        pass
    add_data("\n#############################################\n\n", 'poe.txt')
    if len(str(exp_kList[4])) > 1:
        add_data("       -  Intuitive:     " + "%s / %s\n\n"  % (expres['intuitive'], str(exp_kList[4])), 'poe.txt')
    else:
        add_data("       -  Intuitive:    " + "%s\n\n"  % expres['intuitive'] + "\n", 'poe.txt')
    try:
        add_data(nd.poe_intu["%s" % expres['intuitive'] ] + "\n", 'poe.txt')
    except KeyError:
        pass
    add_data("\n#############################################\n\n", 'poe.txt')
    add_data("     -  Creative:     " + "%s\n\n"   % expres['creative'], 'poe.txt')
    add_data("     -  Vacillating:  " + "%s\n\n"  % expres['vacillating'], 'poe.txt')
    add_data("     -  Grounded:     " + "%s\n\n"  % expres['grounded'], 'poe.txt')
    add_data("\n#############################################\n\n", 'poe.txt')
else:
    add_data("\n - Rational Thought:" + "  %s\n\n" % int(rtn), 'poe.txt')
    add_data("\n#############################################\n\n", 'poe.txt')
    add_data("\n - Alignment:" + "  %s\n\n" % report["alignment"] + "\n", 'poe.txt')
    add_data("\n#############################################\n\n", 'poe.txt')
    add_data("                                      Planes of Expression:\n", 'poe.txt')
    add_data("\n#############################################\n\n", 'poe.txt')
    if len(str(exp_kList[1])) > 1:
        add_data("     -  Physical:     " + "%s / %s\n\n"  % (expres['physical'], str(exp_kList[1])), 'poe.txt')
    else:
        add_data("     -  Physical:     " + "%s\n\n"  % expres['physical'] + "\n", 'poe.txt')
    add_data("\n#############################################\n\n", 'poe.txt')
    if len(str(exp_kList[2])) > 1:
        add_data("     -  Mental:     " + "%s / %s\n\n"  % (expres['mental'], str(exp_kList[2])), 'poe.txt')
    else:
        add_data("     -  Mental:       " + "%s\n\n"  % expres['mental'] + "\n", 'poe.txt')
    add_data("\n#############################################\n\n", 'poe.txt')
    if len(str(exp_kList[3])) > 1:
        add_data("     -  Emotional:     " + "%s / %s\n\n"  % (expres['emotional'], str(exp_kList[3])), 'poe.txt')
    else:
        add_data("     -  Emotional:    " + "%s\n\n"  % expres['emotional'] + "\n", 'poe.txt')
    add_data("\n#############################################\n\n", 'poe.txt')
    if len(str(exp_kList[4])) > 1:
        add_data("     -  Intuitive:     " + "%s / %s\n\n"  % (expres['intuitive'], str(exp_kList[4])), 'poe.txt')
    else:
        add_data("     -  Intuitive:    " + "%s\n\n"  % expres['intuitive'] + "\n", 'poe.txt')
    add_data("\n#############################################\n\n", 'poe.txt')
    add_data("     -  Creative:     " + "%s\n\n"   % expres['creative'], 'poe.txt')
    add_data("     -  Vacillating:  " + "%s\n\n"  % expres['vacillating'], 'poe.txt')
    add_data("     -  Grounded:     " + "%s\n\n"  % expres['grounded'], 'poe.txt')
    add_data("\n#############################################\n\n", 'poe.txt')



create_txt_page('challenge.txt')

### Maturity

if int(mat2) > 0:
    ture = "%s / %s" % (report["maturity"], mat2)
else:
    ture = report["maturity"]

if report["detailed"] == True:
    add_data("\n - Maturity:" + "  %s\n\n" % ture, 'challenge.txt')
    add_data(nd.mat_num["%s" % report["maturity"]] + "\n", 'challenge.txt')
    add_data("\n#############################################\n\n", 'challenge.txt')
else:
    add_data("\n - Maturity:" + "  %s\n\n" % ture, 'challenge.txt')
    add_data("\n#############################################\n\n", 'challenge.txt')


if report["detailed"] == True:
    add_data("\n - Challenge 1:" + "  %s\n\n" % report["challenge_1"], 'challenge.txt')
    add_data(nd.cnum["%s" % str(report["challenge_1"])] + "\n", 'challenge.txt')
    add_data("\n#############################################\n\n", 'challenge.txt')
    add_data("\n - Challenge 2:" + "  %s\n\n" % report["challenge_2"], 'challenge.txt')
    add_data(nd.cnum["%s" % str(report["challenge_2"])] + "\n", 'challenge.txt')
    add_data("\n#############################################\n\n", 'challenge.txt')
    add_data("\n - Challenge 3:" + "  %s\n\n" % report["challenge_3"], 'challenge.txt')
    add_data(nd.cnum["%s" % str(report["challenge_3"])] + "\n", 'challenge.txt')
    add_data("\n#############################################\n\n", 'challenge.txt')
    add_data("\n - Challenge 4:" + "  %s\n\n" % report["challenge_4"], 'challenge.txt')
    add_data(nd.cnum["%s" % str(report["challenge_4"])] + "\n", 'challenge.txt')
    add_data("\n#############################################\n\n", 'challenge.txt')
else:
    add_data("\n - Challenge 1:" + "  %s\n\n" % report["challenge_1"], 'challenge.txt')
    add_data("\n - Challenge 2:" + "  %s\n\n" % report["challenge_2"], 'challenge.txt')
    add_data("\n - Challenge 3:" + "  %s\n\n" % report["challenge_3"], 'challenge.txt')
    add_data("\n - Challenge 4:" + "  %s\n\n" % report["challenge_4"], 'challenge.txt')
    add_data("\n#############################################\n\n", 'challenge.txt')


if report["detailed"] == True:
    add_data("\n - Life Path/Expression Bridge:" + "       %i\n\n" % report["le_bridge"], 'challenge.txt')
    add_data(nd.bridge["%s" % str(report["le_bridge"])] + "\n", 'challenge.txt')
    add_data("\n##########################################\n\n", 'challenge.txt')

    add_data("\n - Hearts Desire/Personality Bridge:" + "  %i\n\n" % report["hp_bridge"], 'challenge.txt')
    add_data(nd.bridge["%s" % str(report["hp_bridge"])] + "\n", 'challenge.txt')
    add_data("\n##########################################\n\n", 'challenge.txt')

    add_data("\n - Life Path/Birthday Bridge:" + "         %i\n\n" % report["lb_bridge"], 'challenge.txt')
    add_data(nd.bridge["%s" % str(report["lb_bridge"])]+ "\n", 'challenge.txt')
    add_data("\n##########################################\n\n", 'challenge.txt')

else:
    add_data("\n - Life Path/Expression Bridge:" + "       %i\n\n" % report["le_bridge"], 'challenge.txt')
    add_data("\n - Hearts Desire/Personality Bridge:" + "  %i\n\n" % report["hp_bridge"], 'challenge.txt')
    add_data("\n - Life Path/Birthday Bridge:" + "         %i\n\n" % report["lb_bridge"], 'challenge.txt')
    add_data("\n##########################################\n\n", 'challenge.txt')


create_txt_page('pinnacle.txt')
### Pinnacle Cycles


if report["detailed"] == True:
    add_data("                                      Pinnacle Cycles:\n", 'pinnacle.txt')
    add_data("\n##########################################\n\n", 'pinnacle.txt')
    add_data("First Cycle:     %s:  %s\n\n" % (report["first_cycle"], pin_cyc["paths"][report["life_path"]]["1st_cycle"]), 'pinnacle.txt')
    add_data(nd.pinnacle_cycle["%s" % str(report["first_cycle"])] + "\n", 'pinnacle.txt')
    add_data("\n##########################################\n\n", 'pinnacle.txt')
    add_data("Second Cycle:     %s:  %s\n\n" % (report["second_cycle"], pin_cyc["paths"][report["life_path"]]["2nd_cycle"]), 'pinnacle.txt')
    add_data(nd.pinnacle_cycle["%s" % str(report["second_cycle"])] + "\n", 'pinnacle.txt')
    add_data("\n##########################################\n\n", 'pinnacle.txt')
    add_data("Third Cycle:     %s:  %s\n\n" % (report["third_cycle"], pin_cyc["paths"][report["life_path"]]["3rd_cycle"]), 'pinnacle.txt')
    add_data(nd.pinnacle_cycle["%s" % str(report["third_cycle"])] + "\n", 'pinnacle.txt')
    add_data("\n##########################################\n\n", 'pinnacle.txt')
    add_data("Fourth Cycle:     %s:  %s\n\n" % (report["fourth_cycle"], pin_cyc["paths"][report["life_path"]]["4th_cycle"]), 'pinnacle.txt')
    add_data(nd.pinnacle_cycle["%s" % str(report["fourth_cycle"])] + "\n", 'pinnacle.txt')
else:
    add_data("\n - Pinnacle Cycles:\n", 'pinnacle.txt')
    add_data("\n##########################################\n\n", 'pinnacle.txt')
    add_data("First Cycle:     %s:  %s\n\n" % (report["first_cycle"], pin_cyc["paths"][report["life_path"]]["1st_cycle"]), 'pinnacle.txt')
    add_data("Second Cycle:     %s:  %s\n\n" % (report["second_cycle"], pin_cyc["paths"][report["life_path"]]["2nd_cycle"]), 'pinnacle.txt')
    add_data("Third Cycle:     %s:  %s\n\n" % (report["third_cycle"], pin_cyc["paths"][report["life_path"]]["3rd_cycle"]), 'pinnacle.txt')
    add_data("Fourth Cycle:     %s:  %s\n\n" % (report["fourth_cycle"], pin_cyc["paths"][report["life_path"]]["4th_cycle"]), 'pinnacle.txt')


create_txt_page('planets.txt')

if len(str(_btime)) > 0 and len(str(_tzone)) > 0 and len(str(coor_n)) > 0 and len(str(coor_w)) > 0:
    stars = chart.getFixedStars()
    star_list = {}
    for item in stars:
        s_list = str(item).replace('<', '').replace('>', '').split()
        star_list[s_list[0]] = str(s_list[1])
    add_data("\n\n", 'planets.txt')
    # add_data("Solar Return:")
    # add_data("             %s             %s\n\n             %s\n\n" % (asc[0], asc[1], asc[2]))
    add_data("\n##########################################\n\n", 'planets.txt')
    add_data("                                      Planets:\n", 'planets.txt')
    add_data("\n##########################################\n\n", 'planets.txt')
    add_data("     Sun:\n\n", 'planets.txt')
    add_data("             Sign: %s\n" % sun.sign, 'planets.txt')
    add_data("             Gender: %s\n" % sun.gender(), 'planets.txt')
    add_data("             Element: %s\n" % sun.element(), 'planets.txt')
    if report["detailed"] == True:
        add_data("\n\n", 'planets.txt')
        add_data(nd.sun_sign["%s" % str(sun.sign)] + "\n", 'planets.txt')
    add_data("\n##########################################\n\n", 'planets.txt')
    add_data("\n\n", 'planets.txt')
    add_data("     Moon:\n\n", 'planets.txt')
    add_data("             Phase: %s\n" % chart.getMoonPhase(), 'planets.txt')
    add_data("             Sign: %s\n" % moon.sign, 'planets.txt')
    add_data("             Gender: %s\n" % moon.gender(), 'planets.txt')
    add_data("             Element: %s\n" % moon.element(), 'planets.txt')
    if report["detailed"] == True:
        add_data("\n\n", 'planets.txt')
        add_data(nd.moon_sign["%s" % str(moon.sign)] + "\n", 'planets.txt')
    add_data("\n##########################################\n\n", 'planets.txt')
    add_data("\n\n", 'planets.txt')
    add_data("     Mercury:\n\n", 'planets.txt')
    add_data("             Sign: %s\n" % mercury.sign, 'planets.txt')
    add_data("             Gender: %s\n" % mercury.gender(), 'planets.txt')
    add_data("             Element: %s\n" % mercury.element(), 'planets.txt')
    if report["detailed"] == True:
        add_data("\n\n", 'planets.txt')
        add_data(nd.mercury_sign["%s" % str(mercury.sign)] + "\n", 'planets.txt')
    add_data("\n##########################################\n\n", 'planets.txt')
    add_data("\n\n", 'planets.txt')
    add_data("     Venus:\n\n", 'planets.txt')
    add_data("             Sign: %s\n" % venus.sign, 'planets.txt')
    add_data("             Gender: %s\n" % venus.gender(), 'planets.txt')
    add_data("             Element: %s\n" % venus.element(), 'planets.txt')
    if report["detailed"] == True:
        add_data("\n\n", 'planets.txt')
        add_data(nd.venus_sign["%s" % str(venus.sign)] + "\n", 'planets.txt')
    add_data("\n##########################################\n\n", 'planets.txt')
    add_data("\n\n", 'planets.txt')
    add_data("     Mars:\n\n", 'planets.txt')
    add_data("             Sign: %s\n" % mars.sign, 'planets.txt')
    add_data("             Gender: %s\n" % mars.gender(), 'planets.txt')
    add_data("             Element: %s\n" % mars.element(), 'planets.txt')
    if report["detailed"] == True:
        add_data("\n\n", 'planets.txt')
        add_data(nd.mars_sign["%s" % str(mars.sign)] + "\n", 'planets.txt')
    add_data("\n##########################################\n\n", 'planets.txt')
    add_data("\n\n", 'planets.txt')
    add_data("     Jupiter:\n\n", 'planets.txt')
    add_data("             Sign: %s\n" % jupiter.sign, 'planets.txt')
    add_data("             Gender: %s\n" % jupiter.gender(), 'planets.txt')
    add_data("             Element: %s\n" % jupiter.element(), 'planets.txt')
    if report["detailed"] == True:
        add_data("\n\n", 'planets.txt')
        add_data(nd.jupiter_sign["%s" % str(jupiter.sign)] + "\n", 'planets.txt')
    add_data("\n##########################################\n\n", 'planets.txt')
    add_data("\n\n", 'planets.txt')
    add_data("     Saturn:\n", 'planets.txt')
    add_data("             Sign: %s\n\n" % saturn.sign, 'planets.txt')
    add_data("             Gender: %s\n\n" % saturn.gender(), 'planets.txt')
    add_data("             Element: %s\n\n" % saturn.element(), 'planets.txt')
    if report["detailed"] == True:
        add_data("\n\n", 'planets.txt')
        add_data(nd.saturn_sign["%s" % str(saturn.sign)] + "\n", 'planets.txt')
    add_data("\n##########################################\n\n", 'planets.txt')
    add_data("                                      Houses:\n", 'planets.txt')
    add_data("\n##########################################\n\n", 'planets.txt')

    create_txt_page('houses.txt')

    add_data("\n\n", 'houses.txt')
    add_data("     House1: %s\n\n" % chart.get(const.HOUSE1).sign, 'houses.txt')
    add_data("         Condition: %s\n\n         Gender: %s\n\n" % (chart.get(const.HOUSE1).condition(), chart.get(const.HOUSE1).gender()), 'houses.txt')
    if report["detailed"] == True:
        add_data("\n\n", 'houses.txt')
        add_data(nd.house1["%s" % str(chart.get(const.HOUSE1).sign)] + "\n", 'houses.txt')
    add_data("\n##########################################\n\n", 'houses.txt')
    add_data("\n\n", 'houses.txt')
    add_data("     House2: %s\n\n" % chart.get(const.HOUSE2).sign, 'houses.txt')
    add_data("         Condition: %s\n\n         Gender: %s\n\n" % (chart.get(const.HOUSE2).condition(), chart.get(const.HOUSE2).gender()), 'houses.txt')
    if report["detailed"] == True:
        add_data("\n\n", 'houses.txt')
        add_data(nd.house2["%s" % str(chart.get(const.HOUSE2).sign)] + "\n", 'houses.txt')
    add_data("\n##########################################\n\n", 'houses.txt')
    add_data("\n\n", 'houses.txt')
    add_data("     House3: %s\n\n" % chart.get(const.HOUSE3).sign, 'houses.txt')
    add_data("         Condition: %s\n\n         Gender: %s\n\n" % (chart.get(const.HOUSE3).condition(), chart.get(const.HOUSE3).gender()), 'houses.txt')
    if report["detailed"] == True:
        add_data("\n\n", 'houses.txt')
        add_data(nd.house3["%s" % str(chart.get(const.HOUSE3).sign)] + "\n", 'houses.txt')
    add_data("\n##########################################\n\n", 'houses.txt')
    add_data("\n\n", 'houses.txt')
    add_data("     House4: %s\n\n" % chart.get(const.HOUSE4).sign, 'houses.txt')
    add_data("         Condition: %s\n\n         Gender: %s\n\n" % (chart.get(const.HOUSE4).condition(), chart.get(const.HOUSE4).gender()), 'houses.txt')
    if report["detailed"] == True:
        add_data("\n\n", 'houses.txt')
        add_data(nd.house4["%s" % str(chart.get(const.HOUSE4).sign)] + "\n", 'houses.txt')
    add_data("\n##########################################\n\n", 'houses.txt')
    add_data("\n\n", 'houses.txt')
    add_data("     House5: %s\n\n" % chart.get(const.HOUSE5).sign, 'houses.txt')
    add_data("         Condition: %s\n\n         Gender: %s\n\n" % (chart.get(const.HOUSE5).condition(), chart.get(const.HOUSE5).gender()), 'houses.txt')
    if report["detailed"] == True:
        add_data("\n\n", 'houses.txt')
        add_data(nd.house5["%s" % str(chart.get(const.HOUSE5).sign)] + "\n", 'houses.txt')
    add_data("\n##########################################\n\n", 'houses.txt')
    add_data("\n\n", 'houses.txt')
    add_data("     House6: %s\n\n" % chart.get(const.HOUSE6).sign, 'houses.txt')
    add_data("         Condition: %s\n\n         Gender: %s\n\n" % (chart.get(const.HOUSE6).condition(), chart.get(const.HOUSE6).gender()), 'houses.txt')
    if report["detailed"] == True:
        add_data("\n\n", 'houses.txt')
        add_data(nd.house6["%s" % str(chart.get(const.HOUSE6).sign)] + "\n", 'houses.txt')
    add_data("\n##########################################\n\n", 'houses.txt')
    add_data("\n\n", 'houses.txt')
    add_data("     House7: %s\n\n" % chart.get(const.HOUSE7).sign, 'houses.txt')
    add_data("         Condition: %s\n\n         Gender: %s\n\n" % (chart.get(const.HOUSE7).condition(), chart.get(const.HOUSE7).gender()), 'houses.txt')
    if report["detailed"] == True:
        add_data("\n\n", 'houses.txt')
        add_data(nd.house7["%s" % str(chart.get(const.HOUSE7).sign)] + "\n", 'houses.txt')
    add_data("\n##########################################\n\n", 'houses.txt')
    add_data("\n\n", 'houses.txt')
    add_data("     House8: %s\n\n" % chart.get(const.HOUSE8).sign, 'houses.txt')
    add_data("         Condition: %s\n\n         Gender: %s\n\n" % (chart.get(const.HOUSE8).condition(), chart.get(const.HOUSE8).gender()), 'houses.txt')
    if report["detailed"] == True:
        add_data("\n\n", 'houses.txt')
        add_data(nd.house8["%s" % str(chart.get(const.HOUSE8).sign)] + "\n", 'houses.txt')
    add_data("\n##########################################\n\n", 'houses.txt')
    add_data("\n\n", 'houses.txt')
    add_data("     House9: %s\n\n" % chart.get(const.HOUSE9).sign, 'houses.txt')
    #add_data("         Condition: %s         Gender: %s\n\n" % (chart.get(const.HOUSE9).condition(), chart.get(const.HOUSE9).gender()))
    add_data("         Condition: %s\n\n" % chart.get(const.HOUSE9).condition(), 'houses.txt')
    if report["detailed"] == True:
        add_data("\n\n", 'houses.txt')
        add_data(nd.house9["%s" % str(chart.get(const.HOUSE9).sign)] + "\n", 'houses.txt')
    add_data("\n##########################################\n\n", 'houses.txt')
    add_data("\n\n", 'houses.txt')
    add_data("     House10: %s\n\n" % chart.get(const.HOUSE10).sign, 'houses.txt')
    #add_data("         Condition: %s\n\n         Gender: %s\n\n" % (chart.get(const.HOUSE10).condition(), chart.get(const.HOUSE10).gender()))
    add_data("         Condition: %s\n\n" % chart.get(const.HOUSE10).condition(), 'houses.txt')
    if report["detailed"] == True:
        add_data("\n\n", 'houses.txt')
        add_data(nd.house10["%s" % str(chart.get(const.HOUSE10).sign)] + "\n", 'houses.txt')
    add_data("\n##########################################\n\n", 'houses.txt')
    add_data("\n\n", 'houses.txt')
    add_data("     House11: %s\n\n" % chart.get(const.HOUSE11).sign, 'houses.txt')
    #add_data("         Condition: %s\n\n         Gender: %s\n\n" % (chart.get(const.HOUSE11).condition(), chart.get(const.HOUSE11).gender()))
    add_data("         Condition: %s\n\n" % chart.get(const.HOUSE11).condition(), 'houses.txt')
    if report["detailed"] == True:
        add_data("\n\n", 'houses.txt')
        add_data(nd.house11["%s" % str(chart.get(const.HOUSE11).sign)] + "\n", 'houses.txt')
    add_data("\n##########################################\n\n", 'houses.txt')
    add_data("\n\n", 'houses.txt')
    add_data("     House12: %s\n\n" % chart.get(const.HOUSE12).sign, 'houses.txt')
    #add_data("         Condition: %s\n\n         Gender: %s\n\n" % (chart.get(const.HOUSE12).condition(), chart.get(const.HOUSE12).gender()))
    add_data("         Condition: %s\n\n" % chart.get(const.HOUSE12).condition(), 'houses.txt')

    if report["detailed"] == True:
        add_data("\n\n", 'houses.txt')
        add_data(nd.house12["%s" % str(chart.get(const.HOUSE12).sign)] + "\n", 'houses.txt')
    add_data("\n##########################################\n\n", 'houses.txt')
    add_data("\n\n", 'houses.txt')


    create_txt_page('stars.txt')
    add_data("Fixed Stars:\n", 'stars.txt')
    for item in star_list:
        add_data("     %s:     %s\n\n" % (item, star_list[item]), 'stars.txt')
    add_data("\n\n", 'stars.txt')
    add_data("\n##########################################\n\n", 'stars.txt')
    add_data("\n\n", 'stars.txt')
    factors = behavior.compute(chart)

    create_txt_page('facs.txt')

    add_data("Behavior:\n", 'facs.txt')
    try:
        for factor in factors:
            add_data("     %s:     %s\n\n" % (factor[0], factor[1][0]), 'facs.txt')
    except Exception as error:
        pass
    add_data("\n##########################################\n\n", 'facs.txt')
    add_data("\n\n", 'facs.txt')
    # Temperament
    temperament = Temperament(chart)

    # add_data temperament factors
    add_data("\n\n", 'facs.txt')
    factors = temperament.getFactors()
    for factor in factors:
        fac_list = []
        try:
            fac_list.append("%s:" % factor['factor'])
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
        if str(factor['factor']) == "Asc Sign":
            fac_list.append("%s" % nd.asc_sign[factor['objID']])
        fac_list.append("\n\n")
        for item in fac_list:
            add_data("%s\n\n" % item, 'facs.txt')
        add_data("\n##########################################\n\n", 'facs.txt')
        add_data("\n\n", 'facs.txt')

else:
    pass

# Check file sizes
try:
    house = os.path.getsize("/home/t3rm1n41/AstroNum/houses.txt")
    planet = os.path.getsize("/home/t3rm1n41/AstroNum/panets.txt")
    star = os.path.getsize("/home/t3rm1n41/AstroNum/stars.txt")
    fac = os.path.getsize("/home/t3rm1n41/AstroNum/facs.txt")
except Exception:
    pass
try:
    new_chap(1, "Core Numbers", "core.txt")
    new_chap(2, "Period Cycles", "period_cycles.txt")
    new_chap(3, "Karmic Lessons / Hidden Passion", "karma.txt")
    new_chap(4, "Cornerstone / Capstone / Rational Thought", "corner.txt")
    new_chap(5, "Planes of Expression", "poe.txt")
    new_chap(6, "Challenge / Bridge Numbers", "challenge.txt")
    new_chap(7, "Pinnacle Cycles", "pinnacle.txt")
    if len(house) >= 1:
        new_chap(8, 'Houses', 'houses.txt')
    if len(planet) >= 1:
        new_chap(9, "Planets", "planets.txt")
    if len(star) >= 1:
        new_chap(10, "Stars", "stars.txt")
    if len(facs) >= 1:
        new_chap(11, "Behavior / Factors", "facs.txt")
except Exception:
    pass
pdf.set_title(title)
pdf.set_author('7R3Y@9R0GR4M13')
pagecount = pdf.page_no()
pdf.output("%s.pdf" % str(filename))

filename = str(filename + ".pdf")

index = 1

bolden = True
darken = False
standard = False

colors = ["cyan", "blue", "magenta", "red", "yellow", "green"]
index = 1
ccount = 0
s = False


print("\n\n")

for item in logo:
    while ccount <= 5 and index <= 18:

        if bolden == True:
            print(colored(logo[str(index)], colors[ccount], attrs=['bold']))
            bolden = False
            standard = True
            index += 1

        elif standard == True:
            print(colored(logo[str(index)], colors[ccount]))

            if s == False:
                standard = False
                darken = True
                index += 1
                s = True

            else:
                bolden = True
                darken = False
                index += 1
                s = False
                ccount += 1


        elif darken == True:
            print(colored(logo[str(index)], colors[ccount], attrs=['dark']))
            darken = False
            standard = True
            index += 1

print("\nThe Oracle has generated a %s for %s %s.\nIt has been saved @ \'%s\'\n\n\n" % (colored(str(pagecount) + " page report", 'magenta', attrs=['bold', 'blink']), colored(report["first_name"], 'yellow', attrs=['bold']), colored(report["last_name"], 'yellow', attrs=['bold']), colored(filename, 'cyan', attrs=['bold'])))

del_tmp()

sys.exit(0)
