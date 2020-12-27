from PySide2.QtWidgets import QGroupBox
from PySide2.QtWidgets import QGridLayout
from PySide2.QtWidgets import QVBoxLayout
from PySide2.QtWidgets import QHBoxLayout
from PySide2.QtWidgets import QScrollArea
from PySide2.QtWidgets import QPushButton
from PySide2.QtWidgets import QWidget
from PySide2.QtWidgets import QSizePolicy
from PySide2.QtCore import Qt
from gui.AlbumWidget import AlbumWidget
from gui.AddAlbumDialog import AddAlbumDialog

class AlbumList(QGroupBox):
    
    def __init__(self, db, parent):
        super().__init__()
        self.db = db
        self.setParent(parent)
        self.setTitle("Albums")

        self.scroll = QScrollArea()

        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignTop)

        self.layout.addLayout(self.init_top())
        self.refresh()

        self.setLayout(self.layout)


    def init_top(self):
        top = QHBoxLayout()
        add = QPushButton("Add Album", self)
        add.clicked.connect(self.add_album)
        top.addWidget(add)        
        return top


    def refresh(self):
        self.scroll.deleteLater()
        scroll_layout = QVBoxLayout(self)
        scroll_widget = QWidget()
        scroll_widget.setLayout(scroll_layout)

        for name in self.db.albums:
            album_widget = AlbumWidget(self.db, self.db.albums[name], self)
            scroll_layout.addWidget(album_widget)

        self.scroll = QScrollArea()
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(False)
        self.scroll.setWidget(scroll_widget)

        self.layout.addWidget(self.scroll)
        

    def add_album(self):
        dialog = AddAlbumDialog(self.db, self)