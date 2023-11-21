# from goto import with_goto
import spacy
import string
nlp = spacy.load("en_core_web_sm")
# doc = nlp("This is a sentence that a Taiwanese wrote in Taiwan. And so it goes.")
# print([(w.text, w.pos_, w.tag_) for w in doc])

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
   

with open("written.txt") as poem_file:
    lines = poem_file.readlines()
poem_code = open("poem_src.py", "w")
poem_code.write("from goto import with_goto")
poem_code.write("import random")

lastvar = "-1"
linecnt = -1
for line in lines:
    tmp_l = ''.join(filter(lambda x: x.isalpha() or x.isspace(), line))
    line_length = len(tmp_l.split())
    linecnt += 1

    if (line_length == 0):
        poem_code.write(f"label .line{linecnt}")
        if(line[-1] == "?"):
            if(lastvar != "-1"):
                poem_code.write(f"{lastvar} = random.randint(0, 1024)")
            else:
                poem_code.write(f"print(random.randint(0, 1024))")
        elif(line[-1] == '!'):
            poem_code.write("exit()")
    elif (line_length == 1):
        poem_code.write(f"var{linecnt} = {var_init(line)}")
        lastvar = f"var{linecnt}"
    elif (line_length == 2):
        poem_code.write(f"label .line{linecnt}")
        if(line.strip()[-1] == "?"):
            poem_code.write(f"{find_var_tag(line, linecnt)} = random.randint(0, 1024)")
            continue

        wd = (line.strip().split())
        if(wd[0].isupper()):
            poem_code.write(f"print(chr({find_var_tag(wd[1], linecnt)}))")
        else:
            poem_code.write(f"print(ord({find_var_tag(wd[1], linecnt)}))")
    else:
        #
