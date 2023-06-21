from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow

from screens.game_screen import GameScreen


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Wordle")
        self.setFixedSize(QSize(225, 290))

        self.game = GameScreen()
        self.setCentralWidget(self.game)


if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    app.exec()