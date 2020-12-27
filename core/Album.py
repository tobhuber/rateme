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
        self.hash = f"{self.title}#{self.interpret[0]}"


    # calculate median of song ratings
    def calculateRating(self):
        result = 0
        for song in self.songs: 
            result += song.rating
        
        return 0 if len(self.songs) == 0 else result / len(self.songs)


    def updateRating(self):
        self.rating = round(self.calculateRating(), 1)


    def addSong(self, song):
        self.songs.append(song)
        self.updateRating()
        self.updateRaters()


    def addInterpret(self, interpret):
        self.interpret.append(interpret)
    

    def updateRaters(self):
        self.raters = set()
        for song in self.songs:
            self.raters.update(set(song.raters.keys()))

    def addRater(self, rater):
        self.raters.add(rater)
        