from tkinter import *
import json


def load_add_item_page():
    # Generates Window
    root = Tk()
    root.geometry("1920x1080")
    root.title("Add an Item to the Menu")

    # Generates Text input boxes and buttons
    item_name_box = Entry(root, width=100, bg='#a4a4a4', font=("Times New Roman", 20, "bold"))
    item_quantity_box = Entry(root, width=100, bg='#a4a4a4', font=("Times New Roman", 20, "bold"))
    item_category_box = Entry(root, width=100, bg='#a4a4a4', font=("Times New Roman", 20, "bold"))
    item_price_box = Entry(root, bg='#a4a4a4', width=100, font=("Times New Roman", 20, "bold"))
    item_description_box = Entry(root, width=100, bg='#a4a4a4', font=("Times New Roman", 20, "bold"))
    submit_button = Button(root, text="Submit", width=50, bg="#40bd40",
                           command=lambda: intermediary_func(item_name_box, item_description_box, item_quantity_box, item_price_box, item_category_box))
    back_button = Button(root, text="Back", command=lambda: root.destroy(), font=("Times New Roman", 15, 'bold'), bg="#c21313")

    # Puts all previously generated text boxes and button on the window
    item_name_box.pack(fill='both', expand=True)
    item_quantity_box.pack(fill='both', expand=True)
    item_category_box.pack(fill='both', expand=True)
    item_description_box.pack(fill='both', expand=True)
    item_price_box.pack(fill='both', expand=True)
    submit_button.pack(fill='both', expand=True)
    back_button.pack(fill='both', expand=True)

    # Configures the Input boxes to fill the page
    item_description_box.config(font=("Times New Roman", 20, "bold"))
    item_quantity_box.config(font=("Times New Roman", 20, "bold"))
    item_category_box.config(font=("Times New Roman", 20, "bold"))
    item_price_box.config(font=("Times New Roman", 20, "bold"))
    item_name_box.config(font=("Times New Roman", 20, "bold"))
    submit_button.config(font=("Times New Roman", 20, "bold"))

    # Puts description of each text box inside
    item_name_box.insert(0, "Item Name")
    item_quantity_box.insert(0, "Item Quantity (Must be a whole number)")
    item_category_box.insert(0, "Item Category")
    item_price_box.insert(0, "Item Price (Must be a number)")
    item_description_box.insert(0, "Item Description")


def save_items_to_json(item_name_box, item_description_box, item_quantity_box, item_price_box, item_category_box):
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


def intermediary_func(item_name_box, item_description_box, item_quantity_box, item_price_box, item_category_box):
    popup()
    save_items_to_json(item_name_box, item_description_box, item_quantity_box, item_price_box, item_category_box)


def popup():
    confirmation = Toplevel()
    confirmation.geometry("500x250")
    confirmation.title("Item Added")
    Label(confirmation, text="This item has been added to the menu", font=("Times New Roman", 20, "bold")).pack()
