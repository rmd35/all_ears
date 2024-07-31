import requests

# Define the endpoint for inserting song data
url = "https://all-ears-flame.vercel.app/songs"

# Example mapping of image names to IDs
image_resource_ids = {
    "your_best_american_girl.png": 1,
    "paper_bag.png": 2,
    "black_none.png": 3,
    "was_ich_liebe.png": 4,
    "thebends.png": 5,
    "brat.png": 6,
    "whitelight.png": 7,
    "soldier.png": 8,
    "theblackparade.png": 9,
    "crystalcastlesii.png": 10,
    "twilight.png": 11,
    "borninwinter.png": 12,
    "the_beatles.png": 13,
    "linger.png": 14,
    "deathconciousness.png": 15,
    "celebrityskin.png": 16,
    "wish_u_were_here.png": 17,
    "visions.png": 18,
    "blond.png": 19,
    "hmhas.png": 20,
    "stairway_to_heaven.png": 21,
    "orion.png": 22,
    "a_forest.png": 23,
    "where_is_my_mind.png": 24,
    "li_beirut.png": 25,
    "forget_her.png": 26,
    "barrow.png": 27,
    "aliceinhell.png": 28,
    "preacher.png": 29,
    "sttims.png": 30
}

# Example song data
songs = [
    {"name": "Your Best American Girl", "artist": "Mitski", "image_resource_id": image_resource_ids["your_best_american_girl.png"]},
    {"name": "Paper Bag", "artist": "Fiona Apple", "image_resource_id": image_resource_ids["paper_bag.png"]},
    {"name": "Black No. 1", "artist": "Type O Negative", "image_resource_id": image_resource_ids["black_none.png"]},
    {"name": "Was ich liebe", "artist": "Rammstein", "image_resource_id": image_resource_ids["was_ich_liebe.png"]},
    {"name": "Black Star", "artist": "Radiohead", "image_resource_id": image_resource_ids["thebends.png"]},
    {"name": "Apple", "artist": "Charli XCX", "image_resource_id": image_resource_ids["brat.png"]},
    {"name": "Goth", "artist": "Sidewalks and Skeletons", "image_resource_id": image_resource_ids["whitelight.png"]},
    {"name": "Soldier of Fortune", "artist": "Opeth", "image_resource_id": image_resource_ids["soldier.png"]},
    {"name": "Welcome to the Black Parade", "artist": "My Chemical Romance", "image_resource_id": image_resource_ids["theblackparade.png"]},
    {"name": "Suffocation", "artist": "Crystal Castles", "image_resource_id": image_resource_ids["crystalcastlesii.png"]},
    {"name": "Duvet", "artist": "bôa", "image_resource_id": image_resource_ids["twilight.png"]},
    {"name": "Born in Winter", "artist": "Gojira", "image_resource_id": image_resource_ids["borninwinter.png"]},
    {"name": "Helter Skelter", "artist": "The Beatles", "image_resource_id": image_resource_ids["the_beatles.png"]},
    {"name": "Linger", "artist": "The Cranberries", "image_resource_id": image_resource_ids["linger.png"]},
    {"name": "Bloodhail", "artist": "Have A Nice Life", "image_resource_id": image_resource_ids["deathconciousness.png"]},
    {"name": "Petals", "artist": "Hole", "image_resource_id": image_resource_ids["celebrityskin.png"]},
    {"name": "Wish You Were Here", "artist": "Pink Floyd", "image_resource_id": image_resource_ids["wish_u_were_here.png"]},
    {"name": "Genesis", "artist": "Grimes", "image_resource_id": image_resource_ids["visions.png"]},
    {"name": "Pink + White", "artist": "Frank Ocean", "image_resource_id": image_resource_ids["blond.png"]},
    {"name": "CHIHIRO", "artist": "Billie Eilish", "image_resource_id": image_resource_ids["hmhas.png"]},
    {"name": "Stairway to Heaven", "artist": "Led Zeppelin", "image_resource_id": image_resource_ids["stairway_to_heaven.png"]},
    {"name": "Orion", "artist": "Metallica", "image_resource_id": image_resource_ids["orion.png"]},
    {"name": "A Forest", "artist": "The Cure", "image_resource_id": image_resource_ids["a_forest.png"]},
    {"name": "Where Is My Mind?", "artist": "Pixies", "image_resource_id": image_resource_ids["where_is_my_mind.png"]},
    {"name": "Li Beirut", "artist": "Fairouz", "image_resource_id": image_resource_ids["li_beirut.png"]},
    {"name": "Lover, You Should've Come Over", "artist": "Jeff Buckley", "image_resource_id": image_resource_ids["forget_her.png"]},
    {"name": "Sodus", "artist": "Cemeteries", "image_resource_id": image_resource_ids["barrow.png"]},
    {"name": "Schizos (Are Never Alone), Pts. I & II", "artist": "Annihilator", "image_resource_id": image_resource_ids["aliceinhell.png"]},
    {"name": "Family Tree", "artist": "Ethel Cain", "image_resource_id": image_resource_ids["preacher.png"]},
    {"name": "Fade Into You", "artist": "Mazzy Star", "image_resource_id": image_resource_ids["sttims.png"]}
]

# Function to insert song data into the database
def insert_songs(songs):
    for song in songs:
        response = requests.post(url, json=song)
        if response.status_code == 200:
            print(f"Successfully inserted {song['name']}")
        else:
            print(f"Failed to insert {song['name']}: {response.status_code}")

# Run the function
insert_songs(songs)
