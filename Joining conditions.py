user_age = int(input('What is your age? '))
user_country = input('What is your county?')

if not user_country == 'Germany' and user_age < 25 or \
    user_country == 'Germany' and user_age < 23:
        print('You do qualify!!')
else:
    print('You don\'t qualify')