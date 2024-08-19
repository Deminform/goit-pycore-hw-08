from base_field import Field, Validate


class Name(Field, Validate):
    def __init__(self, value):
        self._validate(value)
        super().__init__(value)

    def _validate(self, value):
        if not isinstance(value, str):
            raise TypeError('Value must be a string')

    def __str__(self):
        return self._value
