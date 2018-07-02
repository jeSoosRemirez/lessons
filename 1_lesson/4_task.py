while True:
    number = input('Введіть 6 цифр: ')
    if len(number) > 6 or len(number) < 6:
        print('Забагато або замало цифр')
        continue
    sum_num1 = sum([int(num) for num in number[0:3]])
    # The same as 4 line!
    # my_list = []
    # for num in num1:
    #     my_list.append(int(num))
    # my_list_1 = sum(my_list)

    sum_num2 = sum([int(num) for num in number[3:7]])
    # The same as 11 line!
    # my_list = []
    # for num in num2:
    #     my_list.append(int(num))
    # sum_num2 = sum(my_list)
    if sum_num1 == sum_num2:
        print('Мої вітання! Сьогодні вам пощастило!')
        break
    else:
        print('Не фортануло):')
        break

[1, 2, 3].append(4)
