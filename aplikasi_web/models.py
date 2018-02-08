from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String

database = SQLAlchemy()

class Page(database.Model):
    __tablename__ = 'Page'
    id = Column(Integer, primary_key=True)
    title = Column(String)

class Posting(database.Model):
    __tablename__ = 'Posting'
    id = Column(Integer, primary_key=True)
    title = Column(String)