from goto import with_goto
import random
@with_goto
def main():
	# source: so.
	# initial POS: [('so', 'ADV', 'RB'), ('.', 'PUNCT', '.'), ('\n', 'SPACE', '_SP')]
	# parsed: so
	# parsed POS: [('so', 'ADV', 'RB')]
	var0 = -32

	# source: Death and life. Different sides, one coin.
	# initial POS: [('Death', 'NOUN', 'NN'), ('and', 'CCONJ', 'CC'), ('life', 'NOUN', 'NN'), ('.', 'PUNCT', '.'), ('Different', 'ADJ', 'JJ'), ('sides', 'NOUN', 'NNS'), (',', 'PUNCT', ','), ('one', 'NUM', 'CD'), ('coin', 'NOUN', 'NN'), ('.', 'PUNCT', '.'), ('\n', 'SPACE', '_SP')]
	# parsed: Death and life Different sides one coin
	# parsed POS: [('Death', 'NOUN', 'NN'), ('and', 'CCONJ', 'CC'), ('life', 'NOUN', 'NN'), ('Different', 'ADJ', 'JJ'), ('sides', 'NOUN', 'NNS'), ('coin', 'NOUN', 'NN')]
	label .line1
	var0 = 35

	# source: Well.
	# initial POS: [('Well', 'INTJ', 'UH'), ('.', 'PUNCT', '.'), ('\n', 'SPACE', '_SP')]
	# parsed: Well
	# parsed POS: [('Well', 'INTJ', 'UH')]
	var2 = 48

	# source: Unrelentingly we trudge,
	# initial POS: [('Unrelentingly', 'ADV', 'RB'), ('we', 'PRON', 'PRP'), ('trudge', 'VERB', 'VBP'), (',', 'PUNCT', ','), ('\n', 'SPACE', '_SP')]
	# parsed: Unrelentingly we trudge
	# parsed POS: [('Unrelentingly', 'ADV', 'RB'), ('we', 'PRON', 'PRP'), ('trudge', 'VERB', 'VBP')]
	label .line3
	try:
		exec(goto .line6)
	except:
		print('Bad jump at line:\n\t Unrelentingly we trudge,\nExiting program...')
		exit()

	# source:     steps fall, lightly upon Earth
	# initial POS: [('    ', 'SPACE', '_SP'), ('steps', 'NOUN', 'NNS'), ('fall', 'VERB', 'VBP'), (',', 'PUNCT', ','), ('lightly', 'ADV', 'RB'), ('upon', 'SCONJ', 'IN'), ('Earth', 'NOUN', 'NN'), ('\n', 'SPACE', '_SP')]
	# parsed: steps fall lightly upon Earth
	# parsed POS: [('steps', 'NOUN', 'NNS'), ('fall', 'VERB', 'VBP'), ('lightly', 'ADV', 'RB'), ('upon', 'SCONJ', 'IN'), ('Earth', 'NOUN', 'NN')]
	label .line4
	var2 += 53

	# source:     unrelentingly, we trudge
	# initial POS: [('    ', 'SPACE', '_SP'), ('unrelentingly', 'ADV', 'RB'), (',', 'PUNCT', ','), ('we', 'PRON', 'PRP'), ('trudge', 'VERB', 'VBP'), ('\n', 'SPACE', '_SP')]
	# parsed: unrelentingly we trudge
	# parsed POS: [('unrelentingly', 'ADV', 'RB'), ('we', 'PRON', 'PRP'), ('trudge', 'VERB', 'VBP')]
	label .line5
	try:
		exec(goto .line6)
	except:
		print('Bad jump at line:\n\t unrelentingly, we trudge\nExiting program...')
		exit()

	# source:         eternity eventually passing...
	# initial POS: [('        ', 'SPACE', '_SP'), ('eternity', 'NOUN', 'NN'), ('eventually', 'ADV', 'RB'), ('passing', 'VERB', 'VBG'), ('...', 'PUNCT', ':'), ('\n', 'SPACE', '_SP')]
	# parsed: eternity eventually passing
	# parsed POS: [('eternity', 'NOUN', 'NN'), ('eventually', 'ADV', 'RB'), ('passing', 'VERB', 'VBG')]
	label .line6
	var2 = 108

	# source: Darkly, the skies rise
	# initial POS: [('Darkly', 'ADV', 'RB'), (',', 'PUNCT', ','), ('the', 'DET', 'DT'), ('skies', 'NOUN', 'NNS'), ('rise', 'VERB', 'VBP'), ('\n', 'SPACE', '_SP')]
	# parsed: Darkly the skies rise
	# parsed POS: [('Darkly', 'ADV', 'RB'), ('the', 'DET', 'DT'), ('skies', 'NOUN', 'NNS'), ('rise', 'VERB', 'VBP')]
	label .line7
	try:
		exec(goto .line3)
	except:
		print('Bad jump at line:\n\t Darkly, the skies rise\nExiting program...')
		exit()

	# source: Persevere!
	# initial POS: [('Persevere', 'ADV', 'RB'), ('!', 'PUNCT', '.'), ('\n', 'SPACE', '_SP')]
	# parsed: Persevere
	# parsed POS: [('Persevere', 'ADV', 'RB')]
	var8 = 113

	# source: Brightly, our hearts burn; a sun against the night
	# initial POS: [('Brightly', 'ADV', 'RB'), (',', 'PUNCT', ','), ('our', 'PRON', 'PRP$'), ('hearts', 'NOUN', 'NNS'), ('burn', 'VERB', 'VBP'), (';', 'PUNCT', ':'), ('a', 'DET', 'DT'), ('sun', 'NOUN', 'NN'), ('against', 'ADP', 'IN'), ('the', 'DET', 'DT'), ('night', 'NOUN', 'NN'), ('\n', 'SPACE', '_SP')]
	# parsed: Brightly our hearts burn a sun against the night
	# parsed POS: [('Brightly', 'ADV', 'RB'), ('our', 'PRON', 'PRP$'), ('hearts', 'NOUN', 'NNS'), ('burn', 'VERB', 'VBP'), ('a', 'DET', 'DT'), ('sun', 'NOUN', 'NN'), ('against', 'ADP', 'IN'), ('the', 'DET', 'DT'), ('night', 'NOUN', 'NN')]
	label .line9
	try:
		exec(goto .line2)
	except:
		print('Bad jump at line:\n\t Brightly, our hearts burn; a sun against the night\nExiting program...')
		exit()

	# source: We remain 
	# initial POS: [('We', 'PRON', 'PRP'), ('remain', 'VERB', 'VBP')]
	# parsed: We remain
	# parsed POS: [('We', 'PRON', 'PRP'), ('remain', 'VERB', 'VBP')]
	label .line10
	print(var0, end = '')

main()