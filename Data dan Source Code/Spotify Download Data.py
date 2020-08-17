# Import libraries
import pandas as pd
import spotipy
import os
from spotipy.oauth2 import SpotifyClientCredentials

# Set Web API
os.environ['SPOTIPY_CLIENT_ID'] = '9a8cb565889548e69d001505e9940d4b'
os.environ['SPOTIPY_CLIENT_SECRET'] = 'c251cd9f1eaf427081525bf4bd774bea'

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials()) # Set sp = Spotipy
playlist = sp.playlist('spotify:playlist:127UPsxR6RkSAZGRK9wRBT', fields=None, market=None, additional_types=('track', )) # URL Spotify Playlist Genre Blues
tracks = playlist['tracks']['items'] # Set Track = Playlist

track_list = []
for i in range(len(tracks)):
    track_list.append(tracks[i]['track']['uri'])
    
features = sp.audio_features(tracks=track_list) # Set Features = sp.audio_features(Panjang track = track_list)
pd.DataFrame(features).to_csv('D:\Codingan\Visual Studio Code\Spotify\Spotify Analysis 1\Tahap Awal\Data Web API Spotify\Blues.csv') # Save to spreadsheet format .csv