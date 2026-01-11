# Day 12 – Number Guessing Game
# Part of my 100 Days of Code journey
#
# Learning goals for this project:
# - Using random number generation
# - Implementing difficulty levels
# - Managing attempts and game state
# - Using conditionals to give feedback
# - Controlling loops based on win/lose conditions
#
# This project simulates a number guessing game
# where the user must guess a randomly chosen number.

from art import logo
import random

# Display game logo and intro message
print(logo)
print("Welcome to the Number Guessing Game!\n"
      "I'm thinking of a number between 1 and 100.")

# Randomly select a number between 1 and 100
number = random.randint(1, 100)

# Debug output to help during development
print(f"PSST! The number is {number}")

# Ask user to choose difficulty
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

# Set number of attempts based on difficulty
if difficulty == "easy":
    attempts = 10
else:
    attempts = 5

# Main game loop
game_on = True
while game_on:
    # End game if no attempts remain
    if attempts == 0:
        game_on = False
        print("You've run out of guesses. Refresh the page to run again.")

    print(f"You have {attempts} remaining to guess the number.")
    guess = int(input("Make a guess: "))

    # Compare guess with the correct number
    if guess < number:
        print("Too low.\nGuess again.")
        attempts -= 1
    elif guess > number:
        print("Too high.\nGuess again.")
        attempts -= 1
    else:
        print(f"You got it! The answer was {number}.")
        game_on = False
