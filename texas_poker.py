from collections import Counter
from random import choice


class PokerHand:
	"""
	Based on Texas Hold 'Em
	"""

	CARDMAP = {
		'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
		'9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14
	}
	CARDMAP_REVERSED = {val: key for key, val in CARDMAP.items()}
	suits = ['D', 'H', 'S', 'C']
	ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

	def __init__(self, hand):
		self.hand = hand.split()
		self.suits = ['D', 'H', 'S', 'C']
		self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
		self.straight = False
		self.low_straight = False
		self.straight_score = 0
		self.one_pair = False
		self.one_pair_score = 0
		self.two_pair = False
		self.two_pair_score = 0
		self.two_pair_higher = 0
		self.two_pair_lower = 0
		self.three = False
		self.three_score = 0
		self.four = False
		self.four_score = 0
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
		self.hand_breakout = Counter(''.join(self.hand))
		self.card_values = PokerHand.get_card_values(hand)
		self.identify_high_card()
		self.identify_matched_cards()
		self.identify_flush()
		if True in self.identify_straight(self.card_values):
			self.straight, self.low_straight, self.score = self.identify_straight(self.card_values)
		self.best_hand = self.identify_best_hand()
		self.single_values = sorted([x for x in self.card_values if self.card_values.count(x) == 1])
		self.kicker_values = self.card_values[::-1][1:]

	def __repr__(self):
		return str(self.best_hand)

	def __str__(self):
		return str(self.best_hand)

	@staticmethod
	def hand_generator():
		o = 0
		hand = []
		for i in range(2):
			o += 1
			while len(hand) <= 1:
				card = choice(PokerHand.ranks) + choice(PokerHand.suits)
				if card not in hand:
					hand.append(card)
		hand = ' '.join(hand)


	@staticmethod
	def get_card_values(hand):
		'''
		This function takes in the hand as a list and parses out the card values, then sorts the values low to high
		:return: Returns the numerical values of the cards in a given hand (Jack = 11, Queen = 12, King = 13, Ace = 14)
		'''
		card_symbols = []
		for card in hand:
			if card[0] in PokerHand.CARDMAP:
				card_symbols.append(card[0])
		card_values = [PokerHand.CARDMAP[card] for card in card_symbols if card in card_symbols]
		card_values.sort()
		return card_values

	def identify_high_card(self):

		self.high_card_score = self.card_values[-1]
		for k, v in PokerHand.CARDMAP.items():
			if v == self.high_card_score:
				self.high_card = v

	def identify_matched_cards(self):
		two_pair_vals = []
		i = 0
		highest = 0
		# Identifying matched cards (one-pair / two-pair / three-of-a-kind / four-of-a-kind / full-house)
		for val in self.card_values:
			if self.card_values.count(val) == 2:
				self.one_pair = True
				self.one_pair_score = val
			elif self.card_values.count(val) == 3:
				self.three = True
				self.three_score = val
			elif self.card_values.count(val) == 4:
				self.four = True
				self.four_score = val
		for val in self.card_values:
			if self.card_values.count(val) == 2:
				two_pair_vals.append(val)
				i += 1
				if val > highest:
					highest = val
		if i >= 4:
			self.two_pair_higher = two_pair_vals[-1]
			self.two_pair_lower = two_pair_vals[-2]
			self.two_pair = True
			self.two_pair_score = highest

		if self.one_pair and self.three:
			self.full_house = True

	@staticmethod
	def identify_straight(card_values):
		straight = 0
		low_straight = False
		score = 0
		straight_vals = []
		def identify_low_straight(card_values):
			straight = False
			low_straight = False
			score = 0
			low_straight_nums = [2, 3, 4, 5, 14]
			if all(elem in card_values for elem in low_straight_nums):
				low_straight = True
				score = 5
				return straight, low_straight, score
			return straight, low_straight, score

		uniq_vals = list(set(card_values))
		straight_counter = 0
		z = 0
		for val in uniq_vals[1:]:
			if uniq_vals[z] + 1 == val:
				straight_vals.append(uniq_vals[z])
				straight_counter += 1
				z += 1
				if straight_counter == 4:
					straight_vals.append(val)
					break
			else:
				z += 1
				straight_counter = 0
				straight_vals = []
		if straight_counter == 4:
			straight = True
			score = straight_vals[-1]
			return straight, low_straight, score
		straight, low_straight, score = identify_low_straight(card_values)
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
			for hand in self.hand:
				if hand[-1] == flush_suit:
					self.flush_cards.append(hand)
			self.flush_card_values = PokerHand.get_card_values(self.flush_cards)
			self.score = sorted(self.flush_card_values)[-1]
			if True in PokerHand.identify_straight(self.flush_card_values):
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
		:param other: Separate object of type PokerHand class to compare with Self
		:return: String('Win','Loss','Tie') is returned when a tiebreaker is needed (both hands have same result)
		'''

		'''
		Straights - the Straight with the highest top card wins.
		A-K-Q-J-10 beats 10-9-8-7-6, as the A beats the 10. 
		If both Straights contain cards of the same rank, it's a Tie.
		'''
		if self.four:
			if self.four_score > other.four_score:
				return 'Win'
			elif self.four_score < other.four_score:
				return 'Loss'
		if self.straight:
			if self.straight_score > other.straight_score:
				return 'Win'
			elif self.straight_score < other.straight_score:
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
		if self.one_pair:
			kicker = self.find_highest_kicker(other)
			if 'self' in kicker:
				return 'Win'
			elif 'other' in kicker:
				return 'Loss'
			return 'Tie'
		if self.two_pair:
			"""
			Two Pairs - the higher ranked pair wins.   A-A-7-7-3 beats K-K-J-J-9. 
			If the top pairs are equal, the second pair breaks the tie. 
			If both the top pair and the second pair are equal, the kicker (the next highest card) breaks the tie.
			"""
			if self.two_pair_lower > other.two_pair_lower:
				return 'Win'
			elif self.two_pair_lower < other.two_pair_lower:
				return 'Loss'
			kicker = self.find_highest_kicker(other)
			if 'self' in kicker:
				return 'Win'
			elif 'other' in kicker:
				return 'Loss'
		if self.flush:
			kicker = self.find_highest_kicker(other)
			if 'self' in kicker:
				return 'Win'
			elif 'other' in kicker:
				return 'Loss'
			else:
				return 'Tie'
		if self.score == other.score:
			for val in self.card_values[::-1]:
				if val != self.score:
					self.score = val
					break
			for val in other.card_values[::-1]:
				if val != other.score:
					other.score = val
					break
		if self.high_card:
			kicker = self.find_highest_kicker(other)
			if 'self' in kicker:
				return 'Win'
			elif 'other' in kicker:
				return 'Loss'
			else:
				return 'Tie'
		if self.score > other.score:
			return "Win"
		elif self.score < other.score:
			return "Loss"
		return "Tie"

	def find_highest_kicker(self, other):
		'''
		This function determines the card in the hand that is the highest
		kicker (card that is not part of the winning set of cards).
		:param other: Separate object of type PokerHand class to compare with Self
		:return: Returns "self" or "other" (whichever had highest kicker) and the value of the card
		'''
		for x, y in list(zip(self.single_values, other.single_values))[::-1]:
			if x > y:
				return 'self' + str(x)
			elif x < y:
				return 'other' + str(y)
		return 'Tie'

	def compare_with(self, other):
		'''
		This function compares one hand to another and returns "Win", "Loss", or "Tie" from the perspective of self
		:param other: Separate object of type PokerHand class to compare with Self
		:return: String('Win', 'Loss', 'Tie')
		'''
		# self.identify_hand()
		# other.identify_hand()
		self.result = self.get_hand_value()
		other.result = other.get_hand_value()
		if self.result > other.result:
			return "Win"
		if self.result < other.result:
			return 'Loss'

		# Tiebreakers - higher score wins
		if self.result == other.result:
			if self.score > other.score:
				return 'Win'
			elif self.score < other.score:
				return 'Loss'
			else:
				if self.full_house:
					return self.tiebreaker(other)
				if self.high_card:
					return self.tiebreaker(other)
				if self.one_pair:
					return self.tiebreaker(other)
				if self.two_pair:
					return self.tiebreaker(other)
				if self.flush:
					return self.tiebreaker(other)
				if self.straight:
					return self.tiebreaker(other)
				if self.four:
					return self.tiebreaker(other)


a = PokerHand.hand_generator()
# hand = PokerHand('KD KC KS KH AD TH 5D')
# other = PokerHand('KD KC KS KH AD 9H 5D')
# print (hand.best_hand)
# print (hand.score)
# other = PokerHand('3H 4S 5C 6D 7S KS AS')
# print (other.best_hand)
# print (other.score)
# # hand = PokerHand('AH 2D 3C 4D 5S TD TH')
# # print (hand.best_hand)
# # print (hand.get_hand_value())
# # assert (a.best_hand == '3 Of A Kind')
# # hand = '5H 6D KH 3H 7S QH 8H'
# # other = '3H 4S 5C 6D 7S 8H 9H'
# player, opponent = PokerHand(hand), PokerHand(other)
# print (hand.best_hand, hand.score)
# print (hand.best_hand)
# # #
# print(hand.compare_with(other))
