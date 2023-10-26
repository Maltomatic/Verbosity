from goto import with_goto

@with_goto
def poem():
    print("Start here")
    rounds = 3
    label .repeat
    print(rounds)
    rounds -= 1
    if(rounds):
        goto .repeat
    return

poem()
print("Ends here")

import spacy
nlp = spacy.load("en_core_web_sm")
doc = nlp("This is a sentence that a Taiwanese wrote in Taiwan.")
print([(w.text, w.pos_, w.tag_) for w in doc])

doc = nlp("And so it goes")
print([(w.text, w.pos_, w.tag_) for w in doc])
