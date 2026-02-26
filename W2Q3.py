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

if(hcf==1):
    print(f"{a} and {b} are relatively prime")
else:
    print(f"{a} and {b} are NOT relatively prime")