"""Write a program that takes a person's height in meters and weight in kilograms as input
and calculates the person's body mass index (BMI). The program should then print
"Underweight" if the BMI is below 18.5, "Normal weight" if the BMI is between 18.5 and
24.9, "Overweight" if the BMI is between 25 and 29.9, and "Obese" if the BMI is 30 or
higher."""
h = float(input("->"))
w =float(input('->'))
BMI = w / h**2
print(BMI)
if BMI<18.5:
    print('under weight')
elif 18.5<=BMI<=24.9:
    print('normal weight')
elif 25<=BMI<=29.9:
    print("over weight")
else:
    print("obese")