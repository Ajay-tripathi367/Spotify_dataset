Spotify Data Processing Pipeline

This project processes and analyzes Spotify Albums Data, cleans it, and loads it into MySQL for further analysis.

Project Structure

├── data/                   
│   ├── spotify_albums_data_2023.csv       # Raw Spotify albums dataset  
│   ├── spotify_tracks_data_2023.csv       # Raw Spotify tracks dataset  
│   ├── cleaned_spotify_albums.csv         # Cleaned and transformed dataset  
├── script/                 
│   ├── clean_albums.py     # Cleans and transforms the Spotify albums dataset  
│   ├── load_to_mysql.py    # Loads the cleaned data into MySQL  
│   ├── queries.py          # SQL queries for analysis  
│   ├── test.py             # Unit tests for data validation  
├── .env                    # Environment variables (MySQL credentials)  
├── requirements.txt        # Python dependencies  
├── README.md               # Project documentation  

Setup Instructions:
1. Install Dependencies
pip install -r requirements.txt

2.Set Up Environment Variables
Create a .env file and add your MySQL credentials:
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=yourpassword
MYSQL_DATABASE=spotify_db

3.Run Data Cleaning
python script/clean_albums.py

4. Load Data into MySQL
python script/load_to_mysql.py

5.Run Queries
python script/queries.py

Results & Analysis
Top 20 labels by total number of tracks
Top 25 popular tracks released between 2020-2023