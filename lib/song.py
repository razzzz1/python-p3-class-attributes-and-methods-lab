class Song:
    genres = []
    artists = []
    artist_count = {}
    genre_count = {}
    count = 0
    def __init__(self,name,artist,genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.count += 1
        Song.genres.append(genre)
        Song.artists.append(artist)
        self.add_to_genre_count()
        self.add_to_artist_count()
        
    def song_genres(self):
        return self.genres
    def song_artists(self):
        return self.artists
    def add_to_genre_count(self):
        if self.genre in Song.genre_count:
            Song.genre_count[self.genre] += 1
        else:
            Song.genre_count[self.genre] = 1
    def add_to_artist_count(self):
        if self.artist in Song.artist_count:
            Song.artist_count[self.artist] += 1
        else:
            Song.artist_count[self.artist] = 1        


    pass
