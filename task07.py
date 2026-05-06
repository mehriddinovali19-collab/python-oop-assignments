class Movie:

    def __init__(self, title: str, genre: str, duration: int, rating: float):
        self.title = title
        self.genre = genre
        self.duration = duration
        self.rating = rating

    def show_summary(self)-> None:
        print(f"{self.title} - {self.genre} janridagi film. Reyting: {self.rating}/ 10")
    
movie1 = Movie("Inception", "fantastika", 148, 8.8)

movie1.show_summary()