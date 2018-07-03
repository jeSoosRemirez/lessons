want_sleep_hours = int(input('Скільки годин ви хочите спати: '))
want_sleep_minutes = int(input('А хвилин: '))
clock_hours = int(input('Котра година на вашому годиннику(лише години!): '))
clock_minutes = int(input('А хвилин: '))
hours = (want_sleep_hours + clock_hours)
minutes = (want_sleep_minutes + clock_minutes)

alarm_hours = 0
alarm_minutes = 0

if clock_hours == 23:
    alarm_hours = want_sleep_hours - 1
elif hours > 23:
    alarm_hours = hours - 24
elif minutes < 60:
    alarm_minutes = minutes
elif minutes > 60:
    alarm_hours = alarm_hours + 1
    alarm_minutes = minutes - 60
elif minutes == 60:
    alarm_hours = alarm_hours + 1
    alarm_minutes = 0
print(f'Наведіть годинник на {alarm_hours} год і {alarm_minutes} хв')
