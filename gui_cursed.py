import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from PIL import Image, ImageTk
from workers import api
import sys
import os


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

# Create the main window
root = ThemedTk(theme="kroc")
root.title("OK.FIS Deinstallierer 🚬")
style = ttk.Style(root)
background_color = style.lookup("TLabel", "background")  # Get theme's background color
root.configure(bg=background_color)
# Add a label (text)
ttk.Label(root, text="OK.FIS Deinstallierer 🚬", font=("Segoe UI Emoji", 14)).pack(pady=10)

image_path = resource_path("heul.jpg")
image = Image.open(image_path)
resized_image = image.resize((300, 200), Image.LANCZOS)
photo = ImageTk.PhotoImage(resized_image)
image_label = ttk.Label(root, image=photo)
image_label.pack(side=tk.RIGHT, anchor=tk.E, padx=30)

# Add checkboxes
uninstall_odb_driver = tk.IntVar()

ttk.Checkbutton(root, text="ODBC Treiber deinstallieren (funktioniert noch nicht)", variable=uninstall_odb_driver).pack(anchor=tk.W, pady=100)

# Add buttons
ttk.Button(root, text="Deinstallieren jetzt !", command=api.uninstall_app).pack(pady=5)
ttk.Button(root, text="Rausgehen", command=root.quit).pack(pady=5)

# Run the application
if __name__ == "__main__":
    #api.run_as_admin()
    root.mainloop()
