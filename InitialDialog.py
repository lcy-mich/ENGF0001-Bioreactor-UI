from PySide6.QtWidgets import QDialog, QDialogButtonBox
from PySide6.QtCore import Slot, Signal

from settings import MQTT_HOST, MQTT_KEEPALIVE, MQTT_PORT, MQTT_TOPIC

from ui.initialdialog_ui import Ui_Dialog

class InitialDialog(QDialog):
    
    def __init__(self, parent=None):
        super(InitialDialog, self).__init__(parent)
        self.setWindowTitle("Initial Details")
        self.setMinimumSize(400, 150)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.rejectedHandler()

        self.ui.decisionBox.accepted.connect(self.close)
        self.ui.decisionBox.rejected.connect(self.rejectedHandler)

        self.ui.decisionBox.addButton("Connect", QDialogButtonBox.ButtonRole.AcceptRole)
        self.ui.decisionBox.addButton("Reset Information", QDialogButtonBox.ButtonRole.RejectRole)

    
    @Slot()
    def rejectedHandler(self):
        self.ui.hostLine.setText(MQTT_HOST)
        self.ui.portLine.setText(str(MQTT_PORT))
        self.ui.keepaliveLine.setText(str(MQTT_KEEPALIVE))
        self.ui.topicLine.setText(MQTT_TOPIC)


if __name__ == "__main__":
    from sys import exit as sys_exit
    from PySide6.QtWidgets import QApplication

    app = QApplication()

    dialog = InitialDialog()
    dialog.show()

    sys_exit(app.exec())