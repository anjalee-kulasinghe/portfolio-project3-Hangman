import random
from tkinter import *
from tkinter import messagebox

score = 0
run = True

# mian loop
while run:
    # initializing a Tkinter window
    root = Tk()
    root.geometry('905x700')
    root.title('HANGMAN')
    root.config(bg = '#E7FFFF')
    count = 0
    win_count = 0

    # choosing the random word
    index = random.randint(0,58109)
    file = open('words.txt','r') # import the word text file
    list = file.readlines()
    selected_word = list[index].strip('\n')

    # creating the dashes according to the selected word
    dashes_labels = []

    x_position = 250
    for i in range(len(selected_word)):
        x_position += 60
        dash_label = Label(root, text="_", bg="#E7FFFF", font=("arial", 40))
        dash_label.place(x=x_position, y=450)
        dashes_labels.append(dash_label)