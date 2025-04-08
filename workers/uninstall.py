import shutil
import os
import res.communicator as com

def uninstall():
    try:
        com.broadcast("Entferne 'C:\\akdbprg'")
        shutil.rmtree("C:\\akdbprg", ignore_errors=True)
        com.broadcast("Fertig.\n")

        com.broadcast("Entferne 'C:\\ok_bereich'")
        shutil.rmtree("C:\\ok_bereich", ignore_errors=True)
        com.broadcast("Fertig.\n")

        com.broadcast("Entferne 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\OK.FIS-4.0'")
        shutil.rmtree("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\OK.FIS-4.0", ignore_errors=True)
        com.broadcast("Fertig.\n")

        com.broadcast("Entferne 'C:\\Users\\Public\\Desktop\\OK.FIS-4.0'")
        shutil.rmtree("C:\\Users\\Public\\Desktop\\OK.FIS-4.0", ignore_errors=True)
        com.broadcast("Fertig.\n")

        com.broadcast("Entferne Registry keys")
        os.system('REG DELETE HKEY_LOCAL_MACHINE\\SOFTWARE\\Wow6432Node\\AKDB /f')
        os.system('REG DELETE HKEY_LOCAL_MACHINE\\SOFTWARE\\Wow6432Node\\Ok_Verfahren /f')
        com.broadcast("Fertig.\n")

        com.broadcast("Alles fertig!")
    except Exception as e:
        com.broadcast(f"[!] Fehler: {e}")

