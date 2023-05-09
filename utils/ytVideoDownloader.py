from pytube import YouTube
from pytube.exceptions import AgeRestrictedError

from .utils import formatDuration, AgeRestrictedVideoException

class YouTubeVideoDownloader:
    
    def __init__(self, url : str) -> None:
        self.__yt = YouTube(url)
    
    def __getThumbnail_url(self) -> str:
        try:
            return {
                "status":True,
                "thumbnail_url" : self.__yt.thumbnail_url
            }
        except:
            return {
                "status":False
            }
    
    def __getDuration(self) -> str:
        return formatDuration(self.__yt.length)
    
    def __getTitle(self) -> str:
        try:
            return {
                "status":True,
                "title" : self.__yt.title
            }
        except:
            return {
                "status":False
            }
    
    def __getAudioStreams(self) -> list:
                
        try:
            return {
                "status":True,
                "audio_streams" : self.__yt.streams.filter(only_audio=True)
            }
        except AgeRestrictedError:
            raise AgeRestrictedVideoException(msg="This video is age-restricted and cannot be download")

    def __getVideoStreams(self) -> list:
        try:
            return {
                "status":True,
                "video_streams_with_audio" : self.__yt.streams.filter(progressive=True, type="video", file_extension="mp4"), 
                "video_streams_without_audio" : self.__yt.streams.filter(progressive=False, type="video", file_extension="mp4")
            }
        except AgeRestrictedError:
            raise AgeRestrictedVideoException(msg="This video is age-restricted and cannot be download")

        
    def __getStreamsData(self) -> list:
        itags = []
        videoStreamItags = []
        audioStreamItags = []
        
        try:
            audioStreamItags = [
                {
                    "itag" : i.itag,
                    "abr" : i.abr,
                    "mime_type" : i.mime_type.split("/")[-1]
                }
                for i in self.__getAudioStreams()["audio_streams"]
                ]
            
            if self.__getVideoStreams()['status']:
                
                for i in self.__getVideoStreams()['video_streams_with_audio']:
                    
                    if i.itag not in itags:
                        itags.append(i.itag)
                        videoStreamItags.append(
                            {
                                "itag" : i.itag,
                                "res" : i.resolution,
                                "mime_type" : i.mime_type.split("/")[-1],
                                "as_audio" :True
                            }
                        )
                        
                for i in self.__getVideoStreams()['video_streams_without_audio']:
                    
                    if i.itag not in itags:
                        itags.append(i.itag)
                        videoStreamItags.append(
                            {
                                "itag" : i.itag,
                                "res" : i.resolution,
                                "mime_type" : i.mime_type.split("/")[-1],
                                "as_audio" :False
                            }
                        )
        except AgeRestrictedVideoException as e:
            return {
                "status" : False,
                "error" : e.msg
            }
            
        else:
            return {
                "status" : True,
                "audio_itag" : None if audioStreamItags == [] else audioStreamItags, 
                "video_itag" : None if videoStreamItags == [] else videoStreamItags,
            }
    
    def getBasicDetails(self) -> dict:
        try :
            return {
                "status":True,
                "title" : self.__getTitle(),
                "thumbnail_url" : self.__getThumbnail_url(),
                "duration" : self.__getDuration()
            }
        except:
            return {
                'status':False
            }

    def getStreamsData(self) -> dict:
        __sd= self.__getStreamsData()
        print("__SD: ",__sd)
        if __sd['status']:
            
            try :
                return __sd
            except Exception as e:
                print(e)
        
        return __sd
        
    def downloadByItag(self, itag: int) -> None:
        return self.__yt.streams.get_by_itag(itag)

