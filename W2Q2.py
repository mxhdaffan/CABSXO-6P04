def gcd(x, y):
    r = x%y
    
    while(r!=0):
        x = y
        y = r
        r = x%y
    
    return y

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

hcf = gcd(a,b)

print(f"GCD of {a} and {b} = {hcf}")