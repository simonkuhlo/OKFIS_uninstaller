from . import uninstall as uninstall_worker
from . import system


def uninstall_app() -> None:
    uninstall_worker.uninstall()

def run_as_admin() -> None:
    system.request_admin_privileges()