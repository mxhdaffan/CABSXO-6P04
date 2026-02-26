def isArmstrong(num, digits):
    sumd, temp = 0, num
    
    while(temp>0):
        lsd = temp%10
        sumd += (lsd**digits)
        temp = temp//10
    
    if(sumd==num):
        return True
    else:
        return False

dig = int(input("Enter 'N': "))

for i in range(10**(dig-1), 10**dig):
    if(isArmstrong(i, dig)):
        print(i)