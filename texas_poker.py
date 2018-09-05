from collections import Counter
from random import choice


class PokerTable:
	"""
	Based on Texas Hold 'Em
	"""

	CARDMAP = {
		'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
		'9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14
	}
	CARDMAP_REVERSED = {val: key for key, val in CARDMAP.items()}

	ALL_CARDS = [
		'2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', 'TS', 'JS', 'QS', 'KS', 'AS',
		'2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', 'TD', 'JD', 'QD', 'KD', 'AD',
		'2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', 'TC', 'JC', 'QC', 'KC', 'AC',
		'2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', 'TH', 'JH', 'QH', 'KH', 'AH'
	]

	def __init__(
			self, players=2, board=None, player1_hand=None, player2_hand=None, player3_hand=None,
			player1_name='Player1', player2_name='Player2', player3_name='Player3'):
		self.suits = ['D', 'H', 'S', 'C']
		self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
		self.flop = []
		self.turn = []
		self.river = []
		self.board = []
		self.player_dict = {}
		self.player_list = []
		self.hand_dict = {}
		self.winner = []
		self.players_tied = []
		self.all_player_cards = []
		self.player1_name = player1_name
		self.player2_name = player2_name
		self.player3_name = player3_name
		if player1_hand:
			self.hand_dict[1] = player1_hand
		if player2_hand:
			self.hand_dict[2] = player2_hand
		if player3_hand:
			self.hand_dict[3] = player3_hand
		elif not player1_hand and not player2_hand and not player3_hand:
			for i in range(players):
				self.hand_dict[i] = self.deal(2)
		if board:
			self.board = board
		else:
			self.create_board()
		for k, v in self.hand_dict.items():
			for card in v:
				assert card not in self.board
				self.all_player_cards.append(card)


		# Verify that there are no duplicate cards between player hands
		assert len(self.all_player_cards) == len(set(self.all_player_cards))

		for num, hand in enumerate(self.hand_dict.values(), 1):
			# self.player_dict[num] = Player(self.board, hand, name='Player'+str(num))
			self.player_list.append(Player(self.board, hand, name='Player'+str(num)))
			# print (self.player_dict)
			print (self.player_list)
		for player in self.player_list:
			if not self.winner:
				self.winner = player
				continue
			elif player.result > self.winner.result:
				# self.winner.clear()
				self.winner = player
				continue
			elif player.result < self.winner.result:
				continue
			elif player.result == self.winner.result:
				if player.four:
					if player.tiebreaker(self.winner) == 'Win':
						self.winner = player
						self.players_tied = {}
						continue
					elif player.tiebreaker(self.winner) == 'Loss':
						continue
					elif player.tiebreaker(self.winner) == 'Tie':
						self.players_tied.append(player)
						self.players_tied.append(self.winner)
						continue
				if player.full_house:
					if player.tiebreaker(self.winner) == 'Win':
						self.winner = player
						continue
					elif player.tiebreaker(self.winner) == 'Loss':
						continue
					elif player.tiebreaker(self.winner) == 'Tie':
						self.players_tied.append(player)
						self.players_tied.append(self.winner)
						continue
				if player.flush:
					if player.tiebreaker(self.winner) == 'Win':
						self.winner = player
						self.players_tied = []
						continue
					elif player.tiebreaker(self.winner) == 'Loss':
						continue
					elif player.tiebreaker(self.winner) == 'Tie':
						self.players_tied.append(player)
						self.players_tied.append(self.winner)
						continue
				if player.straight:
					if player.tiebreaker(self.winner) == 'Win':
						self.winner = player
						self.players_tied = []
						continue
					elif player.tiebreaker(self.winner) == 'Loss':
						continue
					elif player.tiebreaker(self.winner) == 'Tie':
						self.players_tied.append(player)
						self.players_tied.append(self.winner)
						continue
				if player.two_pair:
					if player.tiebreaker(self.winner) == 'Win':
						self.winner = player
						self.players_tied = []
						continue
					elif player.tiebreaker(self.winner) == 'Loss':
						continue
					elif player.tiebreaker(self.winner) == 'Tie':
						self.players_tied.append(player)
						self.players_tied.append(self.winner)
						continue
				if player.one_pair:
					if player.tiebreaker(self.winner) == 'Win':
						self.winner = player
						self.players_tied = []
						continue
					elif player.tiebreaker(self.winner) == 'Loss':
						continue
					elif player.tiebreaker(self.winner) == 'Tie':
						self.players_tied.append(player)
						self.players_tied.append(self.winner)
						continue
				if player.high_card:
					if player.tiebreaker(self.winner) == 'Win':
						self.winner = player
						self.players_tied = []
						continue
					elif player.tiebreaker(self.winner) == 'Loss':
						continue
					elif player.tiebreaker(self.winner) == 'Tie':
						self.players_tied.append(player)
						self.players_tied.append(self.winner)
						continue
		self.players_tied = sorted(self.players_tied, key=lambda x: x.name)
		if self.players_tied:
			self.winner.name = [player.name for player in self.players_tied]

	def __str__(self):
		if self.players_tied:
			print('TIE!')
			for player in self.players_tied:
				print(player.name)
				print(player.name, 'HAND:', str(player.hand_and_board))
				print ('q',self.winner)
			return str([player.name for player in self.players_tied])
		print(self.winner.name, 'wins')
		print('HAND: ', str(self.winner.hand_and_board))
		print(self.winner.straight_score)
		return self.winner.name

	def create_board(self, *args):
		if args:
			if args[0] == 'flop':
				self.flop = PokerTable.deal(3)
				self.board += self.flop
			elif args[0] == 'next':
				if self.flop and not self.turn:
					self.turn = PokerTable.deal(1)
					self.board += self.turn
				elif (self.flop and self.turn) and not self.river:
					self.river = PokerTable.deal(1)
					self.board += self.river
				else:
					self.flop = PokerTable.deal(3)
					self.board += self.flop
			elif args[0] == 'all':
				self.river = PokerTable.deal(5)
				self.board += self.river
			else:
				self.board = PokerTable.deal(5)
				print("Valid arguments for create_board method are: 'flop', 'next', 'all'")
		else:
			self.board = PokerTable.deal(5)

	@staticmethod
	def deal(num_cards):
		cards = []
		for j in range(num_cards):
			card = choice(PokerTable.ALL_CARDS)
			cards.append(card)
			PokerTable.ALL_CARDS.remove(card)
		return cards

	@staticmethod
	def get_card_values(hand):
		'''
		This function takes in the hand as a list and parses out the card values, then sorts the values low to high
		:return: Returns the numerical values of the cards in a given hand (Jack = 11, Queen = 12, King = 13, Ace = 14)
		'''
		card_symbols = []
		for card in hand:
			if card[0] in PokerTable.CARDMAP:
				card_symbols.append(card[0])
		card_values = [PokerTable.CARDMAP[card] for card in card_symbols if card in card_symbols]
		card_values.sort()
		return card_values


class Player:
	def __init__(self, board, hand, name=None):
		self.board = board
		self.hand = hand
		self.name = name
		self.board_values = PokerTable.get_card_values(self.board)
		self.hand_values = PokerTable.get_card_values(self.hand)
		self.hand_and_board = self.hand + board
		self.straight = False
		self.low_straight = False
		self.straight_score = 0
		self.one_pair = False
		self.one_pair_score = 0
		self.two_pair = False
		self.two_pair_score = 0
		self.two_pair_higher = 0
		self.two_pair_lower = 0
		self.two_pair_kicker = 0
		self.three = False
		self.three_score = 0
		self.four = False
		self.four_score = 0
		self.board_four_val = 0
		self.community_four_kicker_in_hand = 0
		self.result = 0
		self.high_card = None
		self.high_card_score = 0
		self.flush = False
		self.flush_score = 0
		self.flush_cards = []
		self.flush_card_values = []
		self.full_house = False
		self.full_house_score = 0
		self.straight_flush = False
		self.straight_flush_score = 0
		self.royal_flush = False
		self.royal_flush_score = 0
		self.score = 0
		self.tiebreak_score = 0
		self.hand_breakout = Counter(''.join(self.hand_and_board))
		self.card_values = PokerTable.get_card_values(self.hand_and_board)
		self.identify_high_card()
		self.identify_matched_cards()
		self.identify_flush()
		self.straight, self.low_straight, self.straight_score = self.identify_straight(self.card_values)
		self.best_hand = self.identify_best_hand()
		self.single_values = sorted([x for x in self.card_values if self.card_values.count(x) == 1])
		self.kicker_values = self.card_values[::-1][1:]
		self.get_hand_value()

	def identify_high_card(self):

		self.high_card_score = self.card_values[-1]
		for k, v in PokerTable.CARDMAP.items():
			if v == self.high_card_score:
				self.high_card = v

	def identify_matched_cards(self):

		# Identifying matched cards (one-pair / two-pair / three-of-a-kind / four-of-a-kind / full-house)

		for val in self.card_values:
			if self.card_values.count(val) == 2:
				if self.one_pair and val != self.one_pair_score:
					self.two_pair = True

					if val > self.one_pair_score:
						self.two_pair_lower = self.one_pair_score
						self.one_pair_score = val
						self.two_pair_higher = val
						self.two_pair_score = self.two_pair_higher

				self.one_pair = True
				self.one_pair_score = val
			if not self.two_pair_kicker:
				self.two_pair_kicker = val
			if val != self.two_pair_higher and val != self.two_pair_lower and val > self.two_pair_kicker:
				self.two_pair_kicker = val
			if self.card_values.count(val) == 3:
				# Special case in which player has two three-of-a-kinds, which equates to a full house
				if self.three and val != self.three_score:
					self.full_house = True
					if val > self.three_score:
						self.three_score = val
				self.three = True
				self.three_score = val
			if self.card_values.count(val) == 4 and not self.four:
				self.four = True
				self.four_score = val
				non_four_card_val = 0
				for board_val in self.board_values:
					if self.board_values.count(board_val) == 4 and not self.board_four_val:
						self.board_four_val = board_val
					elif self.board_values.count(board_val) == 4 and self.board_four_val:
						continue
					else:
						non_four_card_val = board_val
				if self.board_four_val:
					if max(self.hand_values) > non_four_card_val:
						self.community_four_kicker_in_hand = max(self.hand_values)

		# Need to account for community two-pairs and two-pair tiebreaker when fifth card is on board or in player hand

		if self.one_pair_score and self.three_score and (self.one_pair_score != self.three_score):
				self.full_house = True

	@staticmethod
	def identify_straight(card_values):
		straight = 0
		low_straight = False
		score = 0
		straight_vals = []

		def identify_low_straight(card_values):
			low_straight = False
			score = 0
			low_straight_nums = [2, 3, 4, 5, 14]
			if all(elem in card_values for elem in low_straight_nums):
				low_straight = True
				score = 5
				return low_straight, score
			return low_straight, score

		uniq_vals = list(set(card_values))
		straight_counter = 0
		z = 0
		for val in uniq_vals[1:]:
			if uniq_vals[z] + 1 == val:
				straight_vals.append(uniq_vals[z])
				straight_counter += 1
				z += 1
				if straight_counter >= 4:
					straight_vals.append(val)
					continue
			elif straight_counter >= 4 and uniq_vals[z] + 1 != val:
				break
			else:
				z += 1
				straight_counter = 0
				straight_vals = []
		if straight_counter >= 4:
			straight = True
			score = straight_vals[-1]
			return straight, low_straight, score
		low_straight, score = identify_low_straight(card_values)
		return straight, low_straight, score

	def identify_flush(self):
		"""
		Identify flush, straight flush, or royal flush
		:return:
		"""
		royal_nums = [10, 11, 12, 13, 14]
		flush_suit = ''
		if self.hand_breakout['H'] >= 5 or self.hand_breakout['D'] >= 5 \
				or self.hand_breakout['S'] >= 5 or self.hand_breakout['C'] >= 5:
			self.flush = True
			self.score = self.card_values[-1]
			for k, v in self.hand_breakout.items():
				if v >= 5:
					flush_suit = k
					break
			for hand in self.hand_and_board:
				if hand[-1] == flush_suit:
					self.flush_cards.append(hand)
			self.flush_card_values = PokerTable.get_card_values(self.flush_cards)
			self.score = sorted(self.flush_card_values)[-1]
			if True in Player.identify_straight(self.flush_card_values):
				self.straight_flush = True
				if all(elem in self.flush_card_values for elem in royal_nums):
					self.royal_flush = True
					self.score = 14

	def identify_best_hand(self):
		if self.royal_flush:
			return "Royal Flush"
		if self.straight_flush:
			return 'Straight Flush'
		if self.four:
			return '4 Of A Kind'
		if self.full_house:
			return 'Full House'
		if self.flush:
			return 'Flush'
		if self.straight:
			return 'Straight'
		if self.low_straight:
			return 'Straight'
		if self.three:
			return '3 Of A Kind'
		if self.two_pair:
			return 'Two Pair'
		if self.one_pair:
			return 'One Pair'
		if self.high_card:
			return 'High Card'

	def get_hand_value(self):
		'''
		This function assigns a value to the best hand identified by "identify hand()".
		:return: Returns the self.result value which is used to rank the value of a hand
		'''
		if self.royal_flush:
			self.result = 10
			return self.result
		if self.straight_flush:
			self.result = 9
			return self.result
		if self.four:
			self.result = 8
			return self.result
		if self.full_house:
			self.result = 7
			return self.result
		if self.flush:
			self.result = 6
			return self.result
		if self.straight or self.low_straight:
			self.result = 5
			return self.result
		if self.three:
			self.result = 4
			return self.result
		if self.two_pair:
			self.result = 3
			return self.result
		if self.one_pair:
			self.result = 2
			return self.result
		if self.high_card:
			self.result = 1
			return self.result

	def tiebreaker(self, other):
		'''
		This function determines the winning hand (breaks tie) if both hands are deemed the same (i.e. both one pair).
		:param other: Separate object of type PokerTable class to compare with Self
		:return: String('Win','Loss','Tie') is returned when a tiebreaker is needed (both hands have same result)
		'''

		'''
		Straights - the Straight with the highest top card wins.
		A-K-Q-J-10 beats 10-9-8-7-6, as the A beats the 10. 
		If both Straights contain cards of the same rank, it's a Tie.
		'''
		if self.royal_flush:
			return 'Tie'
		if self.straight_flush:
			if self.straight_flush_score > other.straight_flush_score:
				return 'Win'
			elif self.straight_flush_score < other.straight_flush_score:
				return 'Loss'
			elif self.straight_flush_score == other.straight_flush_score:
				return 'Tie'
		if self.four:
			if self.four_score > other.four_score:
				return 'Win'
			elif self.four_score < other.four_score:
				return 'Loss'
			elif self.four_score == other.four_score:
				if self.community_four_kicker_in_hand > other.community_four_kicker_in_hand:
					return 'Win'
				elif self.community_four_kicker_in_hand < other.community_four_kicker_in_hand:
					return 'Loss'
				return 'Tie'
		if self.full_house:
			if self.three_score > other.three_score:
				return 'Win'
			elif self.three_score < other.three_score:
				return 'Loss'
			elif self.one_pair_score > other.one_pair_score:
				return 'Win'
			elif self.one_pair_score < other.one_pair_score:
				return 'Loss'
			else:
				return 'Tie'
		if self.flush:
			for item in sorted(list(zip(self.flush_card_values, other.flush_card_values)), reverse=True):
				if item[0] > item[1]:
					return 'Win'
				elif item[0] < item[1]:
					return 'Loss'
			return 'Tie'

		if self.straight:
			if self.straight_score > other.straight_score:
				return 'Win'
			elif self.straight_score < other.straight_score:
				return 'Loss'
			return 'Tie'
		if self.two_pair:
			"""
			Two Pairs - the higher ranked pair wins.   A-A-7-7-3 beats K-K-J-J-9. 
			If the top pairs are equal, the second pair breaks the tie. 
			If both the top pair and the second pair are equal, the kicker (the next highest card) breaks the tie.
			"""
			if self.two_pair_higher > other.two_pair_higher:
				return 'Win'
			elif self.two_pair_higher < other.two_pair_higher:
				return 'Loss'
			elif self.two_pair_lower > other.two_pair_lower:
				return 'Win'
			elif self.two_pair_lower < other.two_pair_lower:
				return 'Loss'
			else:
				if self.two_pair_kicker > other.two_pair_kicker:
					return 'Win'
				elif self.two_pair_kicker < other.two_pair_kicker:
					return 'Loss'
				else:
					return 'Tie'
		if self.one_pair:
			kicker = self.find_highest_kicker(other)
			if 'self' in kicker:
				return 'Win'
			elif 'other' in kicker:
				return 'Loss'
			return 'Tie'

		if self.high_card:
			kicker = self.find_highest_kicker(other)
			if 'self' in kicker:
				return 'Win'
			elif 'other' in kicker:
				return 'Loss'
			else:
				return 'Tie'

	def find_highest_kicker(self, other):
		'''
		This function determines the card in the hand that is the highest
		kicker (card that is not part of the winning set of cards).
		:param other: Separate object of type PokerTable class to compare with Self
		:return: Returns "self" or "other" (whichever had highest kicker) and the value of the card
		'''
		for x, y in list(zip(self.single_values, other.single_values))[::-1]:
			if x > y:
				return 'self' + str(x)
			elif x < y:
				return 'other' + str(y)
		return 'Tie'


table = PokerTable(
		board=['KD', 'KC', 'KS', 'KH', 'AD'], player1_hand=['8H', '5D'], player2_hand=['9H', '5C'])
print(table.player_list[0].four_score, table.player_list[1].four_score)
print (table.winner.name)
# print(hand.players_tied)
# print(hand.winner)





