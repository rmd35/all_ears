from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine
from external_api import search_songs, get_song_details  # Import the external API functions

# Create the database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Song Endpoints
@app.post("/songs/", response_model=schemas.Song)
def create_song(song: schemas.SongCreate, db: Session = Depends(get_db)):
    return crud.create_song(db=db, song=song)

@app.get("/songs/", response_model=list[schemas.Song])
def read_songs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_songs(db, skip=skip, limit=limit)

@app.get("/songs/{song_id}", response_model=schemas.Song)
def read_song(song_id: int, db: Session = Depends(get_db)):
    db_song = crud.get_song(db, song_id=song_id)
    if db_song is None:
        raise HTTPException(status_code=404, detail="Song not found")
    return db_song

# Rating Endpoints
@app.post("/ratings/", response_model=schemas.Rating)
def create_rating(rating: schemas.RatingCreate, db: Session = Depends(get_db)):
    return crud.create_rating(db=db, rating=rating)

@app.get("/ratings/", response_model=list[schemas.Rating])
def read_ratings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_ratings(db, skip=skip, limit=limit)

@app.get("/ratings/{rating_id}", response_model=schemas.Rating)
def read_rating(rating_id: int, db: Session = Depends(get_db)):
    db_rating = crud.get_rating(db, rating_id=rating_id)
    if db_rating is None:
        raise HTTPException(status_code=404, detail="Rating not found")
    return db_rating

# Review Endpoints
@app.post("/reviews/", response_model=schemas.Review)
def create_review(review: schemas.ReviewCreate, db: Session = Depends(get_db)):
    return crud.create_review(db=db, review=review)

@app.get("/reviews/", response_model=list[schemas.Review])
def read_reviews(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_reviews(db, skip=skip, limit=limit)

@app.get("/reviews/{review_id}", response_model=schemas.Review)
def read_review(review_id: int, db: Session = Depends(get_db)):
    db_review = crud.get_review(db, review_id=review_id)
    if db_review is None:
        raise HTTPException(status_code=404, detail="Review not found")
    return db_review

# Tag Endpoints
@app.post("/tags/", response_model=schemas.Tag)
def create_tag(tag: schemas.TagCreate, db: Session = Depends(get_db)):
    return crud.create_tag(db=db, tag=tag)

@app.get("/tags/", response_model=list[schemas.Tag])
def read_tags(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_tags(db, skip=skip, limit=limit)

@app.get("/tags/{tag_id}", response_model=schemas.Tag)
def read_tag(tag_id: int, db: Session = Depends(get_db)):
    db_tag = crud.get_tag(db, tag_id=tag_id)
    if db_tag is None:
        raise HTTPException(status_code=404, detail="Tag not found")
    return db_tag

# SongTag Endpoints
@app.post("/song_tags/", response_model=schemas.SongTag)
def create_song_tag(song_tag: schemas.SongTagCreate, db: Session = Depends(get_db)):
    return crud.create_song_tag(db=db, song_tag=song_tag)

@app.get("/song_tags/", response_model=list[schemas.SongTag])
def read_song_tags(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_song_tags(db, skip=skip, limit=limit)

@app.get("/song_tags/{song_tag_id}", response_model=schemas.SongTag)
def read_song_tag(song_tag_id: int, db: Session = Depends(get_db)):
    db_song_tag = crud.get_song_tag(db, song_tag_id=song_tag_id)
    if db_song_tag is None:
        raise HTTPException(status_code=404, detail="SongTag not found")
    return db_song_tag

# External API Endpoints
@app.get("/search_songs/{query}")
def search_songs_endpoint(query: str):
    return search_songs(query)

@app.get("/song_details/{song_id}")
def get_song_details_endpoint(song_id: int):
    return get_song_details(song_id)
