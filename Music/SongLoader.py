import glob
import json
import logging

from Loggs.Logger import Logger
from Music.Album import Album
from Music.Artitst import Artist
from Music.Song import Song
from Music.Data import Data


class SongLoader:
    def __init__(self, data: Data):
        self.data = data

    def load_songs_in_directory(self, path):
        # CR: from glob import glob
        # CR: config json.. also why is this coupled to json.
        files_path = glob.glob(f"{path}/*.json")
        for file_path in files_path:
            self.load_song(file_path)
        logging.info(f"loaded songs in directory in {path} to data successfully.")

    def load_song(self, path):
        # CR: with open
        file = open(path, 'r')
        # CR: coupled to json
        song_dic = json.loads(file.read())
        # CR: config text
        track = song_dic['track']
        # CR: config text
        song = Song(track['id'], track['name'], track['popularity'])
        # CR: config text
        self.data.songs[track['id']] = song
        # CR: track and song sounds the same...
        self.load_album(track, song)
        Logger.logger.info(f"loaded song {track['id']} to data successfully.")
        # CR: close????

    # CR: load_song_to_album
    # CR: personally would check if album exist if so make a method to add to album and
    #  otherwise make a method to create and add to album
    def load_album(self, track, song):
        # CR: bad naming. album_id?
        album_dict = track['album']
        if album_dict['id'] not in self.data.albums.keys():
            # CR: why not make a create_album method and then use load_song method?
            album = Album(album_dict['id'], album_dict['name'], {song.unique_id: song})
            self.data.albums[album_dict['id']] = album
            # CR: spacing
            self.load_artists(track,album)
        else:
            self.data.albums[album_dict['id']].songs[song.unique_id] = song
            # CR: spacing
            self.load_artists(track,self.data.albums[album_dict['id']])

    def load_artists(self, track, album):
        # CR: config
        artists = track['artists']
        for artist in artists:
            # CR: config
            if artist['id'] not in self.data.artists.keys():
                # CR: accessing ['id'] multiple times... put it in a var
                self.data.artists[artist['id']] = Artist(artist['id'], artist['name'], {album.unique_id: album})
            else:
                self.data.artists[artist['id']].albums[album.unique_id] = album
