import re
from base_field import Field, Validate


class Phone(Field, Validate):
    def __init__(self, value):
        self.__validate(value)
        super().__init__(value)

    def __validate(self, value):
        if not re.match(r'^\d{10}$', value):
            raise ValueError("Phone number not added! Invalid phone number. Must contain 10 digits.")

    def __str__(self):
        return self._value
