import sys

user_name = input('What is your name? ')
if user_name == '':
    print('Empty name? That is an invalid response, I am closing the program BYE!')
    sys.exit()
print('Hello,', user_name)
print('Let us get started...')
