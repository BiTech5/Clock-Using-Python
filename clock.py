from time import strftime
from tkinter import *

root=Tk()

root.configure(bg='black')
root.geometry('300x300')
root.resizable(False,False)

root.title("Clock")

def time():
    string=strftime('%H:%M:%S %p')
    mark.config(text=string)
    mark.after(1000,time)

mark=Label(root,font=('calibri',40,'bold'),bg='black',pady=150,foreground='green')
mark.pack()

time()
mainloop()