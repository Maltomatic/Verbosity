
# def summation(word):
#     word = (''.join(filter(str.isalpha, word)))
#     return (sum(bytearray(word.lower(), encoding='utf-8')) - (ord('a')-1)*len(word))

# def find_var_tag(word, linecount):
#     return f"var{summation(word)%linecount}"

# def var_init(word):
#     sign = False
#     shift = False
#     if(word[0].isupper()):
#         sign = True
#     if(word[-1] == '.'):
#         shift = True
#     wd = (''.join(filter(str.isalpha, word)))
#     if(shift):
#         wd = sum(bytearray(wd.lower(), encoding='utf-8')) - (ord('a'))*len(wd)
#     else:
#         wd = sum(bytearray(wd.lower(), encoding='utf-8')) - (ord('a')-1)*len(wd)
#     if(sign):
#         return wd*-1
#     else:
#         return wd

# # test = "Aaaa, ay.   "
# # print(summation(test))
# # print(find_var_tag(test, 100))

# # import string
# # s = input()
# # closing = s[-1] if s[-1] in string.punctuation else None
# # s = (''.join(filter(lambda x: x.isalpha() or x.isspace(), s)))
# # print(s)
# # print(len(s.split()))

from goto import with_goto

@with_goto
def poem():
    print("Start here")
    rounds = 3
    label .repeat
    if(rounds < 0):
        label .negs
        print("So you can jump within an if statement")
        try:
            exec(goto .exciting)
        except:
            print("wrong label, exiting program")
            goto .exiting
    print(rounds)
    rounds -= 1
    if(rounds):
        goto .repeat
    else:
        goto .negs
        label . exiting
        print("And in an else statement too")
    return

poem()
print("Ends here")

# import spacy
# nlp = spacy.load("en_core_web_sm")
# doc = nlp("This is a sentence that a Taiwanese wrote in Taiwan.")
# print([(w.text, w.pos_, w.tag_) for w in doc])

# doc = nlp("Has he done something which he has done?")
# print([(w.text, w.pos_, w.tag_) for w in doc])

# doc = nlp("And having a dream is now a crime. That which is punishable by eternal loss.")
# print([(w.text, w.pos_, w.tag_) for w in doc])

# doc = nlp("He has a dream. Which is true. And so it goes. That that is true.")
# print([(w.text, w.pos_, w.tag_) for w in doc])

# doc = nlp("Which which which which which...")
# print([(w.text, w.pos_, w.tag_) for w in doc])

# doc = nlp("What what what what what...")
# print([(w.text, w.pos_, w.tag_) for w in doc])

# doc = nlp("Where where where where where...")
# print([(w.text, w.pos_, w.tag_) for w in doc])

# doc = nlp("Who who who who who...")
# print([(w.text, w.pos_, w.tag_) for w in doc])
