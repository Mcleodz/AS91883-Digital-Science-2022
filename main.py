from add_item_page import *
from remove_item_page import *
from new_order_page import *

# Creates Main Window
root = Tk()
root.geometry("1920x1080")


# Pack's buttons into Main Window
def home_page():
    add_item_button = Button(root, text="Add an Item to Menu", command=lambda: load_add_item_page(root), height=11, width=200, bg="#a2a2a2")
    add_item_button.config(font=('arial', 15))
    add_item_button.pack()

    remove_item_button = Button(root, text="Remove an Item from Menu", command=lambda: load_remove_item_page(root), height=11, width=200, bg="#a2a2a2")
    remove_item_button.config(font=('arial', 15))
    remove_item_button.pack()

    new_order_button = Button(root, text="Create New Order", command=lambda: load_new_order_page(root), height=11, width=200, bg="#a2a2a2")
    new_order_button.config(font=('arial', 15))
    new_order_button.pack()

    quit_button = Button(root, text="Quit", command=lambda: quit(), height=10, width=200, bg="#c21313")
    quit_button.config(font=('arial', 15))
    quit_button.pack()


home_page()
root.mainloop()
