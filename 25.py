"""Implement a program that checks if a given year is a century year (ending with "00") using if-else
statements."""
year = int(input("Enter a year: "))
if year % 100 == 0:
    print(year,'is century ')
else:
    print(year,'is not century year')

4