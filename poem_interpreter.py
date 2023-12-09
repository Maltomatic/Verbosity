import string, re
patterns_list = [r'\s',r'(n\'t)',r'\'m',r'(\'ll)',r'(\'ve)',r'(\'s)',r'(\'re)',r'(\'d)']
pattern=re.compile('|'.join(patterns_list))

import spacy
nlp = spacy.load("en_core_web_sm")

def summation(line):
    line = ''.join(filter(lambda x: x.isalpha() or x.isspace(), line.strip()))
    l = len(line.split())
    
    if(l > 1):
        line = line.split()
        return sum((ord(wd[0].lower()) - ord('a') + 1) for wd in line)
    else:
        return (sum(bytearray(line.lower(), encoding='utf-8')) - (ord('a')-1)*len(line))

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

def noun_parse_math(ending, cleaned, linecount):
    op = "*="
    if(ending in string.punctuation):
        if(ending == "."):
            op = "-="
        elif(ending == ","):
            op = "/="
        elif(ending == "!"):
            op = "*="
        elif(ending == "?"):
            op = "%="
        elif(ending == ";"):
            op = "//="
        else:
            op = "="
    else:
        op = "="
    op1 = None
    op2 = None
    ln_split = cleaned.split()
    len_op1 = len(ln_split)//2
    if(len(ln_split) % 2):
        # var op int
        op1 = find_var_tag(" ".join(ln_split[0:len_op1]), linecount)
        op2 = summation(" ".join(ln_split[len_op1:])) / len_op1
    else:
        # var op var
        op1 = find_var_tag(" ".join(ln_split[0:len_op1]), linecount)
        op2 = find_var_tag(" ".join(ln_split[len_op1:]), linecount)
    return (f"{op1} {op} {op2}")
        
def goto_catcher(line, cmd):
    return f"try:\n\t\texec({cmd})\n\texcept:\n\t\tprint('Bad jump at line:\\n\\t {line.strip()}\\nExiting program...')\n\t\texit()\n"

def add_tag(linecnt, in_else):
    poem_code.write(f"label .line{linecnt}\n\t")
    if(in_else):
        poem_code.write("\t")
        in_else = False

with open("written.txt") as poem_file:
    lines = poem_file.readlines()
total_ln = len(lines)
poem_code = open("poem_src.py", "w")
poem_code.write("from goto import with_goto\n")
poem_code.write("import random\n")

lastvar = "-1"
linecnt = -1
in_else = False
poem_code.write("@with_goto\ndef main():\n")
for line in lines:
    # print("parsing line " + line)
    poem_code.write(f"\t# source: {line}")
    if(line[-1] != "\n"):
        poem_code.write("\n")
    src_l = line
    line.strip()
    src_doc = nlp(line)
    poem_code.write("\t# initial POS: ")
    poem_code.write(f"{[(w.text, w.pos_, w.tag_) for w in src_doc]}")
    poem_code.write("\n")
    p_space = False
    p_lbr = False
    line = line.split()
    if(src_doc[-2].pos_ == "CCONJ" or src_doc[-2].pos_ == "SCONJ"):
            p_lbr = True
    if(src_doc[-1].pos_ == "CCONJ" or src_doc[-1].pos_ == "SCONJ"):
            p_space = True
    while(1):
        if not (len(line) > 1 and (src_doc[0].pos_ == "AUX" or src_doc[0].pos_ == "CCONJ" or src_doc[0].pos_ == "SCONJ" or src_doc[0].pos_ == "DET" or src_doc[0].pos_ == "ADP")):
            break
        src_doc = src_doc[1:]
        line = line[1:]
    line = " ".join(line)
    tmp_l = ''.join(filter(lambda x: x.isalpha() or x.isspace(), line)).strip()
    poem_code.write(f"\t# parsed: {tmp_l}\n")
    poem_code.write("\t# parsed POS: ")
    contractions = [i for i in pattern.split(line) if (i and "'" in i)]
    # print(contractions)
    doc = []
    for w in src_doc:
        if (w.pos_ != "NUM" and w.pos_ != "PUNCT" and w.pos_ != "SPACE" and w.pos_ != "SYM" and w.text not in contractions):
            doc.append(w)
    poem_code.write(f"{[(w.text, w.pos_, w.tag_) for w in doc]}")
    poem_code.write("\n\t")
    if(p_space):
        poem_code.write("print(' ', end = '')\n\t")
    line_length = len(tmp_l.split())
    linecnt += 1

    if (line_length == 0):
        add_tag(linecnt, in_else)
        if(src_l.strip()[-1] == "?"):
            if(lastvar != "-1"):
                poem_code.write(f"{lastvar} = random.randint(0, 1024)\n")
            else:
                poem_code.write(f"print(random.randint(0, 1024), end = '')\n")
        elif(src_l.strip()[-1] == '!'):
            poem_code.write("exit()\n")

    elif (line_length == 1):
        poem_code.write(f"var{linecnt} = {var_init(line)}\n")
        lastvar = f"var{linecnt}"

    elif (line_length == 2):
        add_tag(linecnt, in_else)
        if(line.strip()[-1] == "?"):
            poem_code.write(f"{find_var_tag(line, linecnt)} = random.randint(0, 1024)\n")
            continue

        wd = (line.strip().split())
        if(wd[0].isupper()):
            poem_code.write(f"print(chr(abs(int({find_var_tag(wd[1], linecnt)}//1))), end = '')\n")
        else:
            poem_code.write(f"print({find_var_tag(wd[1], linecnt)}, end = '')\n")
    else: # length >= 3
        if(doc[0].pos_ in ["NOUN", "PRON", "PROPN"]): # nouns for math
            add_tag(linecnt, in_else)
            cmd = noun_parse_math(line.strip()[-1], tmp_l, linecnt)
            poem_code.write(f"{cmd}\n")
        elif(doc[0].pos_ == "ADV" or ((doc[0].pos_ == "VERB" or doc[0].pos_ == "ADJ") and in_else == True)): #adverbs for goto
            add_tag(linecnt, in_else)
            cmd = f"goto .line{summation(line)%total_ln}"
            poem_code.write(goto_catcher(line, cmd))
        elif(doc[0].pos_ == "VERB" and in_else == False): # verbs for if/else
            add_tag(linecnt, in_else)
            ln = tmp_l.split()
            indicator = ' '.join(ln[0:2])
            rem = ' '.join(ln[2:])
            if(src_l[0:4] == "    " or src_l[0] == "\t"):
                if(doc[2].pos_ == "ADV"):
                    poem_code.write(f" if {find_var_tag(indicator, linecnt)} > 0:\n\t\tgoto .line{summation(rem)%total_ln}\n")
                else:
                    dest = find_var_tag(rem, linecnt)
                    poem_code.write(f" if {find_var_tag(indicator, linecnt)} > 0:\n\t\texec(f'goto .line\u007b{dest}\u007d')\n")
            else:
                if(doc[2].pos_ == "ADV"):
                    poem_code.write(f" if {find_var_tag(ln[0], linecnt)} > {find_var_tag(ln[1], linecnt)}:\n\t\tgoto .line{summation(rem)%total_ln}\n")
                else:
                    dest = find_var_tag(rem, linecnt)
                    poem_code.write(f" if {find_var_tag(ln[0], linecnt)} > {find_var_tag(ln[1], linecnt)}:\n\t\texec(f'goto .line\u007b{dest}\u007d')\n")
            if(line.strip()[-1] == "."):
                # write else clause
                in_else = True
                poem_code.write("else:\n\t")
        elif(doc[0].pos_ == "ADJ" and in_else == "False"):
            add_tag(linecnt, in_else)
            ln = tmp_l.split()
            indicator = ' '.join(ln[0:2])
            rem = ' '.join(ln[2:])
            if(src_l[0:4] == "    " or src_l[0] == "\t"):
                if(doc[2].pos_ == "VERB"):
                    poem_code.write(f" if {find_var_tag(indicator, linecnt)} <= 0:\n\t\tgoto .line{summation(rem)%total_ln}\n")
                else:
                    dest = find_var_tag(rem, linecnt)
                    poem_code.write(f" if {find_var_tag(indicator, linecnt)} <= 0:\n\t\texec(f'goto .line\u007b{dest}\u007d')\n")
            else:
                if(doc[2].pos_ == "VERB"):
                    poem_code.write(f" if {find_var_tag(ln[0], linecnt)} <= {find_var_tag(ln[1], linecnt)}:\n\t\tgoto .line{summation(rem)%total_ln}\n")
                else:
                    dest = find_var_tag(rem, linecnt)
                    poem_code.write(f" if {find_var_tag(ln[0], linecnt)} <= {find_var_tag(ln[1], linecnt)}:\n\t\texec(f'goto .line\u007b{dest}\u007d')\n")
            if(line.strip()[-1] == "."):
                # write else clause
                in_else = True
                poem_code.write("else:\n\t")
        else:
            add_tag(linecnt, in_else)
            poem_code.write("pass\n")
    
    if(p_lbr):
        poem_code.write("print('\n', end = '')\n\t")
    poem_code.write("\n")

poem_code.write("main()")