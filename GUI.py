import customtkinter as tk
from CTkMessagebox import CTkMessagebox
import Material
tk.set_appearance_mode("dark")
tk.set_default_color_theme("dark-blue")


class GUI:

    def __init__(self):

        def calculate_materials():
            data = {}
            for entry, label in entry_label_pairs:
                label_text = label.cget("text")
                entry_text = entry.get()
                if entry_text:
                    data[label_text] = float(entry_text)
            production_report = {}
            for name, amount in data.items():
                Material.combineDict(production_report, Material.material_dict[name].produce(amount))
            if len(production_report) == 0:
                CTkMessagebox(title="Error", message="Enter your required materials first")
                return
            msg = "To produce the items you need:\n"
            for material, requirement in sorted(production_report.items(), key=lambda x: x[0].complexity_rating):
                msg += material.name + ": " + "{:.2f}".format(requirement) + "\n"
            choice = CTkMessagebox(title="Result", message=msg, option_1="Close", option_2="Copy Results")
            if choice.get() == "Copy Results":
                requested_items = "The requested items were:\n"
                for material, requirement in sorted(data.items(),
                                                    key=lambda x: Material.material_dict[x[0]].complexity_rating):
                    requested_items += material + ": " + "{:.2f}".format(requirement) + "\n"
                    root.clipboard_clear()
                    root.clipboard_append(requested_items + "\n" + msg)
                    root.update()

        root = tk.CTk()
        root.title("Material Calculator")
        # Create an empty list to store pairs of Entry and Label widgets
        entry_label_pairs = []

        # Add initial entries
        for i, (name, item) in enumerate(Material.material_dict.items()):
            label = tk.CTkLabel(root, text=name)
            entry = tk.CTkEntry(root)
            label.grid(column=i//5, row=(i % 5)*2)
            entry.grid(column=i//5, row=((i % 5)*2)+1)
            entry_label_pairs.append((entry, label))

        # Add button to send data to the backend
        send_button = tk.CTkButton(root, text="Calculate Materials", command=calculate_materials)
        send_button.grid(row=len(entry_label_pairs) + 1, column=0, columnspan=2)

        root.mainloop()