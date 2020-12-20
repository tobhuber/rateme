from PySide2.QtWidgets import QDialog
from PySide2.QtWidgets import QGridLayout
from PySide2.QtWidgets import QPushButton
from PySide2.QtWidgets import QLabel
from PySide2.QtWidgets import QLineEdit
from core.User import User

class AddUserDialog(QDialog):
    def __init__(self, parent, db):
        super().__init__(parent)
        self.parent = parent 
        self.db = db
        self.setWindowTitle("Add User")
        self.setWhatsThis(f"Enter a users name and click the 'Add'-Button or hit cancel to close this window.")
        layout = QGridLayout()

        label = QLabel("User Name:", self)
        self.line = QLineEdit(self)

        layout.addWidget(label, 0, 0, 1, 1)
        layout.addWidget(self.line, 0, 1, 1, 2)

        add = QPushButton("Add", self)
        cancel = QPushButton("Cancel", self)

        add.clicked.connect(self.add)
        cancel.clicked.connect(self.cancel)

        layout.addWidget(add, 1, 1, 1, 1)
        layout.addWidget(cancel, 1, 2, 1, 1)

        self.setLayout(layout)
        self.show()

    def add(self):
        name = self.line.text()
        self.db.user[name] = User(name)
        self.parent.generate_user_list()
        self.accept()

    def cancel(self):
        self.reject()