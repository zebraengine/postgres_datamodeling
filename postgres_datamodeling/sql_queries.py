# DROP TABLES

songplay_table_drop = "DROP table IF EXISTS songplay"
user_table_drop = "DROP table IF EXISTS user_table"
song_table_drop = "DROP table IF EXISTS songs"
artist_table_drop = "DROP table IF EXISTS artist"
time_table_drop = "DROP table IF EXISTS time"

# CREATE TABLES
songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplay (songplay_id BIGSERIAL PRIMARY KEY, start_time numeric, user_id varchar, level varchar, song_id varchar, artist_id varchar, session_id varchar, location varchar, user_agent varchar);""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS user_table (user_id varchar PRIMARY KEY, first_name varchar, last_name varchar, gender varchar, level varchar);""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs (song_id varchar PRIMARY KEY, title varchar, artist_id varchar, year int, duration numeric);""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artist (artist_id varchar PRIMARY KEY, name varchar, location varchar, latitude numeric, longitude numeric);""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time (start_time numeric PRIMARY KEY, hour numeric, day numeric, week numeric, month numeric, year int, weekday int);""")

# INSERT RECORDS
songplay_table_insert = ("""INSERT INTO songplay (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);""")

user_table_insert = ("""INSERT INTO user (user_id, first_name, last_name, gender, level) VALUES (%s, %s, %s, %s, %s);""")

song_table_insert = ("""INSERT INTO song (song_id, title, artist_id, year, duration) VALUES (%s, %s, %s, %s, %s);""")

artist_table_insert = ("""INSERT INTO artist (artist_id, name, location, latitude, longitude) VALUES (%s, %s, %s, %s, %s);""")

time_table_insert = ("""INSERT into time (start_time, hour, day, week, month, year, weekday) VALUES (%s, %s, %s, %s, %s, %s, %s);""")

# FIND SONGS

song_select = ("""SELECT song.song_id, song.title song.duration FROM songs WHERE duration > 200;""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create,
                        time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop,
                      song_table_drop, artist_table_drop, time_table_drop]
