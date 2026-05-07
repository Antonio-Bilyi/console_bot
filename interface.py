from abc import ABC, abstractmethod
from colorama import Fore, Style

class Interface(ABC):
    @abstractmethod
    def display_message(self, message):
        pass

    @abstractmethod
    def display_contacts(self, book):
        pass

    @abstractmethod
    def display_help(self):
        pass

    @abstractmethod
    def get_user_input(self, user_input):
        pass

class ConsoleInterface(Interface):
    def display_message(self, message):
        print(message)
    
    def display_contacts(self, book):
        if not book.data:
            print(f'{Fore.BLUE}[INFO]: Address book is empty{Style.RESET_ALL}')
        
        else:
            print(f'{Fore.BLUE}\n--- All Contacts ---{Style.RESET_ALL}')
            for element in book.data.values():
                print(element)
            print(f'{Fore.BLUE}--------------------\n{Style.RESET_ALL}')
    
    def display_help(self):
        help_text = f"""{Fore.BLUE}
Available commands:
    - hello: Greet the bot
    - add [name] [phone]: Add or update contact
    - change [name] [old_phone] [new_phone]: Change contact's phone
    - phone [name]: Show contact phone(s)
    - all: Show all contacts
    - add-birthday [name] [date]: Add birthday for contact (DD.MM.YYYY)
    - show-birthday [name]: Show contact's birthday
    - birthdays: Show upcoming birthdays
    - close(exit): Save and exit the bot
    {Style.RESET_ALL}"""
        print(help_text)
    
    def get_user_input(self, user_input):
        return input(f'{user_input}: ')