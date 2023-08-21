"""Write a program that takes a year as input and prints "Leap Year" if the
year is a leap year and "Not a Leap Year" otherwise using If Else"""
year =int(input('enter the year:'))
if year%400==0 and year%100==0:
    print("leap year")
elif year%4==0 and year%100!=0:
    print('leap year')
else:
    print('not leap year')

    