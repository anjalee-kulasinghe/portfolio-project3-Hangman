# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
word_list = ["INTERNET", "COMPUTER", "SOFTWARE", "DATABASE", "INFORMATION"]
chose_word = random.choice(word_list)
print(chose_word)
display = []
for letter in chose_word:
	display += '_'
print(display)
