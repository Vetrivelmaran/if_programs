"""Write a program that takes three numbers as input and prints the
smallest of the three numbers using If Else statements only."""
a =int(input('enter:'))
b=int(input('enmtr:'))
c=int(input('enter:'))
if a<b and a<c:
    print(a,'is smaller')
elif b<c and b<c:
    print(b,'is smaller')
else:
    print(c,'smaller')