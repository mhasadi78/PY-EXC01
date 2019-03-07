day = input('Please enter the day number : \n')
month = input('Please enter the month number : \n')
day = int(day)
month = int(month)
startFlag = True
if day > 30 :
    print('ERROR!\n    We assume that all months have 30 days.') 
    startFlag = False
if month > 12 :
    print('ERROR!\n    We have only 12 months!') 
    startFlag = False   
if startFlag == True :    
    if month == 4 or month == 5:
        print('\nTrue')
    elif month == 3 :
        if day > 20 and day <= 30 :
            print('\nTrue')
        else:
            print('\nFalse')
    elif month == 6 :
        if day >= 1 and day < 20 :
            print('\nTrue')
    else:
        print('\nFalse')    
print('\nProgram Ended')


