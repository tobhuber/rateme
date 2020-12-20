import json

class Saver:
    def save(self, db, path):
        save = {}
        users = db.user
        alben = db.albums
        save["user"] = []
        save["album"] = []
        for name in users:
            save["user"].append({"name": users[name].name})
 
        for album in alben:
            for song in album.songs:
                
                raters = []
                for rater in album.raters:
                    raters.append(rater.name)

                songs = []
                for song in album.songs: 

                    song_raters = []
                    for rater in song.raters:
                        song_raters.append(
                            {
                                "name": rater.name,
                                "rating": song.raters[rater]
                            }
                        )
                    songs.append(
                        {
                            "name": song.name,
                            "album": album.name,
                            "rating": song.rating,
                            "raters": song_raters
                        }
                    )
                save["album"].append(
                    {
                        "title": album.title,
                        "interpret": album.interpret,
                        "rating": album.rating,
                        "cover": album.cover,
                        "raters": raters,
                        "songs": songs
                    }
                )


        with open(path, 'w') as outfile:
            json.dump(save, outfile)