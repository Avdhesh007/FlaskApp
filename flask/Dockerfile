FROM python:3.8.11-alpine

#Set the working directory to app 
WORKDIR /app

#Copy the current directory contents into the container at /app
ADD . /app

# Install the dependencies

RUN pip install -r requirements.txt

#run the command to start uWSGI

#CMD ["uwsgi", 'app.ini']
#CMD ["gunicorn", "-w", " 2 run:app"]
CMD ["gunicorn","-c","gunicorn.conf.py","run:app"]
#CMD ["systemctl","start app"]