import json
from core.User import User
from core.Album import Album
from core.Song import Song

class Loader:

    def load(self, path):
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
                song_album_name = song["album"]
                son = Song(song_name, alb)

                for rater in song["raters"]:
                    son.addRating(users[rater["name"]], rater["rating"])

                alb.addSong(son)
            
            alben[album_title + album_interpret] = alb
                