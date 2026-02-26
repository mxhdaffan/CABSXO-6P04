def isPerfect(num):
    sumf = 0
    
    for i in range(1, num):
        if(num%i==0):
            sumf += i
            
    if(sumf==num):
        return True
    else:
        return False

num = int(input("Enter a number: "))

if(num<0):
    print("INVALID INPUT")
else:
    if(isPerfect(num)):
        print("This is a perfect number")
    else:
        print("This is NOT a perfect number")