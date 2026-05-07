from colorama import Fore, Style

def parser_input(user_input):
    try:
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()

        return cmd, *args
    
    except ValueError:

        return f'{Fore.RED}[ERROR]: Invalid data!{Style.RESET_ALL}'