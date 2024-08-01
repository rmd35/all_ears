# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI()

# Review model
class ReviewCreate(BaseModel):
    song_id: int
    review: str

def get_db_connection():
    conn = sqlite3.connect('reviews.db') 
    return conn

@app.post("/reviews/")
async def create_review(review: ReviewCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO reviews (song_id, review) VALUES (?, ?)",
                   (review.song_id, review.review))
    conn.commit()
    conn.close()
    return {"message": "Review added successfully"}

@app.get("/reviews/{song_id}")
async def get_reviews(song_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reviews WHERE song_id=?", (song_id,))
    reviews = cursor.fetchall()
    conn.close()
    return {"reviews": reviews}
