"""program to check whether the triangle is equilateral, isosceles or scalene triangle."""
a=int(input('enter 1 side'))
b=int(input('enter 2 side'))
c=int(input('enter 3 side'))
if a==b and b==c:
    print('equilateral')
elif a==b or a==c:
    print('isosceles')
else:
    print('scalene ')
    
    