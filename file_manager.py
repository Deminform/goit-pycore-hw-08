from adress_book import AddressBook
import pickle
from abc import ABC, abstractmethod


class BaseFileManager(ABC):
    @staticmethod
    @abstractmethod
    def save(book, filename):
        pass

    @staticmethod
    @abstractmethod
    def load(filename):
        pass


class PickleFileManager(BaseFileManager):
    @staticmethod
    def save(book: AddressBook, filename):
        with open(filename, "wb") as file:
            pickle.dump(book, file)

    @staticmethod
    def load(filename) -> AddressBook:
        with open(filename, "rb") as file:
            return pickle.load(file)
