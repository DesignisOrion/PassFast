
import random 
from tkinter import *
import pyperclip
import random

# initializing the tkinter
root = Tk()
root.title("PASSFAST")
root['background']='#205018'

# setting the width and height
root.geometry("250x200")    # x is small case here


# used to store the password generated
passstr = StringVar()

# store the length of the password entered by the user
passlen = IntVar()

# setting the length of the password to zero initially
passlen.set(0)

# function to generate the password
def generate():
    # storing the keys in a list for password generation
    
    pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
            'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8',
            '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&',
            '*', '(', ')']

    # declaring the empty string
    password = ""

    # loop to generate the random password of the length created by the user
    for x in range(passlen.get()):
        password = password + random.choice(pass1)

    # setting the password to the entry widget
    passstr.set(password)

# function to copy the password to the clipboard
def copytoclipboard():
    random_password = passstr.get()
    pyperclip.copy(random_password)

Label(root, text="PASSFAST", font="Poppins 12 bold").pack()


Label(root, text="Enter the password length", font="Poppins 8 bold").pack(pady=3)
Entry(root, textvariable=passlen).pack(pady=3)
Button(root, text="Generate Password",bg = "dark grey", command=generate).pack(pady=7)
Entry(root, textvariable=passstr).pack(pady=3)
Button(root, text="Copy to clipboard",bg = "dark grey", command=copytoclipboard).pack()

root.mainloop()

#OUTPUT EXAMPLE:

'''
Copied password:
dg$&y$E8ze

'''