import pyfiglet
import random
from colorama import Fore, Back, Style

text = "Password Generator"
ascii_art = pyfiglet.figlet_format(text)
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-_=+[{]}\|;:"

while True:
    try:
        length = int(input("How long do you want the password to be ? ( Please enter only a number ) :  "))
        if length < 6 or length > 32:
            print("Ce plm e cu parola asta")
            continue
        randomItems = random.choices(characters, k=length) 
        break
    except ValueError:
        print("Please enter a number !!!!")
        continue

password = Back.BLACK +  Fore.MAGENTA + "Your password is :" + Fore.RED + "".join(randomItems) + Style.RESET_ALL

print(ascii_art)
print(password)