from pydantic import BaseModel, Field
from typing import Optional

# Song Models
class SongBase(BaseModel):
    title: str = Field(..., max_length=100)
    artist: str = Field(..., max_length=100)
    album: Optional[str] = Field(None, max_length=100)
    genre: Optional[str] = Field(None, max_length=50)
    mood_tags: Optional[str] = Field(None, max_length=100)
    release_date: Optional[str] = Field(None, pattern=r'^\d{4}-\d{2}-\d{2}$')  # Updated from `regex` to `pattern`
    duration: Optional[int] = Field(None, gt=0)
    album_art_url: Optional[str] = Field(None, max_length=200)

class SongCreate(SongBase):
    pass

class Song(SongBase):
    id: int

    class Config:
        orm_mode = True

# Rating Models
class RatingBase(BaseModel):
    song_id: int
    rating: int = Field(..., ge=1, le=5)

class RatingCreate(RatingBase):
    pass

class Rating(RatingBase):
    id: int

    class Config:
        orm_mode = True

# Review Models
class ReviewBase(BaseModel):
    song_id: int
    review: str = Field(..., max_length=500)

class ReviewCreate(ReviewBase):
    pass

class Review(ReviewBase):
    id: int

    class Config:
        orm_mode = True
