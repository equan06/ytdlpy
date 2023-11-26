from pytube import YouTube
import sys

if len(sys.argv) > 1:
    url = sys.argv[1]
    print(url)
    yt = YouTube(url)
    vid_stream = yt.streams.filter(file_extension='mp4').get_highest_resolution()
    vid_name = vid_stream.title
    print(vid_name)
    vid_stream.download()
    print("downloaded video")
    if "en" in yt.captions:
        en_caption = yt.captions["en"]
        srt_text = en_caption.generate_srt_captions()
        with open(f"{vid_name}.srt", "w") as srt_file:
            srt_file.write(srt_text)
        print("downloaded en captions")
    else:
        print("no en captions")

