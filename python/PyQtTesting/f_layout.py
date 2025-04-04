# This script is to test out the QFormLayout which basically have a text field where you could get the string input of the user.

import sys

from PyQt6.QtWidgets import (
        QApplication,
        QFormLayout,
        QLineEdit,
        QWidget
        )

app = QApplication([])
window = QWidget()
window.setWindowTitle("QFormLayout")

layout = QFormLayout()

layout.addRow("Name:", QLineEdit())
layout.addRow("Age:", QLineEdit())
layout.addRow("Job:", QLineEdit())
layout.addRow("Hobbies:", QLineEdit())
window.setLayout(layout)

window.show()
sys.exit(app.exec())
