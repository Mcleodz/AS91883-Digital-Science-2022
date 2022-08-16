import json
from tkinter import *


def update_label():
    menu = []
    with open("items.json", "r") as json_file:
        json_file_thing = json.load(json_file)
        for i in json_file_thing:
            for j in json_file_thing[i]:
                menu.append(j["item name"])
    return ", ".join(menu)


def load_remove_item_page(old_root):
    # Generates Window
    old_root.destroy()
    root = Tk()

    menu_string = update_label()

    list_of_items = Entry(root, width=50, bg='#a3a3a3')
    list_of_items.pack()
    list_of_items.insert(0, menu_string)
    list_of_items.config(state="readonly")

    item_to_remove = Entry(root, width=50, bg='#a3a3a3')
    item_to_remove.pack()

    removing_item_button = Button(root, text="Remove Selected item",
                                  command=lambda: remove_item(item_to_remove, list_of_items))
    removing_item_button.pack()


def remove_item(item_to_remove, list_of_items_label):
    item_being_removed = item_to_remove.get()
    with open("items.json", "r") as json_file:
        json_file_thing = json.load(json_file)
        for i in json_file_thing:
            for j in range(len(json_file_thing[i])):
                if item_being_removed == json_file_thing[i][j]["item name"]:
                    json_file_thing[i].remove(json_file_thing[i][j])
    with open("items.json", "w") as json_file:
        to_write = json.dumps(json_file_thing, indent=4)
        json_file.write(to_write)
    list_of_items_label.config(state="normal")
    list_of_items_label.delete(0, END)
    list_of_items_label.insert(0, update_label())
    list_of_items_label.config(state="readonly")
    item_to_remove.delete(0, END)
