from goto import with_goto
import random
@with_goto
def main():
	# source: So,
	# initial POS: [('So', 'ADV', 'RB'), (',', 'PUNCT', ','), ('\n', 'SPACE', '_SP')]
	# parsed: So
	# parsed POS: [('So', 'ADV', 'RB')]
	var0 = -34

	# source: death and life. Different sides, one coin
	# initial POS: [('death', 'NOUN', 'NN'), ('and', 'CCONJ', 'CC'), ('life', 'NOUN', 'NN'), ('.', 'PUNCT', '.'), ('Different', 'ADJ', 'JJ'), ('sides', 'NOUN', 'NNS'), (',', 'PUNCT', ','), ('one', 'NUM', 'CD'), ('coin', 'NOUN', 'NN'), ('\n', 'SPACE', '_SP')]
	# parsed: death and life Different sides one coin
	# parsed POS: [('death', 'NOUN', 'NN'), ('and', 'CCONJ', 'CC'), ('life', 'NOUN', 'NN'), ('Different', 'ADJ', 'JJ'), ('sides', 'NOUN', 'NNS'), ('coin', 'NOUN', 'NN')]
	label .line1
	var0 += 36

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
		goto .line11
	except:
		print('Bad jump at line:\n\t Unrelentingly we trudge,\nExiting program...')
		exit()

	# source:     steps fall upon Earth, lightly
	# initial POS: [('    ', 'SPACE', '_SP'), ('steps', 'NOUN', 'NNS'), ('fall', 'VERB', 'VBP'), ('upon', 'SCONJ', 'IN'), ('Earth', 'PROPN', 'NNP'), (',', 'PUNCT', ','), ('lightly', 'ADV', 'RB'), ('\n', 'SPACE', '_SP')]
	# parsed: steps fall upon Earth lightly
	# parsed POS: [('steps', 'NOUN', 'NNS'), ('fall', 'VERB', 'VBP'), ('upon', 'SCONJ', 'IN'), ('Earth', 'PROPN', 'NNP'), ('lightly', 'ADV', 'RB')]
	label .line4
	var2 += 53

	# source:     unrelentingly, we trudge
	# initial POS: [('    ', 'SPACE', '_SP'), ('unrelentingly', 'ADV', 'RB'), (',', 'PUNCT', ','), ('we', 'PRON', 'PRP'), ('trudge', 'VERB', 'VBP'), ('\n', 'SPACE', '_SP')]
	# parsed: unrelentingly we trudge
	# parsed POS: [('unrelentingly', 'ADV', 'RB'), ('we', 'PRON', 'PRP'), ('trudge', 'VERB', 'VBP')]
	label .line5
	try:
		goto .line11
	except:
		print('Bad jump at line:\n\t unrelentingly, we trudge\nExiting program...')
		exit()

	# source:         Eternity. Eventually. Passing.
	# initial POS: [('        ', 'SPACE', '_SP'), ('Eternity', 'PROPN', 'NNP'), ('.', 'PUNCT', '.'), ('Eventually', 'ADV', 'RB'), ('.', 'PUNCT', '.'), ('Passing', 'VERB', 'VBG'), ('.', 'PUNCT', '.'), ('\n', 'SPACE', '_SP')]
	# parsed: Eternity Eventually Passing
	# parsed POS: [('Eternity', 'PROPN', 'NNP'), ('Eventually', 'ADV', 'RB'), ('Passing', 'VERB', 'VBG')]
	label .line6
	var2 = 108

	# source: Darkly, the skies rise
	# initial POS: [('Darkly', 'ADV', 'RB'), (',', 'PUNCT', ','), ('the', 'DET', 'DT'), ('skies', 'NOUN', 'NNS'), ('rise', 'VERB', 'VBP'), ('\n', 'SPACE', '_SP')]
	# parsed: Darkly the skies rise
	# parsed POS: [('Darkly', 'ADV', 'RB'), ('the', 'DET', 'DT'), ('skies', 'NOUN', 'NNS'), ('rise', 'VERB', 'VBP')]
	label .line7
	try:
		goto .line11
	except:
		print('Bad jump at line:\n\t Darkly, the skies rise\nExiting program...')
		exit()

	# source: Onwards!
	# initial POS: [('Onwards', 'ADV', 'RB'), ('!', 'PUNCT', '.'), ('\n', 'SPACE', '_SP')]
	# parsed: Onwards
	# parsed POS: [('Onwards', 'ADV', 'RB')]
	var8 = 94

	# source: Brightly, our hearts burn; a sun against the night
	# initial POS: [('Brightly', 'ADV', 'RB'), (',', 'PUNCT', ','), ('our', 'PRON', 'PRP$'), ('hearts', 'NOUN', 'NNS'), ('burn', 'VERB', 'VBP'), (';', 'PUNCT', ':'), ('a', 'DET', 'DT'), ('sun', 'NOUN', 'NN'), ('against', 'ADP', 'IN'), ('the', 'DET', 'DT'), ('night', 'NOUN', 'NN'), ('\n', 'SPACE', '_SP')]
	# parsed: Brightly our hearts burn a sun against the night
	# parsed POS: [('Brightly', 'ADV', 'RB'), ('our', 'PRON', 'PRP$'), ('hearts', 'NOUN', 'NNS'), ('burn', 'VERB', 'VBP'), ('a', 'DET', 'DT'), ('sun', 'NOUN', 'NN'), ('against', 'ADP', 'IN'), ('the', 'DET', 'DT'), ('night', 'NOUN', 'NN')]
	label .line9
	try:
		goto .line11
	except:
		print('Bad jump at line:\n\t Brightly, our hearts burn; a sun against the night\nExiting program...')
		exit()

	# source:     Earth, thusly quivering...
	# initial POS: [('    ', 'SPACE', '_SP'), ('Earth', 'PROPN', 'NNP'), (',', 'PUNCT', ','), ('thusly', 'ADV', 'RB'), ('quivering', 'VERB', 'VBG'), ('...', 'PUNCT', ':'), ('\n', 'SPACE', '_SP')]
	# parsed: Earth thusly quivering
	# parsed POS: [('Earth', 'PROPN', 'NNP'), ('thusly', 'ADV', 'RB'), ('quivering', 'VERB', 'VBG')]
	label .line10
	var2 = 111

	# source: It's though:
	# initial POS: [('It', 'PRON', 'PRP'), ("'s", 'AUX', 'VBZ'), ('though', 'ADV', 'RB'), (':', 'PUNCT', ':'), ('\n', 'SPACE', '_SP')]
	# parsed: Its though
	# parsed POS: [('It', 'PRON', 'PRP'), ('though', 'ADV', 'RB')]
	label .line11
	print(chr(abs(int(var2//1))), end = '')

	# source:     A--
	# initial POS: [('    ', 'SPACE', '_SP'), ('A--', 'NOUN', 'NN'), ('\n', 'SPACE', '_SP')]
	# parsed: A
	# parsed POS: [('A--', 'NOUN', 'NN')]
	var12 = 1

	# source:     Strength, it keeps ever growing, endlessly;
	# initial POS: [('    ', 'SPACE', '_SP'), ('Strength', 'PROPN', 'NNP'), (',', 'PUNCT', ','), ('it', 'PRON', 'PRP'), ('keeps', 'VERB', 'VBZ'), ('ever', 'ADV', 'RB'), ('growing', 'VERB', 'VBG'), (',', 'PUNCT', ','), ('endlessly', 'ADV', 'RB'), (';', 'PUNCT', ':'), ('\n', 'SPACE', '_SP')]
	# parsed: Strength it keeps ever growing endlessly
	# parsed POS: [('Strength', 'PROPN', 'NNP'), ('it', 'PRON', 'PRP'), ('keeps', 'VERB', 'VBZ'), ('ever', 'ADV', 'RB'), ('growing', 'VERB', 'VBG'), ('endlessly', 'ADV', 'RB')]
	label .line13
	var0 -= var12

	# source:         Rising, just like the Phoenix glides; and
	# initial POS: [('        ', 'SPACE', '_SP'), ('Rising', 'VERB', 'VBG'), (',', 'PUNCT', ','), ('just', 'ADV', 'RB'), ('like', 'ADP', 'IN'), ('the', 'DET', 'DT'), ('Phoenix', 'PROPN', 'NNP'), ('glides', 'NOUN', 'NNS'), (';', 'PUNCT', ':'), ('and', 'CCONJ', 'CC'), ('\n', 'SPACE', '_SP')]
	# parsed: Rising just like the Phoenix glides and
	# parsed POS: [('Rising', 'VERB', 'VBG'), ('just', 'ADV', 'RB'), ('like', 'ADP', 'IN'), ('the', 'DET', 'DT'), ('Phoenix', 'PROPN', 'NNP'), ('glides', 'NOUN', 'NNS'), ('and', 'CCONJ', 'CC')]
	label .line14
	if var0 > 0:
		exec(f"goto .line{var0}")
	print(' ', end = '')
	
	# source:         obstacles.
	# initial POS: [('        ', 'SPACE', '_SP'), ('obstacles', 'NOUN', 'NNS'), ('.', 'PUNCT', '.'), ('\n', 'SPACE', '_SP')]
	# parsed: obstacles
	# parsed POS: [('obstacles', 'NOUN', 'NNS')]
	var15 = 87

	# source:     Be-gone, then!
	# initial POS: [('    ', 'SPACE', '_SP'), ('Be', 'AUX', 'VB'), ('-', 'PUNCT', 'HYPH'), ('gone', 'VERB', 'VBN'), (',', 'PUNCT', ','), ('then', 'ADV', 'RB'), ('!', 'PUNCT', '.'), ('\n', 'SPACE', '_SP')]
	# parsed: Begone then
	# parsed POS: [('Be', 'AUX', 'VB'), ('gone', 'VERB', 'VBN'), ('then', 'ADV', 'RB')]
	label .line16
	print(chr(abs(int(var15//1))), end = '')

	# source: 
	pass
	# source: Accept this:
	# initial POS: [('Accept', 'VERB', 'VB'), ('this', 'PRON', 'DT'), (':', 'PUNCT', ':'), ('\n', 'SPACE', '_SP')]
	# parsed: Accept this
	# parsed POS: [('Accept', 'VERB', 'VB'), ('this', 'PRON', 'DT')]
	label .line18
	print(chr(abs(int(var2//1))), end = '')

	# source: time some day will waste all men of this here land
	# initial POS: [('time', 'NOUN', 'NN'), ('some', 'DET', 'DT'), ('day', 'NOUN', 'NN'), ('will', 'AUX', 'MD'), ('waste', 'VERB', 'VB'), ('all', 'DET', 'DT'), ('men', 'NOUN', 'NNS'), ('of', 'ADP', 'IN'), ('this', 'PRON', 'DT'), ('here', 'ADV', 'RB'), ('land', 'NOUN', 'NN'), ('\n', 'SPACE', '_SP')]
	# parsed: time some day will waste all men of this here land
	# parsed POS: [('time', 'NOUN', 'NN'), ('some', 'DET', 'DT'), ('day', 'NOUN', 'NN'), ('will', 'AUX', 'MD'), ('waste', 'VERB', 'VB'), ('all', 'DET', 'DT'), ('men', 'NOUN', 'NNS'), ('of', 'ADP', 'IN'), ('this', 'PRON', 'DT'), ('here', 'ADV', 'RB'), ('land', 'NOUN', 'NN')]
	label .line19
	var8 += 20

	# source: Fear none:
	# initial POS: [('Fear', 'VERB', 'VB'), ('none', 'NOUN', 'NN'), (':', 'PUNCT', ':'), ('\n', 'SPACE', '_SP')]
	# parsed: Fear none
	# parsed POS: [('Fear', 'VERB', 'VB'), ('none', 'NOUN', 'NN')]
	label .line20
	print(chr(abs(int(var8//1))), end = '')

	# source: Legacies persist eternally.
	# initial POS: [('Legacies', 'NOUN', 'NNS'), ('persist', 'VERB', 'VBP'), ('eternally', 'ADV', 'RB'), ('.', 'PUNCT', '.'), ('\n', 'SPACE', '_SP')]
	# parsed: Legacies persist eternally
	# parsed POS: [('Legacies', 'NOUN', 'NNS'), ('persist', 'VERB', 'VBP'), ('eternally', 'ADV', 'RB')]
	label .line21
	var19 = 108

	# source:     Forever existing
	# initial POS: [('    ', 'SPACE', '_SP'), ('Forever', 'ADV', 'RB'), ('existing', 'VERB', 'VBG'), ('\n', 'SPACE', '_SP')]
	# parsed: Forever existing
	# parsed POS: [('Forever', 'ADV', 'RB'), ('existing', 'VERB', 'VBG')]
	label .line22
	print(chr(abs(int(var19//1))), end = '')

	# source: Mankind may expire,
	# initial POS: [('Mankind', 'NOUN', 'NN'), ('may', 'AUX', 'MD'), ('expire', 'VERB', 'VB'), (',', 'PUNCT', ','), ('\n', 'SPACE', '_SP')]
	# parsed: Mankind may expire
	# parsed POS: [('Mankind', 'NOUN', 'NN'), ('may', 'AUX', 'MD'), ('expire', 'VERB', 'VB')]
	label .line23
	var20 = 59

	# source: --man inevitably long have expired
	# initial POS: [('man', 'NOUN', 'NN'), ('inevitably', 'ADV', 'RB'), ('long', 'ADV', 'RB'), ('have', 'AUX', 'VBP'), ('expired', 'VERB', 'VBN'), ('\n', 'SPACE', '_SP')]
	# parsed: man inevitably long have expired
	# parsed POS: [('man', 'NOUN', 'NN'), ('inevitably', 'ADV', 'RB'), ('long', 'ADV', 'RB'), ('have', 'AUX', 'VBP'), ('expired', 'VERB', 'VBN')]
	label .line24
	var20 += 41

	# source: Stories
	# initial POS: [('Stories', 'NOUN', 'NNS'), ('\n', 'SPACE', '_SP')]
	# parsed: Stories
	# parsed POS: [('Stories', 'NOUN', 'NNS')]
	var25 = 105

	# source:     Persist still
	# initial POS: [('    ', 'SPACE', '_SP'), ('Persist', 'PROPN', 'NNP'), ('still', 'ADV', 'RB')]
	# parsed: Persist still
	# parsed POS: [('Persist', 'PROPN', 'NNP'), ('still', 'ADV', 'RB')]
	label .line26
	print(chr(abs(int(var20//1))), end = '')

main()