from tkinter import *
import json


def invalid_quantity():
    invalid_quantity = Tk()
    invalid_quantity.geometry("1000x250")
    invalid_quantity.title("Invalid Quantity")
    Label(invalid_quantity, text="This is an invalid Quantity, Please input a whole number to continue", font=("Times New Roman", 20, "bold")).grid(row=0)
    

def load_add_item_page():
    # Generates Window
    root = Tk()
    root.geometry("1920x1080")
    root.title("Add an Item to the Menu")
    root.configure(background="#a4a4a4")

    # Creates Labels to describe what the text entry boxes DO!
    item_name_box_label = Label(root, width=60, bg='#c3c3c3', text="Item Name")
    item_quantity_box_label = Label(root, width=60, bg='#c3c3c3', text="Item Quantity (Must be a Whole Number")
    item_category_box_label = Label(root, width=60, bg='#c3c3c3', text="Item Category")
    item_description_box_label = Label(root, width=60, bg='#c3c3c3', text="Item Description")
    item_price_box_label = Label(root, width=60, bg='#c3c3c3', text="Item Price (Must be a Number")

    # Generates Text input boxes and buttons
    item_name_box = Entry(root, width=100, bg='#a4a4a4', font=("Times New Roman", 20, "bold"))
    item_quantity_box = Entry(root, width=100, bg='#a4a4a4', font=("Times New Roman", 20, "bold"))
    item_category_box = Entry(root, width=100, bg='#a4a4a4', font=("Times New Roman", 20, "bold"))
    item_price_box = Entry(root, bg='#a4a4a4', width=100, font=("Times New Roman", 20, "bold"))
    item_description_box = Entry(root, width=100, bg='#a4a4a4', font=("Times New Roman", 20, "bold"))
    submit_button = Button(root, text="Submit", width=50, bg="#40bd40",
                           command=lambda: save_items_to_json(item_name_box, item_description_box, item_quantity_box, item_price_box, item_category_box))
    back_button = Button(root, text=" Back ", command=lambda: root.destroy(), font=("Times New Roman", 15, 'bold'), bg="#c21313")

    # Puts all previously generated labels into the load item window
    item_name_box_label.grid(row=0, column=0)
    item_quantity_box_label.grid(row=1, column=0)
    item_category_box_label.grid(row=2, column=0)
    item_description_box_label.grid(row=3, column=0)
    item_price_box_label.grid(row=4, column=0)
    submit_button.grid(row=5, column=1, sticky=W, pady=2)
    back_button.grid(row=5, column=0, sticky=W, pady=2)

    # Puts all previously generated text boxes and buttons on the window
    item_name_box.grid(row=0, column=1)
    item_quantity_box.grid(row=1, column=1)
    item_category_box.grid(row=2, column=1)
    item_description_box.grid(row=3, column=1)
    item_price_box.grid(row=4, column=1)

    # Configures the Input boxes labels to fill the page
    item_description_box_label.config(font=("Times New Roman", 20, "bold"))
    item_quantity_box_label.config(font=("Times New Roman", 20, "bold"))
    item_category_box_label.config(font=("Times New Roman", 20, "bold"))
    item_price_box_label.config(font=("Times New Roman", 20, "bold"))
    item_name_box_label.config(font=("Times New Roman", 20, "bold"))

    item_price_box.config(font=("Times New Roman", 20, "bold"))
    item_description_box.config(font=("Times New Roman", 20, "bold"))
    item_category_box.config(font=("Times New Roman", 20, "bold"))
    item_quantity_box.config(font=("Times New Roman", 20, "bold"))
    item_name_box.config(font=("Times New Roman", 20, "bold"))

    submit_button.config(font=("Times New Roman", 20, "bold"), height=5, width=60)
    back_button.config(font=("Times New Roman", 20, "bold"), height=5, width=60)


def save_items_to_json(item_name_box, item_description_box, item_quantity_box, item_price_box, item_category_box):
    # Puts all user inputs in dictionary
    if not str(item_quantity_box.get()).isnumeric():
        invalid_quantity()

    else:
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
        popup()


def popup():
    confirmation = Toplevel()
    confirmation.geometry("500x250")
    confirmation.title("Item Added")
    confirmation_label = Label(confirmation, text="This item has been added to the menu", font=("Times New Roman", 20, "bold"))
    confirmation_label.grid(row=0, column=3)
