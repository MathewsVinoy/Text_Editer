from PySide6 import QtCore
from PySide6 import QtWidgets

class HiddenButton(QtWidgets.QPushButton):
    hover = QtCore.Signal()

    def __init__(self, parent):
        super(HiddenButton, self).__init__(parent)
        self.setUpdatesEnabled(False)
        self.setFocusPolicy(QtCore.Qt.NoFocus)

    def enterEvent(self, event):
        self.hover.emit()

    def leaveEvent(self, event):
        self.hover.emit()
