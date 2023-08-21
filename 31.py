"""Write a program that takes a person's weight in kilograms as input and prints
"Underweight" if the weight is below 18.5, "Normal weight" if the weight is between 18.5
and 24.9, "Overweight" if the weight is between 25 and 29.9, and "Obese" if the weight
is 30 or higher"""

weight =float(input('enter:'))
if weight<18.5:
    print('under wait')
elif 18<=weight<=24.9:
    print('normal weight')
elif 25<=weight<=29.9:
    print('over wait')
elif weight==30 or weight>30:
    print('obese')
