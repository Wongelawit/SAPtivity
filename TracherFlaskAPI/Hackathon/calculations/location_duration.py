from db import activity_table
from db import location_table

def aggregate_by_location():
    group_room = activity_table.aggregate_by_location()
    
    result = {}

    for room in group_room:
        room_id = room[1]
        location = location_table.get_one(room_id)
        result[location[4]] = 0 

    for room in group_room:
        room_id = room[1]
        location = location_table.get_one(room_id)
        result[location[4]] += location[2]
    
    return result
