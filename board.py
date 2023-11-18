import gspread
from google.oauth2.service_account import Credentials
import random
import hangman_stages

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

# Define the constant variables
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('score_board')
CORRECT_GUESS_SCORE = 10
INCORRECT_GUESS_PENALTY = 5


def get_username():
    '''
    Get the username from the user.
    If an existing username is provided,
    return it without asking for a new one.
    '''
    existing_username = None

    while True:
        data_username = input('Please enter your username: ')

        # Check if the username already exists in the sheet
        user_exists = any(entry['username'] == data_username for entry in get_sheet_data())

        if user_exists:
            print(f"Welcome back, {data_username}!")
            existing_username = data_username
            break
        else:
            print(f"Welcome, {data_username}! Let's play HANGMAN\n")
            break

    return existing_username

def get_sheet_data():
    """
    Retrieve the data from the 'score_board' sheet.
    """
    try:
        score_sheet = SHEET.get_worksheet(0)  # Assuming the first sheet is the 'score_board'
        return score_sheet.get_all_records()
    except Exception as e:
        print(f"Error retrieving sheet data: {e}")
        return []

def update_scoreboard(username, score):
    """
    Update the 'score_board' sheet with the use rname and score.
    If the username already exists, add the new score to the old score.
    """
    try:
        score_sheet = SHEET.get_worksheet(0)

        # Find the row number corresponding to the username
        user_row = None
        for index, row in enumerate(score_sheet.col_values(1)):
            if row == username:
                user_row = index + 1
                break

        if user_row is not None:
            # If the user exists, update the existing row with the new score
            current_score = int(score_sheet.cell(user_row, 2).value)
            new_score = current_score + score
            score_sheet.update_cell(user_row, 2, new_score)
        else:
            # If the user doesn't exist, add a new row for the user
            score_sheet.append_row([username, score])

        print("Score updated successfully!")
    except Exception as e:
        print(f"Error updating score: {e}")


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
    print("3. Correct letter guessed, reveal all occurrences in the word.")
    print("4. Each wrong guess will add a part for the hangman.")
    print("5. Six incorrect guesses will end the game.")
    print("6. Try to guess the word and increase your score!")
    print("7. Each correct guess = 10 marks. Each wrong guess -5 marks.")
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
    '''
    Handle the execution of the hangman game.
    '''
    # Whether the welcome message has been displayed
    welcome_displayed = False
    existing_username = None  # Initialize existing_username

    # Main loop for the game
    while True:
        # Display the welcome message only if it hasn't been displayed before
        if not welcome_displayed:
            print_welcome()
            welcome_displayed = True

        # Ask the player if they want to start the game
        start_game = input(
            "\nWould you like to start the game? (Y/N):"
        ).upper()

        # If the player chooses not to play, exit the game
        if start_game != "Y":
            print("Goodbye!")
            break

        # Inner loop for playing multiple rounds
        while True:
            # Check if the player is ready to play the game
            ready_to_play = get_ready_status()

            # If the player is not ready, exit the current game loop
            if not ready_to_play:
                print("Goodbye!")
                return

            # Get the username
            username = get_username()

            # Play the game
            score = play_game(username)

            # Update the scoreboard
            update_scoreboard(username, score)

            # Set existing_username for the next iteration
            existing_username = username

            # Ask the player if they want to play again
            play_again_input = input(
                "\nWould you like to play again? (Y/N):"
            ).upper()

            # If the player doesn't want to play again, exit the current loop
            if play_again_input != "Y":
                print("Goodbye!")
                return


def get_ready_status():
    """
    Check if the player is ready to play the game
    """
    while True:
        user_input = input("\nReady to play [Y/N]? ").upper()
        if user_input == "Y":
            return True
        elif user_input == "N":
            return False
        else:
            print("Invalid entry. Please enter 'Y' or 'N'.")


def play_game(username):
    """
    Plays the Hangman game, allowing the player to guess words.
    This function includes displaying a welcome message,
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

        # Calculate the score
        score = calculate_score(correct_guesses, incorrect_guesses)

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

    return score

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
