sleep_hours = int(input('Скільки годин ви спали сьогодні(лише години!): '))
sleep_minutes = int(input('А хвилин: '))
sleep = (sleep_hours * 60 + sleep_minutes)

if (sleep_hours == 7 and sleep_minutes >= 20) or (sleep_hours == 8 and sleep_minutes <= 20):
    print('Ви гарно виспались')
elif sleep_hours < 7:
    need_sleep_m = ((7 - sleep_hours) * 60 - sleep_minutes)
    print(f'Ви недоспали {need_sleep_m} хв')
elif sleep_hours > 8:
    need_sleep_m = ((sleep_hours - 8) * 60 - sleep_minutes)
    print(f'Ви переспали {need_sleep_m} хв')
elif sleep_hours == 7 and sleep_minutes < 20:
    need_sleep_m = 20 - sleep_minutes
    print(f'Ви недоспали {need_sleep_m} хв')
elif sleep_hours == 8 and sleep_minutes > 20:
    need_sleep_m = sleep_minutes - 20
    print(f'Ви переспали {need_sleep_m} хв')
