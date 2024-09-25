import QtQuick
import QtQuick.Controls.Basic
import QtQuick.Layouts
import CodeEditorModel

pragma ComponentBehavior: Bound

ApplicationWindow {
     id: root

    property bool expandPath: false
    property bool showLineNumbers: true
    property string currentFilePath: ""

    width: 1100
    height: 600
    minimumWidth: 200
    minimumHeight: 100
    visible: true
    flags: Qt.Window | Qt.FramelessWindowHint
    title: qsTr("File System Explorer Example")
    menuBar: MenuBar {
        dragWindow: root
        Menu {
            title: qsTr("File")
            Action {
                text: qsTr("Increase Font")
            }
            Action {
                text: qsTr("Decrease Font")   
            }
        }
        Menu {
            title: qsTr("Edit")
            Action {
                text: qsTr("Cut")  
            }
            Action {
                text: qsTr("Copy") 
            }
            
        }
    }
    
}
