from collections import UserDict
from record import Record
from datetime import datetime, timedelta
from colorama import Fore, Style

class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record
    
    def find(self, name):

        return self.data.get(name)
    
    def delete(self, name):
        if name in self.data:
            self.data.pop(name)
    
    def get_upcoming_birthday(self, days=7):
        upcoming_birthdays = []

        today = datetime.today().date()

        for element in self.data.values():
            if not element.birthday:
                continue
        
            birthday_date = datetime.strptime(element.birthday.value, '%d.%m.%Y').date()
            birthday_this_year = birthday_date.replace(year=today.year)

            if birthday_this_year < today:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
            if 0 <= (birthday_this_year - today).days <= days:
                congratulation_date = birthday_this_year

                weekday = congratulation_date.weekday()

                if weekday == 5:
                    congratulation_date += timedelta(days=2)
            
                elif weekday == 6:
                    congratulation_date += timedelta(days=1)
            
                upcoming_birthdays.append({
                    'name': element.name.value,
                    'congratulation_date': congratulation_date.strftime('%d.%m.%Y')
                })
    
        return upcoming_birthdays
    
    def __str__(self):
        
        return '\n'.join(
        f"{Fore.BLUE}{str(element)}{Style.RESET_ALL}"
        for element in self.data.values()
    )