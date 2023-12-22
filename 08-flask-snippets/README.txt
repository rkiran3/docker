Start by setting up the environment for this program.
Use library module and folder name to setup environment.

$ python -m venv env

Once setup, activate for this program only, this command will bring up its own
shell.

$ source env/bin/activate

Create a file that will contain the modules required for this program (like
flask..)

(env) $ python -m pip install -r requirements.txt

Also, create a Dockerfile that will build an image to run program.

Dockerfile will contain the command to run the python program and listen to web requests.

(env) $ docker build -t 08-flask-snippets .

# use the --detach option which will run the container standalone
# use the --build to pick up changes, if any
$ docker-compose up --build --detach

$ docker-compose down --remove-orphans 

$ docker container prune

$ docker logs 08-flask-snippets 

$ docker logs --follow 08-flask-snippets 
