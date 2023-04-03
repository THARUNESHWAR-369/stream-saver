import requests
import re

class YT_DOWNLOADER:

    __isValidRequ = False
    
    def __init__(self, video_url) -> None:
        self.__REQUEST_URL = "https://save-from.net/api/convert"
        self.video_url = str(video_url)

        print("self.video_url: ",self.video_url)
        
        self.__isValidRequ = True if 'status' not in self.__sendRequest() else False

    def __sendRequest(self) -> dict:
        
        if self.__isValidURL():
            r = requests.post(self.__REQUEST_URL, params={"url":self.video_url})
            return r.json() if r.status_code == 200 else {
                                                    "status":False
                                                }
        return {
            "status":False
        }

    def check_valid_url(self) -> bool:
        return self.__isValidRequ 

    def __getVideoMetaData(self, req) -> dict:
        meta = req['meta']
        thumb = req['thumb']
        timestamp = req['timestamp']

        updateData = {
            "meta":meta,
            "thumb":thumb,
            "timestamp":timestamp
        }

        return updateData

    def download(self) -> dict:

        if self.check_valid_url():
            req = self.__sendRequest()

            videoMetaData = self.__getVideoMetaData(req)
            video_download_urls = self.__getVideoDownloadUrls(req)
            

            return {
                "status":True,
                "video_meta_data":videoMetaData,
                "video_downloads":video_download_urls
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
        

    def __getVideoDownloadUrls(self, req) -> dict:
        urls = {}
        urls_list = req['url']
        dictData = {
            "without_audio":[],
            "with_audio":[]            
        }
        for url in urls_list:
            if url['ext'] == 'mp4':
                if 'audio' in url:
                    if url['audio'] == False:
                        dictData['without_audio'].append([
                            url['subname'],url['url']
                        ])
                else:
                    dictData['with_audio'].append([
                            url['subname'],url['url']
                        ])
            
            urls.update(
                {
                    "video_data":dictData,
                    "audio_data":None
                }
            )

        return urls

"""

def check_valid_url(url):
    __r = requests.post(REQUEST_URL, params={"url":url}).json()
    if 'meta' not in __r:
        return False
    return True

def get_watch_value(url):
    return url.split('v=')[-1]

def get_thumbnail_url(v):
    return f"https://i.ytimg.com/vi/{v}/hqdefault.jpg"

def get_video_title(r):
    return r['meta']['title']

def get_video_duration(r):
    return r['meta']['duration']

def get_video_quality(r):
    return r['video_quality']

def get_url(r, id):
    try:
        return r['url'][id]['info_url']
    except:
        return r['url'][id]['url']

def get_name(r, id):
    return r['url'][id]['name']

def get_video_quality_(r, id):
    return r['url'][id]['quality']

def get_filesize(r, id):
    try:
        return r['url'][id]['filesize']
    except:
        return 'UNDEFINED'

def get_attrs(r, id):
    if r['url'][id]['attr'] == []:
        return None
    else:
        if r['url'][id]['attr']['class'] == "":
            return None
        return r['url'][id]['attr']['class']


def audio_data(r):
    audio_download_data = []
    video_quality = get_video_quality(r)
    audio_r_len = len(r['url'][len(video_quality):])

    for vq_id in range(audio_r_len):
        audio_download_data.append(
            [
                get_url(r, vq_id),
                get_name(r, vq_id),
                get_video_quality_(r, vq_id),
                get_filesize(r, vq_id),
                get_attrs(r, vq_id)
            ]
        )

    return audio_download_data


def video_data(r):
    video_download_data = []
    video_quality = get_video_quality(r)

    for vq_id in range(len(video_quality)):

        video_download_data.append(
            [
                get_url(r, vq_id),
                get_name(r, vq_id),
                get_video_quality_(r, vq_id),
                get_filesize(r, vq_id),
                get_attrs(r, vq_id)
            ]
        )

    return video_download_data

def url_details(url):
    v = get_watch_value(url=url)

    PARAMS = {
        "url":url
    }

    __r = requests.post(REQUEST_URL, params=PARAMS)

    if __r.status_code == 200:

        r = __r.json()

        return {
            "status" : True,
            "v" : v,
            "thumbnail_url" : get_thumbnail_url(v=v),
            "title" : get_video_title(r),
            "duration" : get_video_duration(r),
            "url": url,
            "video_data" : video_data(r),
            "audio_data" : audio_data(r)
        }

    return {
        "status" : False
    }


"""