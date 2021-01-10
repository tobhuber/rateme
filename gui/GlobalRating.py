from PySide2.QtWidgets import QGroupBox
from PySide2.QtWidgets import QListWidget
from PySide2.QtWidgets import QListWidgetItem
from PySide2.QtWidgets import QVBoxLayout
from PySide2.QtCore import QSize
from gui.RatingListItem import RatingListItem


class GlobalRating(QGroupBox):
    def __init__(self, db, parent):
        super().__init__()
        self.parent = parent
        self.db = db 
        self.layout = QVBoxLayout()
        self.list = QListWidget()

        self.refresh()
        self.setTitle("Best rated Songs")
        self.setLayout(self.layout)
        self.show()


    def refresh(self):
        self.list.deleteLater()
        self.list = QListWidget()
        for song in self.db.songs_rated():
            item = QListWidgetItem(self.list)
            self.list.addItem(item)
            rating_list_item = RatingListItem(song, self.db, self)
            self.list.setItemWidget(item, rating_list_item)
            item.setSizeHint(rating_list_item.sizeHint())
            self.list.setItemWidget(item, rating_list_item)
        
        self.layout.addWidget(self.list)

    def sizeHint(self):
        return QSize(200, 200)
