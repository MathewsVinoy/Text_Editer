import platform
# from PySide6.QtWidgets import QApplication, QHBoxLayout, QWidget, QTextEdit, QLineEdit, QVBoxLayout
from PySide6.QtCore import QProcess
from PySide6.QtWidgets import *


class TerminalMain:
    def __init__(self):
        super(TerminalMain, self).__init__()

        self.bottom_drawer = QWidget()
        self.bottom_layout = QHBoxLayout()
        self.bottom_drawer.setLayout(self.bottom_layout)
        
        self.process = QProcess()
        
        self.term = QWidget()
        # self.term.setReadOnly(True)
        
        self.process.start()
        
        self.bottom_layout.addWidget(self.term)
    


