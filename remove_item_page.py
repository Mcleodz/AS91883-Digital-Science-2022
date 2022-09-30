import json
from tkinter import *


# Updates the text box displaying th Menu
def update_label():
    menu = []
    with open("items.json", "r") as json_file:
        json_file_thing = json.load(json_file)
        for i in json_file_thing:
            for j in json_file_thing[i]:
                menu.append(j["item name"])
    return ", ".join(menu)


# Alerts the user of an item being incorrectly spelt
def incorrectly_spelt():
    incorrectly_spelt = Toplevel()
    incorrectly_spelt.geometry("1000x50")
    incorrectly_spelt.title("item is incorrectly spelt")
    Label(incorrectly_spelt, text="this item is not spelt correctly, Please try again", font=("Times New Roman", 20, "bold")).pack()


# Loads the "Remove item" page for the user
def load_remove_item_page():
    # Generates Window
    root = Tk()
    root.geometry("1920x1080")
    root.title("Remove an Item")

    menu_string = update_label()

    list_of_items = Entry(root, width=50, bg='#a3a3a3', font=("Times New Roman", 15, 'bold'))
    list_of_items.pack(fill=X, expand=0)
    list_of_items.insert(0, menu_string)
    list_of_items.config(state="readonly")

    item_to_remove = Entry(root, width=50, bg='#a3a3a3', font=("Times New Roman", 15, 'bold'))
    item_to_remove.pack(fill='both', expand=True)

    removing_item_button = Button(root, text="Remove Selected item",
                                  command=lambda: remove_item(item_to_remove, list_of_items), font=("Times New Roman", 15, 'bold'), bg="#a3a3a3")
    back_button = Button(root, text="Back", command=lambda: root.destroy(), font=("Times New Roman", 15, 'bold'), bg="#c21313")

    removing_item_button.pack(fill='both', expand=True)
    back_button.pack(fill='both', expand=True)

    item_to_remove.insert(0, "(type the item you wish to remove here)")

# Removes the requested item from the menu
def remove_item(item_to_remove, list_of_items_label):
    item_being_removed = item_to_remove.get().lower()
    with open("items.json", "r") as json_file:
        json_file_thing = json.load(json_file)
        for i in json_file_thing:
            for j in range(len(json_file_thing[i])):
                if item_being_removed == json_file_thing[i][j]["item name"]:
                    json_file_thing[i].remove(json_file_thing[i][j])
                else:
                    incorrectly_spelt()
    with open("items.json", "w") as json_file:
        to_write = json.dumps(json_file_thing, indent=4)
        json_file.write(to_write)
    list_of_items_label.config(state="normal")
    list_of_items_label.delete(0, END)
    list_of_items_label.insert(0, update_label())
    list_of_items_label.config(state="readonly")
    item_to_remove.delete(0, END)
