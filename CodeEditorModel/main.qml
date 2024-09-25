import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    visible: true
    width: 640
    height: 480
        menuBar: MenuBar {

        Menu {
            title: qsTr("File")

            Action {
                text: qsTr("Increase Font")
                shortcut: StandardKey.ZoomIn
                onTriggered: editor.text.font.pixelSize += 1
            }
            Action {
                text: qsTr("Decrease Font")
                shortcut: StandardKey.ZoomOut
                onTriggered: editor.text.font.pixelSize -= 1
            }
        }

        Menu {
            title: qsTr("Edit")

            Action {
                text: qsTr("Cut")
                shortcut: StandardKey.Cut
                enabled: editor.text.selectedText.length > 0
                onTriggered: editor.text.cut()
            }
            Action {
                text: qsTr("Copy")
                shortcut: StandardKey.Copy
                enabled: editor.text.selectedText.length > 0
                onTriggered: editor.text.copy()
            }
            
        }
    }
}
