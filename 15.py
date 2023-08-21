"""program to input any character and check whether it is alphabet, digit or special
character."""
chr = input('enter char :')
if (chr >='A' and chr<='Z')or(chr>='a'and chr<='z'):
    print('alphabet')
elif chr>='0' and chr<='9':
    print('number')
else:
    print('special')