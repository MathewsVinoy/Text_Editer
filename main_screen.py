from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from Menu.MenuBar import MenuBar
from Menu.interactivebutton import InteractiveButton

class WindowHolder(QMainWindow):
    def __init__(self):
        super(WindowHolder, self).__init__()
        self.resize(800, 500)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowSystemMenuHint)

        self.menu_bar = MenuBar(self)
        self.setMenuWidget(self.menu_bar)

        cw = QWidget()
        layout = QHBoxLayout()
        cw.setLayout(layout)
        self.setCentralWidget(cw)
