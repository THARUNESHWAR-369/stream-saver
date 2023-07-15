from flask import Flask, request
from flask import render_template

from utils.ytVideoDownloader import YouTubeVideoDownloader
from utils.downloadBySearch import DownloadBySearch

from pytube.exceptions import RegexMatchError

# create app instance
app = Flask(__name__)

# secret key
app.config['SECRET_KEY'] = "<your secret key>"

# methods
methods = ['POST', "GET"]

# routes
home_route = '/'

@app.route(home_route, methods=["GET"])
def home():
    return render_template('v3.html', error=None, data=None)

@app.route("/getBasicDetails", methods=["POST"])
def getBasicDetails():

    video_url = request.get_json()['video-url']
    #print(video_url)
    try:
        yt = YouTubeVideoDownloader(video_url).getBasicDetails()
        print("basic data: ",yt)
        return yt
    except RegexMatchError:
        return {"status":False}

@app.route("/getStreamsData", methods=["POST"])
def getStreamsData():

    video_url = request.get_json()['video-url']
    #print(video_url)
    yt = YouTubeVideoDownloader(video_url).getStreamsData()
    print("stream data: ",yt)
    return yt

@app.route('/downloadByItag', methods=["POST"])
def downloadByItag():
    itag = request.get_json()['itag']
    video_url = request.get_json()['video-url']
    stream = YouTubeVideoDownloader(video_url).downloadByItag(itag)
    return {"url":stream.url}

@app.route('/searchVideo', methods=['POST'])
def searchVideo():
    video_name = request.get_json()["search-video-name"]
    
    try :
        return {
            "status":True,
            "search_data" : DownloadBySearch(video_name).search()
        }
    except :
        return {
            "status" : False
        }

if __name__ == "__main__":
    app.run(debug=True, port = "5000")

