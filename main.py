from tkinter import *

root = Tk()

root.geometry('100x100')


def home_button():
    home_button = Button(root, text='Home', command=lambda: print("Home Button Pressed"))
    home_button.pack()


def add_item():
    add_item = Button(root, text='Add item', command=lambda: print("Add item Button Pressed"))
    add_item.pack()


def remove_item():
    remove_item = Button(root, text='Remove item', command=lambda: print("Remove item Button Pressed"))
    remove_item.pack()


def new_order():
    new_order = Button(root, text='Create Order', command=lambda: print("Create Order Button Pressed"))
    new_order.pack()


def generate_stock_report():
    gen_stock_report = Button(root, text='Generate Stock Report',
                              command=lambda: print("Generate Stock Report Button Pressed"))
    gen_stock_report.pack()


add_item()
remove_item()
new_order()
generate_stock_report()
home_button()

root.mainloop()
