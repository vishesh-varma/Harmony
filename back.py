import spotdl
from spotdl.search.utils import get_album_tracks,get_playlist_tracks
from spotdl.__main__ import spotifyClient
from spotdl.download.downloader import DownloadManager
import spotdl.search.utils as ut
from spotdl.search.songObj import SongObj
import os
import json

defaultTrack="https://open.spotify.com/track/"
defaultAlbum="https://open.spotify.com/album/"
defaultPlaylist="https://open.spotify.com/playlist/"

def initialize():
    clientID="6b6ace45bd094b1fa438151f35fa3fb0"
    clientSecret="963f4330759a403ea6cafc2ff03dc036"
    spotifyClient.initialize(clientID,clientSecret)
    
def readdata():
    with open('data.json') as f:
        data=json.load(f)
    return data

def download(link : str):
    localdata=readdata()
    currdir=os.getcwd()
    os.chdir(localdata["Directory"])
    falselink=0

    if defaultTrack in link:
        MySong=SongObj.from_url(link)
        download=DownloadManager()
        download.download_single_song(MySong)
        
    elif defaultAlbum in link:
        SongList=ut.get_album_tracks(link)
        download=DownloadManager()
        download.download_multiple_songs(SongList)
        
    elif defaultPlaylist in link:
        SongList=ut.get_playlist_tracks(link)
        download=DownloadManager()
        download.download_multiple_songs(SongList)
        
    elif " " in link:
        MySong=ut.search_for_song(link)
        download=DownloadManager()
        download.download_single_song(MySong)
    else:
        falselink=1
    
    os.chdir(currdir)

    if falselink == 0:
        return True
    else:
        return False

    
