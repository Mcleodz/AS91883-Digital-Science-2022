from tkinter import *
import json


def get_menu():
    menu = []
    with open("items.json", "r") as json_file:
        json_file_thing = json.load(json_file)
        for i in json_file_thing:
            for j in json_file_thing[i]:
                menu.append(j["item name"])
    return ", ".join(menu)


def add_item_to_order():
    root2 = Tk()

    menu = Entry(root2, width=50, bg='#a3a3a3')
    item_to_add = Entry(root2, width=50, bg='#a3a3a3')
    add_item = Button(root2, text="Add this item to order", command=lambda: root2.withdraw())

    menu.pack()
    item_to_add.pack()
    add_item.pack()

    menu.insert(0, get_menu())

    menu.config(state='readonly')

def load_new_order_page(old_root):
    old_root.destroy()
    root = Tk()

    customer_name = Entry(root, width=50, bg='#a3a3a3')
    menu_display = Entry(root, width=50, bg='#a3a3a3')
    add_item_to_order_button = Button(root, text="Add an item to order", command=lambda: add_item_to_order())

    customer_name.pack()
    menu_display.pack()
    add_item_to_order_button.pack()

    menu_display.insert(0, get_menu())
    customer_name.insert(0, 'Customer name / Table Number')

    menu_display.config(state='readonly')
