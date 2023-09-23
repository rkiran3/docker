$ python -m venv env

$ source env/bin/activate

(env) $ python -m pip install -r requirements.txt

(env) $ docker build -t 08-flask-snippets .

# use the --detach option which will run the container standalone
# use the --build to pick up changes, if any
$ docker-compose up --build --detach

$ docker-compose down --remove-orphans 

$ docker container prune

$ docker logs 08-flask-snippets 

$ docker logs --follow 08-flask-snippets 
