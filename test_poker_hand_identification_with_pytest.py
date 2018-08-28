import texas_poker


def test_id():
    hand = texas_poker.PokerTable('2H 3S AC AD TS 4C 6S')
    assert hand.best_hand == 'One Pair'
    assert hand.get_hand_value() == 2


def test_id2():
    hand = texas_poker.PokerTable('2H 4S 6C 8D TS QH AH KD')
    assert hand.best_hand == 'High Card'
    assert hand.get_hand_value() == 1


def test_id3():
    hand = texas_poker.PokerTable('AH AS AC AD TS 4C 5C')
    assert (hand.best_hand == '4 Of A Kind')
    assert hand.get_hand_value() == 8


def test_id4():
    hand = texas_poker.PokerTable('8H 8S 8C 3D 3S 7C 9C')
    assert (hand.best_hand == 'Full House')
    assert hand.get_hand_value() == 7


def test_id5():
    hand = texas_poker.PokerTable('AH AS AC 8D TS 7C 3H')
    assert (hand.best_hand == '3 Of A Kind')
    assert hand.get_hand_value() == 4


def test_id6():
    hand = texas_poker.PokerTable('AS KS QS JS TS 2C 3C')
    assert (hand.best_hand == 'Royal Flush')
    assert hand.get_hand_value() == 10


def test_id7():
    hand = texas_poker.PokerTable('3H 4S 5C 6D 7S AH QH')
    assert (hand.best_hand == 'Straight')
    assert hand.get_hand_value() == 5


def test_id8():
    hand = texas_poker.PokerTable('3H 4S 5C 6D 7S TH QH')
    assert (hand.best_hand == 'Straight')
    assert hand.get_hand_value() == 5


def test_id9():
    hand = texas_poker.PokerTable('KH KS 8C 8D TS 9C 2H')
    assert (hand.best_hand == 'Two Pair')
    assert hand.get_hand_value() == 3


def test_id10():
    hand = texas_poker.PokerTable('AH AS AC 8D 8S 9H 2C')
    assert (hand.best_hand == 'Full House')
    assert hand.get_hand_value() == 7


def test_id11():
    hand = texas_poker.PokerTable('5H 5S 5C 8D 8S 9C 2H')
    assert (hand.best_hand == 'Full House')
    assert hand.get_hand_value() == 7


def test_id12():
    hand = texas_poker.PokerTable('3H 5H 7H 8H TH 9C TC')
    assert (hand.best_hand == 'Flush')
    assert hand.get_hand_value() == 6


def test_id13():
    hand = texas_poker.PokerTable('8H 8S 8C 8D TS 2H 3C')
    assert (hand.best_hand == '4 Of A Kind')
    assert hand.get_hand_value() == 8


def test_id14():
    hand = texas_poker.PokerTable('8H 8S 4C 5D TS 3C QH')
    assert (hand.best_hand == 'One Pair')
    assert hand.get_hand_value() == 2


def test_id15():
    hand = texas_poker.PokerTable('8H 5D 4C 2D TS QH 3C')
    assert (hand.best_hand == 'High Card')
    assert hand.get_hand_value() == 1


def test_id16():
    hand = texas_poker.PokerTable('8H 8D 4C 4D TS 9H 2C')
    assert (hand.best_hand == 'Two Pair')
    assert hand.get_hand_value() == 3


def test_id17():
    hand = texas_poker.PokerTable('8H 8D 5C 4D TS QH KD')
    assert (hand.best_hand == 'One Pair')
    assert hand.get_hand_value() == 2


def test_id18():
    hand = texas_poker.PokerTable('2H 4D 6C 8D TS KH 3D')
    assert (hand.best_hand == 'High Card')
    assert hand.get_hand_value() == 1


def test_id19():
    hand = texas_poker.PokerTable('AH 2D 3C 4D 5S TD TH')
    assert (hand.best_hand == 'Straight')
    assert hand.get_hand_value() == 5


def test_id20():
    hand = texas_poker.PokerTable('AH 2H 3H 4H 5H TH TD')
    assert (hand.best_hand == 'Straight Flush')
    assert hand.get_hand_value() == 9


def test_id21():
    hand = texas_poker.PokerTable('6H 2H 3H 4H 5H TH TD')
    assert (hand.best_hand == 'Straight Flush')
    assert hand.get_hand_value() == 9


def test_id22():
    hand = texas_poker.PokerTable('AD 2C 3H 4C 5H TH TD')
    assert (hand.best_hand == 'Straight')
    assert hand.get_hand_value() == 5


def test_id23():
    hand = texas_poker.PokerTable('KH KC 3S 3H 3D TH TD')
    assert (hand.best_hand == 'Full House')
    assert hand.get_hand_value() == 7


def test_id24():
    hand = texas_poker.PokerTable('AH 2C 3S 4H 5D TD TH')
    assert (hand.best_hand == 'Straight')
    assert hand.get_hand_value() == 5


def test_id25():
    hand = texas_poker.PokerTable('AH KC QS JH TD TH 7C')
    assert (hand.best_hand == 'Straight')
    assert hand.get_hand_value() == 5


def test_id26():
    hand = texas_poker.PokerTable('AH AC QS AS AD TD TH')
    assert (hand.best_hand == '4 Of A Kind')
    assert hand.get_hand_value() == 8


def test_id27():
    hand = texas_poker.PokerTable('2C 4C 6C 8C TC TH TD')
    assert (hand.best_hand == 'Flush')
    assert hand.get_hand_value() == 6


def test_id28():
    hand = texas_poker.PokerTable('2D 4D 6D 8D TD TH 5C')
    assert (hand.best_hand == 'Flush')
    assert hand.get_hand_value() == 6


def test_id29():
    hand = texas_poker.PokerTable('2S 4S AS 5S KS AH TD')
    assert (hand.best_hand == 'Flush')
    assert hand.get_hand_value() == 6


def test_id30():
    hand = texas_poker.PokerTable('5S 4S 3S 2S AS 3C 3D')
    assert (hand.best_hand == 'Straight Flush')
    assert hand.get_hand_value() == 9


def test_id31():
    hand = texas_poker.PokerTable('6D TD 3H 9D 8D 2S 7S')
    assert (hand.best_hand == 'Straight')
    assert hand.get_hand_value() == 5


def test_id32():
    hand = texas_poker.PokerTable('QH 3C KH AH JS JH 2C TH')
    assert (hand.best_hand == 'Royal Flush')
    assert hand.get_hand_value() == 10


def test_id33():
    hand = texas_poker.PokerTable('QH QD KH KD JD JH 2C 8C')
    assert (hand.best_hand == 'Two Pair')
    assert hand.get_hand_value() == 3


def test_id34():
    hand = texas_poker.PokerTable('QH QD KH KD JD JH 2H 8H')
    assert (hand.best_hand == 'Flush')
    assert hand.get_hand_value() == 6


def test_id35():
    hand = texas_poker.PokerTable('QH 5D KS TD 2D JH 3H 8H')
    assert (hand.best_hand == 'High Card')
    assert hand.get_hand_value() == 1


def test_id36():
    hand = texas_poker.PokerTable('3D 4D 5D 6S 7C 4C KH')
    assert (hand.best_hand == 'Straight')
    assert hand.get_hand_value() == 5