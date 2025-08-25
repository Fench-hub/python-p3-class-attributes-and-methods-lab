class Song:
    
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Increment song count
        self.add_song_to_count()

        # Add to lists
        self.genres.append(self.genre)
        self.artists.append(self.artist)

        # Update histograms incrementally
        self.add_to_genre_count(self.genre)
        self.add_to_artist_count(self.artist)

    @classmethod
    def add_song_to_count(cls):
        """Increments the total count of songs."""
        cls.count += 1

    @classmethod
    def add_to_genres(cls):
        """Adds unique genres to the genres list."""
        unique_genres = set(cls.genres)
        cls.genres = list(unique_genres)

    @classmethod
    def add_to_artists(cls):
        """Adds unique artists to the artists list."""
        unique_artists = set(cls.artists)
        cls.artists = list(unique_artists)

    @classmethod
    def add_to_genre_count(cls, genre):
        """Adds to the genre_count dictionary (histogram) incrementally."""
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1

    @classmethod
    def add_to_artist_count(cls, artist):
        """Adds to the artist_count dictionary (histogram) incrementally."""
        cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1

# Example Usage:
song1 = Song("99 Problems", "Jay-Z", "Rap")
song2 = Song("Bohemian Rhapsody", "Queen", "Rock")
song3 = Song("Stan", "Eminem", "Rap")
song4 = Song("Hey Ya!", "OutKast", "Hip Hop")
song5 = Song("Empire State of Mind", "Jay-Z", "Hip Hop")

print(f"Total songs created: {Song.count}")
print(f"Genre histogram: {Song.genre_count}")
print(f"Artist histogram: {Song.artist_count}")

# To demonstrate the unique list methods
Song.add_to_genres()
Song.add_to_artists()

print(f"\nUnique genres list: {Song.genres}")
print(f"Unique artists list: {Song.artists}")