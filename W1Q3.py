def isArmstrong(num):
    digits = len(str(num))
    sumd, temp = 0, num
    
    while(temp>0):
        lsd = temp%10
        sumd += (lsd**digits)
        temp = temp//10

    if(sumd==num):
        return True
    else:
        return False

num = int(input("Enter a number: "))

if(isArmstrong(num)):
    print("This is an armstrong number")
else:
    print("This is NOT an armstrong number")