from pytube import Playlist
from pytube import YouTube

playlist_link = input("Paste your playlist link here: ")

playlist = Playlist(playlist_link)
print(playlist)

# Loop through each video in the playlist
for video_url in playlist.video_urls:
    try:
        yt = YouTube(video_url)
        stream = yt.streams.get_highest_resolution()
        video_title = yt.title.replace('|', '-') + ".mp4"
        print(f"Downloading: {video_title}")
        stream.download('static/videos', filename=video_title)
        print(f"{video_title} downloaded successfully")
    except Exception as e:
        print(f"Error downloading {video_url}: {e}")

print("Download complete for the entire playlist.")
