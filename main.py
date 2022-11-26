from add_item_page import load_add_item_page
from remove_item_page import load_remove_item_page
from new_order_page import load_new_order_page
from manage_discounts_page import load_manage_discount_page
from tkinter import *

# Creates Main Window
root = Tk()
root.geometry("1920x1080")
root.title("Home")


# Pack's buttons into Main Window
def home_page():
    add_item_button = Button(root, text="Add an Item to Menu", command=lambda: load_add_item_page(), height=6, width=200, bg="#a2a2a2")
    add_item_button.config(font=("Times New Roman", 15, "bold"))
    add_item_button.pack(fill="both", expand=True)

    remove_item_button = Button(root, text="Remove an Item from Menu", command=lambda: load_remove_item_page(), height=6, width=200, bg="#a2a2a2")
    remove_item_button.config(font=("Times New Roman", 15, "bold"))
    remove_item_button.pack(fill="both", expand=True)

    new_order_button = Button(root, text="Create New Order", command=lambda: load_new_order_page(), height=6, width=200, bg="#a2a2a2")
    new_order_button.config(font=("Times New Roman", 15, "bold"))
    new_order_button.pack(fill="both", expand=True)

    manage_discount_button = Button(root, text="Manage Discounts", command=lambda: load_manage_discount_page(), height=6, width=200, bg="#a2a2a2")
    manage_discount_button.config(font=("Times New Roman", 15, "bold"))
    manage_discount_button.pack(fill="both", expand=True)

    quit_button = Button(root, text="Quit", command=lambda: quit(), height=6, width=200, bg="#c21313")
    quit_button.config(font=("Times New Roman", 15, "bold"))
    quit_button.pack(fill="both", expand=True)


home_page()
root.mainloop()
