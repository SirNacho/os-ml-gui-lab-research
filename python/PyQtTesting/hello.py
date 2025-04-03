#Simple PyQT script to test out the PyQT GUI Framework. Created by Sir Nacho

import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget

app = QApplication([])

window = QWidget()
window.setWindowTitle("Testing GUI App")
window.setGeometry(750,500,400,50)

testingMsg = QLabel("<h1>Hi, I'm better than Kivy!</h1>", parent=window)
testingMsg.move(60,15)

window.show()
sys.exit(app.exec())
