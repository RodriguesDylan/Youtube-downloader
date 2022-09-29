from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=mC5s9KcaHHY')

print(yt.streams.filter(file_extension='mp4'))

stream = yt.streams.get_audio_only()
stream.download()
