from pathlib import Path
import sys

import pytest

sys.path.append(str(Path(__file__).resolve().parents[1]))

from logic_utils import (
    check_guess,
    get_attempt_limit_for_difficulty,
    get_range_for_difficulty,
    parse_guess,
    update_score,
    validate_guess_range,
)


def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"


def test_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"


def test_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"


@pytest.mark.parametrize(
    "difficulty, expected",
    [
        ("Easy", (1, 20)),
        ("Normal", (1, 50)),
        ("Hard", (1, 100)),
        ("Impossible", (1, 100)),
    ],
)
def test_get_range_for_difficulty(difficulty, expected):
    assert get_range_for_difficulty(difficulty) == expected


def test_parse_guess_empty_input():
    ok, value, err = parse_guess("")
    assert ok is False
    assert value is None
    assert err == "Enter a guess."


def test_parse_guess_none_input():
    ok, value, err = parse_guess(None)
    assert ok is False
    assert value is None
    assert err == "Enter a guess."


def test_parse_guess_invalid_text():
    ok, value, err = parse_guess("abc")
    assert ok is False
    assert value is None
    assert err == "That is not a number."


@pytest.mark.parametrize("raw", [42, [], {}, 3.14])
def test_parse_guess_non_string_input_is_rejected(raw):
    ok, value, err = parse_guess(raw)
    assert ok is False
    assert value is None
    assert err == "That is not a number."


def test_parse_guess_decimal_string_is_rejected():
    ok, value, err = parse_guess("12.9")
    assert ok is False
    assert value is None
    assert err == "That is not a number."


def test_parse_guess_negative_decimal_is_rejected():
    ok, value, err = parse_guess("-12.9")
    assert ok is False
    assert value is None
    assert err == "That is not a number."


def test_parse_guess_whitespace_integer_parses():
    ok, value, err = parse_guess("   42   ")
    assert ok is True
    assert value == 42
    assert err is None


def test_parse_guess_scientific_notation_is_rejected():
    ok, value, err = parse_guess("1e2")
    assert ok is False
    assert value is None
    assert err == "That is not a number."


@pytest.mark.parametrize(
    "guess, low, high, expected_ok, expected_err",
    [
        (1, 1, 20, True, None),
        (20, 1, 20, True, None),
        (0, 1, 20, False, "Guess must be between 1 and 20."),
        (21, 1, 20, False, "Guess must be between 1 and 20."),
    ],
)
def test_validate_guess_range(guess, low, high, expected_ok, expected_err):
    ok, err = validate_guess_range(guess, low, high)
    assert ok is expected_ok
    assert err == expected_err


@pytest.mark.parametrize(
    "guess, low, high",
    [
        (10, None, 20),
        (10, 1, None),
        (10, "1", 20),
        (10, 20, 1),
    ],
)
def test_validate_guess_range_invalid_bounds(guess, low, high):
    ok, err = validate_guess_range(guess, low, high)
    assert ok is False
    assert err == "Game range is invalid."


@pytest.mark.parametrize(
    "difficulty, expected",
    [
        ("Easy", 6),
        ("Normal", 8),
        ("Hard", 5),
        ("Impossible", 5),
    ],
)
def test_get_attempt_limit_for_difficulty(difficulty, expected):
    assert get_attempt_limit_for_difficulty(difficulty) == expected


def test_update_score_win_has_minimum_points_floor():
    assert update_score(current_score=0, outcome="Win", attempt_number=20) == 10


def test_update_score_too_high_even_attempt_adds_points():
    assert update_score(current_score=50, outcome="Too High", attempt_number=2) == 55


def test_update_score_too_high_odd_attempt_subtracts_points():
    assert update_score(current_score=50, outcome="Too High", attempt_number=3) == 45


def test_update_score_too_low_subtracts_points():
    assert update_score(current_score=50, outcome="Too Low", attempt_number=1) == 45


def test_update_score_win_first_attempt_awards_90_points():
    assert update_score(current_score=0, outcome="Win", attempt_number=0) == 90


def test_update_score_unknown_outcome_keeps_score_unchanged():
    assert update_score(current_score=50, outcome="Unknown", attempt_number=1) == 50
