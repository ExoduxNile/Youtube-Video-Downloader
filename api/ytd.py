import yt_dlp

url = 'https://www.youtube.com/shorts/AsQK3BDqYII'

try:
    options = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([url])