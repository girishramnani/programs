from tkinter import messagebox
from tkinter.messagebox import showwarning
from tkinter.filedialog import askopenfilename
__author__ = 'Girish'
import os
from tkinter import *
import tkinter.ttk as ttk


class UI:
    def __init__(self,master):

        self.master = master
        self.init_UI()



    def init_UI(self):
        self.label = Label(self.master,text="FileName:")
        self.entry = Entry(self.master)
        self.button = Button(self.master,text="Select file",command=self.ask)
        self.button2 =Button(self.master,text="Start",command=self.work)
        self.label.grid(row=0,column=0,pady=(5,5),padx=10)
        self.entry.grid(row=0,column=1,pady=(5,5),padx=10)
        self.button.grid(row=0,column=2,pady=(5,5),padx=2)
        self.button2.grid(row=0,column=3,padx=(2,5))


    def ask(self):
        self.file = askopenfilename()
        if self.file !=None:
            pass



    def work(self):
        pass


    def start_translating(self):
        pass



if __name__=="__main__":
    root = Tk()
    root.title("google Translate")
    root.minsize(320,100)
    application = UI(root)
    root.mainloop()

