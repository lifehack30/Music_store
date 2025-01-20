import uuid
from .decorators import timer, counter

class Artist:
    def __init__(self, name="Unknown", genre="Unknown"):
        self.__id = uuid.uuid4()
        self.__name = name
        self.__genre = genre

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, genre):
        self.__genre = genre

    @timer
    @counter
    def __str__(self):
        return f"Артист(ID: {self.id}, ФИО: {self.name}, Пол: {self.genre})"
