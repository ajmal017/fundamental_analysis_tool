from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5.QtGui import QIcon

import fa_backend as fab
from fa_util import find_data_file

UI_FILE_MAINWINDOW = "fa_mainwindow.ui"
UI_FILE_STOCK = "stock.ui"
UI_FILE_ICON = "icon.png"

WINDOW_TITLE = "Fundamental Analysis Tool"

class FaMainWindow(QMainWindow):

    def __init__(self, *args):
        QMainWindow.__init__(self, *args)
        uic.loadUi(find_data_file(UI_FILE_MAINWINDOW), self)
        self.setWindowTitle(WINDOW_TITLE)
        self.setWindowIcon(QIcon(find_data_file("icon.png")))
        self.input_add_stock.returnPressed.connect(self.handle_add_stock)
        self.button_add_stock.clicked.connect(self.handle_add_stock)
        self.button_clear_stock.clicked.connect(self.handle_clear_stock)
        self.count_stock_layouts = 0

    def set_version_info(self, version):
        combined = "{} v{}".format(WINDOW_TITLE, version)
        self.setWindowTitle(combined)

    def handle_add_stock(self):
        try:
            new_ticker = fab.get_ticker(self.input_add_stock.text())
            self.add_stock(new_ticker)
            self.handle_clear_stock()
        except fab.TickerNotFoundException:
            print("invalid ticker name")

    def handle_clear_stock(self):
        self.input_add_stock.clear()

    def add_stock(self, ticker):
        stock = StockWidget(ticker)
        self.list_stocks.insertWidget(self.count_stock_layouts, stock)
        self.count_stock_layouts += 1

class StockWidget(QWidget):

    def __init__(self, ticker):
        QWidget.__init__(self)
        uic.loadUi(find_data_file(UI_FILE_STOCK), self)

        name = "{} ({})".format(fab.get_name(ticker), fab.get_symbol(ticker))
        currency = fab.get_currency(ticker)
        ask = fab.get_formatted_currencystring(fab.get_ask(ticker), currency)
        askbid_spread = fab.get_formatted_currencystring(fab.get_askbid_spread(ticker), currency)
        eps_trailing = fab.get_formatted_currencystring(fab.get_eps_trailing(ticker), currency)
        eps_forward = fab.get_formatted_currencystring(fab.get_eps_forward(ticker), currency)

        self.label_name.setText(name)
        self.label_ask.setText(ask)
        self.label_askbid_spread.setText(askbid_spread)
        self.label_eps_trailing.setText(eps_trailing)
        self.label_eps_forward.setText(eps_forward)
