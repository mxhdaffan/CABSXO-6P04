import math

def eulerTotient(num):
    count = 0

    for i in range(1, num+1):
         if (math.gcd(i,num)==1):
              count += 1
              
    return count

num = int(input("Enter a positive integer: "))

if(num<=0):
     print("\nINVALID INPUT!")
else:
     print(f"\nEuler Totient of {num} = {eulerTotient(num)}")