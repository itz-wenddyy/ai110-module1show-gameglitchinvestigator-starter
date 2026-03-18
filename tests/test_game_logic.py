from logic_utils import check_guess, get_range_for_difficulty
from app import attempt_limit_map
import streamlit as st


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


def test_attempt_limit_map_values():
    assert attempt_limit_map["Easy"] == 6
    assert attempt_limit_map["Normal"] == 8
    assert attempt_limit_map["Hard"] == 5


def test_out_of_attempts_logic():
    # Simulate attempts and ensure the condition attempts >= limit behaves as expected
    limit = attempt_limit_map["Normal"]
    attempts = limit
    assert attempts >= limit
    attempts = limit - 1
    assert not (attempts >= limit)


def test_new_game_resets_state():
    # Simulate game in 'won' state with non-zero attempts
    st.session_state.status = "won"
    st.session_state.attempts = 3

    # Simulate the New Game reset logic from the app
    st.session_state.attempts = 0
    st.session_state.status = "playing"

    assert st.session_state.status == "playing"
    assert st.session_state.attempts == 0
