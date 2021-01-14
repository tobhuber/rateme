class Song:

    def __init__(self, name = "", album = None, raters = {}, rating = -1):
        self.name = name
        self.album = album
        self.rating = rating
        self.raters = raters
        self.hash = f"{self.name}#{self.album.interpret[0]}"
        self.updateRating()

    def __str__(self):
        return f"""
            Song object with:
            name: {self.name}
            album: {self.album.title}
            rating: {self.rating}
            raters: {self.raters}
            hash: {self.hash}

        """


    def updateRating(self):
        result = 0
        for rating in self.raters.values():
            result += rating
        
        self.rating = -1 if len(self.raters) == 0 else round(result / len(self.raters), 2)

    def addRating(self, rater, rating):
        if rater not in self.raters:
            self.raters[rater] = rating
            self.updateRating()
            self.album.addRater(rater)
            self.album.updateRating()
        else:
            self.raters[rater] = rating
            self.updateRating()
            self.album.updateRating()

    def removeRater(self, rater):
        if rater in self.raters:
            del self.raters[rater]
            self.updateRating()
            self.album.updateRating()
            self.album.updateRaters()        
