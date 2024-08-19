from pathlib import Path
from base_interaction import ContactReader, ContactManager
from file_manager import PickleFileManager
from adress_book import AddressBook
from record import Record
from decorator import error_decorator


class UserView(ContactManager, ContactReader):

    def __init__(self, file_path):
        self.file_manager = PickleFileManager(file_path)
        # self.file_path = file_path
        self.book = self.load_data()

    @error_decorator
    def save_data(self):
        self.file_manager.save(self.book)

    @error_decorator
    def load_data(self) -> AddressBook:
        return self.file_manager.load()

    @error_decorator
    def add_contact(self, name, phone_number):
        record = self.book.find(name)
        message = 'Contact updated'
        if record is None:
            record = Record(name)
            record.add_phone(phone_number)
            self.book.add_record(record)
            message = 'Contact added'
            return message
        else:
            record.add_phone(phone_number)
        return message

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
    # path_file = Path('new_addressbook.pkl')
    # path_file.mkdir(parents=True, exist_ok=True)
    # path_file.touch(exist_ok=True)
    new_user = UserView('new_addressbook.pkl')
    new_user.add_contact('Serhii', '1111111111')
    new_user.show_contacts()

