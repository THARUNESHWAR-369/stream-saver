from flask import Flask, request
from flask import render_template, redirect, url_for, send_file, send_from_directory
from source.ytdownload import YT_DOWNLOAD
import os

DOWNLOAD_DIR = 'downloads'

if not os.path.exists(DOWNLOAD_DIR):
    os.mkdir(DOWNLOAD_DIR)


app = Flask(__name__)

yt_download = YT_DOWNLOAD()

@app.route('/', methods=['POST', "GET"])
def home():

    download_type = None
    thumbnail_url = None
    title = None
    video_res = None
    audio_abr = None
    video_url = None   
        
    if request.method == "POST":
        video_url = request.form.to_dict()['video-url']
        print('video_url: ',video_url)
        try:
            video_res, audio_abr, thumbnail_url, title = yt_download.getAudioAndVideoStreams(video_url=video_url)
        
            return render_template('home.html', context={
                "data":
                    {"video_res":video_res, 
                    'audio_abr':audio_abr, 
                    "video_url":video_url,
                    "thumbnail_url":thumbnail_url,
                    "title":title,
                    "error":None
                    }
                    }
                                )        
        except Exception as e:
            
            print("error: [app.py], ",e)
            
            return render_template('home.html', context={
                "data":
                    {"video_res":video_res, 
                    'audio_abr':audio_abr, 
                    "video_url":video_url,
                    "thumbnail_url":thumbnail_url,
                    "title":title,
                    "error":"Provide vaild URL."                        
                    }
                    }
                                )  
            
            
    return render_template('home.html', context={
        "data":
            {"video_res":None,
             "audio_abr":None, 
             "video_url":None,
             "thumbnail_url":None,
             "title":None,
             "error":None
             }
            }
                           )
    

@app.route("/download_file", methods=["GET","POST"])
def download_video():
    
    print('download_video')
    try:
        format = request.form.to_dict()['format']        
        print(format)
        download_type= yt_download.getDownloadType(format=format)
        print(download_type)
        
        fname = yt_download.downloadVideo(download_type, format)   
        print("fname: ",fname)  
    
        return send_file(fname, as_attachment=True)
    except:
        return "Video download failed!"
    

if __name__ == "__main__":
    app.run(debug=True)
    
    
