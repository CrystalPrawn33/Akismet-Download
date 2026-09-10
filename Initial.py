class Movie:
    def __init__(self, title, genre, rating):
        self.title = title
        self.genre = genre
        self.rating = rating


class MovieCollection:
    def __init__(self):
        self.movies = []

    def add_movie(self, title, genre, rating):
        self.movies.append(Movie(title, genre, rating))

    def sort_by_rating(self):
        self.movies.sort(key=lambda movie: movie.rating, reverse=True)

    def get_average_rating(self):
        if not self.movies:
            return 0

        return sum(movie.rating for movie in self.movies) / len(self.movies)

    def print_report(self):
        print("Movie Collection")
        print("================")

        for movie in self.movies:
            print(
                f"{movie.title} | {movie.genre} | "
                f"Rating: {movie.rating:.1f}"
            )

        print("================")
        print(f"Average Rating: {self.get_average_rating():.2f}")


collection = MovieCollection()

collection.add_movie("Inception", "Sci-Fi", 8.8)
collection.add_movie("Interstellar", "Sci-Fi", 8.7)
collection.add_movie("The Green Mile", "Drama", 8.6)
collection.add_movie("Gladiator", "Action", 8.5)

collection.sort_by_rating()
collection.print_report()
