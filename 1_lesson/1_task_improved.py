want_sleep = input('')
clock_hours = input('')
clock_minutes = input('')
if want_sleep % 60 == 0:
    if clock_hours + want_sleep == 23:
        alarm_hours = ((want_sleep % 60) - 1)
        alarm_minutes = clock_minutes
        print(f'{alarm_hours}{alarm_minutes}')