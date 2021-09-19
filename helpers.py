from colorama import init, Fore 

def display( message,is_warning=False):
    if is_warning:
        print(Fore.RED + 'This is Warning')
        print(Fore.RED + message)
    else:
        print(Fore.GREEN + message)