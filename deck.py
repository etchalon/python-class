import random

SUITES = ('HEART', 'SPADE', 'CLUB', 'DIAMOND')
TYPES = (2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A')
ROYALS = ('J', 'Q', 'K')

class Card:
	
	card_type = 0
	suite = ''
	
	def value(self):
		if isinstance(self.card_type, int):
			return self.card_type
		elif self.card_type in ROYALS:
			return 10
		else:
			return 11

	def __str__(self):
		return '%s%s' % (self.card_type, self.suite[0])


class Deck:

	cards = []

	def __init__(self):
		for suite in SUITES:
			for card_type in TYPES:
				tmp_card = Card()
				tmp_card.suite = suite
				tmp_card.card_type = card_type
				self.cards.append(tmp_card)

	def __str__(self):
		tmp_string = ''
		for this_card in self.cards:
			tmp_string += '%s' % this_card
			tmp_string += ', '
		return tmp_string

	def shuffle(self):
		 random.shuffle(self.cards)

	def get_card(self):
		return self.cards.pop(0)






