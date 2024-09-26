import sys
from PySide6.QtWidgets import QApplication
from main_screen import WindowHolder

if __name__ == "__main__":
    app = QApplication([])
    window = WindowHolder()
    window.show()
    app.exec()