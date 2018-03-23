from flask import Flask
from flask import request
from data import insert_data
from controller import controller

app = Flask(__name__)

insert_data.insert_all()

@app.route('/record-activity', methods=['POST'])
def record_activitiy():
    json_content = request.get_json()
    controller.record_activitiy(json_content)
    return 'success-activity'

@app.route('/aggregate/month', methods=['GET'])
def get_monthly_stats():
    controller.get_monthly_stats()
    return 'success-aggregare'
