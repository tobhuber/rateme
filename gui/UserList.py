from PySide2.QtWidgets import QWidget
from PySide2.QtWidgets import QVBoxLayout
from PySide2.QtWidgets import QHBoxLayout
from PySide2.QtWidgets import QPushButton
from PySide2.QtWidgets import QGroupBox
from PySide2.QtWidgets import QFrame
from PySide2 import QtCore
from gui.UserWidget import UserWidget

from gui.AddUserDialog import AddUserDialog


class UserList(QGroupBox):
    
    def __init__(self, db, parent):
        super().__init__()
        self.db = db
        self.setParent(parent)
        self.setTitle("User")
        self.layout = QVBoxLayout()
        self.layout.setAlignment(QtCore.Qt.AlignTop)
        self.layout.addLayout(self.init_top())

        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        self.layout.addWidget(line)
        self.list_box = QGroupBox()
        self.refresh()
        self.setLayout(self.layout)

    def init_top(self):
        top = QHBoxLayout()
        add = QPushButton("Add User", self)
        add.clicked.connect(self.add_user)
        top.addWidget(add)        
        return top

    def add_user(self):
        dialog = AddUserDialog(self.db, self)

    def refresh(self):
        self.layout.removeWidget(self.list_box)
        self.list_box.deleteLater()
        self.list_box = QGroupBox()
        list_layout = QVBoxLayout()
        for name in self.db.user:
            user_widget = UserWidget(self.db, self.db.user[name], self)
            list_layout.addWidget(user_widget)
        self.list_box.setLayout(list_layout)
        self.layout.addWidget(self.list_box)        
