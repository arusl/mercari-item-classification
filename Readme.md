# Mercari Item Classification

> This repo contains a dummy project created during Build@Mercari 2021
> to learn about the Deployment of ML Models

Live Demo: http://udemy-mercari-api.herokuapp.com/

Steps to run the application locally after cloning the repo:
1. Make sure you are inside the root directory `mercari-item-classification`
2. Download dataset from https://www.kaggle.com/c/mercari-price-suggestion-challenge
3. Put the *train.tsv* and *test.csv* under `mercari_model/datasets/`
4. Run `python -m venv env` to create virtual environment, then activate it `source env/Scripts/activate`
5. Run `pip install -r requirements.txt` to install required packages
6. Run `tox -e train` to train and save the pipeline for later inference
7. Run `pytest` or `tox` to run pytest scripts make sure all APIs are working
8. Run `export FLASK_APP=flask_apis` to set which module contains the Flask API
9. Run `flask run` to serve the api, or run `python wsgi.py`
10. Test using any frontend app or Postman to try the APIs

Next todo:
- circleCI for CI/CD
