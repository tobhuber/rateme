import sys

# class representing an music album
class Album:
    

    def __init__(self, title="", interpret=[], cover=None):
        self.title = title
        self.interpret = interpret
        self.rating = 0
        self.songs = []
        self.raters = set()
        self.cover = cover


    # calculate median of song ratings
    def calculateRating(self):
        result = 0
        for song in self.songs: 
            result += song.rating
        return 0 if len(self.songs) == 0 else result / len(self.songs)


    def updateRating(self):
        self.rating = self.calculateRating()


    def addSong(self, song):
        self.songs.append(song)
        self.updateRating()


    def addInterpret(self, interpret):
        self.interpret.append(interpret)
    

    def addRater(self, rater):
        self.raters.add(rater)
