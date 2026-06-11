import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies = pd.DataFrame({
    'title': [
        'Inception',
        'Interstellar',
        'The Dark Knight',
        'Avengers: Endgame',
        'Doctor Strange',
        'Titanic',
        'The Notebook',
        'La La Land'
    ],
    'genre': [
        'Sci-Fi Action',
        'Sci-Fi Drama',
        'Action Crime',
        'Action Superhero',
        'Sci-Fi Superhero',
        'Romance Drama',
        'Romance Drama',
        'Romance Musical'
    ]
})

# Convert genres into vectors
vectorizer = CountVectorizer()
genre_matrix = vectorizer.fit_transform(movies['genre'])

# Calculate similarity matrix
similarity = cosine_similarity(genre_matrix)

# Recommendation function
def recommend(movie_name):
    movie_name = movie_name.lower()

    if movie_name not in movies['title'].str.lower().values:
        print("Movie not found!")
        return

    index = movies[movies['title'].str.lower() == movie_name].index[0]

    scores = list(enumerate(similarity[index]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    print("\nRecommended Movies:\n")

    for movie in scores[1:6]:
        print(movies.iloc[movie[0]]['title'])


movie = input("Enter a movie you like: ")
recommend(movie)