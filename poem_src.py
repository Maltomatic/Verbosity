from goto import with_goto
import random
@with_goto
def main():
		# source: Death.
		#[('Death', 'NOUN', 'NN'), ('.', 'PUNCT', '.'), ('\n', 'SPACE', '_SP')]
	var0 = -38
		# source: That unavoidable monstrosity.
		#[('That', 'DET', 'DT'), ('unavoidable', 'ADJ', 'JJ'), ('monstrosity', 'NOUN', 'NN'), ('.', 'PUNCT', '.'), ('\n', 'SPACE', '_SP')]
	label .line1
	pass
		# source: Life.
		#[('Life', 'NOUN', 'NN'), ('.', 'PUNCT', '.'), ('\n', 'SPACE', '_SP')]
	var2 = -32
		# source: That which lends a rope into the bottomless abyss.
		#[('That', 'PRON', 'DT'), ('which', 'PRON', 'WDT'), ('lends', 'VERB', 'VBZ'), ('a', 'DET', 'DT'), ('rope', 'NOUN', 'NN'), ('into', 'ADP', 'IN'), ('the', 'DET', 'DT'), ('bottomless', 'ADJ', 'JJ'), ('abyss', 'PROPN', 'NNP'), ('.', 'PUNCT', '.'), ('\n', 'SPACE', '_SP')]
	label .line3
	var2 -= 297
		# source: 1, 2, 3?
		#[('1', 'NUM', 'CD'), (',', 'PUNCT', ','), ('2', 'NUM', 'CD'), (',', 'PUNCT', ','), ('3', 'NUM', 'CD'), ('?', 'NOUN', 'NN'), ('\n', 'SPACE', '_SP')]
	label .line4
			# source: Quickly, run.
		#[('Quickly', 'ADV', 'RB'), (',', 'PUNCT', ','), ('run', 'VERB', 'VBN'), ('.', 'PUNCT', '.'), ('\n', 'SPACE', '_SP')]
	label .line5
	print(ord(var3), end = '')
		# source:     One flees as time flows unendingly
		#[('    ', 'SPACE', '_SP'), ('One', 'NUM', 'CD'), ('flees', 'NOUN', 'NNS'), ('as', 'SCONJ', 'IN'), ('time', 'NOUN', 'NN'), ('flows', 'VERB', 'VBZ'), ('unendingly', 'ADV', 'RB'), ('\n', 'SPACE', '_SP')]
	label .line6
	pass
		# source: Flee, flee
		#[('Flee', 'PROPN', 'NNP'), (',', 'PUNCT', ','), ('flee', 'PROPN', 'NNP'), ('\n', 'SPACE', '_SP')]
	label .line7
	print(ord(var0), end = '')
		# source: Merrily we run as we do.
		#[('Merrily', 'ADV', 'RB'), ('we', 'PRON', 'PRP'), ('run', 'VERB', 'VBP'), ('as', 'SCONJ', 'IN'), ('we', 'PRON', 'PRP'), ('do', 'VERB', 'VBP'), ('.', 'PUNCT', '.')]
	label .line8
	try:
		exec(goto .line5)
	except:
		print('Bad jump at line:\n\t Merrily we run as we do.\nExiting program...')
		exit()
main()