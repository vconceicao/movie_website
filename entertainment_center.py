import media
import fresh_tomatoes


# We created an instance of the movie class
# for each movie that We like.

avengers = media.Movie(
    "Avengers",
    "The super heroes get together to defeat Loki the God of Lie",
    "https://static.tvtropes.org/pmwiki/pub/images/the_avengers_7.jpg",
    "https://www.youtube.com/watch?v=E-84FIZ8-Ow")

avatar = media.Movie(
    "Avatar",
    "A marine on an alien planet",
    "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
    "http://www.youtube.com/watch?v=-9ceBgWV8io")

inception = media.Movie(
    "Inception",
    "A movie about dream stealers",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTIJhOc_s0d3e-8RfCAyDEw6H6BWL5e0v0giL7P8tusShbYInyH",  # noqa
    "https://www.youtube.com/watch?v=8hP9D6kZseM")

readyplayerone = media.Movie(
    "Ready Player One",
    "A movie about VR",
    "https://cdn.traileraddict.com/content/warner-bros-pictures/ready-player-one-poster-6.jpg",  # noqa
    "https://www.youtube.com/watch?v=LiK2fhOY0nE")

thedarkknight = media.Movie(
    "The Dark Knight",
    "Batman movie",
    "https://images-na.ssl-images-amazon.com/images/I/41I2BvAEvIL.jpg",
    "https://www.youtube.com/watch?v=kmJLuwP3MbY")

madmax = media.Movie(
    "Mad Max: Fury Road",
    "A guy trying to find plains of silence",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSXl8Xr_djMWV7FvnYuiPUf1Dq3J9tYSARuBaKro0bejnZ93C1n",  # noqa
    "https://www.youtube.com/watch?v=hEJnMQG9ev8")

# A list of the your favourite movies
movies = [avengers, avatar, inception, readyplayerone, thedarkknight, madmax]


# This function will take in your list of movies and generate an HTML file
# including this content, producing a website to showcase your favorite
# movies.
fresh_tomatoes.open_movies_page(movies)
