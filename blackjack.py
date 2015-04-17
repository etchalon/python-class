from deck import Deck

class BlackjackHand:

	cards = []

	def __init__(self, deck):
		self.cards = [deck.get_card(), deck.get_card()]

	def __str__(self):
		tmp_string = ''
		for this_card in self.cards:
			tmp_string += '%s' % this_card
			tmp_string += ', '
		return tmp_string

	def is_blackjack(self):
		if self.value() == 21:
			return True

	def absolute_value(self):
		my_value = 0
		for card in self.cards:
			my_value += card.value()
		return my_value

	def value(self):
		while self.absolute_value() > 21:
			found_ace = self.reduce_aces()
			if not found_ace:
				return self.absolute_value()
		return self.absolute_value()

	def reduce_aces(self):
		for card in self.cards:
			if card.card_type == 'A':
				card.card_type = 1
				return True
		return False


class BlackjackGame:

	deck = Deck()
	dealer_hand = []
	player_hand = []

	def __init__(self):
		self.deck.shuffle()
		self.dealer_hand = BlackjackHand(self.deck)
		self.player_hand = BlackjackHand(self.deck)

	def check(self):
		if self.player_hand.is_blackjack() and not self.dealer_hand.is_blackjack():
			return True
		elif self.dealer_hand.is_blackjack():
			return False
		if self.player_hand.value() > self.dealer_hand.value():
			return True
		return False


