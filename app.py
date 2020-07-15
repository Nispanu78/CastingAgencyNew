import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import models
import auth
import json
from models import db_drop_and_create_all, setup_db, Actor, Movie, casting_db
from auth import AuthError, requires_auth


# Create and configure the app

def create_app(test_config=None):
    # creates and configures the app
    app = Flask(__name__)
    CORS(app, resource={r"/api.*": {"origin": "*"}})
    setup_db(app)

    # CORS Headers

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type, Authorization, true')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PATCH,POST,DELETE')
        return response

    # Home greeting test

    @app.route('/')
    def home():
        return jsonify('Cinema is the 7th art')

# MOVIES
    '''
        GETs /movies
    '''

    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')
    def get_movies(jwt):
        movies = Movie.query.all()
        format_movies = [movie.format() for movie in movies]

        if len(movies) > 0:
            return jsonify({
                'success': True,
                'movies': format_movies
            })
        else:
            return jsonify({
                'success': True,
                'movies': 'There is no movie with that name in our system'
            })

    '''
        POSTs /movies
    '''

    @app.route('/movies', methods=['POST'])
    @requires_auth('post: movies')
    def create_movies(jwt):
        data = request.get_json()
        movie_title = data.get('title')
        movie_release_date = data.get('release_date')

        if not ('title' in data and 'release_date' in data):
            abort(400)

        try:
            movie = Movie(title=movie_title, release_date=movie_release_date)
            movie.insert()

            return jsonify({
                'success': True,
                'movies': [movie.format()]
            }), 200

        except Exception:
            abort(422)

    '''
        PATCHes /movies/<id>
    '''

    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def patch_movies(jwt, movie_id):
        try:
            data = request.get_json()
            movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
            if movie is None:
                abort(404)

            if 'title' in data:
                movie.title = data.get('title')

            if 'release_date' in data:
                movie.release_date = data.get('release_date')

            movie.update()

            return jsonify({
                'success': True,
                'movies': [movie.format()]
            })

        except BaseException:
            abort(422)

    '''
        DELETEs /movies/<id>
    '''

    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie(jwt, movie_id):
        try:
            movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
            if movie is None:
                abort(404)

                movie.delete()

                return jsonify({
                    'success': True,
                    'movies': movie.id
                })
        except BaseException:
            abort(422)

# ACTORS
    '''
        GETs /actors
    '''

    @app.route('/actors', methods=['GET'])
    @requires_auth('get:actors')
    def get_actors(jwt):
        try:
            actors = Actor.query.all()
            actors_formatted = [actor.format() for actor in actors]
            return jsonify({
                'success': True,
                'actors': actors_formatted
            })
        except BaseException:
            abort(422)

    '''
        POSTs /actors
    '''

    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def create_actors(jwt):

        data = request.get_json()

        actor_name = data.get('name', None)
        actor_age = data.get('age', None)
        actor_gender = data.get('gender', None)

        try:

            if not actor_name:
                abort(400)

            actor = Actor(name=actor_name,
                          age=actor_age,
                          gender=actor_gender)
            actor.insert()
            actors_formatted = [actor.format()]

            return jsonify({
                'success': True,
                'actors': actors_formatted
            })
        except BaseException:
            abort(422)

    '''
        PATCHes /actors/<id>
    '''

    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def patch_actors(jwt, actor_id):

        try:
            data = request.get_json()
            actor = Actor.query.filter(Actor.id == actor_id).one_or_none()

            if actor is None:
                abort(404, 'There is no actor with that name in our system')

            if 'name' in data:
                actor.name = data.get('name')

            if 'age' in data:
                actor.age = data.get('age')

            if 'gender' in data:
                actor.gender = data.get('gender')

            actor.update()

            return jsonify({
                'success': True,
                'actors': [actor.format()]
            })

        except BaseException:
            abort(422)

    '''
        DELETEs /actors/<id>
    '''

    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actors(jwt, actor_id):

        try:
            actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
            if actor is None:
                abort(404)

            actor.delete()

            return jsonify({
                'success': True,
                'actors': actor.id
            })
        except BaseException:

            abort(422)

# Error Handling
    '''
    implement error handlers using the @app.errorhandler(error) decorator
    '''

    @app.errorhandler(500)
    def internal_server_error(error):
        return (jsonify({'success': False, 'error': 500,
                         'message': 'Internal server error'}), 500)

    @app.errorhandler(400)
    def bad_request(error):
        return (jsonify({'success': False, 'error': 400,
                         'message': 'Bad Request'}), 400)

    @app.errorhandler(401)
    def unauthorized(error):
        return (jsonify({'success': False, 'error': 401,
                         'message': 'Unauthorized'}), 401)

    @app.errorhandler(404)
    def not_found(error):
        return (jsonify({'success': False, 'error': 404,
                         'message': 'Not found'}), 404)

    @app.errorhandler(422)
    def unprocessable(error):
        return (jsonify({'success': False, 'error': 422,
                         'message': 'Unable to process this instruction'}), 422)

    @app.errorhandler(405)
    def not_allowed(error):
        return (jsonify({'success': False, 'error': 405,
                         'message': 'Method not allowed'}), 405)

    return app


app = create_app()


if __name__ == '__main__':
    app.run()
