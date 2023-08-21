"""Write a program that takes a person's age and income as input and prints the person's
retirement savings goal. The program should print "No Retirement Savings Needed" if
the person is under 18 or over 65, "Low Retirement Savings Goal" if the person's income
is below the middle-income threshold, "Middle Retirement Savings Goal" if the person's
income is between the middle-income threshold and the high-income threshold, and
"High Retirement Savings Goal" if the person's income is above the high-income
threshold."""
age = int(input('enter the age'))
income=int(input('enter income'))
middle_threshold =50000
higher_threshold=100000
if age<18 or age>65:
    print('no retirment saving')
elif middle_threshold<=income<higher_threshold:
    print('middle retirement savings goal')
elif income>higher_threshold:
    print('high retirement savings goal')