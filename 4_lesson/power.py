def power(a, b):
    if b == 0:
        a = 1
        return a
    c = a
    while b != 1:
        a = a * c
        b = b - 1
    return a


val, p = map(int, input('Input num and power').split())
print(power(val, p))
