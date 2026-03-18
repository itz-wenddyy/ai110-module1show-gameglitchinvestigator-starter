import random
import streamlit as st

# --- LOGIC FUNCTIONS ---
# These are kept inside app.py so we don't get ImportError

def get_range_for_difficulty(difficulty: str):
    """Returns the (low, high) range based on the selected difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        # FIX: Hard mode was 1-50. Changed to 1-500.
        return 1, 500
    return 1, 100

def parse_guess(raw: str):
    """Attempts to parse the raw string input into an integer."""
    if not raw or raw.strip() == "":
        return False, None, "Enter a guess."
    try:
        value = int(float(raw))
        return True, value, None
    except Exception:
        return False, None, "That is not a number."

def check_guess(guess, secret):
    """
    FIX: Corrected inverted logic. 
    If guess < secret, we must go HIGHER.
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
        points = max(10, 100 - 10 * attempt_number)
        current_score += points
    elif outcome in ("Too High", "Too Low"):
        # FIX: Removed the "Free Points" bug
        current_score -= 5
    return max(0, current_score)

# --- UI CONFIGURATION & STATE ---

st.set_page_config(page_title="Glitchy Guesser", page_icon="🎮")
st.title("🎮 Game Glitch Investigator")
st.caption("An AI-generated guessing game. Something is off.")

st.sidebar.header("Settings")
# Added unique key to solve the DuplicateElementId error
difficulty = st.sidebar.selectbox(
    "Difficulty", ["Easy", "Normal", "Hard"], 
    index=1, 
    key="difficulty_selector_final"
)

attempt_limit_map = {"Easy": 6, "Normal": 8, "Hard": 5}
attempt_limit = attempt_limit_map[difficulty]
low, high = get_range_for_difficulty(difficulty)

def initialize_game(low_val, high_val):
    """Initialize or reset the game session state."""
    st.session_state.attempts = 0
    st.session_state.secret = random.randint(low_val, high_val)
    st.session_state.status = "playing"
    st.session_state.history = []
    st.session_state.score = 0
    st.session_state.last_hint = ""
    st.session_state.last_difficulty = difficulty
    if "game_counter" not in st.session_state:
        st.session_state.game_counter = 0

if "secret" not in st.session_state or st.session_state.get("last_difficulty") != difficulty:
    initialize_game(low, high)

# --- UI ELEMENTS ---

attempts_left = max(0, attempt_limit - st.session_state.attempts)

# Developer Debug Info
with st.expander("Developer Debug Info", expanded=True):
    st.write("Secret:", st.session_state.get("secret"))
    st.write("Attempts:", st.session_state.get("attempts"))
    st.write("Score:", st.session_state.get("score"))
    st.write("Status:", st.session_state.get("status"))
    st.write("History:", st.session_state.get("history"))

# --- ONE-CLICK FORM FIX ---
# Wrapping in a form ensures the guess registers on the first click
with st.form(key=f"guess_form_{st.session_state.game_counter}"):
    raw_guess = st.text_input("Enter your guess:")
    submit = st.form_submit_button("Submit Guess 🚀", disabled=(st.session_state.status != "playing"))

    if submit:
        ok, guess_int, err = parse_guess(raw_guess)
        if not ok:
            st.error(err)
        else:
            st.session_state.attempts += 1
            st.session_state.history.append(guess_int)
            
            outcome, message = check_guess(guess_int, st.session_state.secret)
            st.session_state.last_hint = message
            st.session_state.score = update_score(st.session_state.score, outcome, st.session_state.attempts)
            
            if outcome == "Win":
                st.session_state.status = "won"
            elif st.session_state.attempts >= attempt_limit:
                st.session_state.status = "lost"
            
            st.rerun()

col1, col2 = st.columns(2)
with col1:
    if st.button("New Game 🔁"):
        st.session_state.game_counter += 1
        initialize_game(low, high)
        st.rerun()
with col2:
    show_hint = st.checkbox("Show hint", value=True)

# --- FEEDBACK DISPLAY ---

if st.session_state.status != "playing":
    if st.session_state.status == "won":
        st.balloons()
        st.success("You already won! Start a new game to play again.")
    else:
        st.error(f"Game over. The secret was {st.session_state.secret}.")

if show_hint and st.session_state.get("last_hint"):
    st.warning(st.session_state.last_hint)

st.info(f"Guess a number between {low} and {high}. Attempts left: {attempts_left}")

st.divider()
st.caption("Built by an AI that claims this code is production-ready.")