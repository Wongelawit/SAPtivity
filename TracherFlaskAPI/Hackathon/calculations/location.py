import sys
import math
import time
from db import point_table
from db import activity_table
from db import location_table

last_room_name = ''
last_time = 0

def find_room(input_data):
    global last_room_name
    global last_time
    all_locations = location_table.get_all()

    x1 = input_data['point']['lat']
    y1 = input_data['point']['long']
    now_time = time.time()

    min_dist = sys.maxint
    min_tuple = (min_dist, None, None)
    found_room = False
    for location in all_locations:
        location_id = location[0]
        point_id = location[1]
        loc_radius = location[2]
        loc_name = location[3]
        loc_type = location[4]

        center_point = point_table.get_point(point_id)

        if center_point is not None:
            x2 = center_point[1]
            y2 = center_point[2]
            
            current_dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            
            if current_dist < min_dist:
                min_dist = current_dist
                min_tuple = (min_dist, location_id, loc_name)

            if current_dist < loc_radius:
                found_room = True
                old_one = last_room_name
                last_room_name = loc_name

                old_time = last_time
                last_time = now_time

                if old_one != loc_name:
                    activity_table.insert((location_id, '333', now_time - old_time))
                    print(loc_name)
                return old_one, loc_name

    if not found_room:
        print ('NOT FOUND ===> ', min_tuple[2])
        old_one = last_room_name
        last_room_name = min_tuple[2]

        old_time = last_time
        last_time = now_time
        
        if old_one != loc_name:       
            activity_table.insert((min_tuple[1], '333', now_time - old_time))
            print(min_tuple[2])
        return old_one, min_tuple[2]
