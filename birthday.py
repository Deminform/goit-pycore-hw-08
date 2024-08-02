import re
from datetime import datetime, date, timedelta
from field import Field


class Birthday(Field):

    def __init__(self, value):
        try:
            value = datetime.strptime(value, '%d.%m.%Y')
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

        super().__init__(value.date().strftime('%d.%m.%Y'))
