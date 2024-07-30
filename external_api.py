import http.client
import json
import os
import logging
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve RapidAPI key from environment variables
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")

# Configure logging
logging.basicConfig(level=logging.INFO)

def search_songs(query):
    try:
        conn = http.client.HTTPSConnection("deezerdevs-deezer.p.rapidapi.com", timeout=10)
        headers = {
            'x-rapidapi-key': RAPIDAPI_KEY,
            'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com"
        }
        conn.request("GET", f"/search?q={query}", headers=headers)
        res = conn.getresponse()
        
        if res.status != 200:
            raise Exception(f"Error: {res.status} {res.reason}")
        
        data = res.read()
        response = json.loads(data.decode("utf-8"))
        
        if 'data' in response:
            logging.info(f"Successfully fetched search results for query: {query}")
            return response['data']
        else:
            logging.error("Unexpected response format.")
            return None
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return None

def get_song_details(song_id):
    try:
        conn = http.client.HTTPSConnection("deezerdevs-deezer.p.rapidapi.com", timeout=10)
        headers = {
            'x-rapidapi-key': RAPIDAPI_KEY,
            'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com"
        }
        conn.request("GET", f"/track/{song_id}", headers=headers)
        res = conn.getresponse()
        
        if res.status != 200:
            raise Exception(f"Error: {res.status} {res.reason}")
        
        data = res.read()
        response = json.loads(data.decode("utf-8"))
        
        logging.info(f"Successfully fetched details for song ID: {song_id}")
        return response
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return None
