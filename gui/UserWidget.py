from PySide2.QtWidgets import QPushButton
from PySide2.QtWidgets import QWidget
from PySide2.QtWidgets import QHBoxLayout
from PySide2.QtWidgets import QMessageBox
from gui.EditUserDialog import EditUserDialog


class UserWidget(QWidget):
    
    def __init__(self, db, user, parent):
        super().__init__()

        self.db = db 
        self.user = user
        self.parent = parent

        self.layout = QHBoxLayout()

        self.init_user()
        self.init_delete()
        self.init_edit()

        self.setLayout(self.layout)
        self.show()

    def init_user(self):
        self.user_button = QPushButton(self.user.name)
        self.user_button.clicked.connect(self.select)
        self.layout.addWidget(self.user_button)
        self.layout.addStretch()

        
    def init_delete(self):
        self.delete_button = QPushButton("-")
        self.delete_button.clicked.connect(self.delete)
        self.layout.addWidget(self.delete_button)

    def init_edit(self):
        self.edit_button = QPushButton("Edit")
        self.edit_button.clicked.connect(self.edit)
        self.layout.addWidget(self.edit_button)

    def delete(self):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Delete User?")
        msg_box.setText("Yeet?")
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        msg_box.setDefaultButton(QMessageBox.Cancel)
        ret = msg_box.exec_()

        if ret == QMessageBox.Yes:    
            if self.db.current_user == self.user:
                self.db.current_user = None
            self.db.delete_user(self.user)
            self.db.user_view.refresh()
            self.db.album_view.refresh()
            self.db.global_rating.refresh()
            self.db.user_rating.refresh()

    def edit(self):
        dialog = EditUserDialog(self.db, self.user, self)

    def select(self):
        self.db.current_user = self.user
        self.db.user_rating.refresh()
        self.parent.setSelected(True)