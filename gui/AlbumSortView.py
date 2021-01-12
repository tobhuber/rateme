from PySide2.QtWidgets import QDialog
from PySide2.QtWidgets import QGridLayout
from PySide2.QtWidgets import QFormLayout
from PySide2.QtWidgets import QListWidget
from PySide2.QtWidgets import QListWidgetItem
from PySide2.QtWidgets import QPushButton
from PySide2.QtWidgets import QAbstractItemView
from PySide2.QtWidgets import QLabel
from PySide2.QtWidgets import QComboBox
from PySide2.QtCore import QSize
from gui.SongListItem import SongListItem


class AlbumSortView(QDialog):
    def __init__(self, db, album, parent):
        super().__init__()
        self.db = db
        self.parent = parent
        self.album = album
        self.changes = {}
        self.layout = QGridLayout()

        self.init_list()
        self.init_options()
        self.init_ok_and_cancel()
        self.setLayout(self.layout)
        self.resize(QSize(700, 500))
        self.show()
        

    def init_list(self):
        self.list = QListWidget()
        self.list.setDragDropMode(QAbstractItemView.InternalMove)
        
        for song in self.album.songs:
            item = QListWidgetItem(self.list)
            self.list.addItem(item)
            song_list_item = SongListItem(song, self)
            item.setSizeHint(song_list_item.sizeHint())
            self.list.setItemWidget(item, song_list_item)
        
        self.layout.addWidget(self.list, 0, 0, 1, 1)


    def init_options(self):

        options_layout = QFormLayout()
        calc_button = QPushButton("Calculate Rating")
        calc_button.clicked.connect(self.calculate_rating)

        self.apply_button = QPushButton("Check all")
        self.apply_button.clicked.connect(self.check_all)

        rater_label = QLabel("Rater:")
        self.rater_box = QComboBox()

        for name in self.db.user:
            self.rater_box.addItem(self.db.user[name].name)

        self.rater_box.currentTextChanged.connect(self.get_raters_rating)
        self.get_raters_rating()

        options_layout.addRow(rater_label, self.rater_box)
        options_layout.addRow(calc_button, self.apply_button)

        self.layout.addLayout(options_layout, 0, 1, 1, 2)
        

    def init_ok_and_cancel(self):
        ok = QPushButton("Ok", self)
        cancel = QPushButton("Cancel", self)

        ok.clicked.connect(self.ok)
        cancel.clicked.connect(self.cancel)

        self.layout.addWidget(ok, 4, 1, 1, 1)
        self.layout.addWidget(cancel, 4, 2, 1, 1)

    def ok(self):
        songs = self.db.songs()
        
        for rater in self.changes:
            for song in self.changes[rater]:
                 rating, changed = self.changes[rater][song]
                 if changed:
                     songs[song.hash].addRating(rater, rating)

        self.db.mainwindow.refresh()
        self.accept()

    def cancel(self):
        self.reject()

    def calculate_rating(self):
        length = self.list.count()
        rating_range = length/11
        for i in range(length):
            item = self.list.item(i)
            widget = self.list.itemWidget(item)
            widget.song_rating.setValue(abs(int(10 - (i / rating_range))))
            

    def get_raters_rating(self):
        if self.rater_box.count() == 0:
            return
        rater = self.db.user[self.rater_box.currentText()]
        for i in range(self.list.count()):
            widget = self.list.itemWidget(self.list.item(i))
            if rater in self.changes:
                if widget.song in self.changes[rater]:
                    rating, changed = self.changes[rater][widget.song]
                    widget.song_rating.setValue(rating)
                    widget.changed.setChecked(changed)
                else:
                    if rater in widget.song.raters:
                        widget.song_rating.setValue(widget.song.raters[rater])
                        widget.changed.setChecked(True)
                    else:
                        widget.song_rating.setValue(0)
                        widget.changed.setChecked(False)
            else:
                if rater in widget.song.raters:
                    widget.song_rating.setValue(widget.song.raters[rater])
                    widget.changed.setChecked(True)
                else:
                    widget.song_rating.setValue(0)
                    widget.changed.setChecked(False)

    def check_all(self):
        for i in range(self.list.count()):
            self.list.itemWidget(self.list.item(i)).changed.setChecked(True)

    def uncheck_all(self):
        for i in range(self.list.count()):
            self.list.itemWidget(self.list.item(i)).changed.setChecked(False)
