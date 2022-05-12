from flask import Flask, send_file
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from flask import session

from pytube import YouTube

import os
from io import BytesIO

from app_utils import check_valid_url
from app_utils import url_details

# create app instance
app = Flask(__name__)

# secret key
app.config['SECRET_KEY'] = "adksjfksjdfiomewo34j3o4jw3oaj4"

# methods
methods = ['POST', "GET"]

# routes
home_route = '/'
download_file_route = '/download_file'


@app.route("/", methods=methods)
def home():
    if request.method == "POST":
        session['video_url'] = request.form['video-url']

        is_valid_url = check_valid_url(session['video_url'] )

        if is_valid_url == True :
            url_data = url_details(url=session['video_url'])
            if  url_data['status'] == True:
                return render_template('index.html', error=None, data=url_data)
        return render_template('index.html', error="Url not Found :)", data=None)


    return render_template('index.html', error=None, data=None)


if __name__ == "__main__":
    app.run(debug=True)

