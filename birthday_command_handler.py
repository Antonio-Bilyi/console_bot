from decorator import input_error
from addressbook import AddressBook
from colorama import Fore, Style

@input_error
def add_birthday(args, book: AddressBook):
    if len(args) < 2:

        raise ValueError(f'{Fore.YELLOW}[WARNING]: Please give me name and birthday!{Style.RESET_ALL}')
    
    name, birthday, *_ = args
    element = book.find(name)

    element.add_birthday(birthday)

    return f'{Fore.GREEN}[SUCCESS]: Birthday added for {name}{Style.RESET_ALL}'

@input_error
def show_birthday(args, book: AddressBook):
    name, *_ = args
    element = book.find(name)

    if element:
        if element.birthday:

            return f"{Fore.BLUE}[INFO]: {name}'s birthday is {element.birthday.value}{Style.RESET_ALL}"
        
        else:

            return f"{Fore.BLUE}[INFO]: Contact {name} doesn't have a birthday set{Style.RESET_ALL}"

@input_error
def birthdays(book: AddressBook):
    upcoming_birthdays = book.get_upcoming_birthday()

    if not upcoming_birthdays:

        return f'{Fore.BLUE}[INFO]: No upcoming birthdays{Style.RESET_ALL}'
    
    result = []
    for el in upcoming_birthdays:
        result.append(f"{Fore.BLUE}{el['name']}{Style.RESET_ALL}: {Fore.WHITE}{el['congratulation_date']}{Style.RESET_ALL}")
    
    return '\n'.join(result)