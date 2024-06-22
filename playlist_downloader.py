from pytube import Playlist, YouTube
import os

playlist_link = input("Paste your playlist link here: ")

playlist = Playlist(playlist_link)
print(playlist)

# Create a directory for the playlist
playlist_title = playlist.title  # Get the title of the playlist
playlist_dir = os.path.join('static/videos', playlist_title)
os.makedirs(playlist_dir, exist_ok=True)  # Create directory if it doesn't exist

# Loop through each video in the playlist
for video_url in playlist.video_urls:
    try:
        yt = YouTube(video_url)
        stream = yt.streams.get_highest_resolution()
        video_title = yt.title.replace('|', '-') + ".mp4"
        print(f"Downloading: {video_title}")
        stream.download(output_path=playlist_dir, filename=video_title)
        print(f"{video_title} downloaded successfully")
    except Exception as e:
        print(f"Error downloading {video_url}: {e}")

print("Download complete for the entire playlist.")
