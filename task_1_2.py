x=int(input("Введите первое число:"))
y=int(input("Введите второе чило:"))
a=(x+y)
b=(x-y)
c=(x*y)
d=(x/y)
f=(x//y)
z=a
if b>z:
    z=b
if c>z:
    z=c
if d>z:
    z=d
if f>z:
    z=f
print ("Наибольшее число:", z)