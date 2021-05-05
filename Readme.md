# Mercari Item Classification

> This repo contains a dummy project created during Build@Mercari 2021
> to learn about the Deployment of ML Models

Steps to reproduce:
0. Clone the repository
1. Make sure you are inside the root directory `mercari-item-classification`
2. Download dataset from https://www.kaggle.com/c/mercari-price-suggestion-challenge
3. Put the *train.tsv* and *test.csv* under `mercari-model/datasets/`
4. 
4. Run `python -m venv env` to create virtual environment, then activate it `source env/Scripts/activate`
5. Run `pip install -r requirements.txt` to install required packages
6. Run `export FLASK_APP=flask_apis` to set which module contains the Flask API
7. Run `flask run` to serve the api
8. Run `pytest` to run pytest scripts make sure all apis are working