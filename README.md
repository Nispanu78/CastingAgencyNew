# Full Stack Casting Agency Backend

## The object of this project is to put into practice my basic knowledge of the following topics:
Python 3
PostgreSQL
SQLAlchemy
Internet Protocols and Communication
Flask APIs
Authentication
Auth0
Role-Based Access Control (RBAC)
Testing Flask applications
Deploying an application with Heroku

Local server: http://127.0.0.1:5000/

### Heroku link:
https://agency2010.herokuapp.com/

#### Authentication

The app is based on roles based authentications, which vary according to the specific function performed by the employee of the casting agency, namely
Casting Assistant, Casting Director and Executive Producer
Casting Assistant: can view actors and movies,
Casting Director: views actors and movies, updates actors and movie, creates and
deletes only actors.
Executive Producer: views actors and movies, updates actors and movie, creates and
deletes actors and movies.
To login: https://dev-s7inf-u3.eu.auth0.com/authorize?audience=http://localhost:5000&response_type=token&client_id=K0AvvStjD7e71HGatG2WozflAeN3itBg&redirect_uri=http://localhost:8100
Casting Assistant logins with:assistant@castingagency.com
Pw: Assistant12345
Casting Director logins with:director@castingagency.com
Pw: Director12345
JWT TOKEN:
Executive Producer logins with:producer@castingagency.com
Pw:Producer12345

##### Project Dependencies

Python 3.8

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

Virtual environment

It is recommended working within a virtual environment whenever using Python for projects.
This keeps dependencies for each project separate and well organized.
Instructions for setting up a virtual environment can be found
in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

PIP Dependencies

Once the virtual environment is setup and running, install dependencies by navigating to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```
This will install all of the required packages within the `requirements.txt` file.

Key Dependencies:

- [Flask](http://flask.pocoo.org/) is a lightweight backend micro-service framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM (Object Relational Mapping).

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension to handle cross origin requests.

Database Setup
With Postgres running, start a database running the following commands from the folder terminal:

```bash
    python3 manage.py casting_db init
    python3 manage.py casting_db migrate
    python3 manage.py casting_db upgrade
```

Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
source setup.sh
python3 app.py
```

######

API Documentation

#RBAC for Casting Assistant
GET/movies
It returns a list of movies.
If it finds the movie it returns success = True, else the following message:"
There is no movie with that name in our system"
Example of successful get/movies request:
{
    "movies": [
        {
            "title": "Test movie"
            "release_date": "Fri, 31 Jul 2020 00:00:00 CET",
        },
    ],
    "success": true
}

GET/actors
It returns a list of actors.
If it finds the actor it returns success = True, else the following message:"
There is no actor with that name in our system"
Examples of successful get/actors request:
{
    "actors": [
        {
            "name": "Arthur Schopenhauer",
            "age": 56,
            "gender": "male",
            "movie_id": 1
        },
    ],
    "success": true
}

Examples of unsuccessful post/actors, post/movies, delete/actors, delete/movies,
patch/actors, patch/movies requests

POST/movies
{
    "error": 401,
    "message": "Unauthorized"
    "success": false
}

POST/actors
{
    "error": 401,
    "message": "Unauthorized"
    "success": false
}

DELETE/movies
{
    "error": 401,
    "message": "Unauthorized"
    "success": false
}
DELETE/actors
{
    "error": 401,
    "message": "Unauthorized"
    "success": false
}
PATCH/movies
{
    "error": 401,
    "message": "Unauthorized"
    "success": false
}
PATCH/actors
{
    "error": 401,
    "message": "Unauthorized"
    "success": false
}

#RBAC for Casting Director

GET/movies
It returns a list of movies.
If it finds the movie it returns success = True, else the following message:"
There is no movie with that name in our system"
Example of successful get/movies request:
{
    "movies": [
        {
            "title": "Test movie"
            "release_date": "Fri, 31 Jul 2020 00:00:00 CET",
        },
    ],
    "success": true
}

GET/actors
It returns a list of actors.
If it finds the actor it returns success = True, else the following message:"
There is no actor with that name in our system"
Examples of successful get/actors request:
{
    "actors": [
        {
            "name": "Arthur Schopenhauer",
            "age": 56,
            "gender": "male",
            "movie_id": 1
        },
    ],
    "success": true
}

POST/actors

It creates a new actor using JSON request parameters and adds it to the database.
If it creates the actor it returns success = True, else it aborts with 422 error message.
Example of successful post/movies request:

{
    "new_actor": {
        "name": "John Taylor",
        "age": 25,
        "gender": "male",
        "movie_id": 6
    },
    "success": true
}

DELETE/actors/<int:id>
It deletes the actors present in the database
If it deletes the actor it returns success = True, else it aborts with 422 error message.
Example of successful delete/actors request:
{
    "deleted_actor": 4,
    "success": true
}

PATCH/movies

It modifies a movie present in the database.
If modification is successful it returns success = True, else it aborts with 422 error message.
Example of successful patch/movies request:
{
    "success": true,
    "updated_movie": {
        "title": "Test movie3"
        "release_date": "Fri, 7 Aug 2020 00:00:00 CET",
    }
}

PATCH/actors

It modifies an actor present in the database.
If modification is successful it returns success = True, else it aborts with 422 error message.
Example of successful patch/actors request:
{
    "success": true,
        "name": "John Taylor",
        "age": 45,
        "gender": "male",
        "movie_id": 8
    }
}

Examples of unsuccessful post/movies, delete/movies requests:

POST/movies
{
    "error": 401,
    "message": "Unauthorized"
    "success": false
}

DELETE/movies
{
    "error": 401,
    "message": "Unauthorized"
    "success": false
}

#RBAC for Executive Producer

GET/movies
It returns a list of movies.
If it finds the movie it returns success = True, else the following message:"
There is no movie with that name in our system"
Example of successful get/movies request:
{
    "movies": [
        {
            "title": "Test movie"
            "release_date": "Fri, 31 Jul 2020 00:00:00 CET",
        },
    ],
    "success": true
}

GET/actors
It returns a list of actors.
If it finds the actor it returns success = True, else the following message:"
There is no actor with that name in our system"
Examples of successful get/actors request:
{
    "actors": [
        {
            "name": "Arthur Schopenhauer",
            "age": 56,
            "gender": "male",
            "movie_id": 1
        },
    ],
    "success": true
}

POST/movie
It creates a new movie using JSON request parameters and adds it to the database.
If it creates the movie it returns success = True, else it aborts with 422 error message.
Example of successful post/movies request:
{
    "new_movie": {
            "title": "Test movie2"
            "release_date": "Mon, 3 Aug 2020 00:00:00 CET",
        },
    "success": true
}

DELETE/movies/<int:id>

It deletes the movies present in the database.
If it deletes the movie it returns success = True, else it aborts with 422 error message.
Example of successful delete/movies request:
{
    "deleted_movie": 4,
    "success": true
}

POST/actors

It creates a new actor using JSON request parameters and adds it to the database.
If it creates the actor it returns success = True, else it aborts with 422 error message.
Example of successful post/movies request:

{
    "new_actor": {
        "name": "John Taylor",
        "age": 25,
        "gender": "male",
        "movie_id": 6
    },
    "success": true
}

DELETE/actors/<int:id>
It deletes the actors present in the database
If it deletes the actor it returns success = True, else it aborts with 422 error message.
Example of successful delete/actors request:
{
    "deleted_actor": 4,
    "success": true
}

PATCH/movies

It modifies a movie present in the database.
If modification is successful it returns success = True, else it aborts with 422 error message.
Example of successful patch/movies request:
{
    "success": true,
    "updated_movie": {
        "title": "Test movie3"
        "release_date": "Fri, 7 Aug 2020 00:00:00 CET",
    }
}

PATCH/actors

It modifies an actor present in the database.
If modification is successful it returns success = True, else it aborts with 422 error message.
Example of successful patch/actors request:
{
    "success": true,
        "name": "John Taylor",
        "age": 45,
        "gender": "male",
        "movie_id": 8
    }
}
