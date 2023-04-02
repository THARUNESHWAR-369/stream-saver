from flask import Flask, request
from flask import render_template
from flask import url_for
from flask import jsonify

from pytube import YouTube

import os
from io import BytesIO

from app_utils import YT_DOWNLOADER

# create app instance
app = Flask(__name__)

# secret key
app.config['SECRET_KEY'] = "<your secret key>"

# methods
methods = ['POST', "GET"]

# routes
home_route = '/'

@app.route(home_route, methods=methods)
def home():
    if request.method == "POST":
        video_url = request.form['video_url']
        print(video_url)

        metaData = YT_DOWNLOADER(video_url).download() 
        
        print("metaData: ",metaData)
        if metaData['status']:
            return jsonify(metaData)
        else:
            return jsonify(metaData)

    return render_template('v2.html', error=None, data=None)


if __name__ == "__main__":
    app.run(debug=True, port = "5500")

