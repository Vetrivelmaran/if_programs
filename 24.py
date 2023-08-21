"""Create a program that converts a numerical grade to a letter grade (A, B, C, etc.) using if-else
statements."""
mark =int(input('enter:'))
if mark>=90:
    print('A')
elif mark>=80:
    print('B')
elif mark>=70:
    print('C')
elif mark>60:
    print('E')
else:
    print('fail')
    