#program to count total number of notes in given amount

ammount =int(input('enter ammount'))
if ammount>=500:
    print(ammount//500,'-500 note')
    ammount=ammount%500
    
if ammount>=100:
    print(ammount//100,' -100 note')
    ammount=ammount%100
    
if ammount>=50:
    print(ammount//50,'-50 notes')
    ammount=ammount%50
    
if ammount<=20 or ammount>20:
    print(ammount//20,'-20 notes')
    ammount=ammount%20
    print(ammount//10,'-10 notes')
    ammount=ammount%10
    if ammount>=1 and ammount<=9:
        print('tack coins for',ammount)
        
    