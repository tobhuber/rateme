from PySide2.QtWidgets import QDialog
from PySide2.QtWidgets import QGridLayout
from PySide2.QtWidgets import QFormLayout
from PySide2.QtWidgets import QLabel
from PySide2.QtWidgets import QComboBox
from PySide2.QtWidgets import QSpinBox
from PySide2.QtWidgets import QPushButton

class AddRaterDialog(QDialog):

    def __init__(self, db, parent):
        super().__init__(parent)
        self.parent = parent
        self.db = db 
        self.layout = QGridLayout()
        self.init_data_area()
        self.init_add_and_cancel()
        self.setLayout(self.layout)
        self.show()

    def init_data_area(self):
        name_label = QLabel("Choose Rater:")
        self.name_box = QComboBox()

        for name in sorted(self.db.user):
            self.name_box.addItem(self.db.user[name].name)

        rating_label = QLabel("Rating:")
        self.rating_box = QSpinBox()
        self.rating_box.setMaximum(10)
        self.rating_box.setMinimum(0)
        self.rating_box.setSingleStep(1)

        data_layout = QFormLayout()
        data_layout.addRow(name_label, self.name_box)
        data_layout.addRow(rating_label, self.rating_box)
        self.layout.addLayout(data_layout, 0, 0, 3, 3)

    def init_add_and_cancel(self):
        add = QPushButton("Add", self)
        cancel = QPushButton("Cancel", self)

        add.clicked.connect(self.add)
        cancel.clicked.connect(self.cancel)

        self.layout.addWidget(add, 4, 1, 1, 1)
        self.layout.addWidget(cancel, 4, 2, 1, 1)

    def add(self):
        rater = self.db.user[self.name_box.currentText()]
        self.parent.raters[rater] = self.rating_box.value()
        self.parent.rater_box.addItem(rater.name)
        self.accept()

    def cancel(self):
        self.reject()