
# Setup a virtual environment for first time so that it will be isolated from the main Python install.
$ python -m venv env


# Activate the environment, use 'deactivate' to leave environment 
$ source env/bin/activate


# Now, specify packages that will be used and install using 'pip' notice, prompt will change to (env) 
# to search for version number, use pypi.org which will show package name.
# https://pypi.org/project/python-dotenv/#history
(env) $ cat requirements.txt
Flask==2.1.0
python-dotenv == 1.0.0

# Install the required packages
(env) $ pip install -r requirements.txt


# To build docker image
$ docker build -t docker/04-flask-app .


# To run docker image with port 5000
$ docker run -p 5000:5000 -e PORT=5000 docker/04-flask-app 

# Test in browser
http://localhost:5000/routes/BNSF
http://localhost:5000/
http://localhost:5000/routes/BNSF/1215



# Use port 8000
$ docker run -p 8000:5000 -e PORT=5000 docker/04-flask-app 

http://localhost:8000/routes/BNSF/1215
