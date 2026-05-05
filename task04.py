class Movie:
    def __init__(self, title: str, genre: str, duration: float, rating: float):
        self.t = title
        self.g = genre 
        self.d = duration
        self.r = rating

movie1 = Movie("Inception", "Sci-Fi", 148, 8.8)

print("Title:", movie1.t)
print("Genre:", movie1.g)
print("Duration:", movie1.d, "minutes")
print("Rating:", movie1.r)