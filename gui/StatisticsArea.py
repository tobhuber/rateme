from PySide2.QtWidgets import QGroupBox
from PySide2.QtWidgets import QHBoxLayout
from PySide2.QtCore import QSize

from gui.GlobalRating import GlobalRating
from gui.UserRating import UserRating

class StatisticsArea(QGroupBox):
    def __init__(self, db, parent):
        super().__init__()
        self.db = db
        self.layout = QHBoxLayout()
        self.global_rating = GlobalRating(self.db, self)
        self.user_rating = UserRating(self.db, self)
        self.layout.addWidget(self.global_rating)
        self.layout.addWidget(self.user_rating)
        self.db.global_rating = self.global_rating
        self.db.user_rating = self.user_rating
        self.setLayout(self.layout)
        self.show()

    def sizeHint(self):
        return QSize(600, 300)