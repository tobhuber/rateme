from PySide2.QtWidgets import QDialog
from PySide2.QtWidgets import QGridLayout
from PySide2.QtWidgets import QPushButton
from PySide2.QtWidgets import QLabel
from PySide2.QtWidgets import QLineEdit

class EditAlbumDialog(QDialog):
    def __init__(self, db, album, parent):
        super().__init__(parent)
        self.album = album
        self.parent = parent 
        self.db = db
        self.setWindowTitle("Edit Album")
        layout = QGridLayout()

        title_label = QLabel("Album Name:", self)
        self.title_edit = QLineEdit(self)

        interpret_label = QLabel("Interpret Name:", self)
        self.interpret_edit = QLineEdit(self)

        layout.addWidget(title_label, 0, 0, 1, 1)
        layout.addWidget(self.title_edit, 0, 1, 1, 2)

        layout.addWidget(interpret_label, 1, 0, 1, 1)
        layout.addWidget(self.interpret_edit, 1, 1, 1, 2)

        edit = QPushButton("Edit", self)
        cancel = QPushButton("Cancel", self)

        edit.clicked.connect(self.edit)
        cancel.clicked.connect(self.cancel)

        layout.addWidget(edit, 2, 1, 1, 1)
        layout.addWidget(cancel, 2, 2, 1, 1)

        self.setLayout(layout)
        self.show()

    def edit(self):
        self.album.title = self.title_edit.text()
        self.album.interpret = [self.interpret_edit.text()]
        self.db.mainwindow.refresh()
        self.accept()

    def cancel(self):
        self.reject()