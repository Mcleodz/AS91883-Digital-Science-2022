from tkinter import *
import json
import datetime


def items_to_add(items_in_order, checkout_button, order_price, add_item_to_order_button):
    root2 = Tk()
    menu = Entry(root2, width=50, bg="#a3a3a3")
    items_to_add_to_order = Entry(root2, width=50, bg="#a3a3a3")
    add_item_button = Button(root2, text="Add the item", command=lambda: add_item(items_in_order, items_to_add_to_order, checkout_button, order_price, add_item_to_order_button, root2))

    menu.pack()
    items_to_add_to_order.pack()
    add_item_button.pack()

    menu.insert(0, get_menu())

    menu.config(state='readonly')


def get_menu():
    menu = []
    with open("items.json", "r") as json_file:
        json_file_thing = json.load(json_file)
        for i in json_file_thing:
            for j in json_file_thing[i]:
                menu.append(j["item name"])
    return ", ".join(menu)


def add_item(items_in_order, items_to_add_to_order, checkout_button, order_price, add_item_to_order_button, root2):
    global all_items_in_the_order
    all_items_in_the_order = []
    with open("items.json", "r") as json_file:
        json_file_thing = json.load(json_file)
        for i in json_file_thing:
            for j in range(len(json_file_thing[i])):
                if items_to_add_to_order.get() == json_file_thing[i][j]["item name"]:
                    items_in_order.pack()
                    add_item_to_order_button.pack_forget()

                    items_in_order.config(state='normal')
                    items_in_order.insert(END, items_to_add_to_order.get() + ", ")
                    items_in_order.config(state='readonly')
                    all_items_in_the_order.append(items_in_order.get())

                    add_item_to_order_button.config(text="Add another item to order")

                    order_price.pack()
                    add_item_to_order_button.pack()
                    checkout_button.pack()
                    root2.destroy()

                    order_price.config(state='normal')
                    order_price.delete(0, END)
                    order_price.insert(0, "Order Price: $" + str(item_price()))
                    order_price.config(state='readonly')

                    break


def load_new_order_page(old_root):
    old_root.destroy()
    root = Tk()

    customer_name = Entry(root, width=50, bg='#a3a3a3')
    items_in_order = Entry(root, width=50, bg='#a3a3a3')
    add_item_to_order_button = Button(root, text="Add an item to order", command=lambda: items_to_add(items_in_order, checkout_button, order_price, add_item_to_order_button))
    checkout_button = Button(root, text="checkout", command=lambda: checkout(items_in_order, customer_name))
    order_price = Entry(root, width=50, bg='#a3a3a3')

    customer_name.pack()
    add_item_to_order_button.pack()

    customer_name.insert(0, 'Customer name / Table Number')


def checkout(items_in_order, customer_name):
    with open("purchases.txt", "a") as purchases_file:
        purchases_file.write("Customer Name/ Table Number: ")
        purchases_file.write(customer_name.get() + "\n")
        purchases_file.write("Contents: ")
        for i in items_in_order.get():
            purchases_file.write(i)
        purchases_file.write("\n")
        purchases_file.write("Price: ")
        purchases_file.write("$" + str(item_price()) + "\n")
        purchases_file.write("Order's GST: ")
        purchases_file.write("$" + str(get_gst()) + "\n")
    quit()


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


def get_gst():
    order_price = item_price()
    gst = 0.15
    total_gst = gst * order_price
    return total_gst