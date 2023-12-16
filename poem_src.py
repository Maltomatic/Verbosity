from goto import with_goto
import random
@with_goto
def main():
	# source: Hmm?
	# initial POS: [('Hmm', 'ADJ', 'JJ'), ('?', 'PUNCT', '.'), ('\n', 'SPACE', '_SP')]
	# parsed: Hmm
	# parsed POS: [('Hmm', 'ADJ', 'JJ')]
	var0 = 34

	# source: What's this?
	# initial POS: [('What', 'PRON', 'WP'), ("'s", 'AUX', 'VBZ'), ('this', 'PRON', 'DT'), ('?', 'PUNCT', '.'), ('\n', 'SPACE', '_SP')]
	# parsed: Whats this
	# parsed POS: [('What', 'PRON', 'WP'), ('this', 'PRON', 'DT')]
	label .line1
	var0 = random.randint(0, 1024)
	# source: show us :)
	# initial POS: [('show', 'VERB', 'VB'), ('us', 'PRON', 'PRP')]
	# parsed: show us
	# parsed POS: [('show', 'VERB', 'VB'), ('us', 'PRON', 'PRP')]
	label .line2
	print(var0, end = '')

main()