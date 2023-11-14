import random
from tkinter import *
from tkinter import messagebox

score = 0
run = True

# Function to handle clicks of the letter buttons
def check(letter, button_idx):
    global count, win_count, run, score
    buttons[button_idx - 1].destroy()  # Destroy the individual button
    if letter in selected_word:
        for i in range(0, len(selected_word)):
            if selected_word[i] == letter and dashes_labels[i].cget("text") == "_":
                win_count += 1
                dashes_labels[i].config(text=letter.upper())  # Update the corresponding label
        if win_count == len(selected_word):
            score += 1
            reveal_word()  # Call the function to reveal the correct word
            answer = messagebox.askyesno('Game Over', 'You won!\nWant to play again?')
            if answer:
                run = True
                root.destroy()
            else:
                run = False
                root.destroy()
    else:
        count += 1
        update_hangman()
        if count == 6:
            reveal_word()  # Call the function to reveal the correct word
            answer = messagebox.askyesno('Game Over', 'You lost!\nWant to play again?')
            if answer:
                run = True
                score = 0
                root.destroy()
            else:
                run = False
                root.destroy()

# Function to update the displayed hangman image
def update_hangman():
    hangman_label.config(image=hangman_images[count])

# Mian loop
while run:
    # Initializing a Tkinter window
    root = Tk()
    root.geometry('950x725')
    root.title('HANGMAN')
    root.config(bg = '#E7FFFF')
    count = 0
    win_count = 0

    # Choosing the random word
    index = random.randint(0,58109)
    file = open('words.txt','r') # import the word text file
    word_list = file.readlines()
    selected_word = word_list[index].strip('\n')

    # Creating the dashes according to the selected word
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
    button_height = 70  # Adjust this value based on the layout
    for i, letter in enumerate('abcdefghijklmnopqrstuvwxyz'):
        row = i // 13  # Change the number 13 based on the number of buttons per row
        col = i % 13
        button = Button(root, bd=0, command=lambda l=letter, idx=i + 1: check(l, idx), bg="#E7FFFF",
                        activebackground="#E7FFFF", font=10, image=image_dict[letter])
        button.place(x=col * 70, y=row * button_height + 595)
        buttons.append(button)

    # Exit button
    exit_image = PhotoImage(file='exit.png')
    exit_button = Button(root, bd=0, command=close, bg="#E7FFFF", activebackground="#E7FFFF", font=10, image=exit_image)
    exit_button.place(x=770, y=10)

    # Score label
    score_label = Label(root, text='SCORE:' + str(score), bg="#E7FFFF", font=("arial", 25))
    score_label.place(x=10, y=10)

    # Function to reveal the correct word
    def reveal_word():
        messagebox.showinfo('Game Over', f'The correct word was: {selected_word.upper()}')

    root.mainloop()