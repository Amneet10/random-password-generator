import random 
import string
from tkinter import *

def randomPasswordGenerator():
    password =[]
  
    numbers= random.choice(string.digits)
    alphabets= random.choice(string.ascii_letters)
    symbols= random.choice(string.punctuation)
    lowercase =random.choice(string.ascii_lowercase)
    uppercase= random.choice(string.ascii_uppercase)
    printtable= random.choice(string.printable)
    password.append(numbers)
    password.append(alphabets)
    password.append(symbols)
    password.append(lowercase)
    password.append(uppercase)
    password.append(printtable)
    print(''.join(password))



root = Tk()
root.title("PASSWORD GENERATOR")
root.geometry("250x200")

btn = Button(root, text="Generate Password", command=randomPasswordGenerator)
btn.grid(row=2, column=2)
lbl = Label(root, font=("times", 15, "bold"))
lbl.grid(row=4, column=2)
root.mainloop()
randomPasswordGenerator()


 



# root = Tk()
# root.title("PASSWORD GENERATOR")
# root.geometry("250x200")
# btn = Button(root, text="Generate Password", command=generate_password)
# btn.grid(row=2, column=2)
# lbl = Label(root, font=("times", 15, "bold"))
# lbl.grid(row=4, column=2)
# root.mainloop()
