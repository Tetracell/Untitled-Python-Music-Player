import sqlite3
import os	
import eyed3


conn = sqlite3.connect('E:\Music\music.db')
music_dir = 'E:\Music'

db_exist = False

'''
for file in os.listdir(music_dir):
	if file.endswith(".db"):
		db_exist = True
'''
		
conn.execute('''CREATE TABLE MUSIC
				(ID INT PRIMARY KEY NOT NULL,
				ARTIST			TEXT	NOT NULL,
				ALBUM			TEXT	NOT NULL,
				TITLE			TEXT	NOT NULL,
                TRACK           INT);''')

'''				
for file in os.listdir(os.getcwd()):
	if file.endswith(".mp3"):
		audiofile = eyed3.load(file)
		conn.execute('INSERT INTO MUSIC (ID, ARTIST, ALBUM, TITLE) \
		VALUES ({},"{}","{}","{}",{})'.format(count,audiofile.tag.artist,audiofile.tag.album, audiofile.tag.title,audiofile.tag.track_num[0]));
'''

count = 0

for dirName, subdirList, fileList in os.walk(music_dir):
    for fname in fileList:
        if fname.endswith(".mp3"):
            audiofile = eyed3.load(os.path.join(dirName,fname))
            try:
                conn.execute('INSERT INTO MUSIC (ID, ARTIST, ALBUM, TITLE, TRACK) \
		        VALUES ({},"{}","{}","{}",{})'.format(count,audiofile.tag.artist,audiofile.tag.album, audiofile.tag.title,audiofile.tag.track_num[0]));
                count += 1
            except:
                pass    

conn.commit()
conn.close()