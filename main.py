from pytube import YouTube

link=input("paste ur link here : ")

yt = YouTube(link)
stream = yt.streams.get_highest_resolution()
video_title = yt.title+".mp4"
print(video_title)
video_title = yt.title.replace('|', '-') + ".mp4"
print(video_title)
stream.download('static/videos',filename=video_title)
print("download complete")