import requests
import re

class YT_DOWNLOADER:

    __isValidRequ = False
    
    def __init__(self, video_url) -> None:
        self.__REQUEST_URL : str = "https://save-from.net/api/convert"
        self.video_url = str(video_url)
        
        self.__isValidRequ = True if 'status' not in self.__sendRequest() else False

    def __sendRequest(self) -> dict:
        
        if self.__isValidURL():
            r = requests.post(self.__REQUEST_URL, params={"url":self.video_url})
            return r.json() if r.status_code == 200 else {"status":False}
        return {
            "status":False
        }

    def __check_valid_url(self) -> bool:
        return self.__isValidRequ 

    def __get_video_title(self, r):
        return r['meta']['title']

    def __get_video_duration(self, r):
        return r['meta']['duration']
        
    def __get_video_audio_data(self, r) -> list:
        video_download_data = []
        audio_download_data = []

        for url in r['url']:
            print(url)
            getData = [
                        url['url'],
                        url['name'],
                        url['subname'],
                        url['ext'],
                        "Undefined" if 'filesize' not in url else url['filesize'],
                        None if (url['attr'] == [] or url['attr']['class'] == "" )else None if url['attr'] == [] else url['attr']['class']
                        
                    ]
            if 'audio' not in url:
                continue
            if url['audio']:
                audio_download_data.append(getData+['audio'])
            else:
                video_download_data.append(getData+['video'])

        return [video_download_data, audio_download_data]
    

    def download(self) -> dict:

        if self.__check_valid_url():
            req = self.__sendRequest()

            video_download_data, audio_download_data = self.__get_video_audio_data(req)

            video_meta_data = {
                "thumb" :req['thumb'],
                "title" : self.__get_video_title(req),
                "duration" : self.__get_video_duration(req),
                "source": self.video_url,
            }
            

            return {
                "status" : True,
                "meta" : video_meta_data,
                "video_download_data" : video_download_data,
                "audio_download_data" : audio_download_data
            }
            
        return {
            "status":False,
            "error":"Invalid URL"
        }
    
    def __isValidURL(self):
 
        regex = ("((http|https)://)(www.)?" +
                "[a-zA-Z0-9@:%._\\+~#?&//=]" +
                "{2,256}\\.[a-z]" +
                "{2,6}\\b([-a-zA-Z0-9@:%" +
                "._\\+~#?&//=]*)") # GreeksForGreeks
        
        p = re.compile(regex)
    
        if (self.video_url == None):
            return False

        if(re.search(p, self.video_url)):
            return True
        else:
            return False
        













