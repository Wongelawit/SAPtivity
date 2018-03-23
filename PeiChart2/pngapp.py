import random
#import StringIO
import json
import io
import requests
from flask import Flask, make_response,jsonify
from flask import send_file
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import matplotlib.patches
app = Flask(__name__)


def binary_to_dict(the_binary):
    jsn = ''.join(chr(int(x, 2)) for x in the_binary.split())
    d = json.loads(jsn)  
    return d

@app.route('/daily_activity',methods=['GET'])
def plot():
    
    pie_plot()
    #response=make_response( jsonify({'image_url': 'foo.png'}))
   # response.headers.set('Content-Type', 'image/png')
   
    return send_file('daily.png', mimetype='image/png')

def pie_plot():
    
    resp = requests.get("http://10.161.106.9:5000/aggregate/day").content
    
    my_json = resp.decode('utf8').replace("'", '"')
    
   

# Load the JSON to a Python list & dump it back out as formatted JSON
    res = json.loads(my_json)
    #res = json.dumps(data, indent=4, sort_keys=True)
   
    
    all_number = []
    all_label = []
    tot = 0

    for key in res:
        value = res[key]
        tot += value
        print("The key and value are ({}) = ({})".format(key, value))
    
    for key in res:
        all_label.append(key)
        all_number.append(((res[key]/tot) * 10000))

    #title = plt.title('daily activity')
    #title.set_ha("center")
    
    plt.gca().axis("equal")
    pie = plt.pie(all_number, startangle=0)
   # labels=["Gym", "Meeting Room", "Kitchen", "Desk"]
    plt.legend(pie[0],all_label, bbox_to_anchor=(0.5,0.5), loc="center left", fontsize=20, 
           bbox_transform=plt.gcf().transFigure)    
    plt.subplots_adjust(left=0.0, bottom=0.1, right=0.45)
    plt.savefig("daily.png", bbox_inches='tight')


@app.route('/weekly_activity',methods=['GET'])
def weekly_activity():
    total = [4,50,2,39]
    #title = plt.title('daily activity')
    #title.set_ha("center")
    
    plt.gca().axis("equal")
    pie = plt.pie(total, startangle=0)
    labels=["Gym", "Meeting Room", "Kitchen", "Desk"]
    plt.legend(pie[0],labels, bbox_to_anchor=(0.5,0.5), loc="center left", fontsize=20, 
           bbox_transform=plt.gcf().transFigure)    
    plt.subplots_adjust(left=0.0, bottom=0.1, right=0.45)
    plt.savefig("week.png", bbox_inches='tight')
    return send_file('week.png', mimetype='image/png')
@app.route('/monthly_activity',methods=['GET'])
def monthly_activity():
    total = [35,10,2,40]
    #title = plt.title('daily activity')
    #title.set_ha("center")
    
    plt.gca().axis("equal")
    pie = plt.pie(total, startangle=0)
    labels=["Gym", "Meeting Room", "Kitchen", "Desk"]
    plt.legend(pie[0],labels, bbox_to_anchor=(0.5,0.5), loc="center left", fontsize=20, 
           bbox_transform=plt.gcf().transFigure)    
    plt.subplots_adjust(left=0.0, bottom=0.1, right=0.45)
    plt.savefig("month.png", bbox_inches='tight')
    return send_file('month.png', mimetype='image/png')
if __name__ == '__main__':
    app.run(host='0.0.0.0')