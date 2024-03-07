from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    video = youtubeObject.title + '.mp4'
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download(output_path='C:/Users/albin/Videos/youtube_videos_downloaded',filename=video + '.mp4')
    except:
        print("An error has occurred")
    print("Download is completed successfully")


link = input("Enter the YouTube video URL: ")
Download(link)

