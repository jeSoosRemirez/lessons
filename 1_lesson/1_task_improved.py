want_sleep_hours = int(input('Скільки годин ви хочите спати: '))
want_sleep_minutes = int(input('А хвилин: '))
clock_hours = int(input('Котра година на вашому годиннику(лише години!): '))
clock_minutes = int(input('А хвилин: '))
hours = (want_sleep_hours + clock_hours)
minutes = (want_sleep_minutes + clock_minutes)

if hours >= 23:
    alarm_hours = (clock_hours + 1)
    alarm_minutes = (60 - minutes)
    if minutes > 60:
        if minutes == 120:
            alarm_hours = (want_sleep_hours + 1)
        elif minutes == 60:
            alarm_hours = want_sleep_hours
else:
    print('Чому так пізно!')
print(f'{alarm_hours} год і {alarm_minutes} хв')
