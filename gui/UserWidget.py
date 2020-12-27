from PySide2.QtWidgets import QPushButton
from PySide2.QtWidgets import QWidget
from PySide2.QtWidgets import QGridLayout
from gui.EditUserDialog import EditUserDialog

class UserWidget(QWidget):
    
    def __init__(self, db, user, parent):
        super().__init__(parent)

        self.db = db 
        self.user = user
        self.parent = parent

        self.layout = QGridLayout()

        self.init_user()
        self.init_delete()
        self.init_edit()

        self.setLayout(self.layout)
        self.show()

    def init_user(self):
        self.user_button = QPushButton(self.user.name)
        self.layout.addWidget(self.user_button, 0, 0, 1, 2)

        
    def init_delete(self):
        self.delete_button = QPushButton("-")
        self.delete_button.clicked.connect(self.delete)
        self.layout.addWidget(self.delete_button, 0, 2, 1, 1)

    def init_edit(self):
        self.edit_button = QPushButton("Edit")
        self.edit_button.clicked.connect(self.edit)
        self.layout.addWidget(self.edit_button, 0, 3, 1, 1)

    def delete(self):
        self.db.delete_user(self.user)
        self.db.user_view.refresh()
        self.db.album_view.refresh()

    def edit(self):
        dialog = EditUserDialog(self.db, self.user, self)


