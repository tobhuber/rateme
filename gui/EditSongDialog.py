from PySide2.QtWidgets import QDialog
from PySide2.QtWidgets import QGridLayout
from PySide2.QtWidgets import QPushButton
from PySide2.QtWidgets import QLabel
from PySide2.QtWidgets import QLineEdit

class EditSongDialog(QDialog):
    def __init__(self, db, song, parent):
        super().__init__(parent)
        self.song = song
        self.parent = parent 
        self.db = db
        self.setWindowTitle("Edit Song")
        layout = QGridLayout()

        label = QLabel("Song Name:", self)
        self.line = QLineEdit(self)

        layout.addWidget(label, 0, 0, 1, 1)
        layout.addWidget(self.line, 0, 1, 1, 2)

        edit = QPushButton("Edit", self)
        cancel = QPushButton("Cancel", self)

        edit.clicked.connect(self.edit)
        cancel.clicked.connect(self.cancel)

        layout.addWidget(edit, 1, 1, 1, 1)
        layout.addWidget(cancel, 1, 2, 1, 1)

        self.setLayout(layout)
        self.show()

    def edit(self):
        self.song.name = self.line.text()
        
        self.db.album_view.refresh()
        self.db.global_rating.refresh()
        self.db.user_rating.refresh()
        self.accept()

    def cancel(self):
        self.reject()