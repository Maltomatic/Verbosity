
def summation(line):
    line = ''.join(filter(lambda x: x.isalpha() or x.isspace(), line.strip()))
    l = len(line.split())
    
    if(l > 1):
        line = line.split()
        val = sum((ord(wd[0].lower()) - ord('a') + 1) for wd in line)
        val *= l
        return val
    else:
        return (sum(bytearray(line.lower(), encoding='utf-8')) - (ord('a')-1)*len(line))

def find_var_tag(word, linecount):
    return f"var{summation(word)%linecount}"

def var_init(word):
    sign = True
    shift = False
    if(word[0].isupper()):
        sign = False
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

while(True):
    cmd = input("Sum, sum_int, var, or init: ")
    s = input("Enter string: ")
    if(cmd == "sum"):
        print(summation(s))
    elif(cmd == "sum_int"):
        s = ''.join(filter(lambda x: x.isalpha(), s.strip()))
        print(int(summation(s)/((int(input("line word length: "))//2)*2)))
    elif(cmd == "var"):
        ln = int(input("Enter line number to test: ").strip())
        print(find_var_tag(s, ln))
    elif(cmd == "init"):
        print(var_init(s))

# from goto import with_goto

# @with_goto
# def poem():
#     print("Start here")
#     rounds = 3
#     label .repeat
#     if(rounds < 0):
#         label .negs
#         print("So you can jump within an if statement")
#         try:
#             exec(goto .exciting)
#         except:
#             print("wrong label, exiting program")
#             goto .exiting
#     print(rounds)
#     rounds -= 1
#     if(rounds):
#         goto .repeat
#     else:
#         goto .negs
#         label . exiting
#         print("And in an else statement too")
#     print("This is the normal exit")
#     return

# poem()
# print("Ends here")

# import spacy
# nlp = spacy.load("en_core_web_sm")
# strn = "That which is unavoidable"
# doc = nlp(strn)
# print([(w.text, w.pos_, w.tag_) for w in doc])

# # doc = nlp("Has he done something which he has done?")
# # print([(w.text, w.pos_, w.tag_) for w in doc])

# # doc = nlp("And having a dream is now a crime. That which is punishable by eternal loss.")
# # print([(w.text, w.pos_, w.tag_) for w in doc])

# # doc = nlp("He has a dream. Which is true. And so it goes. That that is true.")
# # print([(w.text, w.pos_, w.tag_) for w in doc])

# # doc = nlp("Which which which which which...")
# # print([(w.text, w.pos_, w.tag_) for w in doc])

# # doc = nlp("What what what what what...")
# # print([(w.text, w.pos_, w.tag_) for w in doc])

# # doc = nlp("Where where where where where...")
# # print([(w.text, w.pos_, w.tag_) for w in doc])

# # doc = nlp("Who who who who who...")
# # print([(w.text, w.pos_, w.tag_) for w in doc])
