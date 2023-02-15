import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True)
    username = Column(String(80), nullable=False, unique=True)
    firstname = Column(String(80), nullable=False)
    lastname = Column(String(80), nullable=False)
    email = Column(String(250), nullable=False, unique=True)
    created = Column(String(250))
    

class Post(Base):
    __tablename__ = 'post'
    post_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    comment = Column(String(250),ForeignKey('user.user_id'))
    created = Column(String(250))
    total_likes = Column(Integer)

class Comentarios(Base):
    __tablename__ = 'comentarios'
    comment_id = Column(Integer, primary_key=True)
    author_comment_id = Column(Integer, ForeignKey('user.user_id'))
    text = Column(String(250))
    post_id = Column(Integer, ForeignKey('post.post_id'))

class Media(Base):
    __tablename__ = 'media'
    media_id = Column(Integer, primary_key=True)
    tipo = Column(String(250))
    url = Column(String(250))
    post_id = Column(Integer, ForeignKey('post.post_id'))


class Likes(Base):
    __tablename__ = 'likes'
    like_id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.post_id'))
    user_like_id = Column(Integer, ForeignKey('user.user_id'))
   
    def to_dict(self):
        return {}


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
