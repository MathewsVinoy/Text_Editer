import sys
from PySide6.QtCore import QUrl
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QCommandLineParser, qVersion

if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    

    parser = QCommandLineParser()
    parser.addHelpOption()
    parser.addVersionOption()
    parser.addPositionalArgument("", "Initial directory", "[path]")
    parser.process(app)
    args = parser.positionalArguments()

    engine = QQmlApplicationEngine()
    engine.addImportPath(sys.path[0])

    engine.loadFromModule("CodeEditorModel", "Main")

    if not engine.rootObjects():
        sys.exit(-1)

    if (len(args) == 1):
        fsm = engine.singletonInstance("CodeEditorModel", "CodeEditorModel")
        fsm.setInitialDirectory(args[0])

    sys.exit(app.exec())
