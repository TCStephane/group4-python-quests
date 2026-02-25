Learn Python by Coding
The goal of these quests is to build your foundation in programming. Ensure to have Python present on your system via the terminal with command python --version or python3 --version

How to Submit Your Work
Deliverable 1: For each quest, each group member must write a Python script, then push it to the GitHub repository of the group. Attempt at least 4 Tasks from each of the 6 Levels

Example of the Directory/GitHub structure:
group{nbr}-python-quests/
├── quests/
│   ├── quest_01_first_spell.py
│   ├── quest_02_naming_ceremony.py
│   ├── quest_03_treasure_chest.py
│   ├── ... (and so on for all 30 quests)
│   └── quest_30_reflective_scribe.py
│
└── README.md
Deliverable 2: Each group has been assigned two Peer Groups to review. Ensure to provide effective feedback on the attempted questions.
Level 1: The Magic of Words and Numbers (Variables & Printing)
Quest 1: Your First Spell
Concept: print() - The command to make the computer talk.
How to use it: print("Your message here")
Why it's important: This is your window into the program's mind. It lets you see what's happening, display results, and check for mistakes.
Logical Reasoning: If I want to see something on the screen, I need to explicitly tell the computer to print it.
The Quest: Write a Python script that prints out a cool welcome message for a fellow adventurer.
Quest 2: The Naming Ceremony
Concept: Variables - These are like labeled boxes where you can store information.
How to use it: variable_name = "some value"
Why it's important: Variables give names to data so you can remember and reuse it easily.
Logical Reasoning: If I need to remember a piece of information for later, I should store it in a variable with a memorable name.
The Quest: Create variables for a hero's name and their superpower. Print a sentence that introduces the hero and their power.
Quest 3: The Treasure Chest
Concept: Data Types - Python treats text (string) and numbers (integer, float) differently.
How to use it: name = "Gandalf", level = 20
Why it's important: Knowing the type of data is crucial. You can do math with numbers, but not with text.
Logical Reasoning: I must use quotes for text to tell Python it's a string.
The Quest: Create variables for your age (an integer) and favorite food (a string). Print them in a single sentence.
Quest 4: The Town Crier
Concept: Combining variables and strings for output.
How to use it: print("Hello, " + hero_name) or f-strings: print(f"Hello, {hero_name}")
Why it's important: You'll almost always be displaying information stored in your variables.
Logical Reasoning: To create a dynamic message, I need to combine my fixed text with the values stored in my variables.
The Quest: Create variables for a city name, the current year, and your name. Print a message like: "Welcome to [City Name]! The year is [Year], and our newest resident is [Your Name]."
Quest 5: The Echoing Cave
Concept: Reassigning Variables - The value in a variable's "box" can be changed.
How to use it: player_score = 100; player_score = 150
Why it's important: Data changes! A player's score goes up, a character's location changes, time passes. Variables need to be updatable.
Logical Reasoning: The = sign is an assignment, not a permanent declaration of equality.
The Quest: Create a player_health variable and set it to 100. A monster attacks! Subtract 25. The player finds a potion! Add 10. Print the final health.
Level 2: A Dialogue with the Machine (User Input & Basic Math)
Quest 6: The Fortune Teller
Concept: input() - How to ask the user a question and get their answer.
How to use it: user_answer = input("What is your name? ")
Why it's important: This makes your programs interactive!
Logical Reasoning: If I want the user to give me information, I need to use input() to pause the program and wait for their typed response.
The Quest: Ask the user for their name and quest, then print a confirmation message.
Quest 7: The Magic Number Converter
Concept: Type Conversion - Changing data from one type to another.
How to use it: number = int(input("Enter a number: "))
Why it's important: The input() function always gives you a string. If you want to do math, you must convert it to a number.
Logical Reasoning: A computer sees "5" from an input as a word. I must tell it to reinterpret that word as a number before I can do math with it.
The Quest: Ask the user for their birth year, convert it to an integer, and calculate their approximate age.
Quest 8: The Potion Brewer
Concept: Basic Arithmetic Operators (+, -, *, /).
How to use it: result = 10 * 5
Why it's important: This is the foundation of all calculation in programming.
Logical Reasoning: I can use math symbols directly in my code to perform calculations on numbers.
The Quest: You need 3 dragon scales (10 gold each) and 5 elf tears (3 gold each). Calculate the total cost.
Quest 9: The Greedy Goblin
Concept: The Modulo Operator (%) - This gives you the remainder of a division.
How to use it: leftover = 10 % 3 (Result is 1).
Why it's important: It's great for checking if a number is even or odd, and for distributing items evenly.
Logical Reasoning: When I divide A by B, what is left over? The modulo operator tells me just that.
The Quest: A goblin has 27 gold pieces to share among 4 friends. Calculate how many pieces each friend gets and how many the goblin keeps (the remainder).
Quest 10: The Architect's Blueprint
Concept: Floating-Point Numbers (float) - Numbers with decimal points.
How to use it: price = 9.99
Why it's important: Not all math involves whole numbers. Measurements and money often require decimals.
Logical Reasoning: If my calculation might result in a fraction, I should use float to ensure the decimal part isn't lost.
The Quest: Calculate the area of a rectangle. Ask the user for the length and width (they can be decimals) and print the area.
Level 3: The Crossroads of Logic (Conditional Statements)
Quest 11: The Guardian of the Bridge
Concept: if statement - This lets your program make a decision.
How to use it: if age > 18: print("You may pass.")
Why it's important: This is how programs become "smart." They can react differently to different situations.
Logical Reasoning: If a specific condition is met, then execute the following code.
The Quest: Ask for the user's age. If it's 18 or greater, print a message that they are old enough to vote.
Quest 12: The Two-Path Cave
Concept: if-else statement - This provides an alternative path.
How to use it: if choice == "left": print("Treasure!") else: print("Pit!")
Why it's important: It handles all possibilities, providing a default action if the condition isn't met.
Logical Reasoning: If this is true, do action A. For all other cases, do action B.
The Quest: Create a password checker. If the user enters the correct password, print "Access Granted," otherwise print "Access Denied."
Quest 13: The Maze of Many Choices
Concept: if-elif-else statement - This lets you check multiple different conditions in a row.
Why it's important: It allows for complex decision-making with more than two options.
Logical Reasoning: If A is true, do this. Else, if B is true, do that. If none are true, do the final `else` action.
The Quest: Write a grading program. Ask for a score (0-100). Print "A" for 90+, "B" for 80-89, "C" for 70-79, and "Needs Improvement" otherwise.
Quest 14: The Logical Gatekeeper
Concept: Logical Operators (and, or, not) - These let you combine multiple conditions.
Why it's important: Real-world decisions often depend on more than one factor.
Logical Reasoning: To enter the castle, you must have a key AND know the password.
The Quest: A club bouncer requires guests to be 18+ AND have 20+ gold coins. Ask the user for their age and gold, and tell them if they can enter.
Quest 15: The Nested Riddle
Concept: Nested if Statements - An if statement inside another.
Why it's important: It allows for a second layer of decision-making after a first condition is met.
Logical Reasoning: First, check if the user has a key. If they do, THEN check if it's the right color.
The Quest: Mini-adventure. Ask if they go "left" or "right". If "left", ask if they "swim" or "wait". If they swim, they find a treasure. All other choices lead to a different outcome.
Level 4: The Power of Repetition (Loops)
Quest 16: The Marching Ants
Concept: for loop - Repeats code a specific number of times.
How to use it: for i in range(5): print("Hello")
Why it's important: It automates repetitive tasks.
Logical Reasoning: For every item in this sequence, perform this action.
The Quest: Use a for loop to print the numbers from 1 to 10.
Quest 17: The Endless Staircase
Concept: while loop - Repeats code as long as a condition is true.
Why it's important: Perfect for when you don't know how many repetitions you need.
Logical Reasoning: While this condition is true, keep executing this block of code.
The Quest: Start a counter at 0. Use a while loop that stops when the count reaches 5.
Quest 18: The Loop of Riddles
Concept: Using a while loop with a user-input condition.
Why it's important: It's the basis for games, user menus, and data processing.
Logical Reasoning: I will keep repeating this action until the user provides the correct input to stop the loop.
The Quest: Write a guessing game. Think of a secret number. Use a while loop to keep asking the user to guess until they get it right.
Quest 19: The Countdown
Concept: The range() function with three arguments: range(start, stop, step).
Why it's important: It gives you more control over your for loops.
Logical Reasoning: range() lets me define my own start, end, and step size.
The Quest: Simulate a rocket launch. Use a for loop with range() to count down from 10 to 1, then print "Blastoff!".
Quest 20: The Even Number Forager
Concept: Using if inside a for loop.
Why it's important: This lets you process items in a sequence and make a decision about each one.
Logical Reasoning: For each number in this range, check if it meets my condition. If it does, perform an action.
The Quest: Loop through numbers 1 to 20. Use an if statement to check if the number is even. If it is, print it.
Level 5: The Alchemist's Lab (Functions)
Quest 21: The Reusable Incantation
Concept: Defining a function with def.
Why it's important: Functions let you package up code you want to reuse. This is the "Don't Repeat Yourself" (DRY) principle.
Logical Reasoning: Instead of copying and pasting code, I'll put it in a function and "call" it by name.
The Quest: Create a function greet_adventurer() that prints a welcome message. Call it three times.
Quest 22: The Personalized Scroll
Concept: Functions with parameters (arguments).
Why it's important: This makes functions flexible. They can act on the specific data you give them.
Logical Reasoning: My function needs information to do its job. I'll define "parameters" as placeholders for that information.
The Quest: Create a function personalized_greeting(name, quest). Ask the user for their name and quest, then call your function with their answers.
Quest 23: The Oracle's Vision
Concept: Functions that return a value.
Why it's important: Many functions are designed to perform a calculation and give back the result.
Logical Reasoning: This function's job is to compute a value. After it's done, it should return the final answer.
The Quest: Write a function calculate_area(length, width) that returns the area. Call it for two different rectangles and print the results.
Quest 24: The Master Spell
Concept: Calling a function from within another function.
Why it's important: This is how you build complex programs from simple, reusable parts.
Logical Reasoning: I can break a big problem down into smaller tasks. Each task becomes a function.
The Quest: Create ask_for_age() which returns an age, and can_they_vote(age) which prints a message. Call the first, then pass its result to the second.
Level 6: The Grand Challenge
Quest 25: The Number Wizard
The Quest: Upgrade your number guessing game. After each wrong guess, tell the user if their guess was "too high" or "too low".

Quest 26: The Simple Calculator
The Quest: Write a program that acts as a simple calculator. Ask for two numbers and an operation (`add`, `subtract`, etc.). Use functions for each operation and an `if-elif-else` chain to call the correct one.

Quest 27: The FizzBuzz Test
The Quest: A classic challenge. Print numbers from 1 to 100. For multiples of 3, print "Fizz". For multiples of 5, print "Buzz". For multiples of both, print "FizzBuzz".

Quest 28: The Adventure Begins
The Quest: Create a text-based "Choose Your Own Adventure" game. Use functions for different locations and have at least two different endings.

Quest 29: The Code Breaker
The Task: Translate the following human logic into a Python script: Allow a user 3 attempts to guess the secret code (`42`). Give feedback on each guess and stop the game on a correct guess or after 3 failed attempts.

Quest 30: The Reflective Scribe
The Quest: Go back to three of your previous assignments and add comments (# like this) to explain what each part of your code does and why.
