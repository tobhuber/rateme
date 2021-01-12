from PySide2.QtWidgets import QGroupBox
from PySide2.QtWidgets import QListWidget
from PySide2.QtWidgets import QListWidgetItem
from PySide2.QtWidgets import QVBoxLayout
from PySide2.QtCore import QSize
from gui.RatingListItem import RatingListItem


class UserRating(QGroupBox):
    def __init__(self, db, parent):
        super().__init__()
        self.parent = parent
        self.db = db 
        self.layout = QVBoxLayout()
        self.list = QListWidget()

        self.refresh()
        self.setLayout(self.layout)


    def refresh(self):
        self.list.deleteLater()
        self.list = QListWidget()
        self.user = self.db.current_user
        if self.user:
            songs = self.db.songs_rated_by(self.user)
            self.setTitle(f"Best rated by {self.user.name}")
        else: 
            songs = []
            self.setTitle(f"Select a user")

        for song in songs:

            item = QListWidgetItem(self.list)
            self.list.addItem(item)
            rating_list_item = RatingListItem(song, self.db, self, self.user)
            self.list.setItemWidget(item, rating_list_item)
            item.setSizeHint(rating_list_item.sizeHint())
            self.list.setItemWidget(item, rating_list_item)
        
        self.layout.addWidget(self.list)

    def sizeHint(self):
        return QSize(200, 200)