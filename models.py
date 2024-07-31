from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Song(Base):
    __tablename__ = 'songs'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    artist = Column(String, index=True)
    album = Column(String, nullable=True)
    genre = Column(String, nullable=True)
    mood_tags = Column(String, nullable=True)
    duration = Column(Integer, nullable=True)
    album_art_url = Column(String, nullable=True)
