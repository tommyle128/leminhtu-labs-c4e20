from youtube_dl import YoutubeDL

# Download a video:
dl_vid = YoutubeDL()
dl_vid.download(['https://www.youtube.com/watch?v=8sgycukafqQ'])

# Download an audio:
options = {
    'format': 'best audio/audio'
}
dl_audio = YoutubeDL(options)
dl_audio.download(['https://www.youtube.com/watch?v=8sgycukafqQ'])

# Search and download a video:
options2 = {
    'default_search':'ytsearch',
    'max_downloads': 1
}
dl_srch_vid = YoutubeDL(options2)
dl_srch_vid.download(['In the end Linkin Park'])

# Search and download an audio:
options3 = {
    'default_search':'ytsearch',
    'max_downloads': 1,
    'format': 'best audio/audio'
}
dl_srch_vid = YoutubeDL(options3)
dl_srch_vid.download(['In the end Linkin Park'])

