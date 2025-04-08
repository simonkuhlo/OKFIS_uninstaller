import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from workers import api
import res.communicator as com

class GuiListener(com.Listener):
    def on_message(self, message):
        on_message(message)

def on_message(message:str):
    output_text.config(state="normal")
    output_text.insert("end", "\n" + message)
    output_text.config(state="disabled")
    print(message)

com.register_listener(GuiListener())

root = ThemedTk(theme="breeze")
root.title("OK.FIS Deinstallierer")
style = ttk.Style(root)
background_color = style.lookup("TLabel", "background")
root.configure(bg=background_color)

ttk.Label(root, text="OK.FIS Deinstallierer 🚬", font=("Segoe UI Emoji", 14)).pack(pady=20)

# Create a frame to hold the Text widget and scrollbar
frame = ttk.Frame(root)
frame.pack(fill="both", expand=True, padx=10, pady=10)

# Create a Text widget for displaying output
output_text = tk.Text(frame, state="disabled", wrap="word", height=15)
output_text.pack(side="left", fill="both", expand=True)

# Create a vertical scrollbar and link it to the Text widget
scrollbar = ttk.Scrollbar(frame, orient="vertical", command=output_text.yview)
scrollbar.pack(side="right", fill="y")
output_text.configure(yscrollcommand=scrollbar.set)

uninstall_odb_driver = tk.IntVar()

ttk.Checkbutton(root, text="ODBC Treiber deinstallieren (funktioniert noch nicht)", variable=uninstall_odb_driver).pack(anchor=tk.W, pady=5)

ttk.Button(root, text="Deinstallieren", command=api.uninstall_app).pack(pady=5)
ttk.Button(root, text="Schließen", command=root.quit).pack(pady=5)

if __name__ == "__main__":
    #api.run_as_admin()
    root.mainloop()
