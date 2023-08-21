"""Write a program that takes three integers as input and prints them in
ascending order using If Else statements only."""
a =int(input('enter:'))
b =int(input('enter:'))
c =int(input('enter:'))
if a<b and b<c:
    print(a,b,c)
elif c<a and a<b:
    print(c,a,b)
elif a<c and c<b:
    print(a,c,b)
elif c<b and b<a:
    print(c,b,a)
elif b<c and c<a:
    print(b,c,a)
elif b<a and a<c:
    print(b,a,c)
else:
    print('all are same')
    
    