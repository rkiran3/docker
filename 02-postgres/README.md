docker-compose up

# docker compose detached
docker-compose up -d  # 

# This may not work if bash is not available, use "sh" instead
docker-compose exec 02-postgres_postgres_1 bash

# get the container name 
docker container ps
docker ps

# get the Network IP
sudo docker inspect -f '{{ range .NetworkSettings.Networks }} {{ .IPAddress }} {{ end }}' 02-postgres_postgres_1 

# login to container
$ docker exec -it 02-postgres_postgres_1  sh

/ # psql -U postgres
psql (9.5.6)
Type "help" for help.


postgres=# \c mydb;
You are now connected to database "mydb" as user "postgres".
mydb=# \l
                                 List of databases
   Name    |  Owner   | Encoding |  Collate   |   Ctype    |   Access privileges   
-----------+----------+----------+------------+------------+-----------------------
 mydb      | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 postgres  | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 template0 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
           |          |          |            |            | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
           |          |          |            |            | postgres=CTc/postgres
(4 rows)

mydb=# \du
                                   List of roles
 Role name |                         Attributes                         | Member of 
-----------+------------------------------------------------------------+-----------
 postgres  | Superuser, Create role, Create DB, Replication, Bypass RLS | {}
 user      | Superuser                                                  | {}


