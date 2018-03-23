import sqlite3

def setup():
    conn = sqlite3.connect('db/hackathon.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS user (mac text, UNIQUE(mac) ON CONFLICT REPLACE);")
    conn.commit()
    conn.close()

def insert(mac_address):
    conn = sqlite3.connect('db/hackathon.db')
    c = conn.cursor()
    try:
        c.execute("INSERT INTO user VALUES('" + mac_address + "');")
        conn.commit()
    except Exception as e:
        print(e)
    conn.close()
    
def get_all():
    conn = sqlite3.connect('db/hackathon.db')
    c = conn.cursor()
    
    c.execute("SELECT rowid, * FROM user;")
    result = c.fetchall()
    conn.close()
    return result
