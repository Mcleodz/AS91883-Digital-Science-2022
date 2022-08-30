from tkinter import *
import json


def load_add_item_page(old_root):
    # Generates Window
    old_root.destroy()
    root = Tk()

    # Generates Text input boxes and buttons
    item_name_box = Entry(root, width=100, bg='#a4a4a4')
    item_quantity_box = Entry(root, width=100, bg='#a4a4a4')
    item_category_box = Entry(root, width=100, bg='#a4a4a4')
    item_price_box = Entry(root, bg='#a4a4a4', width=50)
    item_description_box = Entry(root, width=100, bg='#a4a4a4')
    submit_button = Button(root, text="Submit",
                           command=lambda: save_items_to_json(root, item_name_box, item_description_box,
                                                              item_quantity_box,
                                                              item_price_box, item_category_box))

    # Puts all previously generated text boxes and button on the window
    item_name_box.pack()
    item_quantity_box.pack()
    item_category_box.pack()
    item_description_box.pack()
    item_price_box.pack()
    submit_button.pack()

    # Puts description of each text box inside
    item_name_box.insert(0, "Item Name")
    item_quantity_box.insert(0, "Item Quantity (Must be a whole number)")
    item_category_box.insert(0, "Item Category")
    item_price_box.insert(0, "Item Price (Must be a number")
    item_description_box.insert(0, "Item Description")


def save_items_to_json(root, item_name_box, item_description_box, item_quantity_box, item_price_box, item_category_box):
    # Puts all user inputs in dictionary
    json_object = {
        "item name": item_name_box.get().lower(),
        "item quantity": item_quantity_box.get().lower(),
        "item description": item_description_box.get().lower(),
        "item price": item_price_box.get().lower()
    }
    # Loads Json file and checks its contents
    with open("items.json", "r") as json_file:
        json_file_thing = json.load(json_file)
        # Checks if category is in json file and if not adds category
        if not item_category_box.get().lower() in json_file_thing:
            json_file_thing[item_category_box.get().lower()] = []
        json_file_thing[item_category_box.get().lower()].append(json_object)
        test = json.dumps(json_file_thing, indent=4)
    # Writes users input to Json file
    with open("items.json", "w") as json_file:
        json_file.write(test)
