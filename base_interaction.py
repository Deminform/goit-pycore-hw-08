from abc import ABC, abstractmethod
from adress_book import AddressBook


class ContactReader(ABC):
    @abstractmethod
    def show_contacts(self):
        pass

    @abstractmethod
    def show_commands(self):
        pass

    @abstractmethod
    def show_birthday(self):
        pass

    @abstractmethod
    def show_upcoming_birthdays(self):
        pass

    @abstractmethod
    def show_phone(self):
        pass


class ContactManager(ABC):
    @abstractmethod
    def add_contact(self, name, phone_number):
        pass

    @abstractmethod
    def delete_contact(self, contact):
        pass

    @abstractmethod
    def update_phone(self, new_phone, old_phone):
        pass

    @abstractmethod
    def add_birthday(self, contact, birthday):
        pass

    @abstractmethod
    def save_data(self):
        pass

    @abstractmethod
    def load_data(self):
        pass
