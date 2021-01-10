from PySide2.QtWidgets import QWidget
from PySide2.QtWidgets import QHBoxLayout
from PySide2.QtWidgets import QLineEdit
from PySide2.QtWidgets import QSpinBox

class RatingListItem(QWidget):
    def __init__(self, song, db, parent, rater=None):
        super().__init__()
        self.song = song
        self.db = db 
        self.parent = parent
        self.layout = QHBoxLayout()
        self.title = QLineEdit()
        self.title.setText(self.song.name)
        self.title.setReadOnly(True)
        self.interpret = QLineEdit()
        self.interpret.setText(self.song.album.interpret[0])
        self.interpret.setReadOnly(True)
        self.rating = QSpinBox()
        if rater:
            self.rating.setMinimum(self.song.raters[rater])
            self.rating.setMaximum(self.song.raters[rater])
            self.rating.setValue(self.song.raters[rater])
        else:
            self.rating.setMinimum(self.song.rating)
            self.rating.setMaximum(self.song.rating)
            self.rating.setValue(self.song.rating)
        self.layout.addWidget(self.title)
        self.layout.addWidget(self.interpret)
        self.layout.addWidget(self.rating)
        self.setLayout(self.layout)
        self.show()