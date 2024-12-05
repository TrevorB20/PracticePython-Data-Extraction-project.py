try:
    value = int(input('Enter A Integer: '))
    print('The inverse of', value,'is', 1/value)
except:
    print('You Selected an invalid Integer, so I will not be able to calculate the number')
    
try:
    value = int(input('Enter An Integer: '))
    print('The inverse of', value, 'is', 1/value)
except ValueError:
    print('You did not provide a number, so I will not calculate the inverse')
except ZeroDivisionError:
    print('You provided the number 0 and so this division by 0 is not possible, sorry')