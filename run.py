import random
import hangman_stages


# Define the scoring constants
CORRECT_GUESS_SCORE = 10
INCORRECT_GUESS_PENALTY = 5


def choose_word():
    """
    Read a list of words from a text file and
    randomly select one word and converted to uppercase.
    """
    try:
        with open("words.txt", "r") as file:
            word_list = file.readlines()
        return random.choice(word_list).strip().upper()
    except FileNotFoundError:
        print("Error: 'words.txt' not found. Make sure the file exists.")
        exit()


def initialize_display(word):
    """
    Initializes a display for a word by creating a list of underscores.
    """
    return ["_" for _ in word]


def is_valid_input(guessed_letter):
    """
    Checks if the inputted guessed letter is valid.
    """
    return guessed_letter.isalpha() and len(guessed_letter) == 1


def print_welcome():
    """
    Welcome message and How to play.
    """
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
    print("1. The secret word, underscore revels the number of letters.")
    print("2. Type a letter to guess the word.")
    print("3. Correct letter guessed, reveal all occurrences in the word")
    print("4. Each wrong guess will add a part for the hangman.")
    print("5. Six incorrect guesses will end the game.")
    print("6. Try to guess the word and increase your score!")
    print("7. Maximum score = 50. Each wrong guess -5 marks")
    print("8. Enjoy the game!")


def calculate_score(correct_guesses, incorrect_guesses):
    """
    Calculate the player's score based on
    the number of correct and incorrect guesses.
    """
    return (
        correct_guesses * CORRECT_GUESS_SCORE
        - incorrect_guesses * INCORRECT_GUESS_PENALTY
    )


def execute_hangman_game():
    # Display the welcome message only if it hasn't been displayed before
    welcome_displayed = False

    while True:
        if not welcome_displayed:
            print_welcome()
            welcome_displayed = True

        # Ask the player if they want to start the game
        print("\nWould you like to play the game? (Y/N):")
        start_game = input().upper()

        # If the player chooses not to play, exit the game
        if start_game != "Y":
            print("Goodbye!")
            break

        # Check if the player is ready to play the game
        ready_to_play = get_ready_status()
        if not ready_to_play:
            print("Goodbye!")
            break

        # Play the game
        play_game()

        # Ask the player if they want to play again
        print("\nWould you like to play again? (Y/N):")
        play_again_input = input().upper()

        # If the player does not want to play again, exit the game
        if play_again_input != "Y":
            print("Goodbye!")
            break

        # Set welcome_displayed to True to avoid repeating the welcome message
        welcome_displayed = True


def get_ready_status():
    """
    Check if the player is ready to play the game
    """
    user_input = input("\nReady to play [Y/N]? ").upper()
    return user_input == "Y"


def play_game():
    """
    Plays the Hangman game, allowing the player to guess words.
    The game includes displaying a welcome message,
    prompting the player to start,
    checking if the player is ready,
    playing the actual game,
    and asking if the player wants to play again.
    The game continues until the player decides to exit.
    """
    chosen_word = choose_word()  # Select a random word
    display = initialize_display(chosen_word)  # Underscores for each letter

    # Set the initial variables
    lives = 6
    guessed_letters = []
    correct_guesses = 0
    incorrect_guesses = 0
    game_over = False

    print("Word to guess: " + " ".join(display))
    # Continue the game until it's over
    while not game_over:
        # Show guessed letters
        print("Guessed letters: " + ' '.join(guessed_letters))
        # Play a turn and get the updated state
        lives, guessed_letters, display, letter_guessed = play_turn(
            chosen_word, lives, guessed_letters, display
        )

        # Update the counters based on the result of the turn
        if letter_guessed:
            correct_guesses += 1
        else:
            incorrect_guesses += 1

        print("Word to guess: " + " ".join(display))

        # Check if the word has been completely guessed
        if "_" not in display:
            game_over = True
            score = calculate_score(correct_guesses, incorrect_guesses)
            print(f"\nWOW, you won the game! The word was: {chosen_word}")
            print(f"Your score: {score}")
        elif lives == 0:
            game_over = True
            print("\nSorry, you lost! The word was: " + chosen_word)

    # Ask the player if they want to play again (moved out of the loop)
    print("Would you like to play again? (Y/N):")
    play_again_input = input().upper()
    if play_again_input == "Y":
        play_game()


def play_turn(chosen_word, lives, guessed_letters, display):
    """
    Plays a single turn of the Hangman game.
    """
    # Print the number of lives remaining
    print("\nNumber of lives you have:", lives)

    # Get the letter guessed by the player
    guessed_letter = get_guessed_letter(guessed_letters)

    # Check if the input is a valid single alphabet letter
    if not is_valid_input(guessed_letter):
        print("Please enter a valid single alphabet letter A-Z.")
        return lives, guessed_letters, display, False

    # Check if the letter has already been guessed
    if guessed_letter in guessed_letters:
        print("You have already guessed this letter.")
        return lives, guessed_letters, display, False

    # Add the guessed letter to the list of guessed letters
    guessed_letters.append(guessed_letter)

    # Update the display based on the guessed letter
    letter_guessed = update_display(chosen_word, guessed_letter, display)

    # If the guessed letter is incorrect, show the hangman stage
    if not letter_guessed:
        lives -= 1
        print("\nOops sorry, wrong guess. Try another letter.")
        print("Hangman stage:")
        print(hangman_stages.stages[lives])
    else:
        print("\nYes, it's a correct guess!")

    return lives, guessed_letters, display, letter_guessed


def get_guessed_letter(guessed_letters):
    """
    Gets a letter guessed by the player and converts it to uppercase.
    """
    return input("Guess a letter: ").upper()


def update_display(chosen_word, guessed_letter, display):
    """
    Updates the display based on the guessed letter in the chosen word.
    """
    letter_guessed = False
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guessed_letter:
            display[position] = chosen_word[position]
            letter_guessed = True
    return letter_guessed


# Call the execute_hangman_game function to start the game
execute_hangman_game()
