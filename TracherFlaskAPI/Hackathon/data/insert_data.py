from db import user_table
from db import point_table
from db import location_table
from db import activity_table

def insert_all():
    # insert_users()
    # insert_points()
    # insert_locations()
    insert_activities()

def insert_users():
    user_table.setup()
    user_table.insert('1221312asdsadfasfd')
    user_table.insert('asdfas132341234')

def insert_points():
    point_table.setup()
    point_table.insert((49.27734784139329, -123.11793916343669, 0))
    point_table.insert((49.27686468160716, -123.11735502264459, 0))
    point_table.insert((49.276156405115906, -123.11815611253125, 0))

    point_table.insert((49.277141678920664, -123.11721790112149, 0))
    point_table.insert((49.277163801984315, -123.11706559544747, 0))
    point_table.insert((49.27738599414482, -123.1177443111094, 0))

def insert_locations():
    location_table.setup()
    location_table.insert((1, 0.000133, "Anemone", "Meeting Room"))
    location_table.insert((2, 0.000038, "Dshop", "Working Station"))
    location_table.insert((3, 0.000086, "Fireplace", "Social"))

    location_table.insert((4, 0.000086, "Lounge", "Social"))
    location_table.insert((5, 0.000036, "Kitchen", "Kitchen"))
    location_table.insert((6, 0.000038, "Desk", "Desk"))

def insert_activities():
    activity_table.setup()
