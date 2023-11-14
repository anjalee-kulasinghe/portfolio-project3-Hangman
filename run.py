import random
from tkinter import *
from tkinter import messagebox

score = 0
run = True

# mian loop
while run:
    # initializing a Tkinter window
    root = Tk()
    root.geometry('950x725')
    root.title('HANGMAN')
    root.config(bg = '#E7FFFF')
    count = 0
    win_count = 0

    # choosing the random word
    index = random.randint(0,58109)
    file = open('words.txt','r') # import the word text file
    word_list = file.readlines()
    selected_word = word_list[index].strip('\n')

    # creating the dashes according to the selected word
    dashes_labels = []

    x_position = 250
    for i in range(len(selected_word)):
        x_position += 60
        dash_label = Label(root, text="_", bg="#E7FFFF", font=("arial", 40))
        dash_label.place(x=x_position, y=450)
        dashes_labels.append(dash_label)
    
    # Create a dictionary to store PhotoImage objects
    image_dict = {}
    for let in 'abcdefghijklmnopqrstuvwxyz':
        image_dict[let] = PhotoImage(file=f"{let}.png")
    
    # Hangman images
    hangman_image = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7']
    hangman_images = [PhotoImage(file=f"{hangman}.png") for hangman in hangman_image]
    hangman_label = Label(root, bg="#E7FFFF", image=hangman_images[count])
    hangman_label.place(x=300, y=-50)

    # Letters placement
    buttons = []
    button_height = 70  # Adjust this value based on your layout
    for i, letter in enumerate('abcdefghijklmnopqrstuvwxyz'):
        row = i // 13  # Change the number 13 based on the number of buttons per row you want
        col = i % 13
        button = Button(root, bd=0, command=lambda l=letter, idx=i + 1: check(l, idx), bg="#E7FFFF",
                        activebackground="#E7FFFF", font=10, image=image_dict[letter])
        button.place(x=col * 70, y=row * button_height + 595)
        buttons.append(button)

    # Exit button
    exit_image = PhotoImage(file='exit.png')
    exit_button = Button(root, bd=0, command=close, bg="#E7FFFF", activebackground="#E7FFFF", font=10, image=exit_image)
    exit_button.place(x=770, y=10)