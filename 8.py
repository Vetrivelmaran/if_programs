"""Write a program that takes three integers as input and prints the
number that appears most frequently. If there are multiple numbers
that appear with the same highest frequency, the program should print
the smallest of those numbers using If Else statements only."""
a=int(input('enter '))
b=int(input('enter '))
c=int(input('enter '))
if a==c:
    print(a)
elif b==a:
    print(b)
elif a<b and a<c:
    print(a)
elif b<a and b<c:
    print(b)
else:
    print(c)
    

    