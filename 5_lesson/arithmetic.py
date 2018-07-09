def arithemic():
    operation = input(str(''))

    num_1 = input(float(''))
    num_2 = input(float(''))

    if operation == '+':
        res = num_1 + num_2
        print(f'{num_1} + {num_2} = {res}')
    elif operation == '-':
        res = num_1 - num_2
        print(f'{num_1} - {num_2} = {res}')
    elif operation == '*':
        res = num_1 * num_2
        print(f'{num_1} * {num_2} = {res}')
    elif operation == '/':
        res = num_1 / num_2
        print(f'{num_1} / {num_2} = {res}')
    elif operation == '//' or operation == '%':
        res = num_1 % num_2
        print(f'{num_1} % {num_2} = {res}')
    else:
        print('Error')


arithemic()

