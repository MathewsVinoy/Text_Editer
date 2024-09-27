from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from Menu.MenuBar import MenuBar
from files_views.file_viewmain import FileViews
from Terminal.terminal import PowerShellApp

class WindowHolder(QMainWindow):
    def __init__(self):
        super(WindowHolder, self).__init__()
        self.resize(800, 500)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowSystemMenuHint)

        self.menu_bar = MenuBar(self)
        self.setMenuWidget(self.menu_bar)

        self.TextEditorFun()
        self.FileDrawerFun()
        self.TerminalSet()

    def TextEditorFun(self):
        self.editor = QTextEdit()
        self.setCentralWidget(self.editor)

    def FileDrawerFun(self):
        file = FileViews()
        right_dock = QDockWidget("Right Drawer", self)
        right_dock.setWidget(file.right_drawer)
        self.addDockWidget(Qt.RightDockWidgetArea, right_dock)

    def TerminalSet(self):
        self.bottom_drawer = QWidget()
        self.bottom_layout = QHBoxLayout()
        self.bottom_drawer.setLayout(self.bottom_layout)

        terminal = PowerShellApp()
        self.bottom_layout.addWidget(terminal)

        bottom_dock = QDockWidget("Bottom Drawer", self)
        bottom_dock.setWidget(self.bottom_drawer)
        self.addDockWidget(Qt.BottomDockWidgetArea, bottom_dock)