# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
import hangman_stages

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter.lower() in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

word_list = ["INTERNET", "COMPUTER", "SOFTWARE", "DATABASE", "INFORMATION"]
choose_word = random.choice(word_list)
print(choose_word)
display = []


# Initialize the number of lives
lives = 6
guessed_letters = []

# Guessing the correct letter
game_over = False

while not game_over:
    guessed_letter = input("Guess a letter: ").lower()
    
    if guessed_letter in guessed_letters:
        print("You have already guessed this letter.")
        continue
    
    guessed_letters.append(guessed_letter)
    
    letter_guessed = False  # Flag to check if the letter was guessed
    for position in range(len(choose_word)):
        letter = choose_word[position].lower()
        if letter == guessed_letter:
            display[position] = choose_word[position]  # Fix the variable name here
            letter_guessed = True  # Set the flag to True
    print(display)

    if not letter_guessed:  # Check if the letter was not guessed
        lives -= 1
        if lives == 0:
            game_over = True
            print("Sorry, you lost the game !!!")
        if '_' not in display:
            game_over = True
            print("WOW, you won the game !!!")
        print(hangman_stages.stages[lives])
