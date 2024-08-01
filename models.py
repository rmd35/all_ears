from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

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
    reviews = relationship("Review", back_populates="song")

class Review(Base):
    __tablename__ = 'reviews'
    
    id = Column(Integer, primary_key=True, index=True)
    song_id = Column(Integer, ForeignKey('songs.id'), index=True)
    review = Column(String, nullable=False)
    song = relationship("Song", back_populates="reviews")
