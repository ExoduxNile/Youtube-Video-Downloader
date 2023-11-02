import yt_dlp

def download_video(url):
    options = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best' 
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([url])