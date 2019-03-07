frstNum = input ('Enter the First Number :  \n')
scndNum = input ('Enter the Second Number :  \n')
thrdNum = input ('Enter the Third Number : \n')

frstNum = int(frstNum)
scndNum = int(scndNum)
thrdNum = int(thrdNum)

if frstNum >= scndNum + thrdNum or scndNum >= frstNum + thrdNum or thrdNum >= frstNum + scndNum :
    print('True')
else:
    print('False')
