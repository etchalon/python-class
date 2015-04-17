from blackjack import BlackjackGame

game = BlackjackGame()

if game.check():
	print 'Player wins with %s' % game.player_hand
	print 'Dealer had %s' % game.dealer_hand
else:
	print 'Player loses with %s' % game.player_hand
	print 'Dealer had %s' % game.dealer_hand