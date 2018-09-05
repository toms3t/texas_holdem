import texas_poker


def test_high_card_tiebreaker():
    table = texas_poker.PokerTable(
        board=['8H', '5D', '4C', '2D', 'TS'], player1_hand=['7D', '3D'], player2_hand=['9S', '3C'])
    assert table.winner.name == 'Player2'


def test_high_card_tiebreaker2():
    table = texas_poker.PokerTable(
        board=['8H', '5D', '4C', '2D', 'TS'], player1_hand=['7D', 'AD'], player2_hand=['9S', '3C'])
    assert table.winner.name == 'Player1'


def test_two_pair_beats_high_card():
    table = texas_poker.PokerTable(
        board=['2H', '4S', '6C', '8D', 'TS'], player1_hand=['3H', 'JH'], player2_hand=['2D', '4D'])
    assert table.winner.name == 'Player2'


def test_3_beats_high_card():
    table = texas_poker.PokerTable(
        board=['2H', '4S', '6C', '8D', 'TS'], player1_hand=['3H', 'JH'], player2_hand=['4C', '4D'])
    assert table.winner.name == 'Player2'


def test_straight_beats_high_card():
    table = texas_poker.PokerTable(
        board=['2H', '4S', '6C', '8D', 'TS'], player1_hand=['3H', '5H'], player2_hand=['JC', '9D'])
    assert table.winner.name == 'Player1'


def test_flush_beats_high_card():
    table = texas_poker.PokerTable(
        board=['2H', '4S', '6C', '8C', 'QC'], player1_hand=['3H', 'AH'], player2_hand=['JC', '2C'])
    assert table.winner.name == 'Player2'


def test_full_house_beats_high_card():
    table = texas_poker.PokerTable(
        board=['2H', '2S', '8D', '8C', 'QC'], player1_hand=['3H', '8S'], player2_hand=['JC', '3C'])
    assert table.winner.name == 'Player1'


def test_4_beats_high_card():
    table = texas_poker.PokerTable(
        board=['2H', '2S', '8D', '8C', 'QC'], player1_hand=['2D', '2C'], player2_hand=['JC', '3C'])
    assert table.winner.name == 'Player1'


def test_straight_flush_beats_high_card():
    table = texas_poker.PokerTable(
        board=['TH', '2C', '3C', '8C', '5C'], player1_hand=['2D', '9C'], player2_hand=['4C', '6C'])
    assert table.winner.name == 'Player2'


def test_royal_flush_beats_high_card():
    table = texas_poker.PokerTable(
        board=['TH', 'JH', '9H', 'AH', '5C'], player1_hand=['2D', '9C'], player2_hand=['KH', 'QH'])
    assert table.winner.name == 'Player2'


def test_4_beats_two_pair():
    table = texas_poker.PokerTable(
        board=['2H', '3S', 'AC', 'AD', 'TS'], player1_hand=['AH', 'AS'], player2_hand=['3C', '2C'])
    assert table.winner.name == 'Player1'


def test_higher_4_wins():
    table = texas_poker.PokerTable(
        board=['AH', 'KS', 'KC', 'AD', 'TS'], player1_hand=['AC', 'AS'], player2_hand=['KH', 'KD'])
    assert table.winner.name == 'Player1'


def test_higher_4_wins2():
    table = texas_poker.PokerTable(
        board=['8H', '8S', '7C', '7D', 'TS'], player1_hand=['8D', '8C'], player2_hand=['7H', '7S'])
    assert table.winner.name == 'Player1'


def test_full_house_beats_straight():
    table = texas_poker.PokerTable(
        board=['7H', '8S', '8C', '4D', '3S'], player1_hand=['3C', '8D'], player2_hand=['5H', '6H'])
    assert table.winner.name == 'Player1'


def test_4_beats_full_house():
    table = texas_poker.PokerTable(
        board=['AH', 'AS', 'AC', '8D', 'TS'], player1_hand=['7C', '7D'], player2_hand=['AD', '7H'])
    assert table.winner.name == 'Player2'


def test_royal_beats_straight_flush():
    table = texas_poker.PokerTable(
        board=['TS', 'KS', 'QS', 'JS', '9C'], player1_hand=['AS', '3C'], player2_hand=['9S', '3S'])
    assert table.winner.name == 'Player1'


def test_higher_straight_wins():
    table = texas_poker.PokerTable(
        board=['3H', '4S', '5C', '6D', '9C'], player1_hand=['2S', 'QH'], player2_hand=['7S', 'QC'])
    assert table.winner.name == 'Player2'


def test_straight_tie():
    table = texas_poker.PokerTable(
        board=['3D', '4D', '5D', '6S', 'AC'], player1_hand=['7C', 'KH'], player2_hand=['7S', 'AS'])
    assert table.winner.name == ['Player1', 'Player2']


def test_two_pair_tiebreaker():
    table = texas_poker.PokerTable(
        board=['KH', 'KS', '8C', '6D', 'TS'], player1_hand=['6S', '7C'], player2_hand=['8D', '9C'])
    assert table.winner.name == 'Player2'


def test_two_pair_tiebreaker2():
    table = texas_poker.PokerTable(
        board=['KH', 'KC', '3S', '3H', '4D'], player1_hand=['8H', '5D'], player2_hand=['7C', 'QS'])
    assert table.winner.name == 'Player2'


def test_higher_three_in_full_house_wins():
    table = texas_poker.PokerTable(
        board=['AH', 'AS', '7C', '7D', '8S'], player1_hand=['7H', 'KH'], player2_hand=['6S', 'AD'])
    assert table.winner.name == 'Player2'


def test_full_house_tie():
    table = texas_poker.PokerTable(
        board=['5H', '5S', '4C', '8D', '8H'], player1_hand=['8S', 'KH'], player2_hand=['8C', '4S'])
    assert table.winner.name == ['Player1', 'Player2']


def test_highest_card_in_flush_tie_wins():
    table = texas_poker.PokerTable(
        board=['3H', '5H', '7H', '8H', 'TD'], player1_hand=['2H', 'KS'], player2_hand=['TH', '8D'])
    assert table.winner.name == 'Player2'


def test_one_pair_beats_high_card():
    table = texas_poker.PokerTable(
        board=['8H', '6S', '4C', '5D', 'TS'], player1_hand=['3D', '3S'], player2_hand=['KH', 'JH'])
    assert table.winner.name == 'Player1'


def test_two_pair_tie():
    table = texas_poker.PokerTable(
        board=['8H', '8D', '4C', '3D', 'TS'], player1_hand=['3S', '6D'], player2_hand=['3H', '6H'])
    assert table.winner.name == ['Player1', 'Player2']


def test_one_pair_tie():
    table = texas_poker.PokerTable(
        board=['8H', '8D', '5C', '4D', 'TS'], player1_hand=['9S', '6H'], player2_hand=['9C', '6C'])
    assert table.winner.name == ['Player1', 'Player2']


def test_high_card_tie():
    table = texas_poker.PokerTable(
        board=['2H', '4D', '6C', '8D', 'TS'], player1_hand=['AH', 'KH'], player2_hand=['AS', 'KS'])
    assert table.winner.name == ['Player1', 'Player2']


def test_ace_as_one():
    table = texas_poker.PokerTable(
        board=['AH', 'TD', '3C', '4D', '5S'], player1_hand=['2C', '7D'], player2_hand=['7S', '7H'])
    assert table.winner.name == 'Player1'


def test_ace_as_one_straight_flush():
    table = texas_poker.PokerTable(
        board=['AH', '9H', '3H', '4H', '5H'], player1_hand=['2H', '7D'], player2_hand=['7S', '7H'])
    assert table.winner.name == 'Player1'


def test_ace_as_one_straight_flush_loses():
    table = texas_poker.PokerTable(
        board=['AH', 'QH', '3H', '4H', '5H'], player1_hand=['7C', '7D'], player2_hand=['2H', 'QD'])
    assert table.winner.name == 'Player2'


def test_ace_as_one_straight_loses():
    table = texas_poker.PokerTable(
        board=['AD', '8C', '3H', '4C', '5H'], player1_hand=['QD', 'QH'], player2_hand=['9H', '2D'])
    assert table.winner.name == 'Player2'


def test_community_full_house():
    table = texas_poker.PokerTable(
        board=['KH', 'KC', '3S', '3H', '3D'], player1_hand=['8H', 'AH'], player2_hand=['7C', 'KS'])
    assert table.winner.name == 'Player2'


def test_community_4_tiebreaker():
    table = texas_poker.PokerTable(
        board=['KD', 'KC', 'KS', 'KH', '4D'], player1_hand=['8H', '5D'], player2_hand=['9H', '5C'])
    assert table.winner.name == 'Player2'


def test_community_4_tiebreaker2():
    table = texas_poker.PokerTable(
        board=['KD', 'KC', 'KS', 'KH', 'AD'], player1_hand=['8H', '5D'], player2_hand=['9H', '5C'])
    assert table.winner.name == ['Player1', 'Player2']


def test_community_4_tiebreaker3():
    table = texas_poker.PokerTable(
        board=['KD', 'KC', 'KS', 'KH', '4D'], player1_hand=['8H', '5D'], player2_hand=['9H', '5C'])
    assert table.winner.name == 'Player2'


def test_two_royal_flushes_is_tie():
    table = texas_poker.PokerTable(
        board=['KD', 'AD', 'QD', 'JD', 'TD'], player1_hand=['4H', '5D'], player2_hand=['JH', '5S'])
    assert table.winner.name == ['Player1', 'Player2']


def test_straight_flush_tie():
    table = texas_poker.PokerTable(
        board=['QD', 'JD', 'TD', '9D', '8D'], player1_hand=['4H', '5D'], player2_hand=['JH', '5S'])
    assert table.winner.name == ['Player1', 'Player2']
