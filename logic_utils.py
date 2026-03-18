import random

def get_range_for_difficulty(difficulty: str):
    """Returns the (low, high) range based on the selected difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        # FIX: Hard mode was 1-50 (too easy). Changed to 1-500.
        return 1, 500
    return 1, 100

def check_guess(guess, secret):
    """
    FIX: Corrected inverted logic. 
    If guess is 10 and secret is 50, guess < secret, so we must go HIGHER.
    """
    if guess == secret:
        return "Win", "🎉 Correct!"
    if guess < secret:
        return "Too Low", "📈 Go HIGHER!"
    if guess > secret:
        return "Too High", "📉 Go LOWER!"

def update_score(current_score: int, outcome: str, attempt_number: int):
    """Updates the player's score based on the outcome of their guess."""
    if outcome == "Win":
        # Award points based on speed
        points = max(10, 100 - 10 * attempt_number)
        current_score += points
    elif outcome in ("Too High", "Too Low"):
        # FIX: Removed the bug that gave points for wrong guesses on even turns
        current_score -= 5
    
    return max(0, current_score)