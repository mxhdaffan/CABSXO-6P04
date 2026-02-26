import math

def euler(num):
    count = 0

    for i in range(1,num+1):
        if(math.gcd(i,num)==1):
            count += 1
    
    return count

def order(r, n):
    if(math.gcd(r,n) != 1):
        return "NOT DEFINED!"
    
    phi = euler(n)

    for k in range(1, phi+1):
        if(((r**k) % n) == 1):
            return k

r, n = map(int, input("Enter r and n: ").split())
print(order(r,n))