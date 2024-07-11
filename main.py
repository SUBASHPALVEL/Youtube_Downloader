import os
from yt_dlp import YoutubeDL

def convert_file_to_list(filename):
    with open(filename, 'r') as file:
        content = file.read()

    urls = content.split()

    return urls

def download_youtube_short(url, output_path="downloads"):
    try:
        ydl_opts = {
            'format': 'best',
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        }

        # Create output directory if it doesn't exist
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        with YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading: {url}")
            ydl.download([url])
            print(f"Download complete: {url}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Usage
filename = "Note.txt"
video_list = convert_file_to_list(filename)

output_path = "Downloads"
for video in video_list:
    download_youtube_short(video, output_path)
    print("--------------------------------------------------------")
