import mysql.connector
from config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE

conn = mysql.connector.connect(
    host=MYSQL_HOST,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    database=MYSQL_DATABASE
)
cursor = conn.cursor()

query_1 = """
SELECT label, COUNT(track_id) AS total_tracks
FROM cleaned_spotify_albums
GROUP BY label
ORDER BY total_tracks DESC
LIMIT 20;
"""

query_2 = """
SELECT track_name, album_name, album_popularity , release_date
FROM cleaned_spotify_albums
WHERE release_date BETWEEN '2020-01-01' AND '2023-12-31'
ORDER BY album_popularity  DESC
LIMIT 25;
"""

print("\n Top 20 Labels by Total Tracks:")
cursor.execute(query_1)
for row in cursor.fetchall():
    print(row)

print("\n Top 25 Popular Tracks (2020-2023):")
cursor.execute(query_2)
for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()
