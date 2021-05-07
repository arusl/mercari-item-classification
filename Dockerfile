#Using the base image with python 3.7
FROM python:3.9.4

#Set our working directory as app
WORKDIR /app 

# Copy the models directory, api, and wsgi.py files
ADD ./flask_apis ./flask_apis
ADD ./mercari_model ./mercari_model
ADD wsgi.py wsgi.py
ADD ./requirements.txt ./requirements.txt

#Installing the required python packages
RUN pip install -r requirements.txt

#Exposing the port 5000 from the container
EXPOSE 5000

#Starting the python application
# CMD ["python", "wsgi.py"]
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]