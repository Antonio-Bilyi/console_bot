from addressbook import AddressBook
from birthday_command_handler import add_birthday, show_birthday, birthdays
from contact_command_handler import add_contact, change_contact, show_contacts, all_contacts
from input_parser import parser_input
from interface import ConsoleInterface
from serialize import save_data, load_data
from colorama import Fore, Style

def main():
    book = load_data()
    ui = ConsoleInterface()

    ui.display_message(f'{Fore.BLUE}Welcome to the assistant bot!{Style.RESET_ALL}')

    while True:
        user_input = ui.get_user_input(f'{Fore.BLUE}Enter a command: {Style.RESET_ALL}')

        if not user_input.strip():
            continue

        command, *args = parser_input(user_input)

        if command in ['close', 'exit']:
            save_data(book)
            ui.display_message(f'{Fore.BLUE}Good bye!{Style.RESET_ALL}')
            break

        elif command == 'hello':
            ui.display_message(f'{Fore.BLUE}How can i help you ?{Style.RESET_ALL}')
        
        elif command == 'help':
            ui.display_help()
        
        elif command == 'add':
            ui.display_message(add_contact(args, book))
        
        elif command == 'change':
            ui.display_message(change_contact(args, book))
        
        elif command == 'phone':
            ui.display_message(show_contacts(args, book))
        
        elif command == 'all':
            ui.display_contacts(book)
        
        elif command == 'add-birthday':
            ui.display_message(add_birthday(args, book))
        
        elif command == 'show-birthday':
            ui.display_message(show_birthday(args, book))
        
        elif command == 'birthdays':
            ui.display_message(birthdays(book))
        
        else:
            ui.display_message(f'{Fore.RED}[ERROR]: Invalid command!{Style.RESET_ALL}')

if __name__ == '__main__':
    main()