class Database:
    def __init__(self, user={}, albums={}, user_view=None, album_view=None):
        self.user = user
        self.albums = albums
        self.user_view = user_view
        self.album_view = album_view

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