from logic_utils import check_guess, get_range_for_difficulty


def test_guess_too_high():
    outcome, _ = check_guess(70, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    outcome, _ = check_guess(30, 50)
    assert outcome == "Too Low"


def test_guess_win():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"


def test_get_range_for_difficulty():
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 100)
    assert get_range_for_difficulty("Hard") == (1, 50)
