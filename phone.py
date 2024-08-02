from field import Field
import re


class Phone(Field):

    def __init__(self, value):
        """ Check if the number is correct """
        if not re.match(r'^\d{10}$', value):
            raise ValueError("Invalid phone number. Must contain 10 digits.")

        super().__init__(value)
