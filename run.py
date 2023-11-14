import random
from tkinter import *
from tkinter import messagebox

score = 0
run = True

# mian loop
while run:
    # initializing a Tkinter window
    root = Tk()
    root.geometry('905x700') # screen size
    root.title('HANGMAN')
    root.config(bg='#E7FFFF') # screen background colour
    count = 0
    win_count = 0
    secret_word_label = Label(root, text='', bg="#E7FFFF", font=("arial", 20))

    # choosing a random word
    index = random.randint(0,853)
    file = open('words.txt','r') # import the word text file
    l = file.readlines()
    selected_word = l[index].strip('\n')