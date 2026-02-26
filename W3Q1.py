def is2k(num):
    for i in range(num):
        if(2**i == num):
            return i
        
    return -1

num = int(input("Enter a number: "))
res = is2k(num)

if(res!=-1):
    print(f"This number is of the form 2^{res} = {num}")
else:
    print("Not in 2^k form!")