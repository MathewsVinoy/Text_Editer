import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    visible: true
    width: 640
    height: 480
    title: qsTr("Hello World")

    Column {
        anchors.centerIn: parent

        Label {
            id: label
            text: qsTr("Hello World")
            font.pointSize: 24
        }

        Button {
            text: qsTr("Click Me")
            onClicked: {
                label.text = qsTr("Button Clicked")
            }
        }
    }
}
