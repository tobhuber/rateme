from PySide2.QtWidgets import QHBoxLayout
from PySide2.QtWidgets import QLabel
from PySide2.QtWidgets import QSpinBox
from PySide2.QtWidgets import QWidget
from PySide2.QtWidgets import QPushButton
from PySide2.QtWidgets import QCheckBox

class SongListItem(QWidget):

    def __init__(self, song, parent):
        super().__init__()
        self.song = song
        self.parent = parent
        
        self.layout = QHBoxLayout()
        self.init_data()
        self.setLayout(self.layout)
        self.show()

    def init_data(self):
        self.changed = QCheckBox()
        self.changed.stateChanged.connect(self.value_changed)
        song_name = QLabel(self.song.name)
        self.song_rating = QSpinBox()
        self.song_rating.setMinimum(0)
        self.song_rating.setMaximum(10)
        self.song_rating.setSingleStep(1)
        self.song_rating.valueChanged.connect(self.value_changed)
        self.song_rating.wheelEvent = lambda event: None
        
        self.layout.addWidget(song_name)
        self.layout.addStretch()
        self.layout.addWidget(self.song_rating)
        self.layout.addWidget(self.changed)


    def value_changed(self):
        rater = self.parent.db.user[self.parent.rater_box.currentText()]

        if rater not in self.parent.changes:
            self.parent.changes[rater] = {}

        self.parent.changes[rater][self.song] = (self.song_rating.value(), self.changed.isChecked())
        
