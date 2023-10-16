import customtkinter as tk

from CTkMessagebox import CTkMessagebox
import Material
tk.set_appearance_mode("dark")
tk.set_default_color_theme("dark-blue")


class GUI:

    def __init__(self):

        def calculate_materials():
            data = {}
            for entry, menu in entry_label_pairs:
                menu_text = menu.get()
                entry_text = entry.get()
                if entry_text:
                    data[menu_text] = float(entry_text)
            production_report = {}
            for name, amount in data.items():
                current_item, _ = Material.name_to_item_dict[name]
                Material.combineDict(production_report,  current_item.produce(amount))

            if len(production_report) == 0:
                CTkMessagebox(title="Result", message="To produce the items you need:\nNothing", option_1="Close")
                return
            msg = "To produce the items you need:\n"
            for material, requirement in sorted(production_report.items(), key=lambda x: x[0].complexity_rating):
                msg += material.names[0] + ": " + "{:.2f}".format(requirement) + "\n"
            choice = CTkMessagebox(title="Result", message=msg, option_1="Close", option_2="Copy Results")
            if choice.get() == "Copy Results":
                requested_items = "The requested items were:\n"
                for material, requirement in sorted(data.items(),
                                                    key=lambda x: Material.name_to_item_dict[x].complexity_rating):
                    requested_items += material + ": " + "{:.2f}".format(requirement) + "\n"
                    root.clipboard_clear()
                    root.clipboard_append(requested_items + "\n" + msg)
                    root.update()

        def item_selected(name):
            current_item, recipe_index = Material.name_to_item_dict[name]
            current_item.recipe = recipe_index

        root = tk.CTk()
        root.title("Material Calculator")
        # Create an empty list to store pairs of Entry and Label widgets
        entry_label_pairs = []
        rows = ((len(Material.material_list) % 5)*2)+1
        columns = (len(Material.material_list) // 5)


        # Add initial entries
        for i, item in enumerate(Material.material_list):
            width = 160
            var = tk.StringVar()
            menu = tk.CTkOptionMenu(root, variable=var, values=item.names, dropdown_hover_color="gray30",
                                    fg_color="DodgerBlue4", button_color="gray30", button_hover_color="gray60", width=width,
                                  command=item_selected)
            menu.set(item.names[item.recipe])
            entry = tk.CTkEntry(root, width=width)
            menu.grid(column=i//5, row=(i % 5)*2)
            entry.grid(column=i//5, row=((i % 5)*2)+1)
            entry_label_pairs.append((entry, menu))


        # Add button to send data to the backend
        send_button = tk.CTkButton(root, text="Calculate Materials", command=calculate_materials)
        send_button.grid(row=len(entry_label_pairs) + 1, column=0, columnspan=2)



        root.mainloop()
