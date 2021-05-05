import flask
from flask import request, jsonify
from flask_cors import CORS
import config
from predict import make_prediction

app = flask.Flask(__name__)
app.config["DEBUG"] = True
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Flask API for Mercari Item Classification</h1>'''

@app.route('/api/v1/predict_category', methods=['POST'])
def predict_category():
    if 'item_name' in request.json:
        item_name = request.json['item_name']
    else:
        return "Error: No item_name field provided. Please specify a item_name."
    
    model_name = config.PIPELINE_NAME
    
    pred = make_prediction([item_name])

    label_dict = {'Beauty': 0, 'Handmade': 1, 'Vintage & Collectibles': 2, 'Men': 3, 'Women': 4, 'Kids': 5, 'Electronics': 6, 'Sports & Outdoors': 7, 'Other': 8, 'Home': 9}
    key_list = list(label_dict.keys())
    val_list = list(label_dict.values())
    position = val_list.index(pred[0])
    item_category = key_list[position]

    return jsonify({'label': item_category})

app.run()