from PySide6.QtWidgets import QMainWindow, QMenuBar, QMenu, QStyleOptionTitleBar, QStyle, QWidget
from PySide6.QtGui import QAction
from PySide6 import QtCore
from Componts.hiddenbutton import HiddenButton

class WindowHolder(QMainWindow):
    def __init__(self):
        super(WindowHolder, self).__init__()
        self.widgetHelpers=[]
        self.resize(1100,700)
        self.setWindowFlag(
            QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowSystemMenuHint
        )
        self.setWindowState(self.windowState() | QtCore.Qt.WindowActive)
        self.titleOpt = QStyleOptionTitleBar()
        self.titleOpt.initFrom(self)
        self.titleOpt.titleBarFlags=(
            QtCore.Qt.Window | QtCore.Qt.MSWindowsOwnDC|
            QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowTitleHint|
            QtCore.Qt.WindowCloseButtonHint
        )
        self.titleOpt.state |= (QStyle.State_Active|QStyle.State_HasFocus)
        self.titleOpt.titleBarState = (self.windowState().value | QStyle.State_Active.value)

        self.systemButton = HiddenButton(self)
        self.minimizeButton= HiddenButton(self)
        self.maximizeButton =HiddenButton(self)
        self.closeButton =HiddenButton(self)

        self.ctrlButtons = {
        QStyle.SC_TitleBarMinButton: self.minimizeButton,
        QStyle.SC_TitleBarMaxButton: self.maximizeButton,
        QStyle.SC_TitleBarNormalButton: self.maximizeButton,
        QStyle.SC_TitleBarCloseButton: self.closeButton,
        }

        self.widgetHelpers.extend([self.minimizeButton, self.maximizeButton, self.closeButton])
        # self.resetTitleHeight()

        self.menubarUI()
        self.statusBar()

    def menubarUI(self):
        menubar= QMenuBar()
        self.setMenuBar(menubar)

        file_menu = QMenu("file",menubar)
        menubar.addMenu(file_menu)
        new_action = QAction("New",self)
        file_menu.addAction(new_action)
        new_action.triggered.connect(self.on_new_action)


    def on_new_action(self):
        print("hello World")
