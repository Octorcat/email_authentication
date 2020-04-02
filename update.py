# update the appointments
# import modules
try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter 
except ImportError:
    # for Python3
    from tkinter import *   ## notice lowercase 't' in tkinter here
    import tkinter as tk
import sqlite3
import tkinter.messagebox

conn = sqlite3.connect('database.db')
c = conn.cursor()

class App:
    def __init__(self, master):
        self.master = master
        


#creating the object
root = tk.Tk()
b = App(root)
root.geometry("1200x720+0+0")
root.resizable(False, False)
root.title("Techmirtz Hospital Appointment Application - Update Appointment")
root.iconphoto(False, tk.PhotoImage(file='icon.png'))

# end the loop
root.mainloop()