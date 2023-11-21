# from goto import with_goto
import spacy
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
linecnt = 0
for line in lines:
    line_length = len(line)
    if (line_length == 1):
        poem_code.write(f"var{linecnt} = {var_init(line)}")
    elif (line_length == 2):
        poem_code.write(f"label .line{linecnt}")
        wd = (line.strip().split())
        if(wd[0].isupper()):
            poem_code.write(f"print(chr({find_var_tag(wd[1], linecnt)}))")
        else:
            poem_code.write(f"print(ord({find_var_tag(wd[1], linecnt)}))")
    else:
        #
