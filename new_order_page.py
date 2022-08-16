from tkinter import *
import json


def items_to_add(items_in_order):
    root2 = Tk()
    menu = Entry(root2, width=50, bg="#a3a3a3")
    items_to_add_to_order = Entry(root2, width=50, bg="#a3a3a3")
    add_item_button = Button(root2, text="Add the item(s)", command=lambda: add_item(items_in_order, items_to_add_to_order, root2))

    menu.pack()
    items_to_add_to_order.pack()
    add_item_button.pack()

    menu.insert(0, get_menu())

    menu.config(state='readonly')
    items_to_add_to_order.get()


def get_menu():
    menu = []
    with open("items.json", "r") as json_file:
        json_file_thing = json.load(json_file)
        for i in json_file_thing:
            for j in json_file_thing[i]:
                menu.append(j["item name"])
    return ", ".join(menu)


def add_item(items_in_order, items_to_add_to_order, root2):
    items_in_order.pack()
    items_in_order.insert(0, items_to_add_to_order.get())
    items_in_order.config(state='readonly')
    root2.destroy()


def load_new_order_page(old_root):
    old_root.destroy()
    root = Tk()

    customer_name = Entry(root, width=50, bg='#a3a3a3')
    items_in_order = Entry(root, width=50, bg='#a3a3a3')
    add_item_to_order_button = Button(root, text="Add an item to order", command=lambda: items_to_add(items_in_order))
    checkout_button = Button(root, text="checkout", command=lambda: print("hi"))

    customer_name.pack()
    add_item_to_order_button.pack()
    checkout_button.pack()

    customer_name.insert(0, 'Customer name / Table Number')
