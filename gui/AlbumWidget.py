from PySide2.QtWidgets import QGroupBox
from PySide2.QtWidgets import QTabWidget
from PySide2.QtWidgets import QVBoxLayout
from PySide2.QtWidgets import QHBoxLayout
from PySide2.QtWidgets import QGridLayout
from PySide2.QtWidgets import QFormLayout
from PySide2.QtWidgets import QWidget
from PySide2.QtWidgets import QLabel
from PySide2.QtWidgets import QComboBox
from PySide2.QtWidgets import QPushButton
from PySide2.QtWidgets import QSlider
from PySide2.QtWidgets import QLineEdit
from PySide2.QtWidgets import QMessageBox
from PySide2.QtWidgets import QListWidget
from PySide2.QtWidgets import QListWidgetItem
from PySide2.QtGui import QPixmap
from PySide2.QtGui import QIcon
from PySide2.QtCore import QSize
from PySide2.QtCore import Qt
from gui.AddSongDialog import AddSongDialog
from gui.AlbumSortView import AlbumSortView
from gui.AlbumSongListItem import AlbumSongListItem
from gui.EditAlbumDialog import EditAlbumDialog

class AlbumWidget(QTabWidget):
    def __init__(self, db, album, parent):
        super().__init__(parent)
        self.db = db
        self.album = album
        self.parent = parent
        self.overview = QWidget()
        self.songs = QWidget()
        self.init_overview()
        self.init_songs()

    def init_overview(self):
        self.layout = QVBoxLayout()
        self.overview.setLayout(self.layout)
        self.init_top()
        self.init_cover_area()
        self.init_data_area()
        self.addTab(self.overview, "Overview")


    def init_songs(self):
        self.songs.deleteLater()
        self.songs = QWidget()
        self.song_layout = QVBoxLayout()
        self.song_list = QListWidget()

        for song in self.album.songs:
            item = QListWidgetItem(self.song_list)
            self.song_list.addItem(item)
            song_item = AlbumSongListItem(self.db, self.album, song, self)
            item.setSizeHint(song_item.sizeHint())
            self.song_list.setItemWidget(item, song_item)
        
        self.song_layout.addWidget(self.song_list)
        self.songs.setLayout(self.song_layout)
        self.addTab(self.songs, "Songs")

        


    def init_top(self):
        top_layout = QHBoxLayout()
        self.title_edit = QLineEdit(self.album.title)
        self.title_edit.setReadOnly(True)
        edit_button = QPushButton("Edit")
        edit_button.clicked.connect(self.edit)
        delete_button = QPushButton("Delete")
        delete_button.clicked.connect(self.delete)
        top_layout.addWidget(self.title_edit)
        top_layout.addStretch()
        top_layout.addWidget(edit_button)
        top_layout.addWidget(delete_button)
        self.layout.addLayout(top_layout)

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

        self.interpret_label = QLabel("Interpret:")
        self.interpret_edit = QLineEdit(self.album.interpret[0])
        self.interpret_edit.setReadOnly(True)

        song_label = QLabel("Songs:")
        add_song_button = QPushButton("+")
        add_song_button.clicked.connect(self.add_song)
        self.song_box = QComboBox()

        for song in self.album.songs:
            self.song_box.addItem(f"{song.rating}    {song.name}")

        song_layout = QGridLayout()
        
        song_layout.addWidget(self.song_box, 0, 0, 1, 3)
        song_layout.addWidget(add_song_button, 0, 4, 1, 1)

        rater_label = QLabel("Raters:")
        self.rater_box = QComboBox()
        rater_list = sorted([rater.name for rater in self.album.raters])
        for item in rater_list:
            self.rater_box.addItem(item)

        rating_label = QLabel("Rating:")
        self.rating = QSlider()
        self.rating.setOrientation(Qt.Horizontal)
        self.rating.setTickInterval(1)
        self.rating.setMinimum(0)
        self.rating.setMaximum(10)
        self.rating.setValue(int(self.album.rating))
        self.rating.wheelEvent = lambda x: None
        self.rating.mousePressEvent = lambda x: None
        self.rating.mouseMoveEvent = lambda x: None
        self.rating.mouseReleaseEvent =  lambda x: None
        self.rating_edit = QLineEdit()
        self.rating_edit.setText(f"{self.album.rating}/10")
        self.rating_edit.setReadOnly(True)
        self.rating_edit.setFixedWidth(65)
        self.rating_edit.setAlignment(Qt.AlignRight)
        rating_layout = QHBoxLayout()
        rating_layout.addWidget(self.rating)
        rating_layout.addWidget(self.rating_edit)

        data_layout.addRow(self.interpret_label, self.interpret_edit)
        data_layout.addRow(song_label, song_layout)
        data_layout.addRow(rater_label, self.rater_box)
        data_layout.addRow(rating_label, rating_layout)

        self.layout.addLayout(data_layout)

    def add_song(self):
        _ = AddSongDialog(self.parent.db, self.album, self)

    def refresh(self):
        self.song_box.clear()
        self.rater_box.clear()

        self.title_edit.setText(self.album.title)
        self.interpret_edit.setText(self.album.interpret[0])
        for song in self.album.songs:
            self.song_box.addItem(f"{song.name}: {song.rating}")

        rater_list = sorted([rater.name for rater in self.album.raters])
        print(rater_list)
        for item in rater_list:
            self.rater_box.addItem(item)

        self.init_songs()
        self.rating.setValue(self.album.rating)
        self.rating_edit.setText(f"{self.album.rating}/10")

    def delete(self):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Delete Album?")
        msg_box.setText("Yeet?")
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        msg_box.setDefaultButton(QMessageBox.Cancel)
        ret = msg_box.exec_()

        if ret == QMessageBox.Yes:    
            self.db.delete_album(self.album)
            self.db.mainwindow.refresh()     

    def edit(self):
        view = EditAlbumDialog(self.db, self.album, self) 

    def open_album_sort_view(self):
        view = AlbumSortView(self.db, self.album, self)