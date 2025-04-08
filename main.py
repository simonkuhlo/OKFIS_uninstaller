import os
from workers import api
import sys


def main_menu():
    """Display the main menu and handle user input."""
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("OK.FIS uninstaller v0.1.8E")
        print("------------------------------------------")
        print("1 Uninstall (silent)")
        print("x Exit")
        print("------------------------------------------")
        
        option = input("Choose an option [1, x]: ").strip().lower()
        
        if option == "1":
            api.uninstall_app()
        elif option == "x":
            sys.exit(0)
        else:
            print("[!] Invalid option. Returning to Menu.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    api.run_as_admin()
    main_menu()