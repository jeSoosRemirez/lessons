sleep_hours = int(input('Скільки годин ви спали сьогодні(лише години!): '))
sleep_minutes = int(input('А хвилин: '))
sleep = (sleep_hours * 60 + sleep_minutes)
if sleep == sleep in range(450, 500):
    print(f'Ви гарно виспалися!')
elif sleep < 450:
    need_sleep_hours = (60 * (7 - sleep_hours))
    minutes = (need_sleep_hours - sleep_minutes)
    print(f'Ви недоспали {minutes} хвилин!')
elif sleep > 500:
    need_sleep_hours = (60 * (8 - sleep_hours))
    minutes = (need_sleep_hours + sleep_minutes)
    print(f'Ви перспали на {minutes} хвилини!')
