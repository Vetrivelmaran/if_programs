"""program to input all sides of a triangle and check whether triangle is valid or not."""
a=int(input('enter 1 side'))
b=int(input('enter 2 side'))
c=int(input('enter 3 side'))
side =a+b
if side>c:
    print('yes')
else:
    print('not')