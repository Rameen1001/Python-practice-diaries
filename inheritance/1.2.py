class media:
    def __init__(self,title):
        self.title=title
class song(media):
    #super().__init__()
    def __init__(self,title,artist,duration):
        super().__init__(title)
        self.artist=artist
        self.duration=duration
def play_short_songs(songs_list):
     for i in songs_list:
         if (i.duration<180):
            print(i.title)
song1=song("m_song","fatah",45)
obj=song("my_song","fgfg",200)
songs_list=[song1,obj]
play_short_songs(songs_list)
