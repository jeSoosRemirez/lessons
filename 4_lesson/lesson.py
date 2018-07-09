#try:    (.../0)
#except
#Модулі
#Як працює ord і chr
#map
#split

mass = [[0 for i in range(4)] for j in range(4)]
a = [i for i in range(5)]
a
b = [i * 2 for i in range(5)]
b
mass
for q in range(4):
    mass[q]




mass = [[i for j in range(3)]for i in range(3)]
mass
for q in range(3):
    mass[q]
mass[1]


#First

num = int(input('Input number: '))

    #Simple
#print('1 num', int(num-num%10000)//10000)
#print('2 num', int(num%num%1000)//1000)
#print('3 num', int(num%num%100)//100)
#print('4 num', int(num%num%10)//10)
#print('5 num', int(num%num%1)//1)

for i in range(5):
    print(i + 1,'num = ' num % (10**(5 - i)))//(10**(4 - i))

    #Improved

n = input('Input number: ')
for i in n:
    print(i)


#Second

x = input('Enter your letter: ')
x = ord(x) - 32
x = chr(x)
print(x)


def power(a, b):
    if b == 0:
        a = 1
        return a
    c = a
    while(b != 1):
        a = a * c
        b = b - 1
    return a
val, p = map(int, input('Input num and power').split(''))
print(power(val, p))
