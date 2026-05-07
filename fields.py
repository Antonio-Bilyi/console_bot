from datetime import datetime
from colorama import Fore, Style

class Field:
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        if value.isdigit() and len(value) == 10:
            super().__init__(value)
        
        else:

            raise ValueError(f'{Fore.RED}[ERROR]: Invalid phone number!{Style.RESET_ALL}')

class Birthday(Field):
    def __init__(self, value):
        try:
            datetime.strptime(value, '%d.%m.%Y')
            super().__init__(value)
        
        except ValueError:

            return f'{Fore.RED}[ERROR]: Invalid date format!{Style.RESET_ALL}'