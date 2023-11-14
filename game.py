import random
import hangman_stages

def choose_word():
    word_list = ["INTERNET", "COMPUTER", "SOFTWARE", "DATABASE", "INFORMATION"]
    return random.choice(word_list)


def getInfile():
	try:
		# First, we check for a file called "wordlist.txt". If it exists in the same directory
		#	as the Hangman program, then we use this file as our word list automatically
		with open('wordlist.txt', 'r'): infile_name = 'wordlist.txt'
	except IOError:
		# If wordlist.txt cannot be found, then we ask the user to specify a text file
		found_file = False
		infile_name = input('Please specify a text file containing a list of words for the Hangman game to choose from (include the full file path if the file is in a different directory than the Hangman program): ')
		# If the user specifies a file name of a file that cannot be found, we keep asking for
		#	a valid input file until a valid one is specified
		while not(found_file):
			try:
				with open(infile_name, 'r'): found_file = True
			except IOError:
				infile_name = input('\n{0} was not found!\n\nPlease try again, or specify a different file (include the full file path if the file is in a different directory than the Hangman program): '.format(infile_name))

	return infile_name

# chooseWord()
#
# Chooses a word randomly from the list of words taken from the input file
def chooseWord(infile_name):
	infile = open(infile_name, 'r')
	word_list = infile.readlines()
	total_words = len(word_list)
	random_num = randint(0, total_words - 1)

	chosen_word = word_list[random_num].replace('\n', '')
	word_len = len(chosen_word)
	return chosen_word, word_len




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
        
        print(hangman_stages.stages[lives])

if __name__ == "__main__":
    play_hangman()
