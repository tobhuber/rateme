# This Python file uses the following encoding: utf-8
import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("RateMe")
        layout = QGridLayout()
        layout.addWidget(QWidget, 0, 0, 3, 3)
        layout.addWidget(QWidget, 0, 3, 4, 1)
        layout.addWidget(QWidget, 3, 0, 1, 3)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
