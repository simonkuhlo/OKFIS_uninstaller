import shutil
import os
import res.communicator as com

def uninstall():
    """Perform the uninstallation tasks."""
    try:
        com.broadcast("Removing 'C:\\akdbprg'")
        shutil.rmtree("C:\\akdbprg", ignore_errors=True)
        com.broadcast("Done.\n")

        com.broadcast("Removing 'C:\\ok_bereich'")
        shutil.rmtree("C:\\ok_bereich", ignore_errors=True)
        com.broadcast("Done.\n")

        com.broadcast("Removing 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\OK.FIS-4.0'")
        shutil.rmtree("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\OK.FIS-4.0", ignore_errors=True)
        com.broadcast("Done.\n")

        com.broadcast("Removing 'C:\\Users\\Public\\Desktop\\OK.FIS-4.0'")
        shutil.rmtree("C:\\Users\\Public\\Desktop\\OK.FIS-4.0", ignore_errors=True)
        com.broadcast("Done.\n")

        com.broadcast("Removing Registry keys")
        os.system('REG DELETE HKEY_LOCAL_MACHINE\\SOFTWARE\\Wow6432Node\\AKDB /f')
        os.system('REG DELETE HKEY_LOCAL_MACHINE\\SOFTWARE\\Wow6432Node\\Ok_Verfahren /f')
        com.broadcast("Done.\n")

        com.broadcast("All tasks completed. Returning to Menu.")
    except Exception as e:
        com.broadcast(f"[!] An error occurred: {e}")

