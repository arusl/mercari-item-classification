import pandas as pd
import joblib

from mercari_model.config import PIPELINE_NAME

def make_prediction(input_data):
    try:
        _pipeline = joblib.load(filename=PIPELINE_NAME)
        results = _pipeline.predict(input_data)
    except IOError:
        print("File not accessible / not exist.")
        results = "==Failed to predict because trained model does not exist=="
    finally:
        return results

if __name__ == "__main__":
    #test pipeline
    pred = make_prediction(['nike yoga pants girl size S','adidas soccer shoes', 'samsung galaxy s10'])
    print({'Beauty': 0, 'Handmade': 1, 'Vintage & Collectibles': 2, 'Men': 3, 'Women': 4, 'Kids': 5, 'Electronics': 6, 'Sports & Outdoors': 7, 'Other': 8, 'Home': 9})
    print(['double door fridge','adidas soccer shoes', 'samsung galaxy s10'])
    print(pred)