import random
import hangman_stages

# Function to choose the random word from a given word list
def choose_word():
    word_list = ["INTERNET", "COMPUTER", "SOFTWARE", "DATABASE", "INFORMATION"]
    return random.choice(word_list)

def initialize_display(word):
    return ['_' for _ in word]

# Function to play the game
def play_hangman():
    chosen_word = choose_word()
    display = initialize_display(chosen_word)

    lives = 6
    guessed_letters = []
    game_over = False

    print("Welcome to Hangman!")
   # print("Your secret word: " + ' '.join(display))  

    while not game_over:
        print(f"Your secret word: {' '.join(display)}") # Display initial underscores
        print(f"Number of lives you have: {lives}")
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
        print("Your secret word: " + ' '.join(display))  # Display updated word with spaces

        if not letter_guessed:
            lives -= 1
            if lives == 0:
                game_over = True
                print("Sorry, you lost the game! The word was: " + chosen_word)
        
        if '_' not in display:  # Check if there are any underscores left
            game_over = True
            print("Congratulations! You won! The word was: " + chosen_word)
            
        print(hangman_stages.stages[lives])

if __name__ == "__main__":
    play_hangman()
