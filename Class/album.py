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
            raise InvalidPriceError("Price cannot be negative")
        self.__price = price

    def __str__(self):
        return f"Album(ID: {self.id}, Title: {self.title}, Artist: {self.artist}, Year: {self.year}, Price: {self.price})"

    @timer
    @counter
    def __add__(self, other):
        if isinstance(other, Album):
            return self.price + other.price
        raise TypeError("Operands must be instances of Album")

    @timer
    @counter
    def __sub__(self, other):
        if isinstance(other, Album):
            return self.price - other.price
        raise TypeError("Operands must be instances of Album")

    @timer
    @counter
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return self.price * other
        raise TypeError("Operand must be a number")

    @timer
    @counter
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return self.price / other
        raise TypeError("Operand must be a number")
