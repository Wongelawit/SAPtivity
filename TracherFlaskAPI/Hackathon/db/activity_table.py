import sqlite3

def setup():
    conn = sqlite3.connect('db/hackathon.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS activity (location_id INT, user_id INT, time INTEGER, FOREIGN KEY(location_id) REFERENCES location(row_id), FOREIGN KEY(user_id) REFERENCES user(row_id));")
    conn.commit()
    conn.close()

def insert(activity):
    conn = sqlite3.connect('db/hackathon.db')
    c = conn.cursor()
    try:
        c.execute("INSERT INTO activity VALUES('" + str(activity[0]) + "','" + str(activity[1]) + "','"  + str(activity[2]) +  "');")
        conn.commit()
    except Exception as e:
        print(e)
    conn.close()
        
def get_all():
    conn = sqlite3.connect('db/hackathon.db')
    c = conn.cursor()
    
    c.execute("SELECT rowid, * FROM activity;")
    result = c.fetchall()
    conn.close()
    return result

def aggregate_by_location():
    conn = sqlite3.connect('db/hackathon.db')
    c = conn.cursor()
    
    c.execute("SELECT SUM(time), location_id FROM activity GROUP BY location_id;")
    result = c.fetchall()
    conn.close()
    return result