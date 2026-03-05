# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

When I first ran it the game looked like a standard streamlit app with a sidebar and a main section. I noticed a few obvious bugs right away. The main text always tells you to guess a number between 1 and 100 even if you change the difficulty. Also if you finish a game and press the new game button it resets your attempts but does not let you submit any new guesses so you have to refresh the page to play again. The hints are also backwards and tell you to go higher when your guess was too high.

---

## 2. How did you use AI as a teammate?

I used my gemini ai account since it is free for students and basically unlimited.
Gemini got the fix right for the new game button freezing by telling me to reset the other session variables and use the low/high vars instead of 1 and 100. I tested it and it worked without me refreshing the page.
An incorrect suggestion was when I asked gemini to fix the hint logic and instead of just swapping the string text it tried to add a bunch of weird logic to make it print the strings conditionally. I just discarded it and changed the strings manually.

---

## 3. Debugging and testing your fixes

I knew my stuff was fixed when I just played the game and saw the bugs I found were gone. 
I ran pytest tests/test_game_logic.py after gemini fixed the check guess test. It basically showed that putting in 60 on a 50 secret gave "Too High" which proved that the hint reversed bug was gone. 
AI didn't really help design the tests I just told it to fix the starter code tests which were broken.

---

## 4. What did you learn about Streamlit and state?

The secret number kept getting messed up because it was converting back and forth between strings and ints on even attempts which broke all the logic. Streamlit basically reruns the whole python script every single time you click a button or type something so if you don't use session state variables your stuff just resets every time. I just removed the weird even attempt string conversion and made sure the new game button actually resets the status state to playing so it doesn't stay frozen.

---

## 5. Looking ahead: your developer habits

I'll probably use gemini inline chat more since it's faster than opening a new tab and typing it all out. Next time I'll make sure to double check the code the AI gives me since it can be pretty dumb sometimes and try to overcomplicate things. It showed me that AI code is a good starting point but you still have to verify it yourself because it makes obvious mistakes.
