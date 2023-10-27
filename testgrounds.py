from goto import with_goto

@with_goto
def poem():
    print("Start here")
    rounds = 3
    label .repeat
    if(rounds < 0):
        label .negs
        print("So you can jump within an if statement")
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

# doc = nlp("And so it goes")
# print([(w.text, w.pos_, w.tag_) for w in doc])
