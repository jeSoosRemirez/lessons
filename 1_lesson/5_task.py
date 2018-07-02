distance = int(input('Введіть відстань між сусідніми будинками(метри): '))
price_per_one = int(input('Введіть ціну кабалю за метр: '))
num_of_houses = int(input('Введіть к-ть будинків: '))

length = (distance * num_of_houses)
price = (price_per_one * length)

print(f'Довжина провода: {length} метрів')
print(f'Ціна: {price}')
