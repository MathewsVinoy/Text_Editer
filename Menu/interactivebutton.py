from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

class InteractiveButton(QPushButton):
    def __init__(self, parent=None):
        super(InteractiveButton, self).__init__(parent)
        self.setFixedSize(30, 30)  # Set a fixed size for the button
        self.hovered = False
        self.setStyleSheet("background-color: transparent; border: none;")

    def enterEvent(self, event):
        self.hovered = True
        self.update()

    def leaveEvent(self, event):
        self.hovered = False
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw the background rectangle
        if self.hovered:
            painter.setBrush(QColor("#ec4143"))
        else:
            painter.setBrush(QColor("transparent"))

        painter.setPen(Qt.NoPen)
        painter.drawRect(self.rect())

        # Draw the "X" mark
        painter.setPen(QPen(QColor("#000000"), 2))  # Set the color and thickness of the lines
        painter.drawLine(self.rect().topLeft(), self.rect().bottomRight())
        painter.drawLine(self.rect().topRight(), self.rect().bottomLeft())