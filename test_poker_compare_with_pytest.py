import texas_poker


def test_compare():
    '''
    Testing 4 aces beats two pair
    '''
    hand = texas_poker.PokerHand('2H 3S AC AD TS AS AH')
    other = texas_poker.PokerHand('2H 3S AC AD TS 2C 3C')
    assert hand.compare_with(other) == 'Win'


def test_compare2():
    '''
    Testing high card loses to two pair
    '''
    hand = texas_poker.PokerHand('2H 4S 6C 8D TS 3H JH')
    other = texas_poker.PokerHand('2H 4S 6C 8D TS 2D 4D')
    assert hand.compare_with(other) == 'Loss'


def test_higher_4():
    '''
    Testing higher 4 of a kind wins
    '''
    hand = texas_poker.PokerHand('AH KS KC AD TS AC AS')
    other = texas_poker.PokerHand('AH KS KC AD TS KH KD')
    assert (hand.compare_with(other) == 'Win')


def test_compare4():
    '''
    Testing full house beats straight
    '''
    hand = texas_poker.PokerHand('7H 8S 8C 4D 3S 3C 8C')
    other = texas_poker.PokerHand('7H 8S 8C 4D 3S 5H 6H')
    assert (hand.compare_with(other) == 'Win')


def test_compare5():
    '''
    Testing full house loses to 4 of a kind
    '''
    hand = texas_poker.PokerHand('AH AS AC 8D TS 7C 7D')
    other = texas_poker.PokerHand('AH AS AC 8D TS AD 7H')
    assert (hand.compare_with(other) == 'Loss')


def test_compare6():
    '''
    Testing royal flush beats straight flush
    '''
    hand = texas_poker.PokerHand('TS KS QS JS 9C AS 3C')
    other = texas_poker.PokerHand('TS KS QS JS 9C 9S 3S')
    assert (hand.compare_with(other) == 'Win')


def test_compare7():
    '''
    Testing higher straight wins
    '''
    hand = texas_poker.PokerHand('3H 4S 5C 6D 9C 2S QH')
    other = texas_poker.PokerHand('3H 4S 5C 6D 9C 7S QC')
    assert (hand.compare_with(other) == 'Loss')


def test_compare8():
    '''
    Testing straight tie
    '''
    hand = texas_poker.PokerHand('3D 4D 5D 6S AC 7C KH')
    other = texas_poker.PokerHand('3D 4D 5D 6S AC 7S AS')
    assert (hand.compare_with(other) == 'Tie')


def test_compare9():
    '''
    Testing higher pair of two pair wins
    '''
    hand = texas_poker.PokerHand('KH KS 8C 6D TS 6S 7C')
    other = texas_poker.PokerHand('KH KS 8C 6D TS 8C 9C')
    assert (hand.compare_with(other) == 'Loss')


def test_compare10():
    '''
    Testing higher 3 of a kind in a full house wins
    '''
    hand = texas_poker.PokerHand('AH AS 7C 7D 8S 7C KH')
    other = texas_poker.PokerHand('AH AS 7C 7D 8S 7S 3S')
    assert (hand.compare_with(other) == 'Tie')


def test_compare11():
    '''
    Testing higher 3 of a kind in a full house wins
    '''
    hand = texas_poker.PokerHand('5H 5S 4C 8D 8S 8S KH')
    other = texas_poker.PokerHand('5H 5S 4C 8D 8S 4D 4S')
    assert (hand.compare_with(other) == 'Win')


def test_compare12():
    '''
    Testing higher card of a flush wins
    '''
    hand = texas_poker.PokerHand('3H 5H 7H 8H TD 2H KS')
    other = texas_poker.PokerHand('3H 5H 7H 8H TD TH 8D')
    assert (hand.compare_with(other) == 'Loss')


def test_compare13():
    '''
    Testing higher card of hand 4 of a kind wins
    '''
    hand = texas_poker.PokerHand('8H 8S 7C 7D TS 8D 8C')
    other = texas_poker.PokerHand('8H 8S 7C 7D TS 7H 7S')
    assert (hand.compare_with(other) == 'Win')


def test_compare14():
    '''
    Testing one pair beats high card
    '''
    hand = texas_poker.PokerHand('8H 6S 4C 5D TS 3D 3S')
    other = texas_poker.PokerHand('8H 6S 4C 5D TS KH JH')
    assert (hand.compare_with(other) == 'Win')


def test_compare15():
    '''
    Testing higher card tiebreaker
    '''
    hand = texas_poker.PokerHand('8H 5D 4C 2D TS 7D 3D')
    other = texas_poker.PokerHand('8H 5D 4C 2D TS 9S 3C')
    assert (hand.compare_with(other) == 'Loss')


def test_compare16():
    '''
    Testing two pair tie
    '''
    hand = texas_poker.PokerHand('8H 8D 4C 3D TS 3D 6D')
    other = texas_poker.PokerHand('8H 8D 4C 3D TS 3H 6H')
    assert (hand.compare_with(other) == 'Tie')


def test_compare17():
    '''
    Testing one pair tie
    '''
    hand = texas_poker.PokerHand('8H 8D 5C 4D TS 9S 6H')
    other = texas_poker.PokerHand('8H 8D 5C 4D TS 9C 6C')
    assert (hand.compare_with(other) == 'Tie')


def test_compare18():
    '''
    Testing high card tie
    '''
    hand = texas_poker.PokerHand('2H 4D 6C 8D TS AH KH')
    other = texas_poker.PokerHand('2H 4D 6C 8D TS AS KS')
    assert (hand.compare_with(other) == 'Tie')


def test_ace_as_one():
    '''
    Testing ace used as a 1 in a straight
    '''
    hand = texas_poker.PokerHand('AH TD 3C 4D 5S 2C 7D')
    other = texas_poker.PokerHand('AH TD 3C 4D 5S 7S 7H')
    assert (hand.compare_with(other) == 'Win')


def test_ace_as_one_straight_flush():
    '''
    Testing ace used as a 1 in a straight flush
    '''
    hand = texas_poker.PokerHand('AH 9H 3H 4H 5H 2H 7D')
    other = texas_poker.PokerHand('AH 9H 3H 4H 5H 7S 7H')
    assert (hand.compare_with(other) == 'Win')


def test_ace_as_one_straight_flush_loses():
    '''
    Testing ace used as a 1 in a straight flush
    '''
    hand = texas_poker.PokerHand('AH QH 3H 4H 5H 7C 7D')
    other = texas_poker.PokerHand('AH QH 3H 4H 5H 2H QD')
    assert (hand.compare_with(other) == 'Loss')


def test_ace_as_one_straight_loses():
    '''
    Testing ace used as a 1 in a straight
    '''
    hand = texas_poker.PokerHand('AD 8C 3H 4C 5H QD QH')
    other = texas_poker.PokerHand('AD 8C 3H 4C 5H 9H 2D')
    assert (hand.compare_with(other) == 'Loss')


def test_full_house_tiebreaker():
    '''
    Testing full house tiebreaker
    '''
    hand = texas_poker.PokerHand('KH KC 3S 3H 3D 8H AH')
    other = texas_poker.PokerHand('KH KC 3S 3H 3D 7C KS')
    assert (hand.compare_with(other) == 'Win')


def test_two_pair_tiebreaker():
    '''
    Testing two pair tiebreaker
    '''
    hand = texas_poker.PokerHand('KH KC 3S 3H 4D 8H 5D')
    other = texas_poker.PokerHand('KH KC 3S 3H 4D 7C QS')
    assert (hand.compare_with(other) == 'Loss')



def test_community_4_tiebreaker():
    '''
    Testing a community 4 of a kind tiebreaker
    '''
    hand = texas_poker.PokerHand('KD KC KS KH 4D 8H 5D')
    other = texas_poker.PokerHand('KD KC KS KH 4D 9H 5D')
    assert (hand.compare_with(other) == 'Loss')


### Need to separate community cards from player cards to show this as a tie
def test_community_4_tiebreaker2():
    '''
    Testing a community 4 of a kind tiebreaker when 5th community card is highest of all players
    '''
    hand = texas_poker.PokerHand('KD KC KS KH AD 8H 5D')
    other = texas_poker.PokerHand('KD KC KS KH AD 9H 5D')
    assert (hand.compare_with(other) == 'Tie')
