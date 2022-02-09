import glob
import json
import logging

from Logger import Logger
from Music.Album import Album
from Music.Artitst import Artist
from Music.Song import Song
from Music.Data import Data


class SongLoader:
    def __init__(self, data: Data):
        self.data = data

    def load_songs_in_directory(self, path):
        files_path = glob.glob(f"{path}/*.json")
        for file_path in files_path:
            self.load_song(file_path)
        logging.info(f"loaded songs in directory in {path} to data successfully.")

    def load_song(self, path):
        file = open(path, 'r')
        song_dic = json.loads(file.read())
        track = song_dic['track']
        song = Song(track['id'], track['name'], track['popularity'])
        self.data.songs[track['id']] = song
        self.load_album(track, song)
        Logger.logger.info(f"loaded song {track['id']} to data successfully.")

    def load_album(self, track, song):
        album_dict = track['album']
        if album_dict['id'] not in self.data.albums.keys():
            album = Album(album_dict['id'], album_dict['name'], {song.unique_id: song})
            self.data.albums[album_dict['id']] = album
            self.load_artists(track,album)
        else:
            self.data.albums[album_dict['id']].songs[song.unique_id] = song
            self.load_artists(track,self.data.albums[album_dict['id']])

    def load_artists(self, track, album):
        artists = track['artists']
        for artist in artists:
            if artist['id'] not in self.data.artists.keys():
                self.data.artists[artist['id']] = Artist(artist['id'], artist['name'], {album.unique_id: album})
            else:
                self.data.artists[artist['id']].albums[album.unique_id] = album
