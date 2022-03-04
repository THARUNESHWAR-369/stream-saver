from flask import Flask, send_file
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from flask import session
from pytube import YouTube

import os
from io import BytesIO

DOWNLOAD_DIR = 'downloads'

# create download directory (if not exists)
if not os.path.exists(DOWNLOAD_DIR):
    os.mkdir(DOWNLOAD_DIR)

# create app instance
app = Flask(__name__)

# secret key
app.config['SECRET_KEY'] = "adksjfksjdfiomewo34j3o4jw3oaj4"

# Initialize download directory
app.config['DOWNLOAD_DIR'] = DOWNLOAD_DIR

# methods
methods = ['POST', "GET"]

# routes
home_route = '/'
download_file_route = '/download_file'

# home page
@app.route(home_route, methods=methods)
def home():
    if request.method == "POST":
        session['link'] = request.form.get("video-url")
        try:
            url = YouTube(session['link'])
            url.check_availability()

            print(session['link'])
        except Exception as e:
            print("[app error]: ",e)
            return render_template("home.html", url=None, error="url not found.")
        return render_template("home.html", url=url, error=None)
    return render_template("home.html", url=None, error= None)

# download file page
@app.route(download_file_route, methods=methods)
def download_file():
    if request.method=="POST":
        buffer = BytesIO()
        url = YouTube(session['link'])
        itag = request.form.get('itag')
            
        video = url.streams.get_by_itag(itag)
        video.stream_to_buffer(buffer)
        buffer.seek(0)
        return send_file(buffer, as_attachment=True, download_name=video.default_filename)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)

