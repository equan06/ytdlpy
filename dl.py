from pytube import YouTube, Playlist
import sys

def download_playlist(url):
        playlist = Playlist(url)
        for video in playlist.videos:
            download_video(video.watch_url)

def download_video(url, caption=False):
    yt = YouTube(url)
    vid_stream = yt.streams.filter(file_extension='mp4').get_highest_resolution()
    vid_name = vid_stream.title
    print(f"downloading video {vid_name} from {url}")
    vid_stream.download()
    print("downloaded video")
    if caption:
        if "en" in yt.captions:
            en_caption = yt.captions["en"]
            srt_text = en_caption.generate_srt_captions()
            with open(f"{vid_name}.srt", "w") as srt_file:
                srt_file.write(srt_text)
            print("downloaded en captions")
        else:
            print("no en captions")

if __name__ == "__main__":
    print(sys.argv)
    type, url = sys.argv[1], sys.argv[2]
    if type == "-p":
        download_playlist(url)
    elif type == "-v":
        download_video(url)
    elif type == "-vc":
        download_video(url, True)


