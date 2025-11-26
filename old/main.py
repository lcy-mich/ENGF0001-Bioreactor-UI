import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QTextEdit, QVBoxLayout
from PyQt6.QtGui import QIcon

class application(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bioreactor UI")
        self.setWindowIcon(QIcon("icon.ico"))
        self.resize(300, 200)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.inputfield = QLineEdit()
        pushbutton = QPushButton("&Say Hello")
        pushbutton.clicked.connect(self.sayHello)
        self.outputfield = QTextEdit()

        layout.addWidget(self.inputfield)
        layout.addWidget(pushbutton)
        layout.addWidget(self.outputfield)

    def sayHello(self):
        inputtext = self.inputfield.text()
        self.outputfield.setText(f"hello there {inputtext}")

app = QApplication([])
app.setStyleSheet('''
   QWidget {
        font-size: 25px;
    }            
    QPushButton {
        font-size: 20px;
    }   
                  
''')

window = application()
window.show()


sys.exit(app.exec())