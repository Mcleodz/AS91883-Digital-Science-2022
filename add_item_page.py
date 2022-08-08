from tkinter import *


def load_add_item_page(old_root):
    old_root.destroy()
    root = Tk()

    item_name = str()
    item_name_box = Entry(root, textvariable=item_name)
    item_quantity_box = Entry(root)
    item_category_box = Entry(root)
    item_price_box = Entry(root)
    item_description_box = Entry(root)
    submit_button = Button(root, text="Submit", command=lambda: save_items(item_name_box, item_name))

    item_description_box.pack()
    item_quantity_box.pack()
    item_name_box.pack()
    item_category_box.pack()
    item_price_box.pack()
    submit_button.pack()


def save_items(name_box, item_name):
    f = open("Item 1.txt", "a")
    f.write("Item Name = " + item_name)
    f.close()
