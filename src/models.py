import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    appearances = Column(String(250), nullable=False)

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    appearances = Column(String(250), nullable=False)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    appearances = Column(String(250), nullable=False)

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
   

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    favorites = relationship('Favorites', backref='user')

def to_dict(self):
    return {}

# Draw ER diagram
render_er(Base, 'diagram.png')
