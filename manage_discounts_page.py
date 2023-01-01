from tkinter import *
import json


# Load "Manage Discount Page"
def load_manage_discount_page():
    manage_discounts_root = Tk()
    manage_discounts_root.geometry("1920x1080")
    manage_discounts_root.title("Manage Discounts")

    add_discounts_button = Button(manage_discounts_root, text="Discount an Item", command=lambda: add_discount(),
                                  height=8, width=200, bg="#a2a2a2")
    add_discounts_button.config(font=("Times New Roman", 15, "bold"))
    add_discounts_button.pack(fill="both", expand=True)

    view_discounts_button = Button(manage_discounts_root, text="View active discounts",
                                   command=lambda: view_discounts(), height=8, width=200, bg="#a2a2a2")
    view_discounts_button.config(font=("Times New Roman", 15, "bold"))
    view_discounts_button.pack(fill='both', expand=True)

    remove_discounts_button = Button(manage_discounts_root, text="Remove a Discount", command=lambda: remove_discount(),
                                     height=8, width=200, bg="#a2a2a2")
    remove_discounts_button.config(font=("Times New Roman", 15, "bold"))
    remove_discounts_button.pack(fill="both", expand=True)

    back_button = Button(manage_discounts_root, text=" Back ", command=lambda: manage_discounts_root.destroy(),
                         height=8,
                         font=("Times New Roman", 15, 'bold'), bg="#c21313")
    back_button.config(font=("Times New Roman", 15, "bold"))
    back_button.pack(fill="both", expand=True)


############################################### Add a Discount Code ####################################################


def item_does_not_exist(item_to_discount):
    item_does_not_exist = Tk()
    item_does_not_exist.geometry("1000x250")
    item_does_not_exist.title("Item Does not exist")
    Label(item_does_not_exist, text=f"'{item_to_discount.get()}' is not on the menu, please enter an existing item",
          font=("Times New Roman", 20, "bold")).pack(side="top")


def item_already_discounted():
    item_already_discounted = Toplevel()
    item_already_discounted.geometry("1000x250")
    item_already_discounted.title("Item has already been discounted")
    Label(item_already_discounted,
          text=" This item has already been discounted, please remove the current discount and try again",
          font=("Times New Roman", 20, "bold")).pack(side="top")


def not_valid_percentage():
    invalid_percentage = Tk()
    invalid_percentage.geometry("1000x250")
    invalid_percentage.title("Invalid Percentage Given")
    Label(invalid_percentage,
          text=f"""'{percentage_discount.get()}' is not a valid percentage.
           please enter a number between 0 and 1.
           Please EXCLUDE the percentage sign (%)""",
          font=("Times New Roman", 20, "bold")).pack(side="top")


def confirmation_of_submission(add_discount_root, item_to_discount):
    global discount_names
    global percentages

    confirmation_of_submission_root = Tk()
    confirmation_of_submission_root.geometry("1000x250")
    confirmation_of_submission_root.title("Confirm submission")
    Button(confirmation_of_submission_root, text="Confirm Submission",
           command=lambda: save_discount(add_discount_root, item_to_discount,
                                         confirmation_of_submission_root), font=("Times New Roman", 15, "bold"),
           bg="#a3a3a3").pack(fill='both', expand=True)

    percentages = percentage_discount.get()
    discount_names = item_to_discount.get().lower()



# Checks validity of users input before continuing
def validity(item_to_discount, add_discount_root):
    if check_item(item_to_discount):
        if check_percentage(percentage_discount):
            confirmation_of_submission(add_discount_root, item_to_discount)


    else:
        item_does_not_exist(item_to_discount)


def check_item(item_to_discount):
    item_list = []
    with open("items.json", "r") as json_file:
        json_file_thing = json.load(json_file)
        item_list = item_to_discount.get().lower()
        item_list2 = "".join(item_list)
        item_list3 = item_list2.split(", ")
        for item in item_list3:
            for i in json_file_thing:
                for j in json_file_thing[i]:
                    if j["item name"] == item:
                        return True
                    else:
                        item_existence = False
        if item_existence == False:
            return False


# Checks if entered percentage is a valid decimalised form of a percentage
def check_percentage(percentage_discount):
    try:
        if float(percentage_discount.get()) >= 1 or float(percentage_discount.get()) <= 0:
            not_valid_percentage()

        else:
            return True

    except ValueError:
        not_valid_percentage()


def add_discount():
    global percentage_discount

    # Loading "add discount" page
    add_discount_root = Tk()
    add_discount_root.geometry("1920x1080")
    add_discount_root.title("Add a Discount")

    # Loading menu
    menu_label = Entry(add_discount_root, width=50, bg='#a3a3a3', font=("Times New Roman", 15, 'bold'))
    menu_label.pack(fill="both", expand=True)
    menu_label.insert(0, get_menu())
    menu_label.config(state='readonly')

    # Loading "item to discount" input box
    item_to_discount = Entry(add_discount_root, width=50, bg='#a3a3a3', font=("Times New Roman", 15, 'bold'))
    item_to_discount.pack(fill="both", expand=True)
    item_to_discount.insert(0, "(Type the name of the item you would like to discount)")

    # Loading "percentage to discount item" Input box
    percentage_discount = Entry(add_discount_root, width=50, bg='#a3a3a3', font=("Times New Roman", 15, 'bold'))
    percentage_discount.pack(fill="both", expand=True)
    percentage_discount.insert(0,
                               "(Enter the DECIMAL FORM (e.g 0.5) of the percentage discount you would like to apply to your selected item")

    # Loading "submit" Button
    submit_button = Button(add_discount_root, text="Submit",
                           command=lambda: validity(item_to_discount, add_discount_root), width=50,
                           bg='#40bd40',
                           font=("Times New Roman", 15, 'bold'))
    submit_button.pack(fill="both", expand=True)

    # Loading "Back" Button
    back_button = Button(add_discount_root, text=" Back ", command=lambda: add_discount_root.destroy(),
                         font=("Times New Roman", 15, 'bold'), bg="#c21313")
    back_button.config(font=("Times New Roman", 15, "bold"))
    back_button.pack(fill="both", expand=True)


def save_discount(add_discount_root, item_to_discount, confirmation_of_submission_root):

    confirmation_of_submission_root.destroy()
    add_discount_root.destroy()

    with open("items.json", "r") as json_file:
        json_file_thing = json.load(json_file)
        for i in json_file_thing:
            for j in json_file_thing[i]:
                if j["item name"] == discount_names:
                    non_discounted_price = j["item price"]

                    discount_json_object = {
                        "discount": percentages,
                        "non discounted price": non_discounted_price
                    }
                    for i in range(1):
                        with open("discounts_applied.json", "r") as json_file:
                            json_file_thing = json.load(json_file)
                            if not discount_names in json_file_thing:
                                json_file_thing[discount_names] = []
                            else:
                                item_already_discounted()
                                break

                            json_file_thing[discount_names].append(discount_json_object)
                            test = json.dumps(json_file_thing, indent=4)

                        with open("discounts_applied.json", "w") as json_file:
                            json_file.write(test)

                        apply_discounts()


############################################  Viewing Active Discount Code  ############################################


def view_discounts():
    # Loading page
    view_discount_page_root = Tk()
    view_discount_page_root.geometry("1920x1080")
    view_discount_page_root.title("View Active Discounts")

    discount_names = Entry(view_discount_page_root, width=50, bg='#a3a3a3', font=("Times New Roman", 15, 'bold'))
    discount_names.pack(fill="both", expand=True)
    discount_names.insert(0, get_active_discount_names())
    discount_names.config(state='readonly')

    discount_percentages = Entry(view_discount_page_root, width=50, bg='#a3a3a3', font=("Times New Roman", 15, 'bold'))
    discount_percentages.pack(fill='both', expand=True)
    discount_percentages.insert(0, get_active_discount_percentages())
    discount_percentages.config(state='readonly')

    back_button = Button(view_discount_page_root, text=" Back ", command=lambda: view_discount_page_root.destroy(),
                         font=("Times New Roman", 15, 'bold'), bg="#c21313")
    back_button.config(font=("Times New Roman", 15, "bold"))
    back_button.pack(fill="both", expand=True)


def get_active_discount_names():
    discount_name = []
    with open("discounts_applied.json", "r") as active_discounts:
        discounts = json.load(active_discounts)
        for i in discounts:
            for j in discounts[i]:
                discount_name.append(i)
    discount_name = "    ".join(discount_name)
    return discount_name


def get_active_discount_percentages():
    discount_percentages = []
    with open("discounts_applied.json", "r") as active_discounts:
        discounts = json.load(active_discounts)
        for i in discounts:
            for j in discounts[i]:
                discount_percentages.append(str(float(j["discount"])*100))
    discount_percentages = "%   ".join(discount_percentages)
    return f"{discount_percentages}%"


#############################################  Removing Discount Code  #################################################


def remove_discount():
    remove_discount_root = Tk()
    remove_discount_root.geometry("1920x1080")
    remove_discount_root.title("Remove a Discount")

    discount_names = Entry(remove_discount_root, width=50, bg='#a3a3a3', font=("Times New Roman", 15, 'bold'))
    discount_names.pack(fill="both", expand=True)
    discount_names.insert(0, get_active_discount_names())
    discount_names.config(state="readonly")

    discount_to_remove = Entry(remove_discount_root, width=50, bg='#a3a3a3', font=("Times New Roman", 15, 'bold'))
    discount_to_remove.pack(fill='both', expand=True)
    discount_to_remove.insert(0, "(Enter the name of the discount you would like to remove)")

    submit_button = Button(remove_discount_root, text="Submit",
                           command=lambda: removing_discount(discount_to_remove), width=50,
                           bg='#40bd40',
                           font=("Times New Roman", 15, 'bold'))
    submit_button.pack(fill="both", expand=True)

    back_button = Button(remove_discount_root, text=" Back ", command=lambda: remove_discount_root.destroy(),
                         font=("Times New Roman", 15, 'bold'), bg="#c21313")
    back_button.config(font=("Times New Roman", 15, "bold"))
    back_button.pack(fill="both", expand=True)


def removing_discount(discount_to_remove):
    discount_being_removed = discount_to_remove.get().lower()

    remove_discount_from_price(discount_being_removed)

    with open("discounts_applied.json", "r") as json_file:
        json_file_thing = json.load(json_file)
        for i in json_file_thing:
            if discount_being_removed == i:
                json_file_thing.pop(i)
                break

    with open("discounts_applied.json", "w") as json_file:
        test = json.dumps(json_file_thing, indent=4)
        json_file.write(test)

    remove_discount_from_price(discount_being_removed)


################################################  Apply Discounts Code  ################################################


def apply_discounts():
    discount = percentages.strip("%")
    discount = float(discount)

    with open("items.json", "r") as json_file:
        json_file_thing = json.load(json_file)
        for i in json_file_thing:
            for j in json_file_thing[i]:
                if j["item name"] == discount_names:
                    discounted_price = float(j["item price"]) - (float(j["item price"]) * discount)

    with open("items.json", "w") as json_file_write:
        for k in json_file_thing:
            for l in json_file_thing[k]:
                if l["item name"] == discount_names:
                    l["item price"] = str(float(discounted_price))
                    json_file_write.write(json.dumps(json_file_thing, indent=4))


#############################################  Un-Applying Discounts Code  #############################################


def remove_discount_from_price(discount_being_removed):
    with open("discounts_applied.json", "r") as json_file:
        json_file_thing = json.load(json_file)
        for i in json_file_thing:
            for j in json_file_thing[i]:
                if i == discount_being_removed:
                    non_discounted_price = j["non discounted price"]
                    json_file.close()

                    with open("items.json", "r") as json_file_read:
                        json_file_read_thing = json.load(json_file_read)
                        for k in json_file_read_thing:
                            for l in json_file_read_thing[k]:
                                if l["item name"] == discount_being_removed:
                                    l["item price"] = non_discounted_price
                                    json_file_read.close()

                                    with open("items.json", "w") as json_file_write:
                                        json_file_write_thing = json.dumps(json_file_read_thing, indent=4)
                                        json_file_write.write(json_file_write_thing)
                                        json_file_write.close()

# Gets all items on the menu
def get_menu():
    menu = []
    with open("items.json", "r") as json_file:
        json_file_thing = json.load(json_file)
        for i in json_file_thing:
            for j in json_file_thing[i]:
                menu.append(j["item name"])
    return ", ".join(menu)