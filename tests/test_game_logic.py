from logic_utils import check_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result, _ = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result, _ = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result, _ = check_guess(40, 50)
    assert result == "Too Low"

def test_update_score_win():
    # Test scoring logic on a win: 100 - 10 * (attempt_number + 1)
    # Attempt 1 -> 100 - 10*(2) = 80
    new_score = update_score(0, "Win", 1)
    assert new_score == 80

def test_update_score_loss():
    # Test scoring logic on a wrong guess (subtracts 5)
    new_score = update_score(100, "Too High", 2)
    assert new_score == 95
