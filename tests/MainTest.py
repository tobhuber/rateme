import sys
import unittest
from core.User import User
from core.Song import Song
from core.Album import Album

class UserTest(unittest.TestCase):
    
    def test_userInit(self):
        user = User("Nele")
        self.assertEqual("Nele", user.name)

class AlbumTest(unittest.TestCase):

    def test_albumName(self):
        album = Album("JBG3")
        self.assertEqual("JBG3", album.title)

    def test_interpret(self):
        album = Album("JBG3", ["Kollegah", "Farid Bang"])
        self.assertEqual(album.interpret.pop(), "Farid Bang")
        self.assertEqual(album.interpret.pop(), "Kollegah")

    def test_addSong(self):
        album = Album("JBG3", ["Kollegah", "Farid Bang"])
        song = Song("Dynamit", album)
        album.addSong(song)
        self.assertEqual(album.songs.pop(), song)

    def test_oneSongRated(self):
        album = Album("JBG3", ["Kollegah", "Farid Bang"])
        song = Song("Dynamit", album)
        album.addSong(song)
        user = User("Tobi")
        song.addRating(user, 10)
        self.assertEqual(10, album.rating)
    
    def test_song0rated(self):
        album = Album("JBG3", ["Kollegah", "Farid Bang"])
        song = Song("Dynamit", album)
        album.addSong(song)
        user = User("Tobi")
        song.addRating(user, 0)
        self.assertEqual(0, album.rating)

class SongTest(unittest.TestCase):

    def test_songInit(self):
        album = Album("Kollegah", "Kollegah")
        song = Song("Herbst", album)
        self.assertEqual(album, song.album)
    
    def test_songRating(self):
        album = Album("JBG3", ["Kollegah", "Farid Bang"])
        song = Song("Dynamit", album)
        album.addSong(song)
        user = User("Tobi")
        song.addRating(user, 0)
        self.assertEqual(0, song.rating)


    
if __name__ == '__main__':
    unittest.main()
