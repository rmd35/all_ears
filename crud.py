from sqlalchemy.orm import Session
import models, schemas
from external_api import fetch_search_results, fetch_track_details

# Song CRUD Operations
def get_songs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Song).offset(skip).limit(limit).all()

def get_song(db: Session, song_id: int):
    return db.query(models.Song).filter(models.Song.id == song_id).first()

def create_song(db: Session, song: schemas.SongCreate):
    db_song = models.Song(**song.dict())
    db.add(db_song)
    db.commit()
    db.refresh(db_song)
    return db_song

def update_song(db: Session, song_id: int, song: schemas.SongCreate):
    db_song = get_song(db, song_id)
    if db_song:
        for key, value in song.dict().items():
            setattr(db_song, key, value)
        db.commit()
        db.refresh(db_song)
        return db_song
    return None

def delete_song(db: Session, song_id: int):
    db_song = get_song(db, song_id)
    if db_song:
        db.delete(db_song)
        db.commit()
        return db_song
    return None

# Similar CRUD functions for Rating, Review, Tag, and SongTag

# Rating CRUD Operations
def get_ratings(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Rating).offset(skip).limit(limit).all()

def get_rating(db: Session, rating_id: int):
    return db.query(models.Rating).filter(models.Rating.id == rating_id).first()

def create_rating(db: Session, rating: schemas.RatingCreate):
    db_rating = models.Rating(**rating.dict())
    db.add(db_rating)
    db.commit()
    db.refresh(db_rating)
    return db_rating

def update_rating(db: Session, rating_id: int, rating: schemas.RatingCreate):
    db_rating = get_rating(db, rating_id)
    if db_rating:
        for key, value in rating.dict().items():
            setattr(db_rating, key, value)
        db.commit()
        db.refresh(db_rating)
        return db_rating
    return None

def delete_rating(db: Session, rating_id: int):
    db_rating = get_rating(db, rating_id)
    if db_rating:
        db.delete(db_rating)
        db.commit()
        return db_rating
    return None

# Review CRUD Operations
def get_reviews(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Review).offset(skip).limit(limit).all()

def get_review(db: Session, review_id: int):
    return db.query(models.Review).filter(models.Review.id == review_id).first()

def create_review(db: Session, review: schemas.ReviewCreate):
    db_review = models.Review(**review.dict())
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review

def update_review(db: Session, review_id: int, review: schemas.ReviewCreate):
    db_review = get_review(db, review_id)
    if db_review:
        for key, value in review.dict().items():
            setattr(db_review, key, value)
        db.commit()
        db.refresh(db_review)
        return db_review
    return None

def delete_review(db: Session, review_id: int):
    db_review = get_review(db, review_id)
    if db_review:
        db.delete(db_review)
        db.commit()
        return db_review
    return None

# Tag CRUD Operations
def get_tags(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Tag).offset(skip).limit(limit).all()

def get_tag(db: Session, tag_id: int):
    return db.query(models.Tag).filter(models.Tag.id == tag_id).first()

def create_tag(db: Session, tag: schemas.TagCreate):
    db_tag = models.Tag(**tag.dict())
    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)
    return db_tag

def update_tag(db: Session, tag_id: int, tag: schemas.TagCreate):
    db_tag = get_tag(db, tag_id)
    if db_tag:
        for key, value in tag.dict().items():
            setattr(db_tag, key, value)
        db.commit()
        db.refresh(db_tag)
        return db_tag
    return None

def delete_tag(db: Session, tag_id: int):
    db_tag = get_tag(db, tag_id)
    if db_tag:
        db.delete(db_tag)
        db.commit()
        return db_tag
    return None
