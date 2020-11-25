import json

class Saver:
    def save(self, users, alben, path):
        save = {}
        
        for user in users:
            save["user"]["name"] = user.name
        
        for album in alben:
            for song in album.songs:
                save["album"]["title"] = album.title
                save["album"]["interpret"] = album.interpret
                save["album"]["rating"] = album.rating
                save["album"]["cover"] = album.cover

                for rater in album.raters:
                    save["album"]["raters"]["name"] = rater.name

                for song in album.songs:
                    save["album"]["songs"]["name"] = song.name
                    save["album"]["songs"]["album"] = album.name
                    save["album"]["songs"]["rating"] = song.rating
                    
                    for rater in song.raters:
                        save["album"]["songs"]["raters"]["name"] = rater.name
                        save["album"]["songs"]["raters"]["rating"] = song.raters[rater]

        with open(path, 'w') as outfile:
            json.dump(save, outfile)