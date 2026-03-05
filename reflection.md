# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

When I first ran it the game looked like a standard streamlit app with a sidebar and a main section. I noticed a few obvious bugs right away. The main text always tells you to guess a number between 1 and 100 even if you change the difficulty. Also if you finish a game and press the new game button it resets your attempts but does not let you submit any new guesses so you have to refresh the page to play again. The hints are also backwards and tell you to go higher when your guess was too high.

---

## 2. How did you use AI as a teammate?

I basically just used copilot inline chat to fix the file and occasionally checked chat.
Copilot got the fix right for the new game button freezing by telling me to reset the other session variables and use the low/high vars instead of 1 and 100. I tested it and it worked without me refreshing the page.
An incorrect suggestion was when I asked copilot agent to fix the hint logic and instead of just swapping the string text it tried to add a bunch of weird logic to make it print the strings conditionally. I just discarded it and changed the strings manually.

---

## 3. Debugging and testing your fixes

I knew my stuff was fixed when I just played the game and saw the bugs I found were gone. 
I ran pytest tests/test_game_logic.py after copilot fixed the check guess test. It basically showed that putting in 60 on a 50 secret gave "Too High" which proved that the hint reversed bug was gone. 
AI didn't really help design the tests I just told it to fix the starter code tests which were broken because they were made to check strings but the function returns a tuple.

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
