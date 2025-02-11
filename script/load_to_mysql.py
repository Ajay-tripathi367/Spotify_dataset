import pandas as pd
import mysql.connector
from config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE

file_path = "data/cleaned_spotify_albums.csv"
df = pd.read_csv(file_path)

conn = mysql.connector.connect(
    host=MYSQL_HOST,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    database=MYSQL_DATABASE
)
cursor = conn.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS cleaned_spotify_albums (
    track_name VARCHAR(255),
    track_id VARCHAR(100) PRIMARY KEY,
    track_number INT,
    duration_ms INT,
    album_type VARCHAR(50),
    artists TEXT,
    total_tracks INT,
    album_name VARCHAR(255),
    release_date DATE,
    label VARCHAR(255),
    album_popularity INT,
    album_id VARCHAR(100),
    artist_id VARCHAR(100),
    duration_sec FLOAT,
    radio_mix VARCHAR(5)
);
"""
cursor.execute(create_table_query)
conn.commit()

insert_query = """
INSERT INTO cleaned_spotify_albums (
    track_name, track_id, track_number, duration_ms, album_type, artists, total_tracks,
    album_name, release_date, label, album_popularity, album_id, artist_id, duration_sec, radio_mix
) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
ON DUPLICATE KEY UPDATE 
    track_name=VALUES(track_name), track_number=VALUES(track_number),
    duration_ms=VALUES(duration_ms), album_type=VALUES(album_type),
    artists=VALUES(artists), total_tracks=VALUES(total_tracks),
    album_name=VALUES(album_name), release_date=VALUES(release_date),
    label=VALUES(label), album_popularity=VALUES(album_popularity),
    album_id=VALUES(album_id), artist_id=VALUES(artist_id),
    duration_sec=VALUES(duration_sec), radio_mix=VALUES(radio_mix);
"""

for _, row in df.iterrows():
    cursor.execute(insert_query, tuple(row))

conn.commit()
cursor.close()
conn.close()

print(" Data successfully loaded into MySQL")
