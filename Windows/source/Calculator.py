num1 = input('Enter 1st number: ')
num2 = input('Enter 2nd number: ')
operation = input('Enter + for addition, - for subtraction, * for multiplication, or / for division: ')
num1 = int(num1)
num2 = int(num2)

if operation == '+':
    sum = (num1 + num2)
    print(num1, operation, num2, '=', sum)

elif operation == '-':
    difference = (num1 - num2)
    print(num1, operation, num2, '=', difference)

elif operation == '*':
    product = (num1 * num2)
    print(num1, operation, num2, '=', product)

elif operation == '/':
    quotient = (num1 / num2)
    print(num1, operation, num2, '=', quotient)

else:
    print('Invalid operation. Please re-run the program')
