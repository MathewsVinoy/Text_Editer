from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


class WindowHolder(QMainWindow):
    def __init__(self):
        super(WindowHolder, self).__init__()
        self.resize(1100, 700)
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        self.editor = QTextEdit()
        layout.addWidget(self.editor)
        self.setCentralWidget(central_widget)
        self.menubarUI()
        self.fileMenu()




    def menubarUI(self):
        fileMenu = self.menuBar().addMenu('File')
        newWindow=fileMenu.addAction('NewWindow')
        newWindow.triggered.connect(self.on_new_action)
        newFile=fileMenu.addAction('NewFile')
        newFile.triggered.connect(self.on_new_action)
        openFile=fileMenu.addAction('OpenFile')
        openFile.triggered.connect(self.on_new_action)
        editMenu = self.menuBar().addMenu("Edit")
        Undo=editMenu.addAction("Undo")
        Undo.triggered.connect(self.on_new_action)
        Redo=editMenu.addAction("Redo")
        Redo.triggered.connect(self.on_new_action)

    def fileMenu(self):
        toolbox = QToolBar(self)
        model =QFileSystemModel()
        model.setRootPath(QDir.currentPath())
        tree=QTreeView(toolbox)
        tree.setModel(model)
        tree.setRootIndex(model.index(QDir.currentPath()))
        self.addToolBar(Qt.LeftToolBarArea, toolbox)

    def on_new_action(self):
        print("hello World")
