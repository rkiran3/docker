
$ docker run -p 5010:5010 -it 07-random-quote

# GET 
$ curl -L http://localhost:5010/quotes
"Trade money for time, not time for money. You\u2019re going to run out of time    first."

# POST
$ curl -L -X POST -H "Content-Type: application/json" -d ' "newpost" ' http://localhost:5010/quotes
$ curl -L -X POST -H "Content-Type: application/json" -d ' "newpost2" ' http://localhost:5010/quotes

# DELETE by index
$ curl -X DELETE   http://localhost:5010/quotes/1



Implement Auth0
https://www.freecodecamp.org/news/build-secure-apis-with-flask-and-auth0/

Get ACCESS_TOKEN From auth0 website
$ curl --request GET -i -H "authorization: Bearer [ACCESS_TOKEN]" http://localhost:5010/user

