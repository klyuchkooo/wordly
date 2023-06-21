from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QPushButton


class WordOnTable(QPushButton):
    def __init__(self, text, color):
        super().__init__()
        self.isEmpty = False
        self.setCheckable(False)
        self.setEnabled(False)
        self.setText(text)
        self.setFixedSize(QSize(40, 40))
        self.setStyleSheet(":disabled {font: bold; font-size: 18px; color: black ;background-color: " + color + "}")
