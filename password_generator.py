from tkinter import *
from tkinter import ttk
from string import ascii_letters,digits,punctuation
from random import choices,shuffle


class PasswordGenerator():
    """
    Desktop App to generate random passwords with a simple interface.
    """
    def __init__(self):
        """
        Initializes the Tkinter interface
        """
        self.root = Tk()
        self.root.title('Password Generator')

        self.length = ttk.Entry(self.root,text = 'length')
        self.length.grid(row = 0,column = 1)
        self.length.focus()
        self.generatedPassword = ttk.Entry(self.root)
        self.generatedPassword.grid(row = 2,column = 0,columnspan = 3,sticky = 'e w')

        Label(self.root,text='Length:').grid(row=0,column=0)
        Button(self.root,text='Generate password',command = lambda: self.generatePassword()).grid(row=1,column=0,columnspan=2)

        self.root.mainloop()
    
    def generatePassword(self):
        """
        Generates a random password with an specific length 
        """
        try:
            l = int(self.length.get())
        except Exception:
            l = 8
        list_of_characters = f'{ascii_letters}{digits}{punctuation}'

        list_of_characters = list(list_of_characters)
        shuffle(list_of_characters)

        password = choices(list_of_characters, k=l)
        password = ''.join(password)
        self.generatedPassword.delete(0,END)
        self.generatedPassword.insert(0,password)
        print(password)


PasswordGenerator()