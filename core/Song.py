class Song:

    def __init__(self, name="", album=""):
        self.name = name
        self.album = album
        self.rating = 0
        self.raters = {}


    def updateRating(self):
        result = 0
        for rating in self.raters.values():
            result += rating
        return 0 if len(self.raters) == 0 else result / len(self.raters)


    # check if rater already rated, if so return, else add rater to raters and update the rating
    def addRating(self, rater, rating):
        if rater not in self.raters:
            self.raters[rater] = rating
            self.rating = self.updateRating()
            self.album.addRater(rater)
            self.album.updateRating()