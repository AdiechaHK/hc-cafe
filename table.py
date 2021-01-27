from tkinter import *

class Table(Frame):
    def __init__(self, ctx, name):
        super(Table, self).__init__()
        self._ctx = ctx
        self.title = StringVar()
        self.title.set(name)
        Label(self, text="some activities will be listed here").pack()

        