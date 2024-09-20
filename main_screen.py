from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from Componts.customfilesystem import CustomFileSystemModel

class WindowHolder(QMainWindow):
    def __init__(self):
        super(WindowHolder, self).__init__()
        self.resize(1100, 700)
        self.sidpos = True
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        self.editor = QTextEdit()
        layout.addWidget(self.editor)

        self.menubarUI()
        self.fileMenu()

    def menubarUI(self):
        fileMenu = self.menuBar().addMenu('File')
        newWindow = fileMenu.addAction('NewWindow')
        newWindow.triggered.connect(self.on_new_action)
        newFile = fileMenu.addAction('NewFile')
        newFile.triggered.connect(self.on_new_action)
        openFile = fileMenu.addAction('OpenFile')
        openFile.triggered.connect(self.on_new_action)

        editMenu = self.menuBar().addMenu("Edit")
        Undo = editMenu.addAction("Undo")
        Undo.triggered.connect(self.on_new_action)
        Redo = editMenu.addAction("Redo")
        Redo.triggered.connect(self.on_new_action)

        viewMenu = self.menuBar().addMenu("View")
        sidebarpos = viewMenu.addAction("SideBar")
        sidebarpos.triggered.connect(self.PosSift)

    def fileMenu(self):
        model = CustomFileSystemModel()
        sidebar = QWidget()
        main_layout = QVBoxLayout(sidebar)
        model.setRootPath(QDir.currentPath())
        tree = QTreeView()
        tree.setModel(model)
        tree.setAnimated(True)
        tree.setIndentation(20)
        tree.setDragEnabled(True)
        tree.setAcceptDrops(True)
        tree.setRootIndex(model.index(QDir.currentPath()))

        for column in range(1, model.columnCount()):
            tree.setColumnHidden(column, True)
        main_layout.addWidget(tree)

        splitter = QSplitter(Qt.Horizontal)

        if self.sidpos == True:
            splitter.addWidget(self.editor)
            splitter.addWidget(sidebar)
        else:
            splitter.addWidget(sidebar)
            splitter.addWidget(self.editor)

        splitter.setSizes([int(self.width() * 0.8), int(self.width() * 0.2)])

        self.setCentralWidget(splitter)

    def on_new_action(self):
        print("hello World")

    def PosSift(self):
        if self.sidpos == True:
            self.sidpos = False
        else:
            self.sidpos = True
        self.fileMenu()
