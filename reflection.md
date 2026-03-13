# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

    - nothing outstanding
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
    - history doesn't clear, new game button doesn't work
    - hints were backwards
    - attempts start at 1 unless you click new game
    - in hard mode, when you enter a number it refreshes back to normal mode
    - you can go lower than 0 attempts
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
    - Copilot
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  - It fixed the session state, when the game difficulty is changed, the session is resetted so it doesn't remember the previous tries.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  - It fixed something but it broke the hint system, the toggle just wouldn't appear anymore.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  - I tested the features by myself, I went in and played the game.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  - I tried to change mode and see if the game state was reset, it didn't. I had Copilot fix it. 
- Did AI help you design or understand any tests? How?
  - I used AI to create pytest unit test for the features.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - For every function that is created, we need a testcase for it, whether it's pytest for backend logic, or playwright for frontend.

- What is one thing you would do differently next time you work with AI on a coding task?
  - I will tell AI to critique the codebase, then go through the parts that it noted and see what's wrong with it. Then I can start debugging. That would make my process faster instead of reading the code line by line. 
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  - It's not reliable, we need a human in the loop system. And we need to understand what AI wrote for us. 
