want_sleep = int(input('Скільки хвилин ви хочете поспати: '))
hours = int(input('Котра година на вашому годиннику(лише години!): '))
minutes = int(input('А скільки хвилин: '))
if hours == 23:
    wake_up_hours = ((want_sleep // 60) - 1)
    wake_up_minutes = (((want_sleep // 60) - (want_sleep / 60)) + minutes)
    if wake_up_minutes > 60:
        wake_up_hours = (wake_up_hours + (wake_up_minutes // 60))
        wake_up_minutes = ((wake_up_minutes // 60) - (wake_up_minutes / 60))
    print(f'Вам потрібно навести будильник на {int(wake_up_hours)}'
          f' годин і {int(wake_up_minutes)} хвилини')
elif hours >= 0 or hours >= 00:
    wake_up_hours = (want_sleep // 60)
    wake_up_minutes = ((want_sleep // 60) - (want_sleep / 60) + minutes)
    if wake_up_minutes > 60:
        wake_up_hours = (wake_up_hours + (wake_up_minutes // 60))
        wake_up_minutes = ((wake_up_minutes // 60) - (wake_up_minutes / 60))
    print(f'Вам потрібно навести будильник на {int(wake_up_hours)}'
          f' годин і {int(wake_up_minutes)} хвилини')
