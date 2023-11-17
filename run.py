import random
import hangman_stages

# Define the scoring constants
CORRECT_GUESS_SCORE = 10
INCORRECT_GUESS_PENALTY = 5


def choose_word():
    '''
    Read a list of words from a text file and
    randomly select one word and converted to uppercase.
    '''
    try:
        with open('words.txt', 'r') as file:
            word_list = file.readlines()
        return random.choice(word_list).strip().upper()
    except FileNotFoundError:
        print("Error: 'words.txt' not found. Make sure the file exists.")
        exit()


def initialize_display(word):
    '''
    Initializes a display for a word by creating a list of underscores.
    '''
    return ['_' for _ in word]


def is_valid_input(guessed_letter):
    '''
    Checks if the inputted guessed letter is valid.
    '''
    return guessed_letter.isalpha() and len(guessed_letter) == 1


def print_welcome():
    '''
    Welcome message and How to play.
    '''
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
    print("7. Maximum score = 60. Each wrong guess -5 marks")
    print("8. Enjoy the game!")


def calculate_score(correct_guesses, incorrect_guesses):
    '''
        Calculate the player's score based on
        the number of correct and incorrect guesses.
    '''
    return (
        correct_guesses * CORRECT_GUESS_SCORE -
        incorrect_guesses * INCORRECT_GUESS_PENALTY
    )


def play_hangman():
    # Display the welcome message only if it hasn't been displayed before
    welcome_displayed = False

    while True:
        if not welcome_displayed:
            print_welcome()
            welcome_displayed = True

        # Ask the player if they want to start the game
        print("Would you like to play the game? (Y/N):")
        start_game = input().upper()

        # If the player chooses not to play, exit the game
        if start_game != 'Y':
            print("Goodbye!")
            break

        while True:
            print("\nReady to play [Y/N]?")
            ready_to_play = input().upper()

            if ready_to_play != 'Y':
                print("Goodbye!")
                break

            
            chosen_word = choose_word() # Get a word to guess from the file
            display = initialize_display(chosen_word)  # Underscores for each letter in the word
            lives = 6  # Set the initial number of lives
            guessed_letters = []  # List to store guessed letters
            game_over = False  # Flag to track if the game is over
            correct_guesses = 0
            incorrect_guesses = 0

            # Display the initial state of the word to guess
            print("Word to guess: " + ' '.join(display))

            # Main loop for each turn of the game
            while not game_over:
                # Display the number of lives the player has
                print("\nNumber of lives you have:", lives)

                # Get the guessed letter from the player
                guessed_letter = input("Guess a letter: ").upper()

                # Validate the guessed letter input
                if not is_valid_input(guessed_letter):
                    print("Please enter a valid single alphabet letter A-Z.")
                    continue

                # Check if the letter has already been guessed
                if guessed_letter in guessed_letters:
                    print("You have already guessed this letter.")
                    continue

                # Add the guessed letter to the list of guessed letters
                guessed_letters.append(guessed_letter)

                # Flag to check if the guessed letter is in the word
                letter_guessed = False

                # Check each position in the chosen word
                for position in range(len(chosen_word)):
                    letter = chosen_word[position]
                    if letter == guessed_letter:
                        # Update the display if the guessed letter is in the word
                        display[position] = chosen_word[position]
                        letter_guessed = True

                # Provide feedback to the player based on the guessed letter
                if letter_guessed:
                    print("You made a correct guess!")
                    correct_guesses += 1
                else:
                    # If the guessed letter is not in the word, decrement the lives
                    lives -= 1
                    incorrect_guesses += 1
                    print("Sorry, wrong guess. Try another letter.")
                    print("Hangman stage:")
                    print(hangman_stages.stages[lives])  # Print the hangman stage

                # Display the updated word with spaces
                print("Word to guess: " + ' '.join(display))

                # Check if the word has been completely guessed
                if '_' not in display:
                    game_over = True
                    score = calculate_score(correct_guesses, incorrect_guesses)
                    print(f"WOW, you won the game! The word was: {chosen_word}")
                    print(f"Your score: {score}")
                elif lives == 0:
                    game_over = True
                    print("Sorry, you lost the game! The word was: " + chosen_word)

            # Ask the player if they want to play again
            print("\nWould you like to play again? (Y/N): ")
            play_again_input = input().upper()

        # If the player chooses not to play again, display a goodbye message
        if play_again_input != 'Y':
            print("Goodbye!")
            break

# Call the play_hangman function to start the game
play_hangman()
