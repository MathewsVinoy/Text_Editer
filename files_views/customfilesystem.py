from PySide6.QtWidgets import QFileSystemModel
from PySide6.QtCore import Qt, QDir
import os

class CustomFileSystemModel(QFileSystemModel):
    def __init__(self, location):
        super().__init__()
        self.loc = location

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                name = os.path.basename(self.loc)
                return name
        return super().headerData(section, orientation, role)
