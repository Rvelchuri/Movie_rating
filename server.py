
"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined




# Replace this with routes and view functions!
@app.route('/')
def homepage():
    return render_template('homepage.html')


@app.route('/movies')
def all_movies():
    """View all movies"""

    movies = crud.return_movie()
    return render_template("all_movies.html", movies = movies)

@app.route('/movies/<movie_id>')
def show_movie(movie_id):
    movie =crud.get_movie_by_id(movie_id)
    return render_template("movie_details.html",movie = movie)

@app.route('/users')
def all_users():
    """view all Users"""
    users = crud.return_user()
    return render_template("all_users.html", users=users)

@app.route('/users/<user_id>')
def show_user(user_id):
    user =crud.get_user_by_id(user_id)
    return render_template("user_details.html", user=user)

@app.route("/users", methods=["POST"])
def register_user():
   email = request.form.get("email")
   password = request.form.get("password")
   user = crud.get_user_by_email(email)

   if user:
       flash("Cannot create an account. Please try again.")
   else:
        crud.create_user(email, password)
        flash("Account was created successfully. Please log in.")
   return redirect("/")

@app.route("/login", methods=["POST"])
def log_in():
    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.login_user(email, password)
    if user:
        key = user.user_id
        session['key'] = key
        flash('Logged in!')
    else:
       flash("Try again")

    return redirect("/")

@app.route("/ratings/<movie_id>", methods=["POST"])
def user_rating(movie_id):
   rating = request.form.get("rating")
   rating = int(rating)
   movie = crud.get_movie_by_id(movie_id)
   key = session['key']
   user = crud.get_user_by_id(key)

   if 'key' in session:
        crud.create_rating(user, movie, rating)
        flash("Rating created")
   else:
        flash("Cannot create rating. Please log in.")
   return redirect(f"/movies/{movie_id}")

if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
