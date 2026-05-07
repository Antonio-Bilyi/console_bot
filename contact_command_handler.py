from decorator import input_error
from addressbook import AddressBook
from record import Record
from colorama import Fore, Style

@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    element = book.find(name)
    message = f'{Fore.GREEN}[SUCCESS]: Contact updated{Style.RESET_ALL}'

    if element is None:
        element = Record(name)
        book.add_record(element)
        message = f'{Fore.GREEN}[SUCCESS]: Contact added{Style.RESET_ALL}'
    
    if phone:
        element.add_phone(phone)
    
    return message

@input_error
def change_contact(args, book: AddressBook):
    name, old_phone, new_phone = args
    element = book.find(name)

    element.edit_phone(old_phone, new_phone)

    return f'{Fore.GREEN}[SUCCESS]: Phone for contact {name} has changed{Style.RESET_ALL}'

@input_error
def show_contacts(args, book: AddressBook):
    name, *_ = args
    element = book.find(name)

    phones = '; '.join(el.value for el in element.phones)

    return f'{Fore.BLUE}[INFO]: Contact {name} has phone number(s) {phones}{Style.RESET_ALL}'

@input_error
def all_contacts(book: AddressBook):

    return '\n'.join(
        f"{Fore.BLUE}{str(element)}{Style.RESET_ALL}"
        for element in book.data.values()
    )