import os

from flask import Flask, jsonify, request
from mercari_model import config
from mercari_model.predict import make_prediction

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # root page
    @app.route('/')
    def welcome():
        return "Welcome!"

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return "Hello, World!"

    @app.route('/test_predict_single_item')
    def predict():
        item_name = 'logitech mouse'
        pred = make_prediction([item_name])
        
        # Convert integer prediction to a label string
        label_dict = config.LABEL_DICT
        key_list = list(label_dict.keys())
        val_list = list(label_dict.values())
        position = val_list.index(pred[0])
        item_category = key_list[position]

        return jsonify({'name': item_name, 'predicted_label': item_category})
    
    @app.route('/api/v1/predict_category', methods=['POST'])
    def predict_category():
        if 'item_name' in request.json:
            item_name = request.json['item_name']
        else:
            return "Error: No item_name field provided. Please specify a item_name."
        
        model_name = config.PIPELINE_NAME
        
        pred = make_prediction([item_name])

        # Convert integer prediction to a label string
        label_dict = config.LABEL_DICT
        key_list = list(label_dict.keys())
        val_list = list(label_dict.values())
        position = val_list.index(pred[0])
        item_category = key_list[position]

        return jsonify({'name': item_name, 'predicted_label': item_category})

    return app

app = create_app()