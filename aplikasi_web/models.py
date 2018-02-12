from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String

database = SQLAlchemy()

class Page(database.Model):
    __tablename__ = 'Page'
    id = Column(Integer, primary_key=True)
    title = Column(String)

class Post(database.Model):
    __tablename__ = 'Post'
    id = Column(Integer, primary_key=True)
    title = Column(String)

