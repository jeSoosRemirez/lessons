def bank(a, years):
    a = float(input('Money: '))
    years = float(input('Years: '))
    while years != 0:
        a += a * 0.1
        years = years - 1
    return a


print(bank(100, 1))
