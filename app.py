from tkinter import *
from tkinter.ttk import *
from tkinter import simpledialog
from table import Table

class Application(Frame):
    """docstring for Application"""
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.master = master
        self.master.title('Maitrisangath')
        self.master.geometry("700x350")
        self.count = 0
        self.setup()
        
    def setup(self):
        self.heading = Frame(self.master)
        self.heading.pack()

        self.title = StringVar()
        self.title.set('Welcome to Helly Chelly Cafe')
        self.ttlLbl = Label(self.heading, text=self.title.get(), font=('default',26))
        self.ttlLbl.pack()

        # Common actions
        self.actionPannel = Frame(self.master)
        self.actionPannel.pack()
        self.newTabBtn = Button(self.actionPannel, text='Add New Table', command=self.add_table)
        self.newTabBtn.pack()

        # Setup notebook
        self.notebook = Notebook(self.master)
        tab = self.create_tab('demo')
        self.notebook.pack(fill="both")

    def add_table(self):
        name = simpledialog.askstring(
            "Input",
            "Enter Table Name:",
            initialvalue=f'Table #{self.count + 1}',
            parent=self.master)
        self.create_tab(name)

    def create_tab(self, name):
        self.count+=1
        tab = Table(self.notebook, name)
        self.notebook.add(tab, text=tab.title.get())

