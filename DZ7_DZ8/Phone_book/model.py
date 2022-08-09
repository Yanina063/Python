
import uuid


class Person:

    def __init__(self, **entries):
        self.id = str(uuid.uuid4())
        self.name = ''    # имя человека
        self.surname = ''        # фамилия человека
        self.phone = ''
        self.comment = ''
        if not (entries is None):
            self.__dict__.update(entries)

    def keys(self):
        return vars(self).keys()

    def to_dict(self):
        return vars(self)

    def print(self):
        print(
            f'\nid: {self.id}'
            f'\nname: {self.name}'
            f'\nsurname: {self.surname}'
            f'\nphone: {self.phone}'
            f'\ncomment: {self.comment}')
        print('\n--------------------------------------------------------------------------------------------------')
