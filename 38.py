"""Write a program that takes a person's credit score as input and prints "Poor Credit" if
the credit score is below 600, "Fair Credit" if the credit score is between 600 and 699,
"Good Credit" if the credit score is between 700 and 799, and "Excellent Credit" if the
credit score is 800 or higher."""
credit=int(input('enter the credit->'))
if credit<600:
    print('poor credit')
elif 600<=credit<=699:
    print('fair credit')
elif 700<=credit<=799:
    print('good credit')
else:
    print('excelent')
