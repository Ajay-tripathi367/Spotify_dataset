import unittest
import pandas as pd
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")

class TestSpotifyData(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.conn = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DATABASE
        )
        cls.cursor = cls.conn.cursor()

    @classmethod
    def tearDownClass(cls):
        cls.cursor.close()
        cls.conn.close()

    def test_csv_integrity(self):
        df = pd.read_csv("data/cleaned_spotify_albums.csv")

        self.assertFalse(df.isnull().values.any(), "CSV contains null values")
        self.assertEqual(set(df["radio_mix"].astype(str).str.upper().unique()), {"TRUE", "FALSE"}, "Invalid values in 'radio_mix' column")


    def test_mysql_table_exists(self):
        self.cursor.execute("SHOW TABLES LIKE 'cleaned_spotify_albums';")
        result = self.cursor.fetchone()
        self.assertIsNotNone(result, "Table 'cleaned_spotify_albums' does not exist")

    def test_top_labels_query(self):
        self.cursor.execute("""
            SELECT label, COUNT(*) AS total_tracks
            FROM cleaned_spotify_albums
            GROUP BY label
            ORDER BY total_tracks DESC
            LIMIT 20;
        """)
        result = self.cursor.fetchall()
        self.assertGreater(len(result), 0, "Query returned no results")

    def test_popular_tracks_query(self):
        self.cursor.execute("""
            SELECT track_name, album_popularity, release_date
            FROM cleaned_spotify_albums
            WHERE release_date BETWEEN '2020-01-01' AND '2023-12-31'
            ORDER BY album_popularity DESC
            LIMIT 25;
        """)
        result = self.cursor.fetchall()
        self.assertTrue(len(result) > 0, "Query returned no results")

if __name__ == "__main__":
    unittest.main()
