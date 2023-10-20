# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
import hangman_stages

# Function to display the word with the guessed letters
def display_word(word, guessed_letters):
    display = " "
    for letter in word:
        if letter.lower() in guessed_letters:
            display += letter
        elif letter.isalpha():
            display += ' _ '
        else:
            display += letter
    return display

# Function to play the Hangman game
def play_hangman():
    word_list = ["INTERNET", "COMPUTER", "SOFTWARE", "DATABASE", "INFORMATION"]
    choose_word = random.choice(word_list)
    guessed_letters = []
    lives = len(hangman_stages.stages) - 1 #number of lives the player has
    score = 0

    print("Welcome to Hangman!")

    while lives > 0:
        print(hangman_stages.stages[lives])
        print("Word:", display_word(choose_word, guessed_letters))
        print("Guessed Letters:", ', '.join(guessed_letters))
        print("Lives:", lives)
        guessed_letter = input("Guess a letter: ").upper()

        if guessed_letter in guessed_letters:
            print("You have already guessed this letter.")
        elif guessed_letter in choose_word:
            print("Correct guess!")
            guessed_letters.append(guessed_letter)
            score += 10
        else:
            print("Incorrect guess!")
            guessed_letters.append(guessed_letter)
            lives -= 1

        if '_' not in display_word(choose_word, guessed_letters):
            print("Congratulations! You won!")
            print("Your Score:", score)
            break

    if lives == 0:
        print(hangman_stages.stages[0])
        print("Sorry, you lost the game.")
        print("The word was:", choose_word)

if __name__ == "__main__":
    play_hangman()
