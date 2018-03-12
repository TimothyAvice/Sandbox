"""
Timothy Avice Du Buisson
"""""
import string
count = 0

while True:
    user_name = input("Please enter your name: ")
    for char in user_name:
        if char.upper() in string.ascii_uppercase:
            count += 1
    if count != 0:
        print(user_name[::2])
        break
    else:
        print("Not valid input")
        continue
