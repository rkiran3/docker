
# This example will show how to build a image
docker build -t 01-hello-world-python .  # dont forget the period at end

# list the image
docker image ps

# list container
docker container ps

# run the image
docker run -it 01-hello-world-python:latest

# run the image and delete
docker run -it --rm  01-hello-world-python

