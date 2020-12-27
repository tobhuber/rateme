from PySide2.QtWidgets import QDialog
from PySide2.QtWidgets import QVBoxLayout
from PySide2.QtWidgets import QGridLayout
from PySide2.QtWidgets import QFormLayout
from PySide2.QtWidgets import QPushButton
from PySide2.QtWidgets import QGroupBox
from PySide2.QtWidgets import QFileDialog
from PySide2.QtWidgets import QLabel
from PySide2.QtWidgets import QLineEdit
from PySide2.QtGui import QIcon
from PySide2.QtGui import QPixmap
from PySide2.QtCore import QSize
from core.Album import Album

class AddAlbumDialog(QDialog):
    def __init__(self, db, parent):
        super().__init__(parent)
        self.parent = parent
        self.db = db        
        self.setWindowTitle("Add Album")
        
        self.layout = QGridLayout()
        self.box_layout = QVBoxLayout()
        
        self.init_cover_prev()
        self.init_data_area()
        self.init_add_and_cancel()
        self.layout.addLayout(self.box_layout, 0, 0, 3, 3)
        self.setLayout(self.layout)
        self.show()

    def init_cover_prev(self):
        self.cover = "recources/default.png"
        self.click = QPushButton(self)
        self.click.clicked.connect(self.cover_dialog)
        cover_box = QGroupBox(self)
        pixmap = QPixmap(self.cover)
        icon = QIcon(pixmap)
        self.click.setIcon(icon)
        self.click.setIconSize(QSize(200, 200))
        self.click.setFixedSize(QSize(200,200))
        cover_layout = QGridLayout()
        cover_layout.addWidget(self.click)
        cover_box.setLayout(cover_layout)
        cover_box.setTitle("Cover Preview")
        self.box_layout.addWidget(cover_box)


    def cover_dialog(self):
        path, modus = QFileDialog().getOpenFileName()
        if path:
            self.cover = path
            pixmap = QPixmap(self.cover)
            icon = QIcon(pixmap)
            self.click.setIcon(icon)
            self.click.setIconSize(QSize(200, 200))
            self.click.setFixedSize(QSize(200,200))

    
    def init_data_area(self):
        data_layout = QFormLayout()

        title_label = QLabel("Title:")
        self.title_edit = QLineEdit()

        interpret_label = QLabel("Interpret:")
        self.interpret_edit = QLineEdit()

        data_layout.addRow(title_label, self.title_edit)
        data_layout.addRow(interpret_label, self.interpret_edit)
        self.box_layout.addLayout(data_layout)

    
    def init_add_and_cancel(self):
        add = QPushButton("Add", self)
        cancel = QPushButton("Cancel", self)

        add.clicked.connect(self.add)
        cancel.clicked.connect(self.cancel)

        self.layout.addWidget(add, 4, 1, 1, 1)
        self.layout.addWidget(cancel, 4, 2, 1, 1)


    def add(self):
        self.title = self.title_edit.text()
        self.interpret = self.interpret_edit.text()
        alb = Album(self.title, [self.interpret], self.cover)
        self.db.albums[alb.hash] = alb
        self.parent.refresh()
        self.accept()       


    def cancel(self):
        self.reject()



