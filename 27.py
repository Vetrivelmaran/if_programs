select =int(input('1.celciou to farenhete\n2.farenheate to celsius \n ->'))
if select==1:
    celsius=float(input('enter'))
    print((celsius * 9/5) + 32)
else:
    fahrenheit =float(input('enter:'))
    print(fahrenheit - 32) * 5/9


