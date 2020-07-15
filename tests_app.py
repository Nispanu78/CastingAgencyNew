import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from models import Actor, Movie, setup_db
from app import create_app
from models import casting_db
import datetime


class CastingAgencyTestCase(unittest.TestCase):

    def setUp(self):
        '''Initializes items to perform tests'''

        self.app = create_app()
        self.client = self.app.test_client
        setup_db(self.app)
        db.create_all()

        self.new_movie = {
            'title': 'Test movie',
            'release_date': datetime.date(2020, 7, 31),
        }

        self.new_actor = {
            'name': 'Arthur Schopenhauer',
            'age': 56,
            'gender': 'Male',
            'movie_id': 1
        }

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.drop_all()
            self.db.create_all()

    def tearDown(self):
        pass

# Test movies
    def test_get_movies(self):
        response = self.client().get('/movies')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])

    def test_fail_get_movies(self):
        response = self.client().get('/moviess')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 404)
        self.assertEqual(
            data['message'],
            'There is no movie with that name in our system')

    def test_add_movie(self):
        response = self.client().post('/movies', json=self.new_movie)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['new_movie']['title'], 'Test Movie')

    def test_fail_add_movie(self):
        response = self.client.post('/movies',
                                    json={'title': 'Test Movie'})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 422)
        self.assertEqual(data['message'], 'Unable to process this instruction')

    def test_delete_movie(self):
        response = self.client().delete('/movies/2')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['deleted'])

    def test_fail_delete_movie(self):
        response = self.client().delete('/movies/1000000000000000000000')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 422)
        self.assertEqual(data['message'], 'Unable to process this instruction')

    def test_patch_movie(self):
        response = self.client().patch('/movies/2', json=self.new_movie)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie_id'])

    def test_fail_patch_movie(self):
        response = self.client().patch('/movies/3000', json=self.new_movie)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 422)
        self.assertEqual(data['message'], 'Unable to process this instruction')

# Test actors
    def test_get_actors(self):
        response = self.client().get('/actors')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    def test_fail_get_actors(self):
        response = self.client().get('/atcor')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['error'], 404)
        self.assertEqual(
            data['message'],
            'There is no actor with that name in our system')

    def test_create_actor(self):
        response = self.client().post('/actors', json=self.new_actor)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['new_actor']['name'], 'Arthur Schopenhauer')

    def test_fail_create_actor(self):
        response = self.client().post(
            '/actors', json={'name': 'Arthur Schopenhauer'})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 422)
        self.assertEqual(data['message'], 'Unable to process this instruction')

    def test_delete_actor(self):
        response = self.client().delete('/actors/1')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['deleted'])

    def test_fail_delete_actor(self):
        response = self.client().delete('/actors/1000000000000000000000')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 422)
        self.assertEqual(data['message'], 'Unable to process this instruction')

    def test_patch_actor(self):
        response = self.client().patch('/actors/2', json=self.new_actor)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor_id'])

    def test_fail_patch_actor(self):
        response = self.client().patch('/actors/1000000000000000000000',
                                       json=self.new_actor)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 422)
        self.assertEqual(data['message'], 'Unable to process this instruction')


if __name__ == "__main__":
    unittest.main()
