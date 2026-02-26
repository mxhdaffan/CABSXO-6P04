def checkPassword(pwd):
    size = len(pwd)
    score = 0
    common = ["123456","password","qwerty","0000"]
    
    if(size >= 8):
        score += 1
    if(size >= 12):
        score += 1
        
    for x in pwd:
        if(x.isalpha()):
            if(x.isupper()):
                score += 1
            elif(x.islower()):
                score += 1
        elif(x.isdigit()):
            score += 1
        else:
            score += 1
            
    if(pwd.lower() in common):
        return "Very Weak (Common Password)"
    elif(score <= 2):
        return "Weak"
    elif(score <= 4):
        return "Medium"
    else:
        return "Strong"
            
pwd = str(input("Enter a password: "))
res = checkPassword(pwd)
print(f"Password strength: {res}")