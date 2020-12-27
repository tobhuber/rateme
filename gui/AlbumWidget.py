from PySide2.QtWidgets import QGroupBox
from PySide2.QtWidgets import QVBoxLayout
from PySide2.QtWidgets import QHBoxLayout
from PySide2.QtWidgets import QGridLayout
from PySide2.QtWidgets import QFormLayout
from PySide2.QtWidgets import QLabel
from PySide2.QtWidgets import QComboBox
from PySide2.QtWidgets import QPushButton
from PySide2.QtWidgets import QSlider
from PySide2.QtWidgets import QLineEdit
from PySide2.QtGui import QPixmap
from PySide2.QtGui import QIcon
from PySide2.QtCore import QSize
from PySide2.QtCore import Qt
from gui.AddSongDialog import AddSongDialog
from gui.AlbumSortView import AlbumSortView

class AlbumWidget(QGroupBox):
    def __init__(self, db, album, parent):
        super().__init__(parent)
        self.db = db
        self.album = album
        self.parent = parent
        self.setTitle(self.album.title)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.setFixedSize(QSize(350, 450))
        self.init_remove()
        self.init_cover_area()
        self.init_data_area()

    def init_remove(self):
        delete_button = QPushButton("Delete")
        delete_button.clicked.connect(self.delete)
        self.layout.addWidget(delete_button)

    def init_cover_area(self):
        cover_area = QGroupBox()
        cover_layout = QGridLayout(cover_area)
        cover_button = QPushButton()

        if (self.album.cover):
            pixmap = QPixmap(self.album.cover)
        else:
            pixmap = QPixmap('recources/default.png')

        pixmap = pixmap.scaled(200, 200, Qt.KeepAspectRatio) 

        icon = QIcon(pixmap)
        cover_button.setIcon(icon)
        cover_button.setIconSize(QSize(200, 200))
        cover_button.setFixedSize(QSize(200, 200))
        cover_button.clicked.connect(self.open_album_sort_view)
        cover_layout.addWidget(cover_button)
        self.layout.addWidget(cover_area)

    
    def init_data_area(self):
        data_layout = QFormLayout()

        interpret_label = QLabel("Interpret:")
        interpret_edit = QLineEdit(self.album.interpret[0])
        interpret_edit.setReadOnly(True)

        song_label = QLabel("Songs:")
        add_song_button = QPushButton("+")
        add_song_button.clicked.connect(self.add_song)
        self.song_box = QComboBox()

        for song in self.album.songs:
            self.song_box.addItem(f"{song.name}: {song.rating}")

        song_layout = QGridLayout()
        
        song_layout.addWidget(self.song_box, 0, 0, 1, 3)
        song_layout.addWidget(add_song_button, 0, 4, 1, 1)

        rater_label = QLabel("Raters:")
        self.rater_box = QComboBox()

        for rater in self.album.raters:
            self.rater_box.addItem(rater.name)

        rating_label = QLabel("Rating:")
        self.rating = QSlider()
        self.rating.setOrientation(Qt.Horizontal)
        self.rating.setTickInterval(1)
        self.rating.setMinimum(0)
        self.rating.setMaximum(10)
        self.rating.setValue(int(self.album.rating))
        self.rating_edit = QLineEdit()
        self.rating_edit.setText(f"{self.album.rating}/10")
        self.rating_edit.setReadOnly(True)
        rating_layout = QHBoxLayout()
        rating_layout.addWidget(self.rating)
        rating_layout.addWidget(self.rating_edit)

        data_layout.addRow(interpret_label, interpret_edit)
        data_layout.addRow(song_label, song_layout)
        data_layout.addRow(rater_label, self.rater_box)
        data_layout.addRow(rating_label, rating_layout)

        self.layout.addLayout(data_layout)

    def add_song(self):
        dialog = AddSongDialog(self.parent.db, self.album, self)

    def refresh(self):
        self.song_box.clear()
        self.rater_box.clear()

        for song in self.album.songs:
            self.song_box.addItem(f"{song.name}: {song.rating}")

        for rater in self.album.raters:
            self.rater_box.addItem(rater.name)

        self.rating.setValue(self.album.rating)
        self.rating_edit.setText(f"{self.album.rating}/10")

    def delete(self):
        self.db.delete_album(self.album)
        self.db.album_view.refresh()        

    def open_album_sort_view(self):
        view = AlbumSortView(self.db, self.album, self)