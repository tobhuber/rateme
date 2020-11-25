from PySide2.QtWidgets import QWidget
from PySide2.QtWidgets import QVBoxLayout


class UserList(QWidget):
    
    def __init__(self, users):
        
        self.setLayout(QVBoxLayout())
