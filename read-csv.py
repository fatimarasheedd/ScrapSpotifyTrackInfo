import pandas as pd
import main

df = pd.read_csv('trackanalysis.csv')

for index, row in df.iterrows():
    track_name = row['Track']
    artist = row['Artist']
    track_id = row['ID']
    valence = row['Valence']
    energy = row['Energy']

    if track_name and artist and pd.isna(track_id) and pd.isna(valence) and pd.isna(energy):
        print(f"Missing values for track: {track_name} by {artist}, adding values ...")

        token = main.get_token()
        song_id = main.get_song_id(token, track_name, artist)

        if song_id:
            print(f"Song id: {song_id}")
            energy, valence = main.get_song_features(token, song_id)
            print(f"Energy: {energy}, Valence: {valence}")
            df.at[index, 'ID'] = song_id
            df.at[index, 'Valence'] = valence
            df.at[index, 'Energy'] = energy
            main.get_album_cover(token, song_id, track_name, artist)
            df.to_csv('trackanalysis.csv', index=False)


        else: 
            print(f"No song id found for {track_name} by {artist}")
            df = df.drop(index)
            df.to_csv('trackanalysis.csv', index=False)

