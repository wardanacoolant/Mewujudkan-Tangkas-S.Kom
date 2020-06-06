import pandas as pd
import spotipy
import os

from spotipy.oauth2 import SpotifyClientCredentials

# Set environment variables
os.environ['SPOTIPY_CLIENT_ID'] = '9a8cb565889548e69d001505e9940d4b'
os.environ['SPOTIPY_CLIENT_SECRET'] = 'c251cd9f1eaf427081525bf4bd774bea'

# Hip Hop
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
playlist = sp.playlist('spotify:playlist:37i9dQZF1DXcA6dRp8rwj6', fields=None, market=None, additional_types=('track', ))
tracks = playlist['tracks']['items']

track_list = []
for i in range(len(tracks)):
    track_list.append(tracks[i]['track']['uri'])
    
features = sp.audio_features(tracks=track_list)
pd.DataFrame(features).to_csv('C:/Users/pradn/AnacondaProjects/Spotify Analysis/data/hiphop.csv')