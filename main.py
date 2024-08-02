from decorator import input_error
from adress_book import AddressBook
from record import Record
from colorama import Fore, init

init(autoreset=True)


@input_error
def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command in ["hi", "hello"]:
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))

        elif command == "change":
            print(change_phone(args, book))

        elif command == "phone":
            print(show_phone(args, book))

        elif command == "all":
            print(book)

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            print(book.get_upcoming_birthdays())

        else:
            print(Fore.YELLOW + "Invalid command.")


@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args: list, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = 'Contact updated'
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = 'Contact added'
    if phone:
        record.add_phone(phone)
    return message


@input_error
def change_phone(args: list, book: AddressBook):
    name, old_phone, new_phone, *_ = args
    record = book.find(name)
    record.edit_phone(old_phone, new_phone)
    return f'Phone changed from {old_phone} to {new_phone} for contact: {record.name.value}'


@input_error
def show_phone(args: list, book: AddressBook):
    name, *_ = args
    record = book.find(name)
    if record is None:
        raise ValueError(f'Record with name: "{name}" does not exist')
    return record.show_phones()


@input_error
def add_birthday(args: list, book: AddressBook):
    name, date_of_birth, *_ = args
    record = book.find(name)
    if record is None:
        raise ValueError(f'Record with name: {name} does not exist')

    if record.birthday is None:
        record.add_birthday(date_of_birth)
    else:
        raise ValueError(f'Record with name: {record.name.value} already has birthday')

    return 'Birthday added'


@input_error
def show_birthday(args: list, book: AddressBook):
    name, *_ = args
    record = book.find(name)
    if record is None:
        raise ValueError(f'Record with name: {name} does not exist')
    return record.show_birthday()


if __name__ == '__main__':
    main()
