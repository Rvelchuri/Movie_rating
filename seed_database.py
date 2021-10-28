from datetime import datetime
import os
from  random import choice,randint
import crud
import model
import server
import json

os.system("dropdb ratings")
os.system("createdb ratings")
model.connect_to_db(server.app)
model.db.create_all()

# Load movie data from JSON file
with open("data/movies.json") as f:
    movie_data = json.loads(f.read())

# Create movies, store them in list so we can use them
# to create fake ratings later
movies_in_db = []
for movie in movie_data:
    title, overview,poster_path = (movie["title"],movie["overview"], movie["poster_path"])
    release_date = datetime.strptime(movie["release_date"],"%Y-%m-%d" )

    # TODO: get the title, overview, and poster_path from the movie
    # dictionary. Then, get the release_date and convert it to a
    # datetime object with datetime.strptime
    
    # TODO: create a movie here and append it to movies_in_db
    add_movie = crud.create_movie(title, overview, release_date, poster_path)
    movies_in_db.append(add_movie)
