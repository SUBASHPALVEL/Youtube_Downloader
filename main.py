import yt_dlp
import os


def download_youtube_video(url, output_path="Downloads"):
    ydl_opts = {
        'format': 'best[height<=1080][ext=mp4]',
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'no_warnings': True,
        'ignoreerrors': True,
    }

    try:

        # Create output directory if it doesn't exist
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            if info is None:
                print("Error: Unable to extract video information.")
                return

            video_title = info['title']
            print(f"Downloading: {video_title}")

            ydl.download([url])

        print("Download complete!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def convert_file_to_list(filename):
    with open(filename, 'r') as file:
        content = file.read()

    urls = content.split()

    return urls


# Usage
filename = "Note.txt"
video_list = convert_file_to_list(filename)

output_path = "Downloads"
for video in video_list:
    download_youtube_video(video, output_path)
    print("--------------------------------------------------------")
