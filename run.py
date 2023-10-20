# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
import hangman_stages

word_list = ["INTERNET", "COMPUTER", "SOFTWARE", "DATABASE", "INFORMATION"]
choose_word = random.choice(word_list)
print(choose_word)
display = []

# Display the number of blanks related to the word selected
for letter in choose_word:
    display += '_'
print(display)

# Initialize the number of lives
lives = 6

# Guessing the correct letter
game_over = False

while not game_over:
    guessed_letter = input("Guess a letter: ").lower()
    for position in range(len(choose_word)):
        letter = choose_word[position].lower()
        if letter == guessed_letter:
            display[position] = choose_word[position]  # Fix the variable name here
    print(display)

    if guessed_letter not in choose_word.lower():
        lives -= 1
        if lives == 0:
            game_over = True
            print("Sorry, you lost the game !!!")
        if '_' not in display:
            game_over = True
            print("WOW, you won the game !!!")