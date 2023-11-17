import random
import hangman_stages

def choose_word():
'''
Read a list of words from a text file and 
randomly select one of the words.
Converted to uppercase. 
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
    print("1. The system will provide a random word, reflecting the number of letters of the word by dash marks.")
    print("2. Type a letter to guess the word.")
    print("3. If the guessed letter is correct, the system will reveal all occurrences of that letter in the word.")
    print("4. Each wrong guess will add a part for the hangman.")
    print("5. Six incorrect guesses will end the game.")
    print("6. Try to guess the word and increase your score!")
    print("7. Enjoy the game!")

def play_hangman():
    # Display the welcome message
    print_welcome()

    # Ask the player if they want to start the game
    print("Would you like to play the game? (Y/N):")
    start_game = input().upper()

    # If the player chooses not to play, exit the game
    if start_game != 'Y':
        print("Goodbye!")
        return

    # Get a word to guess from the file
    chosen_word = choose_word()

    # Initialize the display with underscores for each letter in the chosen word
    display = initialize_display(chosen_word)

    # Set the initial number of lives
    lives = 6
    guessed_letters = []  # List to store guessed letters
    game_over = False  # Flag to track if the game is over

    # Ask the player if they are ready to play
    print("\nReady to play [Y/N]?")
    start_game = input().upper()

    # If the player chooses not to play, exit the game
    if start_game != 'Y':
        print("Goodbye!")
        return

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
        else:
            # If the guessed letter is not in the word, decrement the lives
            lives -= 1
            print("Sorry, wrong guess. Try another letter.")
            print("Hangman stage:")
            print(hangman_stages.stages[lives])  # Print the hangman stage

        # Display the updated word with spaces
        print("Word to guess: " + ' '.join(display))

        # Check if the word has been completely guessed
        if '_' not in display:
            game_over = True
            print("WOW, you won the game! The word was: " + chosen_word)
        elif lives == 0:
            game_over = True
            print("Sorry, you lost the game! The word was: " + chosen_word)

    # Ask the player if they want to play again
    print("\nWould you like to play again? (Y/N): ")
    play_again_input = input().upper()

    # If the player chooses to play again, recursively call the play_hangman function
    if play_again_input == 'Y':
        play_hangman()
    else:
        # If the player chooses not to play again, display a goodbye message
        print("Goodbye!")

# Call the play_hangman function to start the game
play_hangman()
