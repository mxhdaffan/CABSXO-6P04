import math

def isPrime(num):
    if(num<=1):
        return False
    
    for i in range(2, int(math.sqrt(num))+1):
        if(num%i==0):
            return False
    return True

def is2k(num):
    return (num & (num-1)) == 0

def isMersenne(num):
    if(isPrime(num)==False):
        return False
    
    return  is2k(num+1)
    
num = int(input("Enter a number: "))

if(num<0):
    print("Invalid input!")
else:
    if(isMersenne(num)):
        print("This is a mersenne prime number")
    else:
        print("This is NOT a mersenne prime number!")