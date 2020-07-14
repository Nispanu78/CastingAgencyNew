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
JWT TOKEN: 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjJfMF9Cem9raDMtdjYxVzdOLW4zQiJ9.eyJpc3MiOiJodHRwczovL2Rldi1zN2luZi11My5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYwMWE4YzA3NjAwNDQwMDEzOTlmMGI0IiwiYXVkIjoiaHR0cDovL2xvY2FsaG9zdDo1MDAwIiwiaWF0IjoxNTk0NzIxMTAyLCJleHAiOjE1OTQ3MjgzMDIsImF6cCI6IkswQXZ2U3RqRDdlNzFIR2F0RzJXb3pmbEFlTjNpdEJnIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.X0C2_owQk1VcBprD_chcCsQmCF2AgVlolMNR46Asv5jzECDIGB6rPHLEb6oLXpnZj3PFJLIU1mK8fed896hfQu4CFqgauRhl8yhkZFOL8tzDDR0uUbiBJVpxl-KgccCnaa4Z5TqWDaPvOOHKwFMFKKZ4YFWqd8rhC_2N6eVLlOD9jr5XnrzUNpCBfv8js4b0b2D_g_SKmmgG1TYhm-aI4jTQfGFToYeJS_6kWCd8893nijMpkByJz5LfjTMjhvq6-pOrMe_SZ5-Zq-LdZ0dQdsDoZKpgSUjAgqo-5em1KreqWmLfUl8fZ2tCc9eQMf4Fm_RtIaeBFlOflonxBbJjcg'
Casting Director logins with:director@castingagency.com
Pw: Director12345
JWT TOKEN: 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjJfMF9Cem9raDMtdjYxVzdOLW4zQiJ9.eyJpc3MiOiJodHRwczovL2Rldi1zN2luZi11My5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYwMWE4Njc3NjAwNDQwMDEzOTlmMDdkIiwiYXVkIjoiaHR0cDovL2xvY2FsaG9zdDo1MDAwIiwiaWF0IjoxNTk0NzIwNDE2LCJleHAiOjE1OTQ3Mjc2MTYsImF6cCI6IkswQXZ2U3RqRDdlNzFIR2F0RzJXb3pmbEFlTjNpdEJnIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyJdfQ.qUDl6nnP-JgcO7bylHpcwKQbZMmGQFuuFMHiYWSqp6Am3yoyt9S52Gom1MNzjoh5xFDpjYAMzkqFDlQc1p3fB_R3owfkulWmRuIrDezqCdXGcRpAIKOrCsBTCooXbJ6_H49_agfg_mWm9vwOltSipZhjHhXUcCX1l-BlxO9f2EalVGAa9R1JtOOr7ebGXj8QeAPybxvzFICuWgPc5jB5aJLmYUhY1vI3AySzvZbZYIHNKAFlYIss-VvL-dY6pczHJQcvctla8r_zPLH0Q2rRsD1heXhrNfWFavdMDgW6TrcJMG4IuwwsNCNFay4wRtO0i8VrI7XrG6GwFlsFJM80Vw'
Executive Producer logins with:producer@castingagency.com
Pw:Producer12345
JWT TOKEN: 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjJfMF9Cem9raDMtdjYxVzdOLW4zQiJ9.eyJpc3MiOiJodHRwczovL2Rldi1zN2luZi11My5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYwMWFhMjU2YjI1NjEwMDE5MTA4ZGEyIiwiYXVkIjoiaHR0cDovL2xvY2FsaG9zdDo1MDAwIiwiaWF0IjoxNTk0NzIwNTIzLCJleHAiOjE1OTQ3Mjc3MjMsImF6cCI6IkswQXZ2U3RqRDdlNzFIR2F0RzJXb3pmbEFlTjNpdEJnIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.kS19x8eohsj0nNv2zj9XMvnwwDSa6rPmNj3xazN96v5GNmdR872aCE1vQrL_Nj_i6NX4ANdwJLA_V7xv6MDqN3vJUUoiu6R7Cahmar76O7cECI_HhkWfPiqxXZLnWrd_0rzAN9taBcno0ZTyOAcm1n6rxnC7S0DHAdXF3kwH8yAROG44SSf3vR8S6rOXXSSBOBFcOhko0UyeijLNFSXPz1uZpbtkq60VUHn1cGuZmBP5LktgHgz8Rxn_-w0PQywiFNGkHERrf2C1PzMwunCmzmdq2POC0DiPeX2GrVAE3Ia31TiR96s9NxuKEOVYRoP_fXEiVKE3FrJKVLm2Ul-E8w'

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
Example of successful get/actors request:
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

POST/movies

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

DELETE/movies/<int:id>

It deletes the movies present in the database.
If it deletes the movie it returns success = True, else it aborts with 422 error message.
Example of successful delete/movies request:
{
    "deleted_movie": 4,
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
