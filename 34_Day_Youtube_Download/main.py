import yt_dlp

url_to_download = input("Enter the video URL to download Video : ")

yt_lines = {}

with yt_dlp.YoutubeDL(yt_lines) as youtube:
    youtube.download([url_to_download])

print("Your Video Downloads Successfully :")