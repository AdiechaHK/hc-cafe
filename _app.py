from tkinter import *
import csv

#Basic window is created
root = Tk()
root.title("Helly Chilly Cafe")

titleSpace = Frame(root)
titleSpace.pack()

lblWelcome = Label(titleSpace, font=('arial', 26, 'bold'), text="Welcome to Helly Chilly Cafe", bd=12)
lblWelcome.pack()

# Menu list
mainSpace = Frame(root)
mainSpace.pack()

menuList = Frame(mainSpace)
menuList.pack(side=LEFT)


class MenuItem:
    _name: str
    _cost: float
    def __init__(self, name, cost):
        self._name = name
        self._cost = float(cost)
        
    def add_to(self, cntx):
        btn = Button(cntx, text=f'{self._name} ({self._cost})', command=self.select_item)
        btn.pack(fill=X)

    def select_item(self):
        print(f'You clicked on {self._name}')

with open('menu.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    first = True
    line_count = 0
    for row in csv_reader:
        if first:
            first = False
            print(f'Column names are {", ".join(row)}')
        else:

            [name, cost] = row

            item = MenuItem(name, cost)
            item.add_to(menuList)

            line_count += 1
    print(f'Processed {line_count} lines.')


billFrame = Frame(mainSpace)
billFrame.pack()


tmp2 = Label(billFrame, text="Bill here.")
tmp2.pack()

root.mainloop()
