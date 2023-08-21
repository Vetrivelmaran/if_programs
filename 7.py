"""Write a program that takes two integers and a string as input. If the
string is "Add", the program should add the two integers and print the
result. If the string is "Subtract", the program should subtract thesecond integer from the first integer and print the result. If the string is
"Multiply", the program should multiply the two integers and print the
result. If the string is "Divide", the program should divide the first
integer by the second integer and print the result using If Else
statements only.
"""
n1=int(input('enter '))
n2=int(input('entre '))
print('1.add\n2.sub\n3.mul\n4.div')
choose =int(input('enter :'))
if choose==1:
    print(n1+n2)
elif choose==2:
    print(n1-n2)
    
elif choose==3:
    print(n1*n2)
elif choose==4:
    print(n1/n1)
