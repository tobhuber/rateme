from PySide2.QtWidgets import QWidget 
from PySide2.QtWidgets import QHBoxLayout
from PySide2.QtWidgets import QLineEdit
from PySide2.QtWidgets import QPushButton
from PySide2.QtWidgets import QMessageBox
from gui.EditSongDialog import EditSongDialog

class AlbumSongListItem(QWidget):
    def __init__(self, db, album, song, widget):
        super().__init__()
        self.song = song
        self.album = album
        self.db = db
        self.widget = widget
        self.layout = QHBoxLayout()
        self.title = QLineEdit(self.song.name)
        self.title.setReadOnly(True)
        self.delete_button = QPushButton("-")
        self.delete_button.clicked.connect(self.delete)
        self.edit_button = QPushButton("Edit")
        self.edit_button.clicked.connect(self.edit)
        self.layout.addWidget(self.title)
        self.layout.addWidget(self.delete_button)
        self.layout.addWidget(self.edit_button)
        self.setLayout(self.layout)

    def delete(self):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Delete Song?")
        msg_box.setText("Yeet?")
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        msg_box.setDefaultButton(QMessageBox.Cancel)
        ret = msg_box.exec_()

        if ret == QMessageBox.Yes:   
            self.album.deleteSong(self.song)
            self.db.mainwindow.refresh()

    def edit(self):
        dialog = EditSongDialog(self.db, self.song, self.widget)