
$ docker run -itd --env "PORT=5432" --name mycontainer alpine

$ docker ps # prints container Names
CONTAINER ID   IMAGE                       COMMAND                  CREATED          STATUS          PORTS                                                 NAMES
ba6a89b074c5   alpine                      "/bin/sh"                19 seconds ago   Up 18 seconds                                                         mycontainer

$ docker exec mycontainer  /usr/bin/env
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
HOSTNAME=ba6a89b074c5
PORT=5432
HOME=/root

$ docker exec mycontainer /bin/sh -c /usr/bin/env
HOSTNAME=ba6a89b074c5
SHLVL=1
PORT=5432
HOME=/root
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
PWD=/

$ docker inspect mycontainer --format '{{ .Config.Env }}'
[PORT=5432 PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin]

