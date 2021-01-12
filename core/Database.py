class Database:
    def __init__(self, user={}, albums={}, user_view=None, album_view=None, global_rating=None, user_rating=None, mainwindow=None):
        self.user = user
        self.albums = albums
        self.user_view = user_view
        self.album_view = album_view
        self.global_rating = global_rating
        self.user_rating = user_rating
        self.mainwindow = mainwindow
        self.current_user = None

    def songs(self):
        songs = {}
        for album in self.albums:
            for song in self.albums[album].songs:
                songs[song.hash] = song
        return songs

    def delete_user(self, user):
        del self.user[user.name]
        songs = self.songs()
        for key in songs:
            songs[key].removeRater(user)

    def delete_album(self, album):
        del self.albums[album.hash]

    def songs_rated(self):
        return [song for song in sorted(self.songs().values(), key=lambda x: x.rating, reverse=True)]

    def songs_rated_by(self, rater):
        songs_by_user = list(filter(lambda song: rater in song.raters, self.songs().values()))
        songs_by_user_sorted = sorted(songs_by_user, key=lambda song: song.raters[rater], reverse=True)
        return songs_by_user_sorted
