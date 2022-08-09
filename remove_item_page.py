def load_remove_item_page(old_root):
    # Generates Window
    old_root.destroy()
    root = Tk()

    with open("items.json", "r") as json_file:
        json_file_thing = json.load(json_file)

    list_of_items = Entry(root, width=50, bg='a3a3a3', state=disabled)
    list_of_items.pack()
    list_of_items.insert(0, )
