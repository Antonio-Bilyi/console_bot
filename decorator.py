from functools import wraps
from colorama import Fore, Style

def input_error(func):
    @wraps(func)

    def inner(*args, **kwargs):
        try:

            return func(*args, **kwargs)
        
        except KeyError:

            return f'{Fore.RED}[ERROR]: Contact not found!{Style.RESET_ALL}'
        
        except ValueError:

            return f'{Fore.RED}[ERROR]: Invalid value!{Style.RESET_ALL}'
        
        except IndexError:

            return f'{Fore.YELLOW}[WARNING]: Please enter the argument for the command!{Style.RESET_ALL}'
        
        except AttributeError:

            return f'{Fore.RED}[ERROR]: Attribute Error!{Style.RESET_ALL}'
    
    return inner