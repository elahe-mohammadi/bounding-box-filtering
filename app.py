from flask import Flask, jsonify, request
import json
import numpy as np
from datetime import datetime


app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def filtering_api():
    if request.method == 'GET':
        with open('data.txt', 'r') as f:
            data = f.read().splitlines()
        data = [json.loads(item) for item in data]
        return jsonify({"response": data}), 200
    elif request.method == 'POST':
         if request.is_json:
            data = json.loads(request.data)
            main, input = data.get('main'), data.get('input')
            x1, y1 = main["x"], main["y"]
            x2 , y2 = x1 + main["width"], y1 + main["height"]
            out_file = open("data.txt", "a")
            for candid in input:
                x, y, w, h = candid["x"], candid["y"], candid["width"], candid["height"]
                
                
                if ((1 + np.min([x2, x+w])) - np.max([x1, x]) > 0) and ((1 + np.min([y2,y+h]) - np.max([y1, y])) > 0) :
                    candid["time"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    out_file.write(json.dumps(candid)+"\n")
            
            out_file.close()
            return jsonify({"status": "saved"}), 201
         else:
             return "Content type is not supported. It must be json.", 415

if __name__ == '__main__':
    # app.run(debug=True)
    # To make the Flask app accessible from outside the container, you need to modify the app to listen on 0.0.0.0.
    app.run(host='0.0.0.0', debug=True)
