from pytube import Playlist

class PlaylistSearch:
    def __init__(self,)->None:
        self.p = Playlist('https://www.youtube.com/playlist?list=PLS1QulWo1RIaJECMeUT4LFwJ-ghgoSH6n')
        print(self.p.views, self.p.video_urls[:4], self.p.length)
        
        
if __name__ == "__main__":
    pl = PlaylistSearch()
    