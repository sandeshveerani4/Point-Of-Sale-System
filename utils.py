from os import system, name


def clearShell():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
