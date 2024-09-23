from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import platform
from files_views.file_viewmain import FileViews
from terminal.terminal import TerminalMain
from functions.menubarfunction import MenuBarFun

class WindowHolder(QMainWindow):
    def __init__(self):
        super(WindowHolder,self).__init__()
        self.resize(1100, 700)
        self.TextEditorFun()
        self.FileDrawerFun()
        self.TerminalFun()
        self.menu = MenuBarFun(self)
        self.menu.create_menu_bar()
        
    def TextEditorFun(self):
        self.editor = QTextEdit()
        self.setCentralWidget(self.editor)

    def FileDrawerFun(self):
        file = FileViews()
        right_dock = QDockWidget("Right Drawer", self)
        right_dock.setWidget(file.right_drawer)
        self.addDockWidget(Qt.RightDockWidgetArea, right_dock)

    def TerminalFun(self):
        term = TerminalMain()
        bottom_dock = QDockWidget("bottom Drawer", self)
        bottom_dock.setWidget(term.bottom_drawer)
        self.addDockWidget(Qt.BottomDockWidgetArea, bottom_dock)
        
