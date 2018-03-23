#!/usr/bin/env python
# -*- coding: utf-8 -*-
from calculations import location, location_duration

def record_activitiy(input_data):
    return location.find_room(input_data)

def get_daily_stats():
    return location_duration.aggregate_by_location()
