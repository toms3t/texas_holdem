import random
import poker
import logging



suits = ['S', 'D', 'C', 'H']
nums = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
CARDMAP = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
    '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14
}

CARDMAP_REVERSED = {val: key for key, val in CARDMAP.items()}
COUNT = 0
H = ''

def logging_decorator(func):
    import logging
    logging.basicConfig(filename='pokerstats-test.log', level=logging.INFO)
    def wrapper(*args,**kwargs):
        for hand in func(*args):
            logging.info('HAND: {}'.format(hand))
        return wrapper(*args,**kwargs)
    return logging_decorator


@logging_decorator
def hand_builder(num_of_hands):
    o = 0
    hands = []
    for i in range(num_of_hands):
        o += 1
        hand = []
        while len(hand) <= 4:
            if len(hand) == 5: break
            card = random.choice(nums) + random.choice(suits)
            if card not in hand:
                hand.append(card)
        print(o, hand)
        hand = ' '.join(hand)
        h = poker.PokerHand(hand)
        print (h)
        hands.append(h)
    return hands
        # logging.info('HAND {} - {}'.format(h.best_hand, h.hand))

print (hand_builder(100))

# print (hand_builder(10))
# hand_builder(10)
