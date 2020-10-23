import sys
import os

def find_data_file(filename):
    """
    Get full file path, which differs when a program is executed
    with the python interpreter or a standalone executable.
    """
    if getattr(sys, "frozen", False):
        # The application is frozen
        datadir = os.path.dirname(sys.executable)
    else:
        # The application is not frozen
        # Change this bit to match where you store your data files:
        datadir = os.path.dirname(__file__)
    return os.path.join(datadir, filename)
