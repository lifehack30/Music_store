from .album import Album
from .artist import Artist
from .customer import Customer

class MusicStore:
    def __init__(self):
        self.albums = []
        self.artists = []
        self.customers = []

    def add_album(self, title, artist_name, year, price):
        artist = next((a for a in self.artists if a.name == artist_name), None)
        if not artist:
            artist = Artist(name=artist_name)
            self.artists.append(artist)
        album = Album(title=title, artist=artist.name, year=year, price=price)
        self.albums.append(album)
        print(f"Album '{title}' added.")

    def update_album(self, title, new_title=None, new_year=None, new_price=None):
        album = next((a for a in self.albums if a.title == title), None)
        if album:
            if new_title:
                album.title = new_title
            if new_year:
                album.year = new_year
            if new_price:
                album.price = new_price
            print(f"Album '{title}' updated.")
        else:
            print(f"Album '{title}' not found.")

    def delete_album(self, title):
        album = next((a for a in self.albums if a.title == title), None)
        if album:
            self.albums.remove(album)
            print(f"Album '{title}' deleted.")
        else:
            print(f"Album '{title}' not found.")

    def list_albums(self):
        for album in self.albums:
            print(album)

    def add_artist(self, name, genre):
        artist = Artist(name=name, genre=genre)
        self.artists.append(artist)
        print(f"Artist '{name}' added.")

    def update_artist(self, name, new_name=None, new_genre=None):
        artist = next((a for a in self.artists if a.name == name), None)
        if artist:
            if new_name:
                artist.name = new_name
            if new_genre:
                artist.genre = new_genre
            print(f"Artist '{name}' updated.")
        else:
            print(f"Artist '{name}' not found.")

    def delete_artist(self, name):
        artist = next((a for a in self.artists if a.name == name), None)
        if artist:
            self.artists.remove(artist)
            print(f"Artist '{name}' deleted.")
        else:
            print(f"Artist '{name}' not found.")

    def list_artists(self):
        for artist in self.artists:
            print(artist)

    def add_customer(self, name, email):
        customer = Customer(name=name, email=email)
        self.customers.append(customer)
        print(f"Customer '{name}' added.")

    def update_customer(self, name, new_name=None, new_email=None):
        customer = next((c for c in self.customers if c.name == name), None)
        if customer:
            if new_name:
                customer.name = new_name
            if new_email:
                customer.email = new_email
            print(f"Customer '{name}' updated.")
        else:
            print(f"Customer '{name}' not found.")

    def delete_customer(self, name):
        customer = next((c for c in self.customers if c.name == name), None)
        if customer:
            self.customers.remove(customer)
            print(f"Customer '{name}' deleted.")
        else:
            print(f"Customer '{name}' not found.")

    def list_customers(self):
        for customer in self.customers:
            print(customer)