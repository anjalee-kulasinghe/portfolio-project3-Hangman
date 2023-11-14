import random
import hangman_stages

def read_words_from_file(filename):
    with open(filename, 'r') as file:
        words = file.read().splitlines()
    return words

def choose_word():
    word_list = read_words_from_file("wordlist.txt")
    return list(random.choice(word_list))  # Convert the chosen word to a list of characters

def initialize_display(word):
    return ['_' for _ in word]

def play_hangman():
    chosen_word = choose_word()
    display = initialize_display(chosen_word)

    lives = len(hangman_stages.stages) - 1
    guessed_letters = []
    game_over = False

    print("Welcome to Hangman!")
    print("Word to guess:", ' '.join(display))

    while not game_over:
        print(hangman_stages.stages[len(hangman_stages.stages) - lives])
        print("Number of lives you have:", lives)
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
        print("Word to guess:", ' '.join(display))

        if '_' not in display:
            game_over = True
            print("WOW, you won the game! The word was:", ''.join(chosen_word))
        elif not letter_guessed:
            lives -= 1
            incorrect_guesses = len([letter for letter in guessed_letters if letter not in chosen_word])
            if lives == 0:
                game_over = True
                print("Sorry, you lost the game! The word was:", ''.join(chosen_word))
                print("Incorrect guesses:", incorrect_guesses)
        
        print(hangman_stages.stages[len(hangman_stages.stages) - lives])

if __name__ == "__main__":
    play_hangman()
