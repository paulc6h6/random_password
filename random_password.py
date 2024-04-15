import random

characters = "0123456789`~!@#$%^&*()-_=+[{]}|;:,<.>/?abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
password_lenght = int(input("Cate caratre doriti sa aiba parola ?"))
generate = []

for character in characters:
    generate.extend(random.sample(character, password_lenght))

finnal_password = "".join(generate)

print(f"Your password is : {finnal_password}")


