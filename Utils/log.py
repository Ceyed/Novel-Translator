from colorama import Fore, Style, init
import datetime

init(autoreset=True)

def log(log_txt, end=False):
    if end == True:
        print(Fore.GREEN + Style.BRIGHT + log_txt)
    else:
        print(Fore.YELLOW + Style.BRIGHT + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ": ", end='')
        print(log_txt, end=' ')

