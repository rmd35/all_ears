from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.types import Date, Text

from database import Base

class Song(Base):
    __tablename__ = "songs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    artist = Column(String, index=True)
    album = Column(String, nullable=True)
    genre = Column(String, nullable=True)
    mood_tags = Column(String, nullable=True)
    release_date = Column(Date, nullable=True)
    duration = Column(Integer, nullable=True)
    album_art_url = Column(String, nullable=True)

    ratings = relationship("Rating", back_populates="song")
    reviews = relationship("Review", back_populates="song")
    song_tags = relationship("SongTag", back_populates="song")

class Rating(Base):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key=True, index=True)
    song_id = Column(Integer, ForeignKey("songs.id"))
    rating = Column(Integer)

    song = relationship("Song", back_populates="ratings")

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    song_id = Column(Integer, ForeignKey("songs.id"))
    review = Column(Text)

    song = relationship("Song", back_populates="reviews")

class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True)

    song_tags = relationship("SongTag", back_populates="tag")

class SongTag(Base):
    __tablename__ = "song_tags"

    id = Column(Integer, primary_key=True, index=True)
    song_id = Column(Integer, ForeignKey("songs.id"))
    tag_id = Column(Integer, ForeignKey("tags.id"))

    song = relationship("Song", back_populates="song_tags")
    tag = relationship("Tag", back_populates="song_tags")
