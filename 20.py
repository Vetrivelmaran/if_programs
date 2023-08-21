"""program to input angles of a triangle and check whether triangle is valid or not."""
a=int(input('enter angle 1'))
b=int(input('enter angle 2'))
c=int(input('enter angle 3'))
angle =a+b+c
if angle==180:
    print('yes it is tringle')
else:
    print('not triangle')