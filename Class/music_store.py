import os
import json
import uuid
from .album import Album
from .artist import Artist
from .customer import Customer

class MusicStore:
    def __init__(self):
        
        self.albums = []
        self.artists = []
        self.customers = []
        self.save_path = 'Save/'
        self.load_data()

    def save_data(self):
        self.save_albums()
        self.save_artists()
        self.save_customers()

    def load_data(self):
        self.load_albums()
        self.load_artists()
        self.load_customers()

    def save_albums(self):
        with open(os.path.join(self.save_path, 'albums.json'), 'w') as f:
            albums_data = [album.__dict__ for album in self.albums]
            json.dump(albums_data, f, indent=4, default=self.serialize_uuid)

    def load_albums(self):
        if os.path.exists(os.path.join(self.save_path, 'albums.json')):
            with open(os.path.join(self.save_path, 'albums.json'), 'r') as f:
                albums_data = json.load(f)
                for album_data in albums_data:
                    album = Album(
                        title=album_data['_Album__title'],
                        artist=album_data['_Album__artist'],
                        year=album_data['_Album__year'],
                        price=album_data['_Album__price']
                    )
                    album.__id = uuid.UUID(album_data['_Album__id'])
                    self.albums.append(album)

    def save_artists(self):
        with open(os.path.join(self.save_path, 'artists.json'), 'w') as f:
            artists_data = [artist.__dict__ for artist in self.artists]
            json.dump(artists_data, f, indent=4, default=self.serialize_uuid)

    def load_artists(self):
        if os.path.exists(os.path.join(self.save_path, 'artists.json')):
            with open(os.path.join(self.save_path, 'artists.json'), 'r') as f:
                artists_data = json.load(f)
                for artist_data in artists_data:
                    artist = Artist(
                        name=artist_data['_Artist__name'],
                        genre=artist_data['_Artist__genre']
                    )
                    artist.__id = uuid.UUID(artist_data['_Artist__id'])
                    self.artists.append(artist)

    def save_customers(self):
        with open(os.path.join(self.save_path, 'customers.json'), 'w') as f:
            customers_data = [customer.__dict__ for customer in self.customers]
            json.dump(customers_data, f, indent=4, default=self.serialize_uuid)

    def load_customers(self):
        if os.path.exists(os.path.join(self.save_path, 'customers.json')):
            with open(os.path.join(self.save_path, 'customers.json'), 'r') as f:
                customers_data = json.load(f)
                for customer_data in customers_data:
                    customer = Customer(
                        name=customer_data['_Customer__name'],
                        email=customer_data['_Customer__email']
                    )
                    customer.__id = uuid.UUID(customer_data['_Customer__id'])
                    self.customers.append(customer)

    def serialize_uuid(self, obj):
        if isinstance(obj, uuid.UUID):
            return str(obj)
        raise TypeError(f"Type {type(obj)} not serializable")

    def add_album(self, title, artist_name, year, price):
        artist = next((a for a in self.artists if a.name == artist_name), None)
        if not artist:
            artist = Artist(name=artist_name)
            self.artists.append(artist)
        album = Album(title=title, artist=artist.name, year=year, price=price)
        self.albums.append(album)
        self.save_data()
        print(f"Альбом '{title}' добавлен.")

    def update_album(self, title, new_title=None, new_year=None, new_price=None):
        album = next((a for a in self.albums if a.title == title), None)
        if album:
            if new_title:
                album.title = new_title
            if new_year:
                album.year = new_year
            if new_price:
                album.price = new_price
            self.save_data()
            print(f"Альбом '{title}' изменен.")
        else:
            print(f"Альбом '{title}' не найден.")

    def delete_album(self, title):
        album = next((a for a in self.albums if a.title == title), None)
        if album:
            self.albums.remove(album)
            self.save_data()
            print(f"Альбом '{title}' удален.")
        else:
            print(f"Альбом '{title}' не найден.")

    def list_albums(self):
        for album in self.albums:
            print(album)

    def add_artist(self, name, genre):
        artist = Artist(name=name, genre=genre)
        self.artists.append(artist)
        self.save_data()
        print(f"Артист '{name}' добавлен.")

    def update_artist(self, name, new_name=None, new_genre=None):
        artist = next((a for a in self.artists if a.name == name), None)
        if artist:
            if new_name:
                artist.name = new_name
            if new_genre:
                artist.genre = new_genre
            self.save_data()
            print(f"Артист '{name}' изменен.")
        else:
            print(f"Артист '{name}' не найден.")

    def delete_artist(self, name):
        artist = next((a for a in self.artists if a.name == name), None)
        if artist:
            self.artists.remove(artist)
            self.save_data()
            print(f"Артист '{name}' удален.")
        else:
            print(f"Артист '{name}' не найден.")

    def list_artists(self):
        for artist in self.artists:
            print(artist)

    def add_customer(self, name, email):
        customer = Customer(name=name, email=email)
        self.customers.append(customer)
        self.save_data()
        print(f"Клиент '{name}' добавлен.")

    def update_customer(self, name, new_name=None, new_email=None):
        customer = next((c for c in self.customers if c.name == name), None)
        if customer:
            if new_name:
                customer.name = new_name
            if new_email:
                customer.email = new_email
            self.save_data()
            print(f"Клиент '{name}' изменен.")
        else:
            print(f"Клиент '{name}' не найден.")

    def delete_customer(self, name):
        customer = next((c for c in self.customers if c.name == name), None)
        if customer:
            self.customers.remove(customer)
            self.save_data()
            print(f"Клиент '{name}' удален.")
        else:
            print(f"Клиент  '{name}' не найдет.")

    def list_customers(self):
        for customer in self.customers:
            print(customer)
