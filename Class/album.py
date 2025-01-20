import uuid
from .exception import InvalidPriceError
from .decorators import timer, counter

class Album:
    def __init__(self, title="Unknown", artist="Unknown", year=0, price=0.0):
        self.__id = uuid.uuid4()
        self.__title = title
        self.__artist = artist
        self.__year = year
        self.__price = price

    @property
    def id(self):
        return self.__id

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def artist(self):
        return self.__artist

    @artist.setter
    def artist(self, artist):
        self.__artist = artist

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        self.__year = year

    @property
    @timer
    @counter
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price < 0:
            raise InvalidPriceError("Негативная цена не принимается, уйди")
        self.__price = price

    def __str__(self):
        return f"Альбом(ID: {self.id}, Название: {self.title}, Артист: {self.artist}, Год: {self.year}, Цена: {self.price})"

    @timer
    @counter
    def __add__(self, other):
        if isinstance(other, Album):
            return self.price + other.price
        raise TypeError("неа")

    @timer
    @counter
    def __sub__(self, other):
        if isinstance(other, Album):
            return self.price - other.price
        raise TypeError("Неа")

    @timer
    @counter
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return self.price * other
        raise TypeError("Циферки, не надо другого")

    @timer
    @counter
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return self.price / other
        raise TypeError("Циферки, не надо другого")
