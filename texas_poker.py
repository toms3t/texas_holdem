from collections import Counter
from random import choice


class PokerTable:
    """
    Based on Texas No-limit Hold'em Poker.
    Creates Poker game with specified # of players (default=6, max=23).
    The board and player hands can be set manually or dealt automatically
    at random.
    """

    CARDMAP = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "T": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
        "A": 14,
    }

    ALL_CARDS = [
        "2S",
        "3S",
        "4S",
        "5S",
        "6S",
        "7S",
        "8S",
        "9S",
        "TS",
        "JS",
        "QS",
        "KS",
        "AS",
        "2D",
        "3D",
        "4D",
        "5D",
        "6D",
        "7D",
        "8D",
        "9D",
        "TD",
        "JD",
        "QD",
        "KD",
        "AD",
        "2C",
        "3C",
        "4C",
        "5C",
        "6C",
        "7C",
        "8C",
        "9C",
        "TC",
        "JC",
        "QC",
        "KC",
        "AC",
        "2H",
        "3H",
        "4H",
        "5H",
        "6H",
        "7H",
        "8H",
        "9H",
        "TH",
        "JH",
        "QH",
        "KH",
        "AH",
    ]

    def __init__(self, players=6, board=None, player_dict=None):
        self.flop = []
        self.turn = []
        self.river = []
        self.board = []
        self.player_dict = player_dict
        self.player_list = []
        self.hand_dict = {}
        self.player_hand_strength_dict = {}
        self.winner = []
        self.winner_hand_strength = []
        self.winner_hand_and_board = []
        self.winner_best_hand = ""
        self.all_cards = PokerTable.ALL_CARDS
        self.all_player_cards = []
        if self.player_dict:
            self.hand_dict = player_dict
        elif not player_dict:
            for i in range(players):
                self.hand_dict[i] = self.deal(2)
        if board:
            self.board = board
        else:
            self.create_board()
            self.flop = self.board[:3]
            self.turn = self.board[3]
            self.river = self.board[-1]
        self._verify_unique_cards()
        self._create_player_list()
        self._create_player_hand_strength_dict()
        self._determine_winner()

    def __str__(self):
        """
        Prints player name and hand+board for each player.
        Then prints name of the winner(s).
        :return: self.winner.name + 'wins!' or 'tied!'
        """

        for player in self.player_list:
            print(player.name)
            print(player.hand_and_board)
            print(player.best_hand)
            print("\n")
        if len(self.get_winner) > 1:
            return str(self.get_winner) + " tied!"
        return str("".join(self.get_winner)) + " wins!"

    def _verify_unique_cards(self):
        """
        Method that verifies that there are no duplicate cards between players
        and the board.
        :return: None
        """
        # Verify that there are no duplicate cards between
        # the board and the player cards
        for val in self.hand_dict.values():
            for card in val:
                assert card not in self.board
                self.all_player_cards.append(card)

        # Verify that there are no duplicate cards between player hands
        assert len(self.all_player_cards) == len(set(self.all_player_cards))

    def _create_player_list(self):
        """
        Method that creates self.player_list which contains all player objects.
        :return: None
        """
        # Create the list of player object instances
        if self.player_dict:
            for name, hand in self.hand_dict.items():
                self.player_list.append(Player(self.board, hand, name=name))
        else:
            for num, hand in enumerate(self.hand_dict.values(), 1):
                self.player_list.append(
                    Player(self.board, hand, name="Player" + str(num))
                )

    def _create_player_hand_strength_dict(self):
        """
        Method that creates the self.player_hand_strength_dict dictionary.
        :return: None
        """
        # Create the dictionary of player names and hand strength
        for player in self.player_list:
            self.player_hand_strength_dict[player.name] = (
                player.best_hand,
                player.hand_and_board,
                player.hand_strength,
            )

    def _determine_winner(self):
        """
        Method determines the winner of the game based on the player with the
        highest "hand_strength" value in self.player_hand_strength_dict
        :return: None
        """
        # Set "self.winner" as the player(s) with the best hand(s)
        self.winner = sorted(
            [
                k
                for k, v in self.player_hand_strength_dict.items()
                if v[2]
                == max(
                    [x[2] for x in self.player_hand_strength_dict.values()])
            ]
        )
        self.winner_hand_and_board = sorted(
            [
                (k, v[1])
                for k, v in self.player_hand_strength_dict.items()
                if v[2] == max(
                    [x[2] for x in self.player_hand_strength_dict.values()])
            ]
        )
        self.winner_hand_strength = sorted(
            [
                v[2]
                for k, v in self.player_hand_strength_dict.items()
                if v[2] == max(
                    [x[2] for x in self.player_hand_strength_dict.values()])
            ]
        )[0]
        self.winner_best_hand = sorted(
            [
                v[0]
                for k, v in self.player_hand_strength_dict.items()
                if v[2] == max(
                    [x[2] for x in self.player_hand_strength_dict.values()])
            ]
        )[0]

    @property
    def get_winner(self):
        """
        Returns winner name(s)
        :return: self.winner
        """
        return self.winner

    @property
    def get_winner_hand_and_board(self):
        """
        Returns winner's hand and board cards
        :return: self.winner_hand_and_board
        """
        return self.winner_hand_and_board

    @property
    def get_winner_hand_strength(self):
        """
        Returns winner's hand strength as list of cards used for comparison
        :return: self.winner_hand_strength
        """
        return self.winner_hand_strength

    @property
    def get_winner_best_hand(self):
        """
        Returns string with the name of the winner's best hand
        (i.e. Full House)
        :return: self.winner_best_hand
        """
        return self.winner_best_hand

    def create_board(self, flop=False, next_card=False, all_cards=False):
        """
        Method that deals the flop, turn,
        and river cards (flop+turn+river = board).
        Sets the self.board attribute and
        the self.river, self.turn, and self.flop attributes if set to True.
        :param flop: Bool
        :param next_card: Bool
        :param all_cards: Bool
        :return: None
        """

        if flop:
            self.flop = self.deal(3)
            self.board += self.flop
        elif next_card:
            if self.flop and not self.turn:
                self.turn = self.deal(1)
                self.board += self.turn
            elif (self.flop and self.turn) and not self.river:
                self.river = self.deal(1)
                self.board += self.river
            else:
                self.flop = self.deal(3)
                self.board += self.flop
        elif all_cards:
            self.river = self.deal(5)
            self.board += self.river
        else:
            self.board = self.deal(5)

    def deal(self, num_cards):
        """
        Method that deals random cards to players or the board
        and removes dealt cards from the all_cards list.
        :param num_cards: Number of cards to deal.
        :return: Returns list of randomly chosen cards.
        """

        cards = []
        for _ in range(num_cards):
            card = choice(self.all_cards)
            cards.append(card)
            self.all_cards.remove(card)
        return cards

    @staticmethod
    def get_card_values(hand):
        """
        This function takes in a player's hand as a list
        and parses the card values('2' through 'A'),
        then sorts the values low to high.
        :return: Returns the sorted numerical values of the card values
        in a given hand
        (Jack = 11, Queen = 12, King = 13, Ace = 14).
        """

        card_symbols = []
        for card in hand:
            if card[0] in PokerTable.CARDMAP:
                card_symbols.append(card[0])
        card_values = [
            PokerTable.CARDMAP[card]
            for card in card_symbols
            if card in card_symbols
        ]
        card_values.sort()
        return card_values


class Player:
    """
    The Player class represents each player in the game.
    One player instance is instantiated per player.
    Class inputs are the board, the cards the player
    is dealt from the PokerTable class, and a name(optional).
    The class takes the board cards plus the player cards and determines the
    best hand the player can use with 5 cards. The best hand is identified and
    given a strength value (self.hand_strength) from 100(lowest)
    to 1000(highest).
    Hand Strength is used to determine the winner of the game.
    Tiebreakers are included in the self.hand_strength list
    and are implemented using the rules identified here
    https://www.adda52.com/poker/poker-rules/cash-game-rules/tie-breaker-rules
    """

    def __init__(self, board, hand, name=None):
        self.board = board
        self.hand = hand
        self.name = name
        self.hand_values = PokerTable.get_card_values(self.hand)
        self.hand_strength = []
        self.hand_and_board = self.hand + board
        self.best_hand = ''
        self.straight = False
        self.low_straight = False
        self.straight_score = []
        self.one_pair = False
        self.one_pair_score = []
        self.two_pair = False
        self.two_pair_score = []
        self.two_pair_higher = 0
        self.two_pair_lower = 0
        self.two_pair_kicker = 0
        self.three = False
        self.three_score = []
        self.four = False
        self.four_score = []
        self.high_card = None
        self.high_card_score = []
        self.flush = False
        self.flush_score = []
        self.flush_cards = []
        self.flush_card_values = []
        self.full_house = False
        self.full_house_score = []
        self.straight_flush = False
        self.straight_flush_score = []
        self.low_straight_flush = False
        self.royal_flush = False
        self.royal_flush_score = []
        self.hand_breakout = Counter("".join(self.hand_and_board))
        self.card_values = PokerTable.get_card_values(self.hand_and_board)
        self._identify_high_card()
        self._identify_matched_cards()
        self._identify_flush()
        self.straight, self.low_straight, self.straight_score = \
            self._identify_straight(
                self.card_values
            )
        self._identify_best_hand()
        self.get_hand_value()

    @property
    def get_player_hand(self):
        """
        Public method to return player hand cards
        :return: self.hand
        """
        return self.hand

    @property
    def get_player_best_hand(self):
        """
        Returns string with the name of the player's best hand
        (i.e. Full House)
        :return: self.best_hand
        """
        return self.best_hand

    @property
    def get_player_hand_and_board(self):
        """
        Returns player's hand and board cards
        :return: self.hand_and_board
        """
        return self.hand_and_board

    @property
    def get_player_hand_strength(self):
        """
        Returns player's hand strength as list of cards used for comparison
        :return: self.hand_strength
        """
        return self.hand_strength

    def _identify_high_card(self):
        """
        For a given hand + board, identifies the highest card by value.
        Sets the self.high_card and self.high_card_score
        attributes.
        :return: None
        """

        self.high_card = self.card_values[-1]
        self.high_card_score = self.card_values[::-1]

    def _identify_matched_cards(self):
        """
        Identifying matched cards
        (one-pair / two-pair / three-of-a-kind / four-of-a-kind / full-house).
        This method sets the following attributes:
        self.one_pair
        self.one_pair_score
        self.two_pair
        self.two_pair_score
        self.three
        self.three_score
        self.four
        self.four_score
        self.full_house
        self.two_pair_lower
        self.one_pair_score
        self.two_pair_higher
        self.two_pair_score
        self.two_pair_kicker
        :return: None
        """

        for val in self.card_values:
            # Identifying one pair and two pair sets
            if self.card_values.count(val) == 2:
                if not self.one_pair:
                    self.one_pair = True
                    self.one_pair_score.append(val)
                if self.one_pair and val != self.one_pair_score[0]:
                    self.two_pair = True
                    if val > self.one_pair_score[0]:
                        self.two_pair_lower = self.one_pair_score[0]
                        self.two_pair_higher = val
                        self.one_pair_score.insert(0, val)
                if len(self.one_pair_score) == 1:
                    self.one_pair_score += sorted(
                        [
                            x
                            for x in self.card_values
                            if self.card_values.count(x) == 1
                        ],
                        reverse=True,
                    )[:3]

            # Finding highest card to act as the fifth card kicker if tie
            if (
                    val != self.two_pair_higher
                    and val != self.two_pair_lower
                    and val > self.two_pair_kicker
            ):
                self.two_pair_kicker = val
            self.two_pair_score = [
                self.two_pair_higher,
                self.two_pair_lower,
                self.two_pair_kicker,
            ]

            if self.card_values.count(val) == 3:
                # Identifying three of a kind hands
                if self.three and val != self.three_score[0]:
                    # Special case in which player has two three-of-a-kinds,
                    # which equates to a full house
                    self.full_house = True
                    self.full_house_score = sorted(
                        [val, self.three_score[0]], reverse=True
                    )
                self.three = True

                if not self.three_score:
                    # The self.three_score variable is a list starting with
                    # the value of the 3 of a kind card, plus individual cards
                    # in descending order to act as tiebreakers if needed
                    self.three_score.append(val)
                    self.three_score += sorted(
                        [
                            x
                            for x in self.card_values
                            if self.card_values.count(x) == 1
                        ],
                        reverse=True,
                    )[:2]

            if self.card_values.count(val) == 4 and not self.four:
                self.four = True
                # The self.four_score variable is a list starting with the
                # value of the 4 of a kind card, plus the highest
                # individual card to act as a tiebreaker if needed
                self.four_score.append(val)
                self.four_score += sorted(
                    [x for x in set(self.card_values) if x != val],
                    reverse=True,
                )[:1]

        # Identifying a full house
        if (
                self.one_pair_score
                and self.three_score
                and (self.one_pair_score != self.three_score)
        ):
            self.full_house = True
            self.full_house_score = [
                self.three_score[0],
                self.one_pair_score[0],
            ]

    @staticmethod
    def _identify_low_straight(card_values):
        """
        Identifies whether a set of cards equates to a
        "low straight" (Ace, 2, 3, 4, 5) in poker.
        :param card_values: Values for each card in player's hand and board
        :return: low_straight bool, straight_score

        """
        low_straight_flag = False
        straight_score = []
        low_straight_nums = [2, 3, 4, 5, 14]
        if all(elem in card_values for elem in low_straight_nums):
            low_straight_flag = True
            straight_score.append(5)
            return low_straight_flag, straight_score
        return low_straight_flag, straight_score

    @staticmethod
    def _identify_straight(card_values):
        """
        Identifies whether a set of cards equates to a
        "straight" (5 cards with consecutive values) in poker.
        :param card_values: Values for each card
        :return: straight bool, low_straight bool, straight_score

        """
        straight = False
        low_straight = False
        straight_values = []
        unique_values = list(set(card_values))
        straight_counter = 0
        i = 0
        for val in unique_values[1:]:
            if unique_values[i] + 1 == val:
                straight_values.append(unique_values[i])
                straight_counter += 1
                i += 1
                if straight_counter >= 4:
                    straight_values.append(val)
            elif straight_counter >= 4 and unique_values[i] + 1 != val:
                break
            else:
                i += 1
                straight_counter = 0
                straight_values = []
        if straight_counter >= 4:
            straight = True
            score = [straight_values[-1]]
            return straight, low_straight, score
        low_straight, score = Player._identify_low_straight(card_values)
        return straight, low_straight, score

    def _identify_flush(self):
        """
        Identifies flush (5 cards of the same suit),
        straight flush (5 cards, same suit, in sequential order),
        or royal flush (A-K-Q-J-T same suit).
        Sets the following object attributes:
        self.flush
        self.flush_card_values
        self.straight_flush
        self.low_straight_flush
        self.straight_flush_score
        self.royal_flush
        :return: None
        """
        royal_values = [10, 11, 12, 13, 14]
        flush_suit = ""

        # Identifying a flush
        if (
                self.hand_breakout["H"] >= 5
                or self.hand_breakout["D"] >= 5
                or self.hand_breakout["S"] >= 5
                or self.hand_breakout["C"] >= 5
        ):
            self.flush = True
            for k, v in self.hand_breakout.items():
                if v >= 5:
                    flush_suit = k
                    break
            for hand in self.hand_and_board:
                if hand[-1] == flush_suit:
                    self.flush_cards.append(hand)
            self.flush_card_values = PokerTable.get_card_values(
                self.flush_cards
            )
            self.straight_flush, self.low_straight_flush, \
                self.straight_flush_score = Player._identify_straight(
                    self.flush_card_values
                )
            if self.straight_flush or self.low_straight_flush:
                self.straight_flush_score = [
                    Player._identify_straight(self.flush_card_values)[-1]
                ]

                # Identifying a royal flush
                if all(
                        elem in self.flush_card_values for elem in royal_values
                ):
                    self.royal_flush = True
            self.flush_score = self.flush_card_values[::-1]

    def _identify_best_hand(self):
        """
        This method returns the string representation
        of the player's best hand to the self.best_hand variable
        :return: "result" type = String
        """
        result = ''
        if self.high_card:
            result = "High Card"
        if self.one_pair:
            result = "One Pair"
        if self.two_pair:
            result = "Two Pair"
        if self.three:
            result = "3 Of A Kind"
        if self.straight or self.low_straight:
            result = "Straight"
        if self.flush:
            result = "Flush"
        if self.full_house:
            result = "Full House"
        if self.four:
            result = "4 Of A Kind"
        if self.straight_flush or self.low_straight_flush:
            result = "Straight Flush"
        if self.royal_flush:
            result = "Royal Flush"
        self.best_hand = result

    def get_hand_value(self):
        """
        This method calculates self.hand_strength
        based on best hand identified by the method "_identify_best_hand".
        :return: Returns self.hand_strength list

        """
        if self.high_card:
            self.hand_strength = [100] + self.high_card_score
        if self.one_pair:
            self.hand_strength = [200] + self.one_pair_score
        if self.two_pair:
            self.hand_strength = [300] + self.two_pair_score
        if self.three:
            self.hand_strength = [400] + self.three_score
        if self.straight or self.low_straight:
            self.hand_strength = [500] + self.straight_score
        if self.flush:
            self.hand_strength = [600] + self.flush_score
        if self.full_house:
            self.hand_strength = [700] + self.full_house_score
        if self.four:
            self.hand_strength = [800] + self.four_score
        if self.straight_flush or self.low_straight_flush:
            self.hand_strength = [900] + self.straight_flush_score
        if self.royal_flush:
            self.hand_strength = [1000]


print(PokerTable(players=23))
