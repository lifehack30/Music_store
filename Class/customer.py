import uuid
from .exception import InvalidEmailError
from .decorators import timer, counter

class Customer:
    def __init__(self, name="Unknown", email="unknown@example.com"):
        self.__id = uuid.uuid4()
        self.__name = name
        self.__email = email

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
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        if not self.is_valid_email(email):
            raise InvalidEmailError("Invalid email address")
        self.__email = email

    def is_valid_email(self, email):
        # Простая проверка на наличие @ и . в email
        return '@' in email and '.' in email

    @timer
    @counter
    def __str__(self):
        return f"Customer(ID: {self.id}, Name: {self.name}, Email: {self.email})"
