from PySide2.QtWidgets import QDialog
from PySide2.QtWidgets import QGridLayout
from PySide2.QtWidgets import QLabel
from PySide2.QtWidgets import QFormLayout
from PySide2.QtWidgets import QHBoxLayout
from PySide2.QtWidgets import QLineEdit
from PySide2.QtWidgets import QComboBox
from PySide2.QtWidgets import QPushButton
from PySide2.QtWidgets import QSlider
from gui.AddRaterDialog import AddRaterDialog
from core.Song import Song

class AddSongDialog(QDialog):
    def __init__(self, db, album, parent):
        super().__init__(parent)
        self.db = db
        self.album = album
        self.parent = parent
        self.raters = {}
        self.rating = 0
        self.setWindowTitle("Add Song")
        self.layout = QGridLayout()
        self.init_data_area()
        self.init_add_and_cancel()
        self.setLayout(self.layout)
        self.show()

    def init_data_area(self):
        data_layout = QFormLayout()

        album_label = QLabel("Album:")
        album_edit = QLineEdit()
        album_edit.setReadOnly(True)
        album_edit.setText(self.album.title)

        song_label = QLabel("Title:")
        self.song_edit = QLineEdit()

        rater_label = QLabel("Rater:")
        self.rater_box = QComboBox()
        rater_add_button = QPushButton("Add Rater")
        rater_add_button.clicked.connect(self.add_rater)
        rater_layout = QHBoxLayout()
        rater_layout.addWidget(self.rater_box)
        rater_layout.addWidget(rater_add_button)
        
        data_layout.addRow(album_label, album_edit)
        data_layout.addRow(song_label, self.song_edit)
        data_layout.addRow(rater_label, rater_layout)

        self.layout.addLayout(data_layout, 0, 0, 3, 3)


    def init_add_and_cancel(self):

        add = QPushButton("Add", self)
        cancel = QPushButton("Cancel", self)

        add.clicked.connect(self.add)
        cancel.clicked.connect(self.cancel)

        self.layout.addWidget(add, 4, 1, 1, 1)
        self.layout.addWidget(cancel, 4, 2, 1, 1)

    def add(self):
        title = self.song_edit.text()
        son = Song(title, self.album, self.raters, self.rating)
        self.db.albums[self.album.hash].addSong(son)
        self.parent.refresh()             
        self.accept()

    def cancel(self):
        self.reject()

    def add_rater(self):
        add_rater = AddRaterDialog(self.db, self)

