#program to input month number and print number of days in that month
num =int(input('enter '))
if num==2:
    print('2 days')
elif num==4 or num==6 or num ==9 or num ==11:
    print('30 days')
else:
    print('31 days')