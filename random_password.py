import pyfiglet
import random
from colorama import Fore, Back, Style

title = "Password Generator"
ascii_art = pyfiglet.figlet_format(title)
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-_=+[{]}\|;:"

print(ascii_art)

while True:
    try:
        length = int(input("How long do you want the password to be ? ( Please enter only a number between 6 and 32 characters) :  "))
        if length < 6 or length > 32:
            print(Fore.RED + "Enter a password length between 6 and 32 characters" + Style.RESET_ALL)
            continue
        randomItems = random.choices(characters, k=length) 
        break
    except ValueError:
        print(Fore.RED + "Please enter a number !" + Style.RESET_ALL)
        continue

password = Back.BLACK +  Fore.MAGENTA + "Your password is :" + Fore.RED + "".join(randomItems) + Style.RESET_ALL

print(password)