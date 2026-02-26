import itertools
import time

def brute_force(pwd):
    start = time.time()
    length = len(pwd)
    digits, attempts = "0123456789", 0
    
    print(f"\nCracking {length} digit password...")
    
    for guess in itertools.product(digits, repeat=length):
        attempts += 1
        guess_pwd = "".join(guess)
        
        if(guess_pwd==pwd):
            stop = time.time()
            print("Guessed Password: ", guess_pwd)
            print("Attempts: ", attempts)
            print(f"Time Taken: {stop-start} seconds")
            return
    
    print("Password NOT FOUND!")
            
pwd = str(input("Enter a numeric password: "))
brute_force(pwd)