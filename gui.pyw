import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from workers import api
import res.communicator as com

class GuiListener(com.Listener):
    def on_message(self, message):
        on_message(message)

def on_message(message:str):
    print(message)

com.register_listener(GuiListener())

root = ThemedTk(theme="breeze")
root.title("OK.FIS Deinstallierer")
style = ttk.Style(root)
background_color = style.lookup("TLabel", "background")
root.configure(bg=background_color)

ttk.Label(root, text="OK.FIS Deinstallierer 🚬", font=("Segoe UI Emoji", 14)).pack(pady=20)

uninstall_odb_driver = tk.IntVar()

ttk.Checkbutton(root, text="ODBC Treiber deinstallieren (funktioniert noch nicht)", variable=uninstall_odb_driver).pack(anchor=tk.W, pady=5)

ttk.Button(root, text="Deinstallieren", command=api.uninstall_app).pack(pady=5)
ttk.Button(root, text="Schließen", command=root.quit).pack(pady=5)

if __name__ == "__main__":
    api.run_as_admin()
    root.mainloop()
