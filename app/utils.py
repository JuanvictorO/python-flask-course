from enum import Enum

class MovieProperty(Enum):
    POPULAR = 'popular'
    KIDS = 'kids'
    YEAR_2020 = '2020'
    DRAMA = 'drama'
    TOM_CRUISE = 'tom_cruise'

URLS = {
    MovieProperty.POPULAR: "https://api.themoviedb.org/3/movie/popular?",
    MovieProperty.KIDS: "https://api.themoviedb.org/3/discover/movie?certification_country=US&certification.lte=G&sort_by=popularity.desc&",
    MovieProperty.YEAR_2020: "https://api.themoviedb.org/3/discover/movie?primary_release_year=2020&sort_by=vote_average.desc&",
    MovieProperty.DRAMA: "https://api.themoviedb.org/3/discover/movie?with_genres=18&sort_by=vote_average.desc&vote_count.gte=10&",
    MovieProperty.TOM_CRUISE: "https://api.themoviedb.org/3/discover/movie?with_genres=878&with_cast=500&sort_by=vote_average.desc&"
}

def get_movie_url(property: MovieProperty, api_key: str) -> str:
    try:
        movie_property = MovieProperty(property)
        url = URLS[movie_property]
        return f"{url}api_key={api_key}&language=pt-BR"
    except ValueError:
        raise ValueError(f"Invalid property: {property}")