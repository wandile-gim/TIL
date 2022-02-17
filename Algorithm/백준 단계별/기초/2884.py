a,b = map(int, "10 10".split(' '))
# a = 0
# b = 10
if b - 45 < 0 :
    if a-1 < 0:
        a = 23
        b = b + 60 - 45
    else:
        a = a - 1
        b = b + 60 -45
else: 
    b = 60 - b
    a = a

print(a,b,end=' ')

if b > 44:
    print(a, b-45)
elif b < 45 and a > 0:
    print(a-1, b+15)
else:
    print(23, b + 15)