# This Python file uses the following encoding: utf-8
import sys
from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QMainWindow
from PySide2.QtWidgets import QGridLayout
from PySide2.QtWidgets import QWidget
from PySide2.QtWidgets import QPushButton
from PySide2.QtWidgets import QAction
from PySide2.QtWidgets import QMenuBar
from PySide2.QtWidgets import QFileDialog
from PySide2 import QtCore
from gui.UserList import UserList
from core.Database import Database
from files.Saver import Saver
from files.Loader import Loader




class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.db = Database()
        self.central = QWidget()
        self.setCentralWidget(self.central)
        self.setWindowTitle("RateMe")
        self.setFixedSize(1280, 720)
        self.layout = QGridLayout()
        self.init_menu_bar()
        self.user_list = UserList(self.db, self)
        self.layout.addWidget(self.user_list, 1, 3, 4, 1)
        self.central.setLayout(self.layout)

        self.refresh()

    def init_menu_bar(self):
        bar = QMenuBar(self)
        file = bar.addMenu("File")
        imp = QAction("Import", self)
        imp.setShortcut("Ctrl+I")
        imp.triggered.connect(self.import_dialog)
        file.addAction(imp)
        save = QAction("Save", self)    
        save.setShortcut("Ctrl+S")
        save.triggered.connect(self.save_dialog)
        file.addAction(save)
        self.layout.addWidget(bar, 0, 0, 1, 4)
        
    def import_dialog(self):
        loader = Loader()
        path, modus = QFileDialog().getOpenFileName()
        self.db = loader.load(path)
        self.refresh()

    def save_dialog(self):
        saver = Saver()
        path, mode = QFileDialog().getSaveFileName()
        saver.save(self.db, path)

    def refresh(self):
        self.layout.removeWidget(self.user_list)
        self.user_list.deleteLater()
        self.user_list = UserList(self.db, self)
        self.layout.addWidget(self.user_list, 1, 3, 4, 1)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
