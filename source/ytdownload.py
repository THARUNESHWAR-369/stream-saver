from pytube import YouTube

class YT_DOWNLOAD:
       
    def getAudioAndVideoStreams(self, video_url):
        
        video, video_res = [], []
        audio, audio_abr = [], []
              
        #print('[ytdownload.py] video_url: ',video_url)
        
        yt = YouTube(video_url)
       
        #print('yt, ',yt)
        
        self.video = yt.streams.filter(type='video', progressive=True).order_by('resolution')
        self.video_res = [stream.resolution for stream in self.video]
        
        self.audio = yt.streams.filter(type='audio').order_by('abr')
        self.audio_abr = [stream.abr for stream in self.audio]
        
        return self.video_res, self.audio_abr, yt.thumbnail_url, yt.title

    def getDownloadType(self, format):
        return 'audio' if format.endswith('kbps') else 'video'
    
    def downloadVideo(self, download_type, format):
        
        #print(download_type)
        filename = None        
    
        if download_type == 'video':
            download_path = self.video[self.video_res.index(format)].download(output_path="downloads")
            #print(download_path)
            filename = download_path#.split('//')[-1]
            #print(filename)
        if download_type == 'audio':
            download_path = self.audio[self.audio_abr.index(format)].download("downloads")
            filename = download_path.split('//')[-1]
        
        #print("Filename: ",filename)
        return filename
    
