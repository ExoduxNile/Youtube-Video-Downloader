import yt_dlp
import ffmpeg

import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])  
def download_video():

  if request.method == 'POST':
    
    url = request.form['url']
    
    # Build ffmpeg command 
    command = ['node', 'ffmpeg.js', 
      '-i', url,
      '-c:v', 'libx264', 
      '-crf', '28',
      'output.mp4'
    ]
    
    # Execute ffmpeg.js script 
    subprocess.run(command)

    return "Video downloaded!"

  return render_template('index.html')