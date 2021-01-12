from PySide2.QtWidgets import QWidget
from PySide2.QtWidgets import QVBoxLayout
from PySide2.QtWidgets import QHBoxLayout
from PySide2.QtWidgets import QPushButton
from PySide2.QtWidgets import QGroupBox
from PySide2.QtWidgets import QFrame
from PySide2.QtWidgets import QScrollArea
from PySide2.QtWidgets import QListWidget
from PySide2.QtWidgets import QListWidgetItem
from PySide2 import QtCore
from gui.UserWidget import UserWidget

from gui.AddUserDialog import AddUserDialog


class UserList(QGroupBox):

    def __init__(self, db, parent):
        super().__init__()
        self.db = db
        self.setTitle("User")
        self.list = QListWidget()
        self.scroll = QScrollArea()
        self.layout = QVBoxLayout()
        self.layout.addLayout(self.init_top())
        self.refresh()
        self.setLayout(self.layout)

    def init_top(self):
        top = QHBoxLayout()
        add = QPushButton("Add User", self)
        add.clicked.connect(self.add_user)
        top.addStretch()
        top.addWidget(add)        
        return top

    def add_user(self):
        dialog = AddUserDialog(self.db, self)

    def refresh(self):
        self.list.deleteLater()
        self.list = QListWidget()

        for name in sorted(self.db.user):
            item = QListWidgetItem(self.list)
            self.list.addItem(item)
            user_item = UserWidget(self.db, self.db.user[name], item)
            item.setSizeHint(user_item.sizeHint())
            self.list.setItemWidget(item, user_item)

        self.layout.addWidget(self.list)

    def sizeHint(self):
        return QtCore.QSize(320, 720)
