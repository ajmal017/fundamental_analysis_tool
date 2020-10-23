#!/usr/bin/env python3

import sys
import ctypes

from PyQt5.QtWidgets import QApplication

from fa_gui import FaMainWindow

WINAPPID = "meyerlasse.fundamental_analysis_tool"
VERSION = "0.0.1"

if __name__ == "__main__":
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(WINAPPID)
    app = QApplication(sys.argv)
    main_window = FaMainWindow()
    main_window.set_version_info(VERSION)
    main_window.show()
    sys.exit(app.exec())
