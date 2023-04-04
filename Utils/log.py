from colorama import Fore, Style, init
import datetime

init(autoreset=True)


def log(log_txt):
    print(Fore.YELLOW + Style.BRIGHT + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ": ", end='')
    print(log_txt, end='.. ')


def single_log(log_txt):
    print(Fore.YELLOW + Style.BRIGHT + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ": ", end='')
    print(log_txt, end='..\n')


def done_log():
    print(Fore.GREEN + Style.BRIGHT + 'Done')


def failed_log():
    print(Fore.RED + Style.BRIGHT + log_txt)


def tqdm_desc(desc):
    return Fore.YELLOW + Style.BRIGHT + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ": " + Style.RESET_ALL + desc
