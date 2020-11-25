from PySide2.QtWidgets import QPushButton

class UserWidget(QPushButton):
    
    def __init__(self, user):
        super(UserWidget, self).__init__()
        self.setText(user.name)
        
