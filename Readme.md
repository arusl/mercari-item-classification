# Mercari Item Classification

> This repo contains a dummy project created during Build@Mercari 2021
> to learn about the Deployment of ML Models

Steps to reproduce after cloning the repo:
1. Make sure you are inside the root directory `mercari-item-classification`
2. Download dataset from https://www.kaggle.com/c/mercari-price-suggestion-challenge
3. Put the *train.tsv* and *test.csv* under `mercari_model/datasets/`
4. Run `python -m venv env` to create virtual environment, then activate it `source env/Scripts/activate`
5. Run `pip install -r requirements.txt` to install required packages
6. Run `export FLASK_APP=flask_apis` to set which module contains the Flask API
7. Run `flask run` to serve the api
8. Run `pytest` to run pytest scripts make sure all APIs are working
9. Test using any frontend app or Postman to try the APIs

Next todo:
- add tox
    - esp. to train model after cloning, instead of pushing the trained pipeline to github
- add shell script to automate dataset download
- understand the module system, and why, for example, `python predict.py` doesn't work, but predicting using pytest works
- deploy to heroku manually
- deploy to heroku using docker
- (opt) circleCI for CI/CD