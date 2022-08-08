from tkinter import *
from add_item_page import *


root = Tk()

root.geometry('100x100')


def home_page():

    add_item_button = Button(root, text="Add an Item to Menu",
                             command=lambda: load_add_item_page(root)).pack()


home_page()
root.mainloop()
