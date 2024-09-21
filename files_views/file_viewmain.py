from files_views.customfilesystem import CustomFileSystemModel
from PySide6.QtWidgets import QWidget, QVBoxLayout, QTreeView
from PySide6.QtCore import QDir

class FileViews:
    def __init__(self):
        super(FileViews, self).__init__()
        self.filepath = QDir.currentPath()
        self.model = CustomFileSystemModel(self.filepath)
        self.right_drawer = QWidget()
        self.right_layout = QVBoxLayout()
        self.right_drawer.setLayout(self.right_layout)
        self.model.setRootPath(self.filepath)
        
        self.tree = QTreeView()
        self.tree.setModel(self.model)
        self.tree.setAnimated(True)
        self.tree.setIndentation(20)
        self.tree.setDragEnabled(True)
        self.tree.setAcceptDrops(True)
        self.tree.setRootIndex(self.model.index("/", 0, 0))
        # self.tree.clicked.connect(self.open_fileInviews)
        
        for column in range(1, self.model.columnCount()):
            self.tree.setColumnHidden(column, True)
        self.right_layout.addWidget(self.tree)