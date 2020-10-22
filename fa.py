import sys

from PyQt5.QtWidgets import QApplication

import fa_backend as fab
from fa_gui import FaMainWindow

VERSION = "0.0.1"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = FaMainWindow()
    main_window.set_version_info(VERSION)
    main_window.show()
    sys.exit(app.exec_())
