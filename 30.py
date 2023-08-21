"""Write a program that takes a person's age as input and prints "Child" if the age is under
18, "Adult" if the age is between 18 and 65, and "Senior" if the age is over 65.
"""
age=int(input())
if age<18:
    print("child")
elif 18<=age<=65:
    print("adult")
else:
    print("senior")