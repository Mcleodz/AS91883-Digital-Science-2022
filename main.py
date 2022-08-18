from tkinter import *
from add_item_page import *
from remove_item_page import *
from new_order_page import *
root = Tk()


def home_page():
    add_item_button = Button(root, text="Add an Item to Menu", command=lambda: load_add_item_page(root))
    add_item_button.pack()

    remove_item_button = Button(root, text="Remove an Item from Menu", command=lambda: load_remove_item_page(root))
    remove_item_button.pack()

    new_order_button = Button(root, text="Create New Order", command=lambda: load_new_order_page(root))
    new_order_button.pack()

    quit_button = Button(root, text="Quit", command=lambda: quit())
    quit_button.pack()


home_page()
root.mainloop()
