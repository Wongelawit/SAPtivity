import sqlite3

def setup():
    conn = sqlite3.connect('db/hackathon.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS location (center_id INT, radius INT, name TEXT, type TEXT, FOREIGN KEY(center_id) REFERENCES point(row_id));")
    conn.commit()
    conn.close()

def insert(location):
    conn = sqlite3.connect('db/hackathon.db')
    c = conn.cursor()
    try:
        c.execute("INSERT INTO location VALUES('" + str(location[0]) + "','" + str(location[1]) + "','"  + str(location[2]) + "','"  + str(location[3]) + "');")
        conn.commit()
    except Exception as e:
        print(e)
    conn.close()

def get_one(id):
    conn = sqlite3.connect('db/hackathon.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM location WHERE rowid='" + str(id) + "';")
    result = c.fetchone()
    conn.close()
    return result


def get_all():
    conn = sqlite3.connect('db/hackathon.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM location;")
    result = c.fetchall()
    conn.close()
    return result
