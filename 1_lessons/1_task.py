x = int(input("Скільки хвилин ви хочете поспати: "))
h = int(input("Котра година на вашому годиннику(лише години!): "))
m = int(input("А скільки хвилин: "))
hsleep = (x // 60 + h)
if hsleep >= 23:
    sleeph = (24 - hsleep)
msleep = (x % 60 - sleeph + m)
if msleep >= 60:
    sleepm = ((msleep % 60))
    sleeph = (msleep // 60)
print(f'Вам потрібно навести будильник на {sleeph} год і {sleepm} хв')

#Ще не ГОТОВО!!!!!!!!!!!! ААААААААААААА
