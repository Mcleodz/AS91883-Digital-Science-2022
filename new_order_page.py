import json
from tkinter import *
from functools import partial
from datetime import datetime

global order
order = []

################################################ Loading New Order Page ################################################


def load_new_order_page():
    root = Tk()
    root.title("New Order")
    root.geometry("1920x1080")

    customer_name_entry = Entry(root, width=50, bg='#a3a3a3', font=("Times New Roman", 15, 'bold'))
    customer_name_entry.pack(fill="both", expand=True)
    customer_name_entry.insert(0, "(customer name / table number)")
    customer_name = customer_name_entry.get()

    order_displayed = Entry(root, width=50, bg='#a3a3a3', font=("Times New Roman", 15, 'bold'))
    order_displayed.pack(fill="both", expand=True)
    order_displayed.insert(0, "")
    order_displayed.insert(0, ", ".join(order))
    order_displayed.config(state="readonly")

    order_price_displayed = Entry(root, width=50, bg='#a3a3a3', font=("Times New Roman", 15, 'bold'))
    order_price_displayed.pack(fill="both", expand=True)
    order_price_displayed.insert(0, "$" + str(item_price()))
    order_price_displayed.config(state="readonly")

    add_items_button = Button(root, text="Add an item to the order", command=lambda: add_items(root), font=("Times New Roman", 15, 'bold'), bg="#a3a3a3")
    add_items_button.pack(fill="both", expand=True)

    remove_an_item_button = Button(root, text="Remove an item from the order", command=lambda:remove_items(root), font=("Times New Roman", 15, 'bold'), bg="#a3a3a3")
    remove_an_item_button.pack(fill="both", expand=True)

    purchase_button = Button(root, text="Checkout", command=lambda: checkout(customer_name, root), font=("Times New Roman", 15, 'bold'), bg="#40bd40")
    purchase_button.pack(fill="both", expand=True)

    back_button = Button(root, text="Back", command=lambda: root.destroy(), font=("Times New Roman", 15, 'bold'), bg="#c21313")
    back_button.pack(fill="both", expand=True)

############################################## Adding items to users order #############################################


def add_items(root):
    root2 = Toplevel()
    root2.title("add item to order")
    root2.geometry("1920x1080")

    root.destroy()

    button_identities = []
    button_count = 0

    with open("items.json", "r") as json_file:
        json_object = json.load(json_file)
        for i in json_object:
            new_label = Label(root2, text=i, font=("Times New Roman", 15, "bold"), bg="#a2a2a2")
            new_label.pack(fill="both", expand=True)
            for j in json_object[i]:
                new_button = Button(root2, text=(j["item name"]), font=("Times New Roman", 15, "bold"), command=partial(add_to_order, button_count, button_identities), bg="#40bd40")
                new_button.pack(fill="both", expand=True)
                button_identities.append(new_button)
                button_count += 1

    submit_button = Button(root2, text="Submit", command=lambda: int_func(root2), font=("Times New Roman", 15, 'bold'), bg="#a3a3a3")
    submit_button.pack(fill="both", expand=True)


def add_to_order(button_count, button_identities):
    button_name = (button_identities[button_count])
    with open("items.json", "r") as json_file_read:
        json_object = json.load(json_file_read)
        for i in json_object:
            for j in json_object[i]:
                if button_name["text"] == j["item name"]:
                    order.append(j["item name"])
                    new_item_count = int(j["item quantity"]) - 1

    with open("items.json", "w") as json_file_write:
        for k in json_object:
            for l in json_object[k]:
                if l["item name"] == button_name["text"]:
                    l["item quantity"] = str(new_item_count)
        json_file_write.write(json.dumps(json_object, indent=4))
        json_file_write.close()

################################################### Saving Order Info ##################################################

def checkout(customer_name, root):
    time_of_order = datetime.now()
    root.destroy()
    with open("purchases.txt", "a") as purchases:
        purchases.write("\n")
        purchases.write("\n")
        purchases.write("Time: " + time_of_order.strftime("%d/%m/%Y %H:%M:%S") + "\n")
        purchases.write("Customer/Table Number: " + customer_name)
        purchases.write("\n")
        purchases.write("Order: " + ", ".join(order))
        purchases.write("\n")
        purchases.write("Order Price: " + str(item_price()))
        purchases.write("\n")
        purchases.write("Order GST: " + str(get_gst()))


# Calculates the total price of the order
def item_price():
    all_items = order
    price = 0
    with open("items.json", "r") as json_file:
        json_file_thing = json.load(json_file)
        for item in all_items:
            for i in json_file_thing:
                for j in json_file_thing[i]:
                    if j["item name"] == item:
                        price += float(j['item price'])
    return price


# Calculates the GST Value of the order
def get_gst():
    order_price = item_price()
    gst = 0.15
    unrounded_total_gst = gst * order_price
    rounded_total_gst = float(str("{:0.2f}".format(unrounded_total_gst)))
    return rounded_total_gst


def int_func(root2):
    root2.destroy()
    load_new_order_page()


############################################## Removing Items from order ##############################################

def remove_items(root2):
    root = Tk()
    root.geometry("1920x1080")
    root.title("Remove items from order")

    button_identities = []
    button_count = 0

    for i in order:
        new_button = Button(root, text=i, font=("Times New Roman", 15, "bold"), command=partial(remove_from_order, button_identities, button_count, root2, root), bg="#40bd40")
        new_button.pack(fill="both", expand=True)
        button_identities.append(new_button)
        button_count += 1

    back_button = Button(root, text="Back", command=lambda: root.destroy(), font=("Times New Roman", 15, 'bold'), bg="#a3a3a3")
    back_button.pack(fill="both", expand=True)


def remove_from_order(button_identities, button_count, root3, root):
    button_name = (button_identities[button_count])
    for i in order:
        if button_name["text"] == i:
            order.remove(i)
            button_name.pack_forget()
            int_func(root3)
            root.destroy()

    with open("items.json", "r") as json_file_read:
        json_object = json.load(json_file_read)
        for j in json_object:
            for k in json_object[j]:
                if button_name["text"] == k["item name"]:
                    order.append(k["item name"])
                    new_item_count = int(k["item quantity"]) + 1

    with open("items.json", "w") as json_file_write:
        for l in json_object:
            for m in json_object[l]:
                if m["item name"] == button_name["text"]:
                    m["item quantity"] = str(new_item_count)
        json_file_write.write(json.dumps(json_object, indent=4))
        json_file_write.close()