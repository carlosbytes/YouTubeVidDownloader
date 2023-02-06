from pytube import YouTube
from sys import argv

link = argv[1]

yt = YouTube(link)

print("Title: ", yt.title)
print("Views: ", yt.views)
print("*********************")

youtube_res = yt.streams.get_highest_resolution()
save_path = "/Users/carlos/Movies/YouTubeDownloads"
print("Downloading video standby...")
try:
    youtube_res.download(save_path)
except Exception as e:
    print("Not able to download")
    print(e)
else: 
    print("Video downloaded and saved to {}".format(save_path))
