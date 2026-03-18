# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
I think the hints are backwards
Doesn't let you start entering answers after ending a game
The main screen, range, doesnt change when you change the difficulty
The attemps allowed are wrong on the display
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

#1 What the AI suggested: Copilot Agent Mode refactored the check_guess function into logic_utils.py and flipped the comparison operators.

Was it correct? Yes, it fixed the backwards hints. However, I had to fix a ModuleNotFoundError during testing by setting the PYTHONPATH.

Verification: I verified the fix by running pytest. A guess of 70 against a secret of 50 now correctly returns "Too High."

#2What the AI suggested: Copilot suggested moving the range calculation logic to ensure it triggers a rerun of the st.info component when the sidebar changes.

Was it correct? Yes, it fixed the visual desync. It also correctly pointed out that I should reset the secret number if the range changes mid-game.

Verification: I manually tested the dropdown in the browser and saw the text change from "1 to 20" to "1 to 100" instantly.

#3What the AI suggested: Copilot suggested using a centralized attempt_limit variable and identified that the subtraction logic in the st.info box was using an outdated variable.

Was it correct? Yes, it fixed the "off-by-one" error where the game would end but the UI still said "1 attempt left."

Verification: I ran pytest and manually played an "Easy" game, counting 6 clicks before the "Out of attempts!" message appeared.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
