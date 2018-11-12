import texas_poker


def test_high_card_tiebreaker():
    table = texas_poker.PokerTable(
        board=["8H", "5D", "4C", "2D", "TS"],
        player_dict={'Player1': ["7D", "3D"], 'Player2': ["9S", "3C"]},
    )
    assert table.winner == ["Player2"]


def test_high_card_tiebreaker2():
    table = texas_poker.PokerTable(
        board=["8H", "5D", "4C", "2D", "TS"],
        player_dict={'Player1': ["7D", "AD"], 'Player2':  ["9S", "3C"]}
    )
    assert table.winner == ["Player1"]


def test_one_pair_beats_high_card():
    table = texas_poker.PokerTable(
        board=["7H", "5D", "4C", "2D", "TS"],
        player_dict={'Player1': ["7D", "AD"], 'Player2':  ["9S", "3C"]}
    )
    assert table.winner == ["Player1"]


def test_two_pair_beats_high_card():
    table = texas_poker.PokerTable(
        board=["2H", "4S", "6C", "8D", "TS"],
        player_dict={'Player1': ["3H", "JH"], 'Player2':  ["2D", "4D"]}
    )
    assert table.winner == ["Player2"]


def test_3_beats_high_card():
    table = texas_poker.PokerTable(
        board=["2H", "4S", "6C", "8D", "TS"],
        player_dict={'Player1': ["3H", "JH"], 'Player2':  ["4C", "4D"]}
    )
    assert table.winner == ["Player2"]


def test_straight_beats_high_card():
    table = texas_poker.PokerTable(
        board=["2H", "4S", "6C", "8D", "TS"],
        player_dict={'Player1': ["3H", "5H"], 'Player2':  ["JC", "9D"]}
    )
    assert table.winner == ["Player1"]


def test_flush_beats_high_card():
    table = texas_poker.PokerTable(
        board=["2H", "4S", "6C", "8C", "QC"],
        player_dict={'Player1': ["3H", "AH"], 'Player2':  ["JC", "2C"]}
    )
    assert table.winner == ["Player2"]


def test_full_house_beats_high_card():
    table = texas_poker.PokerTable(
        board=["2H", "2S", "8D", "8C", "QC"],
        player_dict={'Player1': ["3H", "8S"], 'Player2':  ["JC", "3C"]}
    )
    assert table.winner == ["Player1"]


def test_4_beats_high_card():
    table = texas_poker.PokerTable(
        board=["2H", "2S", "8D", "8C", "QC"],
        player_dict={'Player1': ["2D", "2C"], 'Player2':  ["JC", "3C"]}
    )
    assert table.winner == ["Player1"]


def test_straight_flush_beats_high_card():
    table = texas_poker.PokerTable(
        board=["TH", "2C", "3C", "8C", "5C"],
        player_dict={'Player1': ["2D", "9C"], 'Player2':  ["4C", "6C"]}
    )
    assert table.winner == ["Player2"]


def test_royal_flush_beats_high_card():
    table = texas_poker.PokerTable(
        board=["TH", "JH", "9H", "AH", "5C"],
        player_dict={'Player1': ["2D", "3C"], 'Player2':  ["KH", "QH"]}
    )
    assert table.winner == ["Player2"]


def test_one_pair_tiebreaker():
    table = texas_poker.PokerTable(
        board=["7H", "9D", "4C", "2D", "TS"],
        player_dict={'Player1': ["7D", "3D"], 'Player2':  ["9S", "3C"]}
    )
    assert table.winner == ["Player2"]


def test_one_pair_tiebreaker2():
    table = texas_poker.PokerTable(
        board=["KH", "QD", "4C", "2D", "TS"],
        player_dict={'Player1': ["7S", "7H"], 'Player2':  ["7D", "7C"]}
    )
    assert table.winner == ["Player1", "Player2"]


def test_one_pair_tiebreaker3():
    table = texas_poker.PokerTable(
        board=["6H", "2D", "4C", "8D", "TS"],
        player_dict={'Player1': ["4S", "TH"], 'Player2':  ["3D", "TC"]}
    )
    assert table.winner == ["Player1"]


def test_two_pair_beats_one_pair():
    table = texas_poker.PokerTable(
        board=["2H", "4S", "6C", "8D", "TS"],
        player_dict={'Player1': ["3H", "TH"], 'Player2':  ["2D", "4D"]}
    )
    assert table.winner == ["Player2"]


def test_3_beats_one_pair():
    table = texas_poker.PokerTable(
        board=["2H", "4S", "6C", "8D", "TS"],
        player_dict={'Player1': ["8H", "JH"], 'Player2':  ["4C", "4D"]}
    )
    assert table.winner == ["Player2"]


def test_straight_beats_one_pair():
    table = texas_poker.PokerTable(
        board=["2H", "4S", "6C", "8D", "TS"],
        player_dict={'Player1': ["3H", "5H"], 'Player2':  ["TC", "9D"]}
    )
    assert table.winner == ["Player1"]


def test_flush_beats_one_pair():
    table = texas_poker.PokerTable(
        board=["2H", "4S", "6C", "8C", "QC"],
        player_dict={'Player1': ["3H", "QH"], 'Player2':  ["JC", "2C"]}
    )
    assert table.winner == ["Player2"]


def test_full_house_beats_one_pair():
    table = texas_poker.PokerTable(
        board=["2H", "2S", "8D", "7C", "QC"],
        player_dict={'Player1': ["8H", "8S"], 'Player2':  ["JC", "3C"]}
    )
    assert table.winner == ["Player1"]


def test_4_beats_one_pair():
    table = texas_poker.PokerTable(
        board=["2H", "2S", "3D", "8C", "QC"],
        player_dict={'Player1': ["2D", "2C"], 'Player2':  ["JC", "3C"]}
    )
    assert table.winner == ["Player1"]


def test_straight_flush_beats_one_pair():
    table = texas_poker.PokerTable(
        board=["9H", "2C", "3C", "8C", "5C"],
        player_dict={'Player1': ["2D", "9C"], 'Player2':  ["4C", "6C"]}
    )
    assert table.winner == ["Player2"]


def test_royal_flush_beats_one_pair():
    table = texas_poker.PokerTable(
        board=["TH", "JH", "9H", "AH", "5C"],
        player_dict={'Player1': ["2D", "9C"], 'Player2':  ["KH", "QH"]}
    )
    assert table.winner == ["Player2"]


def test_two_pair_tiebreaker():
    table = texas_poker.PokerTable(
        board=["7H", "9C", "4C", "2D", "3S"],
        player_dict={'Player1': ["9D", "3D"], 'Player2':  ["9S", "3C"]}
    )
    assert table.winner == ["Player1", "Player2"]


def test_two_pair_tiebreaker2():
    table = texas_poker.PokerTable(
        board=["3H", "AD", "4C", "2D", "KS"],
        player_dict={'Player1': ["2S", "AH"], 'Player2':  ["3D", "KC"]}
    )
    assert table.winner == ["Player1"]


def test_two_pair_tiebreaker3():
    table = texas_poker.PokerTable(
        board=["KH", "KS", "8C", "6D", "TS"],
        player_dict={'Player1': ["6S", "7C"], 'Player2':  ["8D", "9C"]}
    )
    assert table.winner == ["Player2"]


def test_two_pair_tiebreaker4():
    table = texas_poker.PokerTable(
        board=["KH", "KC", "3S", "3H", "4D"],
        player_dict={'Player1': ["8H", "5D"], 'Player2':  ["7C", "QS"]}
    )
    assert table.winner == ["Player2"]


def test_two_pair_tiebreaker5():
    table = texas_poker.PokerTable(
        board=["9H", "6H", "KC", "7S", "7C"],
        player_dict={'Player1': ["9C", "JH"], 'Player2':  ["QH", "9D"]}
    )
    assert table.winner == ["Player1", "Player2"]


def test_two_pair_tiebreaker6():
    table = texas_poker.PokerTable(
        board=["AH", "AC", "KC", "KS", "QC"],
        player_dict={'Player1': ["9C", "JH"], 'Player2':  ["5H", "9D"]}
    )
    assert table.winner == ["Player1", "Player2"]


def test_3_beats_two_pair():
    table = texas_poker.PokerTable(
        board=["2H", "4S", "6C", "8D", "JS"],
        player_dict={'Player1': ["8H", "JH"], 'Player2':  ["4C", "4D"]}
    )
    assert table.winner == ["Player2"]


def test_straight_beats_two_pair():
    table = texas_poker.PokerTable(
        board=["2H", "4S", "6C", "9C", "TS"],
        player_dict={'Player1': ["3H", "5H"], 'Player2':  ["TC", "9D"]}
    )
    assert table.winner == ["Player1"]


def test_flush_beats_two_pair():
    table = texas_poker.PokerTable(
        board=["3S", "4S", "6C", "8C", "QC"],
        player_dict={'Player1': ["3H", "QH"], 'Player2':  ["JC", "2C"]}
    )
    assert table.winner == ["Player2"]


def test_full_house_beats_two_pair():
    table = texas_poker.PokerTable(
        board=["2H", "2S", "8D", "JD", "3S"],
        player_dict={'Player1': ["8H", "8S"], 'Player2':  ["JC", "3C"]}
    )
    assert table.winner == ["Player1"]


def test_4_beats_two_pair():
    table = texas_poker.PokerTable(
        board=["2H", "2S", "9D", "JD", "3S"],
        player_dict={'Player1': ["2D", "2C"], 'Player2':  ["JC", "3C"]}
    )
    assert table.winner == ["Player1"]


def test_straight_flush_beats_two_pair():
    table = texas_poker.PokerTable(
        board=["9H", "2C", "3C", "8S", "5C"],
        player_dict={'Player1': ["2D", "9C"], 'Player2':  ["4C", "6C"]}
    )
    assert table.winner == ["Player2"]


def test_royal_flush_beats_two_pair():
    table = texas_poker.PokerTable(
        board=["TH", "JH", "9H", "AH", "5C"],
        player_dict={'Player1': ["5D", "9C"], 'Player2':  ["KH", "QH"]}
    )
    assert table.winner == ["Player2"]


def test_3_tiebreaker():
    table = texas_poker.PokerTable(
        board=["7H", "3D", "4C", "2D", "3S"],
        player_dict={'Player1': ["9D", "3H"], 'Player2':  ["9S", "3C"]}
    )
    assert table.winner == ["Player1", "Player2"]


def test_3_tiebreaker2():
    table = texas_poker.PokerTable(
        board=["3H", "AD", "4C", "2D", "KS"],
        player_dict={'Player1': ["AS", "AH"], 'Player2':  ["KD", "KC"]}
    )
    assert table.winner == ["Player1"]


def test_3_tiebreaker3():
    table = texas_poker.PokerTable(
        board=["KC", "AH", "8H", "KS", "KD"],
        player_dict={'Player1': ["7H", "3H"], 'Player2':  ["5H", "9C"]}
    )
    assert table.winner == ["Player2"]


def test_3_tiebreaker4():
    table = texas_poker.PokerTable(
        board=["KC", "AH", "3H", "KS", "KD"],
        player_dict={'Player1': ["QH", "4H"], 'Player2':  ["5H", "QC"]}
    )
    assert table.winner == ["Player1", "Player2"]


def test_straight_beats_3():
    table = texas_poker.PokerTable(
        board=["3H", "8S", "6C", "9C", "7S"],
        player_dict={'Player1': ["3S", "3D"], 'Player2':  ["TC", "9D"]}
    )
    assert table.winner == ["Player2"]


def test_flush_beats_3():
    table = texas_poker.PokerTable(
        board=["3S", "4S", "6D", "8D", "QD"],
        player_dict={'Player1': ["QS", "QH"], 'Player2':  ["JD", "2D"]}
    )
    assert table.winner == ["Player2"]


def test_full_house_beats_3():
    table = texas_poker.PokerTable(
        board=["2H", "2S", "2D", "JD", "3S"],
        player_dict={'Player1': ["8H", "8S"], 'Player2':  ["KC", "AS"]}
    )
    assert table.winner == ["Player1"]


def test_4_beats_3():
    table = texas_poker.PokerTable(
        board=["2H", "2S", "3D", "JD", "3S"],
        player_dict={'Player1': ["2D", "2C"], 'Player2':  ["QC", "3C"]}
    )
    assert table.winner == ["Player1"]


def test_straight_flush_beats_3():
    table = texas_poker.PokerTable(
        board=["9H", "2C", "3C", "8S", "5C"],
        player_dict={'Player1': ["2D", "2S"], 'Player2':  ["4C", "6C"]}
    )
    assert table.winner == ["Player2"]


def test_royal_flush_beats_3():
    table = texas_poker.PokerTable(
        board=["TS", "JS", "9S", "AS", "5C"],
        player_dict={'Player1': ["9D", "9C"], 'Player2':  ["KS", "QS"]}
    )
    assert table.winner == ["Player2"]


def test_straight_tiebreaker():
    table = texas_poker.PokerTable(
        board=["AH", "3D", "4C", "2D", "TS"],
        player_dict={'Player1': ["5D", "3H"], 'Player2':  ["5S", "3C"]}
    )
    assert table.winner == ["Player1", "Player2"]


def test_straight_tiebreaker2():
    table = texas_poker.PokerTable(
        board=["3H", "5D", "4C", "2D", "KS"],
        player_dict={'Player1': ["AS", "AH"], 'Player2':  ["6D", "7C"]}
    )
    assert table.winner == ["Player2"]


def test_flush_beats_straight():
    table = texas_poker.PokerTable(
        board=["3S", "4S", "6D", "8D", "QD"],
        player_dict={'Player1': ["5S", "7H"], 'Player2':  ["JD", "2D"]}
    )
    assert table.winner == ["Player2"]


def test_full_house_beats_straight():
    table = texas_poker.PokerTable(
        board=["2H", "2S", "9D", "JD", "TS"],
        player_dict={'Player1': ["8H", "QS"], 'Player2':  ["JC", "JS"]}
    )
    assert table.winner == ["Player2"]


def test_full_house_beats_straight2():
    table = texas_poker.PokerTable(
        board=["7H", "8S", "8C", "4D", "3S"],
        player_dict={'Player1': ["3C", "8D"], 'Player2':  ["5H", "6H"]}
    )
    assert table.winner == ["Player1"]


def test_4_beats_straight():
    table = texas_poker.PokerTable(
        board=["2H", "2S", "3D", "6D", "3S"],
        player_dict={'Player1': ["2D", "2C"], 'Player2':  ["4C", "5C"]}
    )
    assert table.winner == ["Player1"]


def test_straight_flush_beats_straight():
    table = texas_poker.PokerTable(
        board=["9H", "2C", "3C", "8S", "5C"],
        player_dict={'Player1': ["4D", "6S"], 'Player2':  ["4C", "6C"]}
    )
    assert table.winner == ["Player2"]


def test_royal_flush_beats_straight():
    table = texas_poker.PokerTable(
        board=["TS", "JS", "9S", "AS", "5C"],
        player_dict={'Player1': ["KD", "QD"], 'Player2':  ["KS", "QS"]}
    )
    assert table.winner == ["Player2"]


def test_flush_tiebreaker():
    table = texas_poker.PokerTable(
        board=["AH", "3C", "4C", "AC", "TS"],
        player_dict={'Player1': ["8C", "2C"], 'Player2':  ["9C", "6C"]}
    )
    assert table.winner == ["Player2"]


def test_flush_tiebreaker2():
    table = texas_poker.PokerTable(
        board=["3H", "5H", "TC", "2D", "KH"],
        player_dict={'Player1': ["6H", "AH"], 'Player2':  ["7H", "TH"]}
    )
    assert table.winner == ["Player1"]


def test_full_house_beats_flush():
    table = texas_poker.PokerTable(
        board=["2H", "2D", "9D", "JD", "TS"],
        player_dict={'Player1': ["8D", "AD"], 'Player2':  ["JC", "JS"]}
    )
    assert table.winner == ["Player2"]


def test_4_beats_flush():
    table = texas_poker.PokerTable(
        board=["2H", "2S", "AC", "7C", "3C"],
        player_dict={'Player1': ["2D", "2C"], 'Player2':  ["4C", "5C"]}
    )
    assert table.winner == ["Player1"]


def test_straight_flush_beats_flush():
    table = texas_poker.PokerTable(
        board=["9H", "2C", "3C", "8S", "5C"],
        player_dict={'Player1': ["4D", "QC"], 'Player2':  ["4C", "6C"]}
    )
    assert table.winner == ["Player2"]


def test_royal_flush_beats_flush():
    table = texas_poker.PokerTable(
        board=["TS", "JS", "9S", "AS", "5C"],
        player_dict={'Player1': ["4S", "7S"], 'Player2':  ["KS", "QS"]}
    )
    assert table.winner == ["Player2"]


def test_full_house_tiebreaker():
    table = texas_poker.PokerTable(
        board=["AH", "2C", "2H", "TC", "TS"],
        player_dict={'Player1': ["8C", "2D"], 'Player2':  ["TD", "6C"]}
    )
    assert table.winner == ["Player2"]


def test_full_house_tiebreaker2():
    table = texas_poker.PokerTable(
        board=["7D", "5H", "TC", "TD", "KH"],
        player_dict={'Player1': ["5C", "5S"], 'Player2':  ["7H", "TH"]}
    )
    assert table.winner == ["Player2"]


def test_4_beats_full_house():
    table = texas_poker.PokerTable(
        board=["2H", "2S", "AC", "7C", "3C"],
        player_dict={'Player1': ["2D", "2C"], 'Player2':  ["AD", "AS"]}
    )
    assert table.winner == ["Player1"]


def test_4_beats_full_house2():
    table = texas_poker.PokerTable(
        board=["AH", "AS", "AC", "8D", "TS"],
        player_dict={'Player1': ["7C", "7D"], 'Player2':  ["AD", "7H"]}
    )
    assert table.winner == ["Player2"]


def test_straight_flush_beats_full_house():
    table = texas_poker.PokerTable(
        board=["9H", "2C", "3C", "5C", "9C"],
        player_dict={'Player1': ["9S", "5S"], 'Player2':  ["4C", "6C"]}
    )
    assert table.winner == ["Player2"]


def test_royal_flush_beats_full_house():
    table = texas_poker.PokerTable(
        board=["TS", "JS", "AS", "5D", "5C"],
        player_dict={'Player1': ["5H", "AD"], 'Player2':  ["KS", "QS"]}
    )
    assert table.winner == ["Player2"]


def test_4_tiebreaker():
    table = texas_poker.PokerTable(
        board=["AH", "2C", "2H", "TC", "TS"],
        player_dict={'Player1': ["TD", "TH"], 'Player2':  ["2D", "2S"]}
    )
    assert table.winner == ["Player1"]


def test_4_tiebreaker2():
    table = texas_poker.PokerTable(
        board=["7D", "TS", "TC", "TD", "TH"],
        player_dict={'Player1': ["AC", "5S"], 'Player2':  ["7H", "QH"]}
    )
    assert table.winner == ["Player1"]


def test_straight_flush_beats_4():
    table = texas_poker.PokerTable(
        board=["9H", "2C", "3C", "5C", "5S"],
        player_dict={'Player1': ["5H", "5D"], 'Player2':  ["4C", "6C"]}
    )
    assert table.winner == ["Player2"]


def test_royal_flush_beats_4():
    table = texas_poker.PokerTable(
        board=["TS", "JS", "AS", "5D", "5C"],
        player_dict={'Player1': ["5H", "5S"], 'Player2':  ["KS", "QS"]}
    )
    assert table.winner == ["Player2"]


def test_straight_flush_tiebreaker():
    table = texas_poker.PokerTable(
        board=["6H", "3H", "2H", "4H", "5H"],
        player_dict={'Player1': ["AH", "TH"], 'Player2':  ["7H", "AC"]}
    )
    assert table.winner == ["Player2"]


def test_straight_flush_tiebreaker2():
    table = texas_poker.PokerTable(
        board=["6H", "3H", "7D", "4H", "5H"],
        player_dict={'Player1': ["7H", "TH"], 'Player2':  ["2H", "AC"]}
    )
    assert table.winner == ["Player1"]


def test_royal_flush_beats_straight_flush():
    table = texas_poker.PokerTable(
        board=["TS", "JS", "AS", "QS", "5C"],
        player_dict={'Player1': ["8S", "9S"], 'Player2':  ["KS", "4S"]}
    )
    assert table.winner == ["Player2"]


def test_higher_4_wins():
    table = texas_poker.PokerTable(
        board=["AH", "KS", "KC", "AD", "TS"],
        player_dict={'Player1': ["AC", "AS"], 'Player2':  ["KH", "KD"]}
    )
    assert table.winner == ["Player1"]


def test_higher_4_wins2():
    table = texas_poker.PokerTable(
        board=["8H", "8S", "7C", "7D", "TS"],
        player_dict={'Player1': ["8D", "8C"], 'Player2':  ["7H", "7S"]}
    )
    assert table.winner == ["Player1"]


def test_royal_beats_straight_flush():
    table = texas_poker.PokerTable(
        board=["TS", "KS", "QS", "JS", "9C"],
        player_dict={'Player1': ["AS", "3C"], 'Player2':  ["9S", "3S"]}
    )
    assert table.winner == ["Player1"]


def test_higher_straight_wins():
    table = texas_poker.PokerTable(
        board=["3H", "4S", "5C", "6D", "9C"],
        player_dict={'Player1': ["2S", "QH"], 'Player2':  ["7S", "QC"]}
    )
    assert table.winner == ["Player2"]


def test_straight_tie():
    table = texas_poker.PokerTable(
        board=["3D", "4D", "5D", "6S", "AC"],
        player_dict={'Player1': ["7C", "KH"], 'Player2':  ["7S", "AS"]}
    )
    assert table.winner == ["Player1", "Player2"]


def test_higher_three_in_full_house_wins():
    table = texas_poker.PokerTable(
        board=["AH", "AS", "7C", "7D", "8S"],
        player_dict={'Player1': ["7H", "KH"], 'Player2':  ["6S", "AD"]}
    )
    assert table.winner == ["Player2"]


def test_full_house_tie():
    table = texas_poker.PokerTable(
        board=["5H", "5S", "4C", "8D", "8H"],
        player_dict={'Player1': ["8S", "KH"], 'Player2':  ["8C", "4S"]}
    )
    assert table.winner == ["Player1", "Player2"]


def test_highest_card_in_flush_tie_wins():
    table = texas_poker.PokerTable(
        board=["3H", "5H", "7H", "8H", "TD"],
        player_dict={'Player1': ["2H", "KS"], 'Player2':  ["TH", "8D"]}
    )
    assert table.winner == ["Player2"]


def test_two_pair_tie():
    table = texas_poker.PokerTable(
        board=["8H", "8D", "4C", "3D", "TS"],
        player_dict={'Player1': ["3S", "6D"], 'Player2':  ["3H", "6H"]}
    )
    assert table.winner == ["Player1", "Player2"]


def test_one_pair_tie():
    table = texas_poker.PokerTable(
        board=["8H", "8D", "5C", "4D", "TS"],
        player_dict={'Player1': ["9S", "6H"], 'Player2':  ["9C", "6C"]}
    )
    assert table.winner == ["Player1", "Player2"]


def test_high_card_tie():
    table = texas_poker.PokerTable(
        board=["2H", "4D", "6C", "8D", "TS"],
        player_dict={'Player1': ["AH", "KH"], 'Player2':  ["AS", "KS"]}
    )
    assert table.winner == ["Player1", "Player2"]


def test_ace_as_one_in_straight():
    table = texas_poker.PokerTable(
        board=["AH", "TD", "3C", "4D", "5S"],
        player_dict={'Player1': ["2C", "7D"], 'Player2':  ["7S", "7H"]}
    )
    assert table.winner == ["Player1"]


def test_ace_as_one_straight_flush():
    table = texas_poker.PokerTable(
        board=["AH", "9H", "3H", "4H", "5H"],
        player_dict={'Player1': ["2H", "7D"], 'Player2':  ["7S", "7H"]}
    )
    assert table.winner == ["Player1"]


def test_ace_as_one_straight_flush_loses():
    table = texas_poker.PokerTable(
        board=["AH", "QH", "3H", "4H", "5H"],
        player_dict={'Player1': ["7C", "7D"], 'Player2':  ["2H", "QD"]}
    )
    assert table.winner == ["Player2"]


def test_ace_as_one_straight_loses():
    table = texas_poker.PokerTable(
        board=["AD", "8C", "3H", "4C", "5H"],
        player_dict={'Player1': ["QD", "QH"], 'Player2':  ["9H", "2D"]}
    )
    assert table.winner == ["Player2"]


def test_community_full_house():
    table = texas_poker.PokerTable(
        board=["KH", "KC", "3S", "3H", "3D"],
        player_dict={'Player1': ["8H", "AH"], 'Player2':  ["7C", "KS"]}
    )
    assert table.winner == ["Player2"]


def test_community_4_tiebreaker():
    table = texas_poker.PokerTable(
        board=["KD", "KC", "KS", "KH", "4D"],
        player_dict={'Player1': ["8H", "5D"], 'Player2':  ["9H", "5C"]}
    )
    assert table.winner == ["Player2"]


def test_community_4_tiebreaker2():
    table = texas_poker.PokerTable(
        board=["KD", "KC", "KS", "KH", "AD"],
        player_dict={'Player1': ["8H", "5D"], 'Player2':  ["9H", "5C"]}
    )
    assert table.winner == ["Player1", "Player2"]


def test_community_4_tiebreaker3():
    table = texas_poker.PokerTable(
        board=["KD", "KC", "KS", "KH", "4D"],
        player_dict={'Player1': ["8H", "5D"], 'Player2':  ["9H", "5C"]}
    )
    assert table.winner == ["Player2"]


def test_two_royal_flushes_is_tie():
    table = texas_poker.PokerTable(
        board=["KD", "AD", "QD", "JD", "TD"],
        player_dict={'Player1': ["4H", "5D"], 'Player2':  ["JH", "5S"]}
    )
    assert table.winner == ["Player1", "Player2"]


def test_straight_flush_tie():
    table = texas_poker.PokerTable(
        board=["QD", "JD", "TD", "9D", "8D"],
        player_dict={'Player1': ["4H", "5D"], 'Player2':  ["JH", "5S"]}
    )
    assert table.winner == ["Player1", "Player2"]