class Song:
    count = 0
    genres = set()
    artists = set()
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        Song.count += 1

        if genre not in Song.genres:
            Song.genres.add(genre)
            Song.genre_count[genre] = 0
        Song.genre_count[genre] += 1

        if artist not in Song.artists:
            Song.artists.add(artist)
            Song.artist_count[artist] = 0
        Song.artist_count[artist] += 1
