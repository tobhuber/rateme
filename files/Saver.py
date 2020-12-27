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
 
        for key in alben:                
            raters = []
            for rater in alben[key].raters:
                raters.append(rater.name)

            songs = []
            for song in alben[key].songs: 

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
                        "album": alben[key].title,
                        "rating": song.rating,
                        "raters": song_raters
                    }
                )
            save["album"].append(
                {
                    "title": alben[key].title,
                    "interpret": alben[key].interpret,
                    "rating": alben[key].rating,
                    "cover": alben[key].cover,
                    "raters": raters,
                    "songs": songs
                }
            )


        with open(path, 'w') as outfile:
            json.dump(save, outfile)