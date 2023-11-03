import yt_dlp
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def download_video():
    if request.method == 'POST':
        url = request.form['url']
        
        options = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'
        }

        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])

        return "Video downloaded!"

    return render_template('form.html')