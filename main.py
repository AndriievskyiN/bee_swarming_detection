from script import cv2, datetime, os
from script.take_pictures import take_pictures
from script.save_to_github import pushToGitHub
import sqlite3

current_time = datetime.now()
conn = sqlite3.connect("pushed.db")
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS pushed (
    wasPushed INT
)''')
conn.commit()


if __name__ == "__main__":
    take_pictures(current_time)
    cur.execute("SELECT wasPushed FROM pushed")
    try:
        wasPushed = cur.fetchone()[0]
    except:
        pushToGitHub(current_time)
        cur.execute('''INSERT INTO pushed 
                        VALUES (1)''')
        conn.commit()
