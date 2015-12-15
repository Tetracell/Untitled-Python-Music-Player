import sqlite3
import os	
import eyed3
import codecs
import sys


conn = sqlite3.connect('E:\Music\music.db')
music_dir = u'E:\Music'

db_exist = False

'''
for file in os.listdir(music_dir):
	if file.endswith(".db"):
		db_exist = True
'''
		
conn.execute('''CREATE TABLE MUSIC
				(ID INT PRIMARY KEY NOT NULL,
				ARTIST			TEXT,
				ALBUM			TEXT,
				TITLE			TEXT,
                TRACK           TEXT,
                FILENAME        TEXT);''')

'''				
for file in os.listdir(os.getcwd()):
	if file.endswith(".mp3"):
		audiofile = eyed3.load(file)
		conn.execute('INSERT INTO MUSIC (ID, ARTIST, ALBUM, TITLE) \
		VALUES ({},"{}","{}","{}",{})'.format(count,audiofile.tag.artist,audiofile.tag.album, audiofile.tag.title,audiofile.tag.track_num[0]));
'''

count = 0
problem = codecs.open('E:\Music\problem_children.txt', 'w', encoding ='utf-8')

for dirName, subdirList, fileList in os.walk(music_dir):
    for fname in fileList:
        if fname.endswith(".mp3"):
            audiofile = eyed3.load(os.path.join(dirName,fname))
            try:
                '''
                conn.execute('INSERT INTO MUSIC (ID, ARTIST, ALBUM, TITLE, TRACK) \
		        VALUES ({},"{}","{}","{}",{})'.format(count,unicode(audiofile.tag.artist),unicode(audiofile.tag.album), unicode(audiofile.tag.title),audiofile.tag.track_num[0]));
                count += 1
                '''
                conn.execute('INSERT INTO MUSIC (ID, ARTIST, ALBUM, TITLE, TRACK, FILENAME) \
                VALUES (?, ?, ?, ?, ?, ?)', (count,audiofile.tag.artist,audiofile.tag.album, audiofile.tag.title,audiofile.tag.track_num[0], os.path.join(dirName, fname)))
            
            except:
                pass

            count += 1   

conn.commit()
conn.close()
problem.close()

''' Orphaned Code

For checking exceptions:

problem.write(os.path.join(dirName, fname))
                problem.write(u'\r\n')
                problem.write(unicode(sys.exc_info()[0]))
                problem.write(u'\r\n')
                problem.flush()
'''