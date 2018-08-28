import random
import texas_poker
import logging



suit = ['S', 'D', 'C', 'H']
rank = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
CARDMAP = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
    '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14
}

CARDMAP_REVERSED = {val: key for key, val in CARDMAP.items()}
COUNT = 0
H = ''


def logging_decorator(func):
    import logging
    logging.basicConfig(filename='pokerstats-test.log', level=logging.INFO, filemode='w')

    def wrapper(dict):
        for handobj, hand in func(dict).items():
            logging.info('HAND: {} - {}'.format(handobj, hand))
        return func(dict)
    return wrapper


@logging_decorator
def hand_builder(num_of_hands):
    o = 0
    hands = {}
    for i in range(num_of_hands):
        o += 1
        hand = []
        while len(hand) <= 6:
            card = random.choice(rank) + random.choice(suit)
            if card not in hand:
                hand.append(card)
        hand = ' '.join(hand)
        handobj = texas_poker.PokerHand(hand)
        print (hand, handobj)
        hands[hand] = handobj
    return hands

hand_builder(1000)
