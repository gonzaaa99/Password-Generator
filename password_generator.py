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

        #Entry
        self.length = ttk.Entry(self.root,text = 'length')                              #Length
        self.length.grid(row = 0,column = 1)
        self.length.insert(0,'8')
        self.length.focus()
        self.generatedPassword = ttk.Entry(self.root)                                   #Generated password
        self.generatedPassword.grid(row = 3,column = 0,columnspan = 3,sticky = 'e w')

        #Label
        Label(self.root,text='Length:').grid(row=0,column=0)

        #Button
        Button(self.root,text='Generate password',command = lambda: self.generatePassword()).grid(row=2,column=0,columnspan=3)

        #Check Buttons
        self.letters_var     = IntVar()     # 1 yes, 0 no
        self.digits_var      = IntVar()     # 1 yes, 0 no
        self.punctuation_var = IntVar()     # 1 yes, 0 no
        letters_chkbtn =     Checkbutton(self.root, text="letters",     variable=self.letters_var,       onvalue=1, offvalue=0)
        digits_chkbtn =      Checkbutton(self.root, text="digits",      variable=self.digits_var,        onvalue=1, offvalue=0)
        punctuation_chkbtn = Checkbutton(self.root, text="punctuation", variable=self.punctuation_var,   onvalue=1, offvalue=0)
        letters_chkbtn.select()
        digits_chkbtn.select()
        punctuation_chkbtn.select()
        letters_chkbtn.grid(    row = 1,column = 0)
        digits_chkbtn.grid(     row = 1,column = 1)
        punctuation_chkbtn.grid(row = 1,column = 2)

        #Mainloop
        self.root.mainloop()
    
    def generatePassword(self):
        """
        Generates a random password with an specific length 
        """
        #Check lenght, if empty, length = 8
        try:
            l = int(self.length.get())
        except Exception:
            l = 8

        #Check characters to use
        list_of_characters = ''
        if self.letters_var.get()==1:
            list_of_characters+=f'{ascii_letters}'
        if self.digits_var.get()==1:
            list_of_characters+=f'{digits}'
        if self.punctuation_var.get()==1:
            list_of_characters+=f'{punctuation}'
        
        #Convert to list and shuffle
        list_of_characters = list(list_of_characters)
        shuffle(list_of_characters)

        #Generate the password
        password = choices(list_of_characters, k=l)
        password = ''.join(password)

        #Show password
        self.generatedPassword.delete(0,END)
        self.generatedPassword.insert(0,password)

PasswordGenerator()