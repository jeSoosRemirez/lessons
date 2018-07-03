def calculate():
    operation = input('''
    Type operation:
    + for addition
    - for subtraction
    * for multiplication
    / for division
    ''')

    num_1 = int(input('Type first number: '))
    num_2 = int(input('Type second number: '))

    if operation == '+':
        summary = num_1 + num_2
        print(f'{num_1} + {num_2} = {summary}')
    elif operation == '-':
        summary = num_1 - num_2
        print(f'{num_1} - {num_2} = {summary}')
    elif operation == '*':
        summary = num_1 * num_2
        print(f'{num_1} * {num_2} = {summary}')
    elif operation == '/':
        summary = num_1 / num_2
        print(f'{num_1} / {num_2} = {summary}')


def again():
    calc_again = input('''
If you want continue calculate
type Y for Yes or N for No.
''')
    if calc_again.upper == 'Y':
        calculate()
    elif calc_again.upper == 'N':
        print('So long...')
    else:
        again()


calculate()
