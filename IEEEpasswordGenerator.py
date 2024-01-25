# This code is to create a tool that would generate different passwords
import random
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@$%^&*()#'
number = input('Amount of passwords you want: ')
number = int(number)
length = input('What do you want the length of your passwords to be: ')
length = int(length)
print('\nYour passwords are as follows: ')
for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)