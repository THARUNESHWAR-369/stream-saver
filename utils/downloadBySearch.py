
from pytube import Search

from .ytVideoDownloader import YouTubeVideoDownloader
from .utils import formatDuration

class DownloadBySearch:
    
    def __init__(self, search_name) -> None:
        self.__search_name = search_name
        
    def search(self) -> list:
        searchData = []
        s = Search(self.__search_name)
        #print(s.results, len(s.results))
        for idx, res in enumerate(s.results[:10]):
            searchData.append({
                "id":idx,
                "title":res.title, 
                "thumbnail_url":res.thumbnail_url, 
                "video_url":res.watch_url, 
                "video-duration": formatDuration(res.length)
                })
        #print(s.completion_suggestions)
        return searchData

