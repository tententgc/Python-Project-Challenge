from string import whitespace
from tkinter import *
from random import randint


root = Tk()
root.title("Guessing Number")
root.geometry("500x500")

num_label = Label(root, text="Guess a number between 1 and 100",
                  font=("Helvetica", 16))
num_label.pack(pady=20)

def guesser(): 
    if guess_box.get().isdigit():
        num_label.config(text="Pick a number between 1 and 100") 
        dif = abs(num - int(guess_box.get()) )
        
        #check if the guess is correct 
        if int(guess_box.get()) == num:
            bc = "SystemButtonFace"
            num_label.config(text="Correct!")
        elif dif == 5:
            bc= "white"
        elif dif < 5: 
            bc ="red"
        else : 
            bc = "blue"
        
        root.config(background=bc) 
        num_label.config(bg=bc) 
    else: 
        guess_box.delete(0, END) 
        num_label.config(text="Please enter a number") 

def rando():
    global num 
    num = randint(1, 100)
    #clear the label 
    guess_box.delete(0, END)
    num_label.config(bg="SystemButtonFace")
    root.config(background="SystemButtonFace") 


guess_box = Entry(root, font=("Helvetica", 100), width=2)
guess_box.pack(pady=20)

guess_button = Button(root, text="submit", command=guesser)
guess_button.pack(pady=20)

rand_button = Button(root, text="New ", command=rando)
rand_button.pack(pady=20)


#generate number before start game
rando()
root.mainloop()
