import ctypes
import sys

def is_admin():
    """Check if the script is running with administrator privileges."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def request_admin_privileges():
    """Request administrator privileges if not already elevated."""
    if not is_admin():
        # Relaunch the script with administrator privileges
        try:
            ctypes.windll.shell32.ShellExecuteW(
                None,  # No parent window
                "runas",  # Run as administrator
                sys.executable,  # Path to the Python interpreter
                " ".join(sys.argv),  # Arguments (the script and its parameters)
                None,  # Default directory
                1  # Show the window normally
            )
        except Exception as e:
            print(f"Failed to request admin privileges: {e}")
        sys.exit()  # Exit the current process after requesting elevation