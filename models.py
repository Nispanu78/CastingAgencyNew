import os
from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json

casting_db = SQLAlchemy()

'''
Setup_db(app)

'''


def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ['DATABASE_URL']
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    casting_db.app = app
    casting_db.init_app(app)
    casting_db.create_all()

# It can be used to drop existing tables and create a new database


def db_drop_and_create_all():
    casting_db.drop_all()
    casting_db.create_all()


'''
Movies with titles and release dates
'''


class Movie(casting_db.Model):
    __tablename__ = 'movies'

    id = Column(Integer(), primary_key=True)
    movie_title = Column(String(150), nullable=False)
    movie_release_date = Column(String(50), nullable=False)

    def __init__(self, title, release_date):
        self.movie_title = title
        self.movie_release_date = release_date

    def insert(self):
        casting_db.session.add(self)
        casting_db.session.commit()

    def update(self):
        casting_db.session.commit()

    def delete(self):
        casting_db.session.delete(self)
        casting_db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title': self.movie_title,
            'release_date': self.movie_release_date
        }


'''
Actors with name, age and gender
'''


class Actor(casting_db.Model):
    __tablename__ = 'actors'

    id = Column(Integer(), primary_key=True)
    name = Column(String(100), nullable=False)
    age = Column(String(2), nullable=False)
    gender = Column(String(10), nullable=False)

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def insert(self):
        casting_db.session.add(self)
        casting_db.session.commit()

    def update(self):
        casting_db.session.commit()

    def delete(self):
        casting_db.session.delete(self)
        casting_db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender
        }
