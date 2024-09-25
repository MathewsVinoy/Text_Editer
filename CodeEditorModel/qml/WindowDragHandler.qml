import QtQuick
import QtQuick.Controls

// Allows dragging the window when placed on an unused section of the UI.
DragHandler {

    required property ApplicationWindow dragWindow

    target: null
    onActiveChanged: {
        if (active) dragWindow.startSystemMove()
    }
}
