import json
from core.Database import Database
from core.User import User
from core.Album import Album
from core.Song import Song

class Loader:

    def load(self, path):
        db = Database()
        with open(path) as json_file:
            data = json.load(json_file)

        users = {}
        for user in data["user"]:
            users[user["name"]] = User(user["name"])

        alben = {}

        for album in data["album"]:

            album_title = album["title"]
            album_interpret = album["interpret"]
            album_cover = album["cover"]
            alb = Album(album_title, album_interpret, album_cover)

            for song in album["songs"]:
                song_name = song["name"]
                son = Song(name=song_name, album=alb, raters={}, rating=0)
                for rater in song["raters"]:
                    son.addRating(users[rater["name"]], rater["rating"])
                alb.addSong(son)
            
            alben[alb.hash] = alb

        db.user = users
        db.albums = alben

        return db
            
                