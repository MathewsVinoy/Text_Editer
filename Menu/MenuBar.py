from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import sys

class MenuBar(QWidget):
    height = 35

    def __init__(self, parent):
        super(MenuBar, self).__init__()
        self.parent = parent
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.menu_bar = QMenuBar()
        self.menu_file = self.menu_bar.addMenu('File')
        self.menu_file_open = self.menu_file.addAction('Open')
        self.menu_file_save = self.menu_file.addAction('Save')
        self.menu_file_saveas = self.menu_file.addAction('Save As...')
        self.menu_file_quit = self.menu_file.addAction('Exit')
        self.menu_file_quit.triggered.connect(qApp.quit)

        self.menu_work = self.menu_bar.addMenu('Work')
        self.menu_analysis = self.menu_bar.addMenu('Analysis')
        self.menu_edit = self.menu_bar.addMenu('Edit')
        self.menu_window = self.menu_bar.addMenu('Window')
        self.menu_help = self.menu_bar.addMenu('Help')

        self.layout.addWidget(self.menu_bar)

        self.closeButton = QPushButton(' ')
        self.closeButton.clicked.connect(self.on_click_close)

        self.maxButton = QPushButton(' ')
        self.maxButton.clicked.connect(self.on_click_maximize)

        self.hideButton = QPushButton(' ')
        self.hideButton.clicked.connect(self.on_click_hide)

        self.layout.addWidget(self.hideButton)
        self.layout.addWidget(self.maxButton)
        self.layout.addWidget(self.closeButton)
        self.setLayout(self.layout)

        self.start = QPoint(0, 0)
        self.pressing = False
        self.maximize = False

    def resizeEvent(self, event):
        super(MenuBar, self).resizeEvent(event)

    def mousePressEvent(self, event):
        self.start = self.mapToGlobal(event.pos())
        self.pressing = True

    def mouseMoveEvent(self, event):
        if self.pressing:
            self.end = self.mapToGlobal(event.pos())
            self.movement = self.end - self.start
            self.parent.move(self.mapToGlobal(self.movement))
            self.start = self.end

    def mouseReleaseEvent(self, event):
        self.pressing = False

    def on_click_close(self):
        sys.exit()

    def on_click_maximize(self):
        if self.maximize: 
            self.maximize = not self.maximize
            self.parent.setWindowState(Qt.WindowNoState)
        else:
            self.maximize = not self.maximize
            self.parent.setWindowState(Qt.WindowMaximized)

    def on_click_hide(self):
        self.parent.showMinimized()