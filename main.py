from add_item_page import *
from remove_item_page import *
from new_order_page import *

# Creates Main Window
root = Tk()
root.geometry("1920x1080")
root.title("Main")


# Pack's buttons into Main Window
def home_page():
    add_item_button = Button(root, text="Add an Item to Menu", command=lambda: load_add_item_page(root), height=9, width=200, bg="#a2a2a2")
    add_item_button.config(font=("Times New Roman", 20, "bold"))
    add_item_button.pack(fill="both", expand=True)

    remove_item_button = Button(root, text="Remove an Item from Menu", command=lambda: load_remove_item_page(root), height=9, width=200, bg="#a2a2a2")
    remove_item_button.config(font=("Times New Roman", 20, "bold"))
    remove_item_button.pack(fill="both", expand=True)

    new_order_button = Button(root, text="Create New Order", command=lambda: load_new_order_page(root), height=9, width=200, bg="#a2a2a2")
    new_order_button.config(font=("Times New Roman", 20, "bold"))
    new_order_button.pack(fill="both", expand=True)

    quit_button = Button(root, text="Quit", command=lambda: quit(), height=9, width=200, bg="#c21313")
    quit_button.config(font=("Times New Roman", 20, "bold"))
    quit_button.pack(fill="both", expand=True)


home_page()
root.mainloop()
