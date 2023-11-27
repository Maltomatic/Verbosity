from goto import with_goto
import random
@with_goto
def main():
	# source: Stay!
	# initial POS: [('Stay', 'VERB', 'VB'), ('!', 'PUNCT', '.'), ('\n', 'SPACE', '_SP')]
	# parsed: Stay
	# parsed POS: [('Stay', 'VERB', 'VB')]
	var0 = -65

	# source: My dear, please, please
	# initial POS: [('My', 'PRON', 'PRP$'), ('dear', 'ADJ', 'JJ'), (',', 'PUNCT', ','), ('please', 'INTJ', 'UH'), (',', 'PUNCT', ','), ('please', 'INTJ', 'UH'), ('\n', 'SPACE', '_SP')]
	# parsed: My dear please please
	# parsed POS: [('My', 'PRON', 'PRP$'), ('dear', 'ADJ', 'JJ'), ('please', 'INTJ', 'UH'), ('please', 'INTJ', 'UH')]
	label .line1
	var0 = var0

	# source: Please.
	# initial POS: [('Please', 'INTJ', 'UH'), ('.', 'PUNCT', '.'), ('\n', 'SPACE', '_SP')]
	# parsed: Please
	# parsed POS: [('Please', 'INTJ', 'UH')]
	var2 = -52

	# source:     Mercy on my soul, I plead
	# initial POS: [('    ', 'SPACE', '_SP'), ('Mercy', 'PROPN', 'NNP'), ('on', 'ADP', 'IN'), ('my', 'PRON', 'PRP$'), ('soul', 'NOUN', 'NN'), (',', 'PUNCT', ','), ('I', 'PRON', 'PRP'), ('plead', 'VERB', 'VBP'), ('\n', 'SPACE', '_SP')]
	# parsed: Mercy on my soul I plead
	# parsed POS: [('Mercy', 'PROPN', 'NNP'), ('on', 'ADP', 'IN'), ('my', 'PRON', 'PRP$'), ('soul', 'NOUN', 'NN'), ('I', 'PRON', 'PRP'), ('plead', 'VERB', 'VBP')]
	label .line3
	var2 = var2

	# source: I would've gone to do -- anything!
	# initial POS: [('I', 'PRON', 'PRP'), ('would', 'AUX', 'MD'), ("'ve", 'AUX', 'VB'), ('gone', 'VERB', 'VBN'), ('to', 'PART', 'TO'), ('do', 'VERB', 'VB'), ('--', 'PUNCT', ':'), ('anything', 'PRON', 'NN'), ('!', 'PUNCT', '.'), ('\n', 'SPACE', '_SP')]
	# parsed: I wouldve gone to do  anything
	# parsed POS: [('I', 'PRON', 'PRP'), ('would', 'AUX', 'MD'), ('gone', 'VERB', 'VBN'), ('to', 'PART', 'TO'), ('do', 'VERB', 'VB'), ('anything', 'PRON', 'NN')]
	print(' ', end = '')
	label .line4
	var3 *= var1

	# source: Anything you'd've said
	# initial POS: [('Anything', 'PRON', 'NN'), ('you', 'PRON', 'PRP'), ("'d", 'AUX', 'MD'), ("'ve", 'AUX', 'VB'), ('said', 'VERB', 'VBN'), ('\n', 'SPACE', '_SP')]
	# parsed: Anything youdve said
	# parsed POS: [('Anything', 'PRON', 'NN'), ('you', 'PRON', 'PRP'), ('said', 'VERB', 'VBN')]
	print(' ', end = '')
	label .line5
	var3 = 44.0

	# source: Should you have told me
	# initial POS: [('Should', 'AUX', 'MD'), ('you', 'PRON', 'PRP'), ('have', 'AUX', 'VB'), ('told', 'VERB', 'VBN'), ('me', 'PRON', 'PRP'), ('\n', 'SPACE', '_SP')]
	# parsed: you have told me
	# parsed POS: [('you', 'PRON', 'PRP'), ('have', 'AUX', 'VB'), ('told', 'VERB', 'VBN'), ('me', 'PRON', 'PRP')]
	print(' ', end = '')
	label .line6
	var3 = var3

	# source: And said
	# initial POS: [('And', 'CCONJ', 'CC'), ('said', 'VERB', 'VBD'), ('\n', 'SPACE', '_SP')]
	# parsed: said
	# parsed POS: [('said', 'VERB', 'VBD')]
	var7 = 33

	# source: You'd stay
	# initial POS: [('You', 'PRON', 'PRP'), ("'d", 'AUX', 'MD'), ('stay', 'VERB', 'VB'), ('\n', 'SPACE', '_SP')]
	# parsed: Youd stay
	# parsed POS: [('You', 'PRON', 'PRP'), ('stay', 'VERB', 'VB')]
	print(' ', end = '')
	label .line8
	print(var1, end = '')

main()