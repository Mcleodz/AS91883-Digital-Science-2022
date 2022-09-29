from tkinter import *
import json
from datetime import datetime


# Alerts the user of an item being out of stock
def out_of_stock_alert(item):
    out_of_stock = Toplevel()
    out_of_stock.geometry("1000x50")
    out_of_stock.title("out of stock item")
    Label(out_of_stock, text=item + " is out of stock", font=("Times New Roman", 20, "bold")).pack()


def incorrectly_spelt():
    out_of_stock = Toplevel()
    out_of_stock.geometry("1000x50")
    out_of_stock.title("item is incorrectly spelt")
    Label(out_of_stock, text="this item is not spelt correctly, Please try again", font=("Times New Roman", 20, "bold")).pack()


# Makes page to add items to the order
def items_to_add(items_in_order, checkout_button, order_price, add_item_to_order_button, back_button):
    root2 = Tk()
    root2.title("Add an item to the menu")
    root2.geometry("1920x1080")

    menu = Entry(root2, width=50, bg="#a3a3a3", font=("Times New Roman", 15, 'bold'))
    items_to_add_to_order = Entry(root2, width=50, bg="#a3a3a3", font=("Times New Roman", 15, 'bold'))
    add_item_button = Button(root2, text="Add the item", command=lambda: add_item(items_in_order, items_to_add_to_order, checkout_button, order_price, add_item_to_order_button, back_button, root2), font=("Times New Roman", 15, 'bold'), bg="#40bd40")
    back_button2 = Button(root2, text="Back", command=lambda: root2.destroy(), font=("Times New Roman", 15, 'bold'), bg="#c21313")

    menu.pack(fill="both", expand=True)

    items_to_add_to_order.pack(fill="both", expand=True)
    add_item_button.pack(fill="both", expand=True)
    back_button2.pack(fill='both', expand=True)

    menu.insert(0, get_menu())
    items_to_add_to_order.insert(0, "(Type items to add here)")

    menu.config(state='readonly')


# Gets all items on the menu
def get_menu():
    menu = []
    with open("items.json", "r") as json_file:
        json_file_thing = json.load(json_file)
        for i in json_file_thing:
            for j in json_file_thing[i]:
                menu.append(j["item name"])
    return ", ".join(menu)


# Adds the requested item to the order
def add_item(items_in_order, items_to_add_to_order, checkout_button, order_price, add_item_to_order_button, back_button, root2):
    global all_items_in_the_order
    all_items_in_the_order = []
    items_to_be_added_to_the_order = items_to_add_to_order.get()
    # Finds the requested item on the menu
    with open("items.json", "r") as json_file:
        json_file_thing = json.load(json_file)
        for i in json_file_thing:
            for j in range(len(json_file_thing[i])):
                if items_to_be_added_to_the_order.lower() == json_file_thing[i][j]["item name"]:
                    # Adds the requested item to the order along with the price
                    items_in_order.pack(fill='both')
                    add_item_to_order_button.pack_forget()
                    back_button.pack_forget()

                    items_in_order.config(state='normal')
                    items_in_order.insert(END, items_to_add_to_order.get() + ", ")
                    items_in_order.config(state='readonly', bg="#a3a3a3")
                    all_items_in_the_order.append(items_in_order.get())

                    add_item_to_order_button.config(text="Add another item to order")

                    order_price.pack(fill='both', expand=True)
                    add_item_to_order_button.pack(fill='both', expand=True)
                    checkout_button.pack(fill='both', expand=True)
                    back_button.pack(fill='both', expand=True)

                    root2.destroy()

                    order_price.config(state='normal')
                    order_price.delete(0, END)
                    order_price.insert(0, "Order Price: $" + str(item_price()))
                    order_price.config(state='readonly', bg="#a3a3a3")

                    break
                else:
                    # If the requested item is not on the menu, the user is notified
                    incorrectly_spelt()


# Loads the "New Order Page" and destroys old root
def load_new_order_page():
    root = Tk()
    root.title("New Order")
    root.geometry("1920x1080")

    back_button = Button(root, text="Back", command=lambda: root.destroy(), font=("Times New Roman", 15, 'bold'), bg="#c21313")
    customer_name = Entry(root, width=50, bg='#a3a3a3', font=("Times New Roman", 15, 'bold'))
    items_in_order = Entry(root, width=50, bg='#a3a3a3', font=("Times New Roman", 15, 'bold'))
    add_item_to_order_button = Button(root, text="Add an item to order", command=lambda: items_to_add(items_in_order, checkout_button, order_price, add_item_to_order_button, back_button), font=("Times New Roman", 15, 'bold'), bg="#b3b3b3")
    checkout_button = Button(root, text="Checkout", command=lambda: checkout(items_in_order, customer_name), font=("Times New Roman", 15, 'bold'), bg="#40bd40")
    order_price = Entry(root, width=50, bg='#a3a3a3', font=("Times New Roman", 15, 'bold'))

    customer_name.pack(fill="both", expand=True)
    add_item_to_order_button.pack(fill="both", expand=True)
    back_button.pack(fill="both", expand=True)

    customer_name.insert(0, 'Customer name / Table Number')


# Saves the contents of the order to a file and runs code to remove the amount of items from the menu
def checkout(items_in_order, customer_name):
    time_of_order = datetime.now()
    with open("purchases.txt", "a") as purchases_file:
        purchases_file.write("\n")
        purchases_file.write("\n")
        purchases_file.write("Time: " + time_of_order.strftime("%d/%m/%Y %H:%M:%S") + "\n")
        purchases_file.write("Customer Name/ Table Number: ")
        purchases_file.write(customer_name.get() + "\n")
        purchases_file.write("Contents: ")
        for i in items_in_order.get():
            purchases_file.write(i)
        purchases_file.write("\n")
        purchases_file.write("Price: ")
        purchases_file.write("$" + str(item_price()) + "\n")
        purchases_file.write("Order's GST: ")
        purchases_file.write("$" + str(get_gst()))
        subtract_item()


# Calculates the total price of the order
def item_price():
    all_items = "".join(all_items_in_the_order)
    all_items = all_items.split(", ")
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
    total_gst = gst * order_price
    return total_gst


# Removes one from the quantity of every item in the order
def subtract_item():
    # Opens Json file in read mode to get value of the quantity
    all_items = "".join(all_items_in_the_order).strip(",")
    all_items = all_items.split(", ")
    with open("items.json", "r") as json_file:
        json_file_thing = json.load(json_file)
        for item in all_items:
            for i in json_file_thing:
                for j in json_file_thing[i]:
                    if j["item name"] == item:
                        # Checks if the new quantity is a valid quantity
                        if int(j["item quantity"])-1 == (0-1):
                            out_of_stock_alert(item)
                        else:
                            new_quantity = int(j["item quantity"])-1
                            json_file.close()
                            # Re-opens the file and overwrites the original quantity
                            with open("items.json", "w") as json_file_write:
                                for item in all_items:
                                    for k in json_file_thing:
                                        for l in json_file_thing[k]:
                                            if l["item name"] == item:
                                                l["item quantity"] = str(new_quantity)
                                json_file_write.write(json.dumps(json_file_thing, indent=4))
                                json_file_write.close()
                                quit()
