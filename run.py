import random
import hangman_stages

# Define the scoring constants
CORRECT_GUESS_SCORE = 10
INCORRECT_GUESS_PENALTY = 5

def choose_word():
    try:
        with open('words.txt', 'r') as file:
            word_list = file.readlines()
        return random.choice(word_list).strip().upper()
    except FileNotFoundError:
        print("Error: 'words.txt' not found. Make sure the file exists.")
        exit()

def initialize_display(word):
    return ['_' for _ in word]

def is_valid_input(guessed_letter):
    return guessed_letter.isalpha() and len(guessed_letter) == 1

def print_welcome():
    print(r"""
__        _______ _     ____ ___  __  __ _____ 
 \ \      / / ____| |   / ___/ _ \|  \/  | ____|
  \ \ /\ / /|  _| | |  | |  | | | | |\/| |  _|  
   \ V  V / | |___| |__| |__| |_| | |  | | |___ 
    \_/\_/  |_____|_____\____\___/|_|  |_|_____|
  _____ ___    _   _    _    _   _  ____ __  __    _    _   _ 
 |_   _/ _ \  | | | |  / \  | \ | |/ ___|  \/  |  / \  | \ | |
   | || | | | | |_| | / _ \ |  \| | |  _| |\/| | / _ \ |  \| |
   | || |_| | |  _  |/ ___ \| |\  | |_| | |  | |/ ___ \| |\  |
   |_| \___/  |_| |_/_/   \_\_| \_|\____|_|  |_/_/   \_\_| \_|
""")
    print("How to play:")
    print("1. The secret word,number of letters of the word by dash marks.")
    print("2. Type a letter to guess the word.")
    print(
        "3. Correct letter guessed, reveal all occurrences in the word"
    )
    print("4. Each wrong guess will add a part for the hangman.")
    print("5. Six incorrect guesses will end the game.")
    print("6. Try to guess the word and increase your score!")
    print("7. Enjoy the game!")

def calculate_score(correct_guesses, incorrect_guesses):
    return correct_guesses * CORRECT_GUESS_SCORE - incorrect_guesses * INCORRECT_GUESS_PENALTY

def play_hangman():
    print_welcome()

    print("Would you like to play the game? (Y/N):")
    start_game = input().upper()

    if start_game != 'Y':
        print("Goodbye!")
        return

    chosen_word = choose_word()
    display = initialize_display(chosen_word)

    lives = 6
    guessed_letters = []
    correct_guesses = 0
    incorrect_guesses = 0
    game_over = False

    print("\nReady to play [Y/N]?")
    start_game = input().upper()

    if start_game != 'Y':
        print("Goodbye!")
        return

    print("Word to guess: " + ' '.join(display))

    while not game_over:
        print("\nNumber of lives you have:", lives)
        guessed_letter = input("Guess a letter: ").upper()

        if not is_valid_input(guessed_letter):
            print("Please enter a valid single alphabet letter A-Z.")
            continue

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

        if letter_guessed:
            print("You made a correct guess!")
            correct_guesses += 1
        else:
            lives -= 1
            incorrect_guesses += 1
            print("Sorry, wrong guess. Try another letter.")
            print("Hangman stage:")
            print(hangman_stages.stages[lives])

        print("Word to guess: " + ' '.join(display))

        if '_' not in display:
            game_over = True
            score = calculate_score(correct_guesses, incorrect_guesses)
            print(f"WOW, you won the game! The word was: {chosen_word}")
            print(f"Your score: {score}")
        elif lives == 0:
            game_over = True
            print(f"Sorry, you lost the game! The word was: {chosen_word}")

    print("\nWould you like to play again? (Y/N): ")
    play_again_input = input().upper()

    if play_again_input == 'Y':
        play_hangman()
    else:
        print("Goodbye!")

play_hangman()
