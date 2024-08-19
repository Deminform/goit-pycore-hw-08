from pathlib import Path
from base_interaction import ContactReader, ContactManager
from file_manager import PickleFileManager
from adress_book import AddressBook


class UserView(ContactManager, ContactReader):

    def __init__(self, filepath):
        self.filepath = filepath
        self.book = self.load_data()

    def save_data(self, book: AddressBook):
        PickleFileManager.save(self.book, self.filepath)

    def load_data(self) -> AddressBook:
        return PickleFileManager.load(self.filepath)

    def add_contact(self, contact):
        pass

    def delete_contact(self, contact):
        pass

    def update_phone(self, new_phone, old_phone):
        pass

    def add_birthday(self, contact, birthday):
        pass

    def show_contacts(self):
        print(self.book)

    def show_commands(self):
        pass

    def show_birthday(self):
        pass

    def show_upcoming_birthdays(self):
        pass

    def show_phone(self):
        pass


if __name__ == '__main__':
    path_file = Path('new_addressbook.pkl')
    # path_file.mkdir(parents=True, exist_ok=True)
    path_file.touch(exist_ok=True)
    new_user = UserView(path_file)
    new_user.show_contacts()
