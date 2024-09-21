from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import platform
from files_views.file_viewmain import FileViews

class WindowHolder(QMainWindow):
    def __init__(self):
        super(WindowHolder,self).__init__()
        
        bottom_drawer = QWidget()
        bottom_layout = QHBoxLayout()
        bottom_drawer.setLayout(bottom_layout)
        
        bottom_dock =QDockWidget("bottom Drawer", self)
        bottom_dock.setWidget(bottom_drawer)
        self.addDockWidget(Qt.BottomDockWidgetArea, bottom_dock)
        
        self.TextEditorFun()
        self.FileDrawerFun()
        self.menubarUI()
            
    def TextEditorFun(self):
        self.editor = QTextEdit()
        self.setCentralWidget(self.editor)
        
        
    def FileDrawerFun(self):
        file = FileViews()
        right_dock =QDockWidget("Right Drawer", self)
        right_dock.setWidget(file.right_drawer)
        self.addDockWidget(Qt.RightDockWidgetArea, right_dock)
        
    def menubarUI(self):
        fileMenu = self.menuBar().addMenu('File')
        newWindow = fileMenu.addAction('NewWindow')
        # newWindow.triggered.connect(self.new_window)
        newFile = fileMenu.addAction('NewFile')
        # newFile.triggered.connect(self.new_file)
        openFile = fileMenu.addAction('OpenFile')
        # openFile.triggered.connect(self.open_file)
        openFolder = fileMenu.addAction('OpenFolder')
        # openFolder.triggered.connect(self.open_folder)

        editMenu = self.menuBar().addMenu("Edit")
        Undo = editMenu.addAction("Undo")
        # Undo.triggered.connect(self.on_new_action)
        Redo = editMenu.addAction("Redo")
        # Redo.triggered.connect(self.on_new_action)

        viewMenu = self.menuBar().addMenu("View")
        sidebarpos = viewMenu.addAction("SideBar")
        # sidebarpos.triggered.connect(self.PosSift)