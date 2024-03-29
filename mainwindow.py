# This Python file uses the following encoding: utf-8
import sys
from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QMainWindow
from PySide2.QtWidgets import QGridLayout
from PySide2.QtWidgets import QWidget
from PySide2.QtWidgets import QAction
from PySide2.QtWidgets import QMenuBar
from PySide2.QtWidgets import QFileDialog
from PySide2.QtWidgets import QSizePolicy
from PySide2.QtGui import QIcon
from PySide2 import QtCore
from gui.UserList import UserList
from gui.AlbumList import AlbumList
from gui.StatisticsArea import StatisticsArea
from core.Database import Database
from files.Saver import Saver
from files.Loader import Loader


from PySide2.QtWinExtras import QtWin
myappid = 'mycompany.myproduct.subproduct.version'
QtWin.setCurrentProcessExplicitAppUserModelID(myappid)

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.db = Loader().load('db.json')
        self.central = QWidget()
        self.setCentralWidget(self.central)
        self.setWindowTitle("RateMe")
        self.resize(1100, 820)
        self.layout = QGridLayout()
        self.init_menu_bar()

        self.user_list = UserList(self.db, self)
        self.layout.addWidget(self.user_list, 0, 2, 2, 1)

        self.album_list = AlbumList(self.db, self)
        self.layout.addWidget(self.album_list, 0, 0, 2, 1)

        self.statistics_area = StatisticsArea(self.db, self)
        self.layout.addWidget(self.statistics_area, 1, 0, 1, 2)

        self.central.setLayout(self.layout)
        self.db.mainwindow = self

        self.refresh()

    def init_menu_bar(self):
        bar = self.menuBar()
        file = bar.addMenu("File")
        imp = QAction("Import", self)
        imp.setShortcut("Ctrl+I")
        imp.triggered.connect(self.import_dialog)
        file.addAction(imp)
        save = QAction("Save", self)    
        save.setShortcut("Ctrl+S")
        save.triggered.connect(self.save)
        file.addAction(save)
        save_as = QAction("Save As", self)
        save_as.triggered.connect(self.save_as_dialog)
        file.addAction(save_as)
        
    def import_dialog(self):
        loader = Loader()
        path, _ = QFileDialog().getOpenFileName(None, "Import", "", "json (*.json)")
        self.db = loader.load(path)
        self.refresh()

    def save(self):
        saver = Saver()
        path = './db.json'
        saver.save(self.db, path)

    def save_as_dialog(self):
        saver = Saver()
        path, _ = QFileDialog().getSaveFileName(None, "Save As", "", "json (*.json)")
        saver.save(self.db, path)

    def refresh(self):
        self.layout.removeWidget(self.user_list)
        self.layout.removeWidget(self.album_list)
        self.layout.removeWidget(self.statistics_area)

        self.user_list.deleteLater()
        self.album_list.deleteLater()
        self.statistics_area.deleteLater()

        self.user_list = UserList(self.db, self)
        self.album_list = AlbumList(self.db, self)
        self.statistics_area = StatisticsArea(self.db, self)

        self.user_list.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.album_list.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.statistics_area.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.db.user_view = self.user_list
        self.db.album_view = self.album_list

        self.layout.addWidget(self.user_list, 0, 2, 2, 1)
        self.layout.addWidget(self.album_list, 0, 0, 1, 2)
        self.layout.addWidget(self.statistics_area, 1, 0, 1, 2)



if __name__ == "__main__":
    app = QApplication([])
    app.setWindowIcon(QIcon('recources/ratemeicon.ico'))
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
