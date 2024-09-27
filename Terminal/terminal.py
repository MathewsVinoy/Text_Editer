import sys
import subprocess
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QLineEdit
from PySide6.QtCore import Qt

class PowerShellApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        self.output = QTextEdit()
        self.output.setReadOnly(True)
        self.output.setStyleSheet("background-color: #1e1e1e; color: #cccccc; font-family: 'Courier New', Courier, monospace;")
        self.layout.addWidget(self.output)

        self.input = QLineEdit()
        self.input.setStyleSheet("background-color: #2d2d2d; color: #cccccc; font-family: 'Courier New', Courier, monospace;")
        self.input.returnPressed.connect(self.handle_input)
        self.layout.addWidget(self.input)

        self.setLayout(self.layout)

    def handle_input(self):
        command = self.input.text()
        self.input.clear()

        # Process the command
        self.process_command(command)

    def process_command(self, command):
        self.output.append(f"> {command}\n")

        try:
            result = subprocess.run(['powershell', '-Command', command], capture_output=True, text=True)
            self.output.append(result.stdout)
            if result.stderr:
                self.output.append(result.stderr)
        except Exception as e:
            self.output.append(f"Error: {str(e)}\n")