"""Write a program that takes a person's income as input and prints the person's tax
bracket. The program should print "No Tax" if the income is below the taxable income
threshold, "Low Tax Bracket" if the income is between the taxable income threshold and
the middle-income tax bracket, "Middle Tax Bracket" if the income is between the
middle-income tax bracket and the high-income tax bracket, and "High Tax Bracket" if
the income is above the high-income tax bracket."""
income =int(input('enter the tax :'))
low_tax =20000
midle_tax = 50000
high_tax =100000
if income<low_tax:
    print('no tax')
elif low_tax<=income<midle_tax:
    print('low tax bracket')
elif midle_tax<=income:
    print('middle tac bbracket')
else:
    print('high  tax bracket')