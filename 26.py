"""Create a program that checks if a given year is a leap year and, if not, displays the number of years
left until the next leap year using if-else statements."""
year =int(input('enter :'))
if (year%100==0 and year%4==0) or (year%4==0 and year):
    print('leap year')
elif year%4==1:
    print('3 years left')
elif year%4==2:
    print('2 year left')
elif year%4==3:
    print('1 year left')
