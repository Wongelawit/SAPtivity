from flask import Flask, send_from_directory, jsonify, request
from flask_cors import CORS
from data import insert_data
from controller import controller

app = Flask(__name__)
cors = CORS(app, resources={r"/map-now": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app)

insert_data.insert_all()

current_room = ''
old_room = ''

@app.route('/record-activity', methods=['POST'])
def record_activitiy():
    global current_room
    global old_room
    json_content = request.get_json()
    old_room, current_room = controller.record_activitiy(json_content)
    return 'success-activity'

@app.route('/aggregate/day', methods=['GET'])
def get_daily_stats():
    result = controller.get_daily_stats()
    print (result)
    response = jsonify(result)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/map-now', methods=['GET'])
def get_map(): 
    response = jsonify("{\"oldid\":\"" + old_room + "\", \"newid\":\"" + current_room + "\"}")
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response