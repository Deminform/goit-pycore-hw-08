from datetime import datetime
from base_field import Field, Validate


class Birthday(Field, Validate):
    def __init__(self, value):
        self.__validate(value)
        super().__init__(value)

    def __validate(self, value):
        try:
            datetime.strptime(value, '%d.%m.%Y')
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

    def __str__(self):
        return self._value
