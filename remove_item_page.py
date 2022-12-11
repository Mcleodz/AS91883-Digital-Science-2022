from tkinter import *
import json
from functools import partial


def load_remove_item_page():

    root = Tk()
    root.title("Remove Item")
    root.geometry("1920x1080")

    button_identities = []
    button_count = 0

    with open("items.json", "r") as json_file:
        json_object = json.load(json_file)
        for i in json_object:
            new_label = Label(root, text=i + "s to remove:", font=("Times New Roman", 15, "bold"), bg="#a2a2a2")
            new_label.pack(fill="both", expand=True)
            for j in json_object[i]:
                new_button = Button(root, text=(j["item name"]), font=("Times New Roman", 15, "bold"), command=partial(delete, button_count, button_identities), bg="#40bd40")
                new_button.pack(fill="both", expand=True)
                button_identities.append(new_button)
                button_count += 1
    back_button = Button(root, text="Back", command=lambda: root.destroy(), font=("Times New Roman", 15, 'bold'), bg="#c21313")
    back_button.pack(fill="both", expand=True)


def delete(button_count, button_identities):
    button_name = (button_identities[button_count])
    with open("items.json", "r") as json_file_read:
        json_object = json.load(json_file_read)
        for i in json_object:
            for j in json_object[i]:
                if button_name["text"] == j["item name"]:
                    button_name.pack_forget()
                    json_object[i].remove(j)

    with open("items.json", "w") as json_file:
        to_write = json.dumps(json_object, indent=4)
        json_file.write(to_write)

