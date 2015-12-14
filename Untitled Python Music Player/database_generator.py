import sqlite3
import os	
import eyed3


conn = sqlite3.connect('E:\Music\music.db')
music_dir = 'E:\Music'

db_exist = False

for file in os.listdir(os.getcwd()):
	if file.endswith(".db"):
		db_exist = True
		
if db_exist == False:
	conn.execute('''CREATE TABLE MUSIC
				(ID INT PRIMARY KEY NOT NULL,
				ARTIST			TEXT	NOT NULL,
				ALBUM			TEXT	NOT NULL,
				TITLE			TEXT	NOT NULL,
                TRACK           INT);''')
				
for file in os.listdir(os.getcwd()):
	if file.endswith(".mp3"):
		audiofile = eyed3.load(file)
		conn.execute('INSERT INTO MUSIC (ID, ARTIST, ALBUM, TITLE) \
		VALUES ({},"{}","{}","{}")'.format(audiofile.tag.track_num[0],audiofile.tag.artist,audiofile.tag.album, audiofile.tag.title));

conn.commit()
conn.close()