import platform
from PySide6.QtWidgets import QApplication, QHBoxLayout, QWidget, QTextEdit, QLineEdit, QVBoxLayout
from PySide6.QtCore import QProcess

class TerminalMain(QWidget):
    def __init__(self):
        super(TerminalMain, self).__init__()

        self.bottom_drawer = QWidget()
        self.bottom_layout = QHBoxLayout()
        self.bottom_drawer.setLayout(self.bottom_layout)

        layout = QVBoxLayout()

        self.process = QProcess()
        self.process.readyReadStandardOutput.connect(self.handle_output)
        self.process.readyReadStandardError.connect(self.handle_error)
        self.process.started.connect(self.handle_output)
        self.process.finished.connect(self.closeEvent)

        if platform.system() == "Windows":
            self.process.start("powershell.exe")
        elif platform.system() == "Linux":
            self.process.start("bash")

        self.terminal_output = QTextEdit()
        self.terminal_output.setReadOnly(True)
        self.terminal_output.setStyleSheet("""
                background-color: #000000;
                color: #FFFFFF;
                font-family: Titillium;
                font-size: 12px;
                """)
        layout.addWidget(self.terminal_output)

        self.input_line = QLineEdit()
        self.input_line.returnPressed.connect(self.send_input)
        layout.addWidget(self.input_line)

        container = QWidget()
        container.setLayout(layout)
        self.bottom_layout.addWidget(container)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.bottom_drawer)
        self.setLayout(main_layout)

    def handle_output(self):
        output = self.process.readAllStandardOutput().data().decode()
        self.terminal_output.append(output)

    def handle_error(self):
        error = self.process.readAllStandardError().data().decode()
        self.terminal_output.append(error)

    def send_input(self):
        input_text = self.input_line.text()
        self.process.write(input_text.encode() + b'\n')
        self.input_line.clear()

    def closeEvent(self, event):
        self.process.terminate()
        self.process.waitForFinished(1000)  # Wait up to 1 second for the process to finish
        super().closeEvent(event)
