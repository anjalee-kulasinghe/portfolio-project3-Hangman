import random
import hangman_stages

def read_words_from_file(filename):
    with open(filename, 'r') as file:
        words = file.read().splitlines()
    return words

def choose_word():
    word_list = read_words_from_file("hangman_wordlist.txt")
    return random.choice(word_list)

def initialize_display(word):
    return ['_' for _ in word]

def play_hangman():
    chosen_word = choose_word()
    display = initialize_display(chosen_word)

    lives = 6  # Adjust the initial number of lives
    guessed_letters = []
    game_over = False

    print("Welcome to Hangman!")
    print("Word to guess: " + ' '.join(display))  # Display underscores for each letter

    while not game_over:
        print("Number of lives you have:", lives)  # Print the number of lives
        guessed_letter = input("Guess a letter: ").upper()
        
        if guessed_letter in guessed_letters:
            print("You have already guessed this letter.")
            continue
        
        guessed_letters.append(guessed_letter)
        
        letter_guessed = False
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if letter == guessed_letter:
                display[position] = chosen_word[position]
                letter_guessed = True
        print("Word to guess: " + ' '.join(display))  # Display updated word with spaces

        if '_' not in display:
            game_over = True
            print("WOW, you won the game! The word was: " + chosen_word)  # Moved the winning condition check here
        elif not letter_guessed:
            lives -= 1
            if lives == 0:
                game_over = True
                print("Sorry, you lost the game! The word was: " + chosen_word)

if __name__ == "__main__":
    play_hangman()
