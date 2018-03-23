import sqlite3

def setup():
    conn = sqlite3.connect('db/hackathon.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS point (latitude REAL, longitude REAL, altitude REAL, UNIQUE(latitude, longitude, altitude) ON CONFLICT REPLACE);")
    conn.commit()
    conn.close()

def insert(point):
    conn = sqlite3.connect('db/hackathon.db')
    c = conn.cursor()
    try:
        c.execute("INSERT INTO point VALUES('" + str(point[0]) + "','" + str(point[1]) + "','"  + str(point[2]) + "');")
        conn.commit()
    except Exception as e:
        print(e)
    conn.close()

def get_point(id):
    conn = sqlite3.connect('db/hackathon.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM point WHERE rowid=" + str(id) + ";")
    result = c.fetchone()
    conn.close()
    return result

def get_all():
    conn = sqlite3.connect('db/hackathon.db')
    c = conn.cursor()
    
    c.execute("SELECT rowid, * FROM point;")
    result = c.fetchall()
    conn.close()
    return result
