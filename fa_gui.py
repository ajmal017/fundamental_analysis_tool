from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QSizePolicy

WINDOW_TITLE = "Fundamental Analysis Tool"

class FaMainWindow(QMainWindow):

    def __init__(self, *args):
        QMainWindow.__init__(self, *args)
        self.setWindowTitle(WINDOW_TITLE)
        self.central_widget = QWidget()
        self.central_layout = QVBoxLayout()
        self.central_widget.setLayout(self.central_layout)
        self.setCentralWidget(self.central_widget)
        self.label_test = QLabel("Test-Label")
        self.central_layout.addWidget(self.label_test)
        self.label_test1 = QLabel("Test-Label")
        self.central_layout.addWidget(self.label_test1)
        self.statusBar().showMessage("Ready")
        #self.setFixedSize(self.central_layout.sizeHint())
        self.setSizePolicy(QSizePolicy(QSizePolicy.Fixed,
                                       QSizePolicy.Fixed))

    def set_version_info(self, version):
        combined = "{} v{}".format(WINDOW_TITLE, version)
        self.setWindowTitle(combined)
