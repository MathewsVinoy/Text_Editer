from PySide6.QtWidgets import QFileSystemModel
from PySide6.QtCore import Qt

class CustomFileSystemModel(QFileSystemModel):
    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return "Project"
        return super().headerData(section, orientation, role)
