class SongMachine(object):

    artist = "Bowie"

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = ["Happy birthday to you",
              "happy birthday to you",
              "happy birhtday to you!"]

bot = SongMachine(lyrics=happy_bday)
bot.sing_me_a_song()
