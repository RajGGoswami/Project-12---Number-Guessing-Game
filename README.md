# Project-12---Number-Guessing-Game

This is a beginner Python project built as part of my 100 Days of Code challenge.

The goal of this project is to build a number guessing game where the user must identify a randomly chosen number within a limited number of attempts.

**Project Overview**

The Number Guessing Game allows the user to:

Choose a difficulty level

Guess a number between 1 and 100

Receive feedback after each guess

Win by guessing the correct number

Lose if all attempts are used

Difficulty levels:

Easy = 10 attempts

Hard = 5 attempts

**Project File Structure**

main.py
Contains the game logic, difficulty selection, and user interaction.

art.py
Stores the ASCII art logo displayed at game start.

**Why this project exists**

This project helped reinforce control flow logic and showed how small changes (difficulty levels) can significantly affect gameplay.

It also helped me understand how to build repeatable game loops with clear win and lose conditions.

**What I learned**

How to generate random numbers using random.randint()

How to implement difficulty-based logic

How to track remaining attempts

How to provide meaningful user feedback

How to control program flow with while loops

How to end a game cleanly

**How the code works (step-by-step)**

Display the game logo and instructions

Generate a random number between 1 and 100

Ask the user to choose a difficulty level

Assign attempts based on difficulty

Prompt the user to guess the number

Compare the guess with the correct number

Reduce attempts after each incorrect guess

End the game when the number is guessed or attempts run out

**Example Output**

Welcome to the Number Guessing Game!

I'm thinking of a number between 1 and 100.

Choose a difficulty. Type 'easy' or 'hard':
easy

You have 10 remaining to guess the number.

Make a guess:
50

Too high.
Guess again.

You have 9 remaining to guess the number.

Make a guess:
32

You got it! The answer was 32.
