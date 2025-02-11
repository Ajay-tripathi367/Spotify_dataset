import pandas as pd

albums_df = pd.read_csv('data/spotify-albums_data_2023.csv')
tracks_df = pd.read_csv('data/spotify_tracks_data_2023.csv')

artist_name_columns = [col for col in albums_df.columns if col.startswith('artist_') and col != 'artist_id']
albums_df['artists'] = albums_df[artist_name_columns].apply(lambda x: ', '.join(x.dropna().astype(str)), axis=1)
albums_df = albums_df.drop(columns=artist_name_columns, errors='ignore')

tracks_df.rename(columns={'id': 'track_id'}, inplace=True)

filtered_tracks = tracks_df[(tracks_df['explicit'] == False) & (tracks_df['track_popularity'] > 50)]
albums_df = albums_df[albums_df['track_id'].isin(filtered_tracks['track_id'])]

albums_df = albums_df.drop_duplicates()

albums_df = albums_df.dropna()

if 'duration_ms' in albums_df.columns:  
    albums_df['radio_mix'] = albums_df['duration_ms'] <= 180000

albums_df.to_csv('data/cleaned_spotify_albums.csv', index=False)

print("Cleaning and transformation complete. Saved as 'data/cleaned_spotify_albums.csv'.")
