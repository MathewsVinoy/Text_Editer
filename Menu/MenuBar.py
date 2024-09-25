from PySide6.QtWidgets import *

class MenuBar:
    def __init__(self, window):
        self.window = window
        self.create_menu_bar()

    def create_menu_bar(self):
        fileMenu = self.window.menuBar().addMenu('File')
        newWindow = fileMenu.addAction('NewWindow')
        newFile = fileMenu.addAction('NewFile')
        openFile = fileMenu.addAction('OpenFile')
        openFolder = fileMenu.addAction('OpenFolder')

        editMenu = self.window.menuBar().addMenu("Edit")
        Undo = editMenu.addAction("Undo")
        Redo = editMenu.addAction("Redo")

        viewMenu = self.window.menuBar().addMenu("View")
        sidebarpos = viewMenu.addAction("SideBar")
        
    
