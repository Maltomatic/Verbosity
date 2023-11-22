import string

import spacy
nlp = spacy.load("en_core_web_sm")

def summation(word):
    word = (''.join(filter(str.isalpha, word)))
    return (sum(bytearray(word.lower(), encoding='utf-8')) - (ord('a')-1)*len(word))

def find_var_tag(word, linecount):
    return f"var{summation(word)%linecount}"

def var_init(word):
    sign = False
    shift = False
    if(word[0].isupper()):
        sign = True
    if(word[-1] == '.'):
        shift = True
    wd = (''.join(filter(str.isalpha, word)))
    if(shift):
        wd = sum(bytearray(wd.lower(), encoding='utf-8')) - (ord('a'))*len(wd)
    else:
        wd = sum(bytearray(wd.lower(), encoding='utf-8')) - (ord('a')-1)*len(wd)
    if(sign):
        return wd*-1
    else:
        return wd

def parse_math(ending, cleaned, linecount):
    op = "="
    if(ending in string.punctuation):
        if(ending == "."):
            op = "-="
        elif(ending == ","):
            op = "+="
        elif(ending == "!"):
            op = "*="
        elif(ending == "?"):
            op = "/="
        elif(ending == ";"):
            op = "%="
    len_op1 = 0
    op1 = None
    op2 = None
    if(len(cleaned) % 2):
        # var op int
        len_op1 = len(cleaned)//2 + 1
        op1 = find_var_tag(" ".join(cleaned.split()[0:len_op1]), linecount)
        op2 = summation(" ".join(cleaned.split()[len_op1:]))
    else:
        # var op var
        len_op1 = len(cleaned)/2
        op1 = find_var_tag(" ".join(cleaned.split()[0:len_op1]), linecount)
        op2 = find_var_tag(" ".join(cleaned.split()[len_op1:]), linecount)
    return (f"{op1} {op} {op2}")
        
def goto_catcher(line, cmd):
    return f"try:\n\texec({cmd})\nexcept:\n\tprint('Bad jump at line:\n\t {line}\nExiting program...')\n\texit()"

with open("written.txt") as poem_file:
    lines = poem_file.readlines()
poem_code = open("poem_src.py", "w")
poem_code.write("from goto import with_goto\n")
poem_code.write("import random\n")

lastvar = "-1"
linecnt = -1
for line in lines:
    doc = nlp(line)
    p_space = False
    p_lbr = False
    for w in doc:
        if(w.pos_ == "AUX"):
            p_space = True
    if(doc[-1].pos_ == "CCONJ" or doc[-1].pos_ == "SCONJ"):
            p_lbr = True
    while(1):
        if(doc[0].pos_ == "AUX" or doc[0].pos_ == "CCONJ" or doc[0].pos_ == "SCONJ" or doc[0].pos_ == "DET" or doc[0].pos_ == "ADP" or (doc[0].tag_ == "WDT" and (len(doc) == 1 or (doc[1].text.lower() == doc[0].text.lower())))):
            pass
        else:
            break
        doc = doc[1:]
        line = line[1:]
    if(p_space):
        poem_code.write("print(' ', end = '')")
    tmp_l = ''.join(filter(lambda x: x.isalpha() or x.isspace(), line))
    line_length = len(tmp_l.split())
    linecnt += 1

    if (line_length == 0):
        poem_code.write(f"label .line{linecnt}\n")
        if(line[-1] == "?"):
            if(lastvar != "-1"):
                poem_code.write(f"{lastvar} = random.randint(0, 1024)\n")
            else:
                poem_code.write(f"print(random.randint(0, 1024), end = '')\n")
        elif(line[-1] == '!'):
            poem_code.write("exit()\n")

    elif (line_length == 1):
        poem_code.write(f"var{linecnt} = {var_init(line)}\n")
        lastvar = f"var{linecnt}"

    elif (line_length == 2):
        poem_code.write(f"label .line{linecnt}\n")
        if(line.strip()[-1] == "?"):
            poem_code.write(f"{find_var_tag(line, linecnt)} = random.randint(0, 1024)\n")
            continue

        wd = (line.strip().split())
        if(wd[0].isupper()):
            poem_code.write(f"print(chr({find_var_tag(wd[1], linecnt)}), end = '')\n")
        else:
            poem_code.write(f"print(ord({find_var_tag(wd[1], linecnt)}), end = '')\n")
    else: # length >= 3
        if(doc[0].pos_ in ["NOUN", "PRON", "PROPN"]): # nouns for math
            poem_code.write(f"label .line{linecnt}\n")
            line = parse_math(line[-1], tmp_l, linecnt)
            poem_code.write(f"{line}\n")
        elif(doc[0].pos_ == "ADV"): #adverbs for goto
            poem_code.write(f"label .line{linecnt}\n")
            cmd = f"goto .line{summation(line)%linecnt}\n"
            poem_code.write(goto_catcher(line, cmd))
        elif(doc[0].pos_ == "VERB"): # verbs for if/else
            poem_code.write(f"label .line{linecnt}\n")
            ###

    
    if(p_lbr):
        poem_code.write("print('\n', end = '')")