import yt_dlp
import os

def download_channel_videos(channel_url, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    ydl_opts = {
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
        'format': 'bestvideo+bestaudio/best',
        'noplaylist': False,
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([channel_url])
    
if __name__ == '__main__':
    channel_url = 'https://www.youtube.com/channel/'  # USAR O ID DEPOIS DE CHANNEL
    output_folder = 'downloaded_videos'
    download_channel_videos(channel_url, output_folder)
