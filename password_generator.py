from tkinter import Label,Button,StringVar,Tk
from string import ascii_letters,digits,punctuation
from random import choices,shuffle

def generatePassword(length = 8):
    global output
    list_of_characters = f'{ascii_letters}{digits}{punctuation}'

    list_of_characters = list(list_of_characters)
    shuffle(list_of_characters)

    password = choices(list_of_characters, k=length)
    password = ''.join(password)
    output.set(password)

root = Tk()
root.title('Password Generator')
output = StringVar()

Button(root,text='Generate password',command = generatePassword).grid(row=0,column=0)
Label(root,textvariable=output).grid(row=1,column=0,columnspan=3)

root.mainloop()